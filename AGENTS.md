# shacharmirkin.github.io

This repo is the Jekyll source for https://shacharmirkin.github.io.

## Structure

- `_posts/` — blog posts (`YYYY-MM-DD-slug.md`)
- `_layouts/`, `_includes/` — HTML templates
- `assets/` — CSS, JS, images
- `tools/a11y/` — pa11y CI (not published to the site)
- `tests/` — pytest checks on `_site` after `bundle exec rake test`

## Build and test

```bash
bundle install
bundle exec rake test    # jekyll build + default rake tasks
pytest tests/test_site_artifacts.py
```

Match existing Markdown/HTML style in nearby files. Do not commit `_site/`, `vendor/`, or `tools/a11y/node_modules/`.

## Agent-facing files

- `/llms.txt` — site map and usage hints for LLM agents
- `/index.md` — plain markdown summary of the homepage (`agent-index.source.md`, copied at build time)
- `/.well-known/agent.json` — minimal agent discovery stub

Public docs are the rendered pages; there is no OpenAPI or MCP endpoint on this site.
