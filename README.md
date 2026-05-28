# shacharmirkin.github.io

Jekyll site. Build, test, and accessibility tooling:

- **Build + HTMLProofer:** `bundle exec rake test`
- **Pytest:** `uv sync --group dev && uv run pytest tests/test_site_artifacts.py -m integration`
- **Accessibility (pa11y):** [tools/a11y/README.md](tools/a11y/README.md)
- **Local scratch (not in git):** `sandbox/`
