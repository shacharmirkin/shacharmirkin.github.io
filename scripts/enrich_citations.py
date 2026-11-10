#!/usr/bin/env python3
"""Fill missing abstracts in _data/citations.yml and refresh _data/scholar.yml.

Uses OpenAlex (author works + abstract_inverted_index) and arXiv API for arxiv URLs.
Run from repo root: uv run python scripts/enrich_citations.py
Weekly CI refreshes scholar.yml only: uv run python scripts/enrich_citations.py --scholar-only
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import unicodedata
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml

REPO = Path(__file__).resolve().parents[1]
CITATIONS_PATH = REPO / "_data" / "citations.yml"
SCHOLAR_PATH = REPO / "_data" / "scholar.yml"
OPENALEX_AUTHOR_ID = "https://openalex.org/A5029642107"
SCHOLAR_USER_ID = "xsEZbOkAAAAJ"
BADGE_API = f"https://google-scholar-badge.vercel.app/citations?user={SCHOLAR_USER_ID}"


def normalize_title(title: str) -> str:
    title = unicodedata.normalize("NFKD", title).lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def abstract_from_inv(inv: dict[str, list[int]] | None) -> str | None:
    if not inv:
        return None
    max_pos = max(max(positions) for positions in inv.values())
    words = [""] * (max_pos + 1)
    for word, positions in inv.items():
        for pos in positions:
            words[pos] = word
    text = " ".join(words).strip()
    return text or None


def fetch_openalex_works(session: requests.Session) -> list[dict]:
    works: list[dict] = []
    cursor = "*"
    while cursor:
        resp = session.get(
            "https://api.openalex.org/works",
            params={
                "filter": f"authorships.author.id:{OPENALEX_AUTHOR_ID}",
                "per-page": 200,
                "cursor": cursor,
                "select": "id,title,publication_year,abstract_inverted_index,doi,ids",
            },
            timeout=30,
        )
        resp.raise_for_status()
        payload = resp.json()
        works.extend(payload["results"])
        cursor = payload["meta"].get("next_cursor")
        time.sleep(0.2)
    return works


def best_openalex_match(title: str, works: list[dict], min_ratio: float = 0.88) -> dict | None:
    norm = normalize_title(title)
    best: dict | None = None
    best_score = 0.0
    for work in works:
        candidate = normalize_title(work.get("title") or "")
        if not candidate:
            continue
        if candidate == norm:
            return work
        score = SequenceMatcher(None, norm, candidate).ratio()
        if score > best_score:
            best_score = score
            best = work
    if best_score >= min_ratio:
        return best
    return None


def fetch_crossref_abstract(entry: dict, session: requests.Session) -> str | None:
    doi = entry.get("doi")
    if doi and not doi.startswith("http"):
        doi_url = f"https://doi.org/{doi.lstrip('doi:')}"
    elif entry.get("url"):
        parsed_url = urlparse(entry["url"])
        host = (parsed_url.hostname or "").lower()
        if host == "doi.org" or host.endswith(".doi.org"):
            doi_url = entry["url"]
        else:
            doi_url = None
    else:
        doi_url = None

    if doi_url:
        resp = session.get(
            f"https://api.crossref.org/works/{doi_url}",
            headers={"Accept": "application/json"},
            timeout=30,
        )
        if resp.ok:
            items = resp.json().get("message", {}).get("abstract")
            if items:
                return re.sub(r"<[^>]+>", "", items).strip()

    title = entry.get("title", "")
    if not title:
        return None
    resp = session.get(
        "https://api.crossref.org/works",
        params={"query.title": title, "rows": 3},
        headers={"Accept": "application/json"},
        timeout=30,
    )
    if not resp.ok:
        return None
    for item in resp.json().get("message", {}).get("items", []):
        if normalize_title(item.get("title", [""])[0]) != normalize_title(title):
            continue
        abstract = item.get("abstract")
        if abstract:
            return re.sub(r"<[^>]+>", "", abstract).strip()
    return None


def fetch_arxiv_abstract(url: str, session: requests.Session) -> str | None:
    m = re.search(r"arxiv\.org/(?:abs|pdf)/([\w.:-]+)", url, re.I)
    if not m:
        return None
    arxiv_id = m.group(1).removesuffix(".pdf")
    resp = session.get(
        "https://export.arxiv.org/api/query",
        params={"id_list": arxiv_id},
        timeout=30,
    )
    resp.raise_for_status()
    m2 = re.search(r"<summary>(.*?)</summary>", resp.text, re.S)
    if not m2:
        return None
    text = re.sub(r"\s+", " ", m2.group(1)).strip()
    return text or None


def fetch_scholar_citations(session: requests.Session) -> int | None:
    try:
        resp = session.get(BADGE_API, timeout=20)
        resp.raise_for_status()
        message = resp.json().get("message", "")
        if str(message).isdigit():
            return int(message)
    except Exception as exc:  # noqa: BLE001 - report and continue
        print(f"warning: scholar badge API failed: {exc}", file=sys.stderr)
    return None


def refresh_scholar_yml(session: requests.Session, *, dry_run: bool = False) -> int:
    scholar = {}
    if SCHOLAR_PATH.exists():
        scholar = yaml.safe_load(SCHOLAR_PATH.read_text(encoding="utf-8")) or {}

    citations_count_api = fetch_scholar_citations(session)
    if citations_count_api is None:
        print("Scholar badge API failed; leaving scholar.yml unchanged", file=sys.stderr)
        return 1

    scholar["citations"] = citations_count_api
    scholar["user_id"] = SCHOLAR_USER_ID
    scholar["updated_at"] = date.today().isoformat()
    print(f"Scholar citations: {citations_count_api}")

    if dry_run:
        print("(dry run — no files written)")
        return 0

    SCHOLAR_PATH.write_text(
        yaml.dump(scholar, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    print(f"Wrote {SCHOLAR_PATH.name}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing files")
    parser.add_argument("--report-only", action="store_true", help="Only print gap report")
    parser.add_argument(
        "--scholar-only",
        action="store_true",
        help="Only refresh _data/scholar.yml (used by weekly CI)",
    )
    args = parser.parse_args()

    session = requests.Session()
    session.headers["User-Agent"] = "shacharmirkin.github.io-citation-enricher"

    if args.scholar_only:
        return refresh_scholar_yml(session, dry_run=args.dry_run)

    citations: list[dict] = yaml.safe_load(CITATIONS_PATH.read_text(encoding="utf-8"))
    works = fetch_openalex_works(session)
    print(f"OpenAlex works for author: {len(works)}")

    openalex_by_title = {normalize_title(w["title"]): w for w in works if w.get("title")}
    citation_titles = {normalize_title(c["title"]) for c in citations if c.get("title")}

    missing_in_citations = []
    for work in works:
        norm = normalize_title(work["title"])
        if norm in citation_titles:
            continue
        if best_openalex_match(work["title"], [{"title": c["title"]} for c in citations], min_ratio=0.82):
            continue
        missing_in_citations.append(work)

    missing_abstract_sources = []
    added_abstracts = 0
    for entry in citations:
        if entry.get("abstract"):
            continue
        title = entry.get("title", "")
        abstract: str | None = None
        source = ""

        work = best_openalex_match(title, works)
        if work:
            abstract = abstract_from_inv(work.get("abstract_inverted_index"))
            if abstract:
                source = "openalex"

        if not abstract:
            abstract = fetch_crossref_abstract(entry, session)
            if abstract:
                source = "crossref"
            time.sleep(0.3)

        if not abstract and entry.get("url"):
            abstract = fetch_arxiv_abstract(entry["url"], session)
            if abstract:
                source = "arxiv"
            time.sleep(0.3)

        if abstract:
            entry["abstract"] = abstract
            added_abstracts += 1
            print(f"+ abstract ({source}): {title[:70]}")
        else:
            missing_abstract_sources.append(title)

    print(f"\nCitations in YAML: {len(citations)}")
    print(f"Abstracts added this run: {added_abstracts}")
    print(f"Still missing abstract: {len(missing_abstract_sources)}")
    for title in missing_abstract_sources:
        print(f"  - {title}")

    print(f"\nPossibly missing from citations.yml ({len(missing_in_citations)}):")
    for work in sorted(missing_in_citations, key=lambda w: w.get("publication_year") or 0, reverse=True):
        year = work.get("publication_year", "?")
        print(f"  - [{year}] {work['title']}")

    citations_count = sum(1 for c in citations if c.get("abstract"))
    print(f"\nCoverage: {citations_count}/{len(citations)} entries have abstract")

    if args.report_only:
        return 0

    if args.dry_run:
        print("\n(dry run — no files written)")
        return 0

    CITATIONS_PATH.write_text(
        yaml.dump(citations, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )
    print(f"\nWrote {CITATIONS_PATH.name}")

    if refresh_scholar_yml(session) == 0:
        print(f"Wrote {SCHOLAR_PATH.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
