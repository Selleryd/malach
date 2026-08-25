# Malach Public Website

## V7.2 Mobile Perfection

V7.2 preserves the approved V7.1 desktop experience and adds a dedicated mobile presentation system for 320–899px viewports. The mobile layer reflows the hero and command deck, converts long feature/authority sections into touch-native scroll-snap stories, rebuilds navigation and subpages for mobile, adds safe-area support, and disables expensive desktop-only effects on coarse pointers.

For an actual-phone preview on the same Wi-Fi network:

```bash
HOST=0.0.0.0 PORT=8080 python3 scripts/preview.py
```

Then open `http://<your-mac-lan-ip>:8080` on the phone.

Malach V7.1 is the public marketing website for Malach — 24/7 autonomous advertising intelligence, proprietary decision models and governed execution.

## Local preview

```bash
python3 scripts/preview.py
```

Open `http://127.0.0.1:8080`.

## Validation

```bash
npm test
python3 scripts/browser_smoke.py
```

## Generation

The public pages are generated from `scripts/build_site_v7.py`.