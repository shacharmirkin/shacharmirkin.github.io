#!/usr/bin/env bash
# WCAG checks on built HTML via pa11y-ci (Puppeteer Chromium — no system ChromeDriver).
set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
A11Y="$(cd "$(dirname "$0")" && pwd)"
cd "$A11Y"
PORT="${A11Y_PORT:-4321}"
export PUPPETEER_CACHE_DIR="${PUPPETEER_CACHE_DIR:-$A11Y/.cache/puppeteer}"

if [[ ! -f "$REPO/_site/index.html" ]]; then
  echo "Building site into _site…"
  (cd "$REPO" && bundle exec jekyll build --destination _site)
fi

if [[ ! -d node_modules/pa11y-ci ]]; then
  echo "Installing tools/a11y npm dependencies…"
  npm ci 2>/dev/null || npm install
fi

npx puppeteer browsers install chrome

npx serve "$REPO/_site" -l "$PORT" --no-request-logging &
SERVE_PID=$!
cleanup() {
  kill "$SERVE_PID" 2>/dev/null || true
}
trap cleanup EXIT

echo "Waiting for http://127.0.0.1:$PORT/ …"
for _ in $(seq 1 50); do
  if curl -sf "http://127.0.0.1:$PORT/" >/dev/null; then
    break
  fi
  sleep 0.2
done

echo "Running pa11y-ci (axe runner, WCAG2AA)…"
npx pa11y-ci --config .pa11yci.json
