"""Assertions on ./_site after `bundle exec rake test` (or `jekyll build`).

CI runs rake before these tests. Locally: `bundle exec rake test && pytest tests/test_site_artifacts.py`.
"""

from __future__ import annotations

from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
SITE = REPO / "_site"


@pytest.mark.integration
def test_core_files_exist() -> None:
    assert SITE.is_dir(), "Run `bundle exec rake test` first to create _site"
    assert (SITE / "robots.txt").is_file()
    robots = (SITE / "robots.txt").read_text(encoding="utf-8")
    assert "Content-Signal:" in robots
    assert (SITE / "llms.txt").is_file()
    assert (SITE / "index.md").is_file()
    assert (SITE / ".well-known" / "agent.json").is_file()
    assert (SITE / "sitemap.xml").is_file()
    assert (SITE / "feed.xml").is_file()
    assert (SITE / "index.html").is_file()
    assert (SITE / "fr" / "index.html").is_file()


@pytest.mark.integration
def test_home_html_has_seo_tags() -> None:
    html = (SITE / "index.html").read_text(encoding="utf-8")
    assert "og:title" in html
    assert "application/ld+json" in html
    assert '"@type": "Organization"' in html or '"@type":"Organization"' in html


@pytest.mark.integration
def test_layout_has_accessibility_landmarks() -> None:
    html = (SITE / "index.html").read_text(encoding="utf-8")
    assert 'class="skip-link"' in html
    assert 'id="main-content"' in html
    assert "<main" in html
    assert 'aria-label="Main navigation"' in html


@pytest.mark.integration
def test_post_layout_has_read_aloud() -> None:
    post_html = SITE / "2026" / "03" / "13" / "llm-sees-something-else" / "index.html"
    if not post_html.is_file():
        candidates = list(SITE.glob("**/index.html"))
        post_html = next(
            (p for p in candidates if "post-read-aloud" in p.read_text(encoding="utf-8")),
            None,
        )
        assert post_html is not None, "Build a post page with layout: post"
    html = post_html.read_text(encoding="utf-8")
    assert 'id="post-read-aloud"' in html
    assert 'id="read-aloud-play"' in html
    assert "post-read-aloud.js" in html
    assert 'data-rate="' in html
