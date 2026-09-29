# Publication thumbnails

Generates first-page (or custom-page) PNG previews from each entry’s `pdf` field in `_data/citations.yml`.

```bash
uv sync --group dev
uv run python tools/publications/generate_thumbnails.py
```

Options:

- `--title "partial title"` — only matching publications
- `--force` — re-render even when the PNG already exists

Per-publication metadata in `_data/citations.yml`:

- `thumbnail_page` — **1-based** PDF page index used for the image (default `1`; edit before re-running the script)
- `thumbnail` — site path written by the script, e.g. `/assets/publications/thumbnails/2013-error-prediction-with-partial-feedback.png`

Images are written under `assets/publications/thumbnails/`.
