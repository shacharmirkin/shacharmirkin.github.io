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
    assert (SITE / "sitemap.xml").is_file()
    assert (SITE / "feed.xml").is_file()
    assert (SITE / "index.html").is_file()
    assert (SITE / "fr" / "index.html").is_file()


@pytest.mark.integration
def test_home_html_has_seo_tags() -> None:
    html = (SITE / "index.html").read_text(encoding="utf-8")
    assert "og:title" in html
    assert "application/ld+json" in html
