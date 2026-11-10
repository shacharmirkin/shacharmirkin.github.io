#!/usr/bin/env python3
"""Render publication PDF thumbnails and update _data/citations.yml metadata."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse

import fitz  # pymupdf
import requests
from ruamel.yaml import YAML

REPO_ROOT = Path(__file__).resolve().parents[2]
CITATIONS_PATH = REPO_ROOT / "_data" / "citations.yml"
THUMB_DIR = REPO_ROOT / "assets" / "publications" / "thumbnails"
THUMB_WIDTH = 168
THUMB_HEIGHT = 222


def slug_for_pub(pub: dict) -> str:
    year = pub.get("year") or "unknown"
    title = pub.get("title") or "untitled"
    base = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    base = base[:72].strip("-") or "publication"
    return f"{year}-{base}"


def pdf_source(pub: dict) -> str | Path | None:
    pdf = pub.get("pdf")
    if pdf:
        return pdf
    url = pub.get("url") or ""
    if isinstance(url, str) and url.lower().endswith(".pdf"):
        return url
    return None


def resolve_local_path(source: str) -> Path | None:
    if not source.startswith("/"):
        return None
    path = REPO_ROOT / source.lstrip("/")
    return path if path.is_file() else None


def fetch_pdf_bytes(source: str) -> bytes:
    local = resolve_local_path(source)
    if local:
        return local.read_bytes()
    resp = requests.get(source, timeout=120, headers={"User-Agent": "shacharmirkin.github.io-thumbnail-bot/1.0"})
    resp.raise_for_status()
    return resp.content


def render_page(pdf_bytes: bytes, page_index: int) -> fitz.Pixmap:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    try:
        if page_index < 0 or page_index >= doc.page_count:
            raise ValueError(f"page {page_index + 1} out of range (1–{doc.page_count})")
        page = doc.load_page(page_index)
        rect = page.rect
        scale = min(THUMB_WIDTH / rect.width, THUMB_HEIGHT / rect.height)
        matrix = fitz.Matrix(scale, scale)
        return page.get_pixmap(matrix=matrix, alpha=False)
    finally:
        doc.close()


def thumb_public_url(slug: str) -> str:
    return f"/assets/publications/thumbnails/{slug}.png"


def load_citations() -> list[dict]:
    yaml_loader = YAML()
    yaml_loader.preserve_quotes = True
    with CITATIONS_PATH.open(encoding="utf-8") as f:
        data = yaml_loader.load(f)
    if not isinstance(data, list):
        raise SystemExit(f"Expected list in {CITATIONS_PATH}")
    return data


def save_citations(data: list[dict]) -> None:
    yaml_writer = YAML()
    yaml_writer.default_flow_style = False
    yaml_writer.width = 4096
    yaml_writer.indent(mapping=2, sequence=4, offset=2)
    with CITATIONS_PATH.open("w", encoding="utf-8") as f:
        yaml_writer.dump(data, f)


def generate_for_pub(pub: dict, *, force: bool) -> tuple[bool, str]:
    title = pub.get("title", "(untitled)")
    page_num = int(pub.get("thumbnail_page") or 1)
    if page_num < 1:
        return False, f"skip {title}: thumbnail_page must be >= 1"

    source = pdf_source(pub)
    if not source:
        return False, f"skip {title}: no pdf (or pdf url)"

    slug = slug_for_pub(pub)
    out_path = THUMB_DIR / f"{slug}.png"
    pub_path = thumb_public_url(slug)

    if out_path.is_file() and not force and pub.get("thumbnail") == pub_path:
        pub.setdefault("thumbnail_page", page_num)
        pub["thumbnail"] = pub_path
        return True, f"ok {title}: kept {out_path.name}"

    try:
        pdf_bytes = fetch_pdf_bytes(str(source))
        # Stable cache key for debugging failed downloads
        digest = hashlib.sha256(pdf_bytes).hexdigest()[:12]
        pix = render_page(pdf_bytes, page_num - 1)
        THUMB_DIR.mkdir(parents=True, exist_ok=True)
        pix.save(out_path)
        pub["thumbnail_page"] = page_num
        pub["thumbnail"] = pub_path
        return True, f"ok {title}: {out_path.name} (pdf sha256 {digest}, page {page_num})"
    except Exception as exc:  # noqa: BLE001 — CLI tool reports per-item failures
        return False, f"fail {title}: {exc}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="Regenerate even if thumbnail exists")
    parser.add_argument("--title", help="Only process publications whose title contains this substring")
    args = parser.parse_args()

    pubs = load_citations()
    ok, fail, skip = 0, 0, 0
    for pub in pubs:
        title = pub.get("title", "")
        if args.title and args.title.lower() not in title.lower():
            continue
        success, message = generate_for_pub(pub, force=args.force)
        print(message)
        if success:
            ok += 1
        elif message.startswith("skip"):
            skip += 1
        else:
            fail += 1

    save_citations(pubs)
    print(f"\nDone: {ok} generated/kept, {skip} skipped, {fail} failed")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
