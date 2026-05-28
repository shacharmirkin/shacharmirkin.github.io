# Accessibility audit (pa11y + axe)

WCAG checks on the built site (`_site/`) using **Puppeteer’s Chromium** (not system Chrome).

From **`tools/a11y/`**:

```bash
npm ci          # first time
npm run a11y    # build _site if needed, serve, run pa11y-ci
```

From repo root:

```bash
(cd tools/a11y && npm run a11y)
```

Config: `.pa11yci.json` — edit the URL list when you add important templates.

**Manual checks** (not automated): keyboard-only navigation, 200% zoom, axe DevTools on pages you changed.

Do **not** use `@axe-core/cli` against system Chrome unless you sync drivers — it breaks when Chrome auto-updates.
