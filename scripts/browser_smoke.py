import asyncio
import base64
import mimetypes
import re
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
ROUTES = ['/', '/product/', '/auto-agent/', '/intelligence/', '/advantage/', '/attribution/', '/voice/', '/security/', '/pricing/', '/about/', '/support/', '/privacy/', '/terms/', '/login/']

CSS = (ROOT / 'assets/css/styles.css').read_text(encoding='utf-8')
SITE_JS = (ROOT / 'assets/js/site.js').read_text(encoding='utf-8')
CHART_JS = (ROOT / 'assets/js/chart.js').read_text(encoding='utf-8').replace('export class ', 'class ').replace('export function ', 'function ')
HOME_JS = re.sub(r"^import .*?;\s*", '', (ROOT / 'assets/js/home.js').read_text(encoding='utf-8'), flags=re.M)
SUBPAGE_JS = re.sub(r"^import .*?;\s*", '', (ROOT / 'assets/js/subpage.js').read_text(encoding='utf-8'), flags=re.M)
PRICING_JS = (ROOT / 'assets/js/pricing.js').read_text(encoding='utf-8')


def route_file(route):
    return ROOT / 'index.html' if route == '/' else ROOT / route.strip('/') / 'index.html'


def data_uri(path: Path):
    mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def inline_html(route):
    html = route_file(route).read_text(encoding='utf-8')
    html = re.sub(r'<link rel="stylesheet" href="/assets/css/styles\.css">', f'<style>{CSS}</style>', html)
    html = re.sub(r'<link rel="(?:icon|apple-touch-icon|manifest)"[^>]*>', '', html)
    # inline local images
    for match in set(re.findall(r'(/assets/media/[^"\']+)', html)):
        path = ROOT / match.lstrip('/')
        if path.exists():
            html = html.replace(match, data_uri(path))
    # remove external JS tags and inject a bundled module
    html = re.sub(r'<script type="module" src="/assets/js/[^\"]+"></script>', '', html)
    scripts = SITE_JS
    if route == '/': scripts += '\n' + CHART_JS + '\n' + HOME_JS
    elif route in ['/product/', '/auto-agent/']:
        scripts += '\n' + CHART_JS + '\n' + SUBPAGE_JS
    elif route == '/pricing/': scripts += '\n' + PRICING_JS
    html = html.replace('</body>', f'<script type="module">{scripts}</script></body>')
    return html


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path='/usr/bin/chromium', headless=True, args=['--no-sandbox'])
        page = await browser.new_page(viewport={'width': 1440, 'height': 1000})
        errors = []
        page.on('pageerror', lambda exc: errors.append(f'pageerror: {exc}'))
        page.on('console', lambda msg: errors.append(f'console {msg.type}: {msg.text}') if msg.type == 'error' and 'Failed to parse URL' not in msg.text else None)
        for route in ROUTES:
            await page.set_content(inline_html(route), wait_until='load')
            await page.wait_for_timeout(120)
            overflow = await page.evaluate('document.documentElement.scrollWidth > document.documentElement.clientWidth + 2')
            if overflow: errors.append(f'{route}: horizontal overflow at desktop')
            await page.set_viewport_size({'width': 390, 'height': 844})
            await page.set_content(inline_html(route), wait_until='load')
            await page.wait_for_timeout(100)
            overflow_mobile = await page.evaluate('document.documentElement.scrollWidth > document.documentElement.clientWidth + 2')
            if overflow_mobile: errors.append(f'{route}: horizontal overflow at mobile')
            await page.set_viewport_size({'width': 1440, 'height': 1000})
        if errors:
            print('\n'.join(errors))
            await browser.close()
            raise SystemExit(1)
        print(f'Browser smoke passed: {len(ROUTES)} routes, desktop and mobile.')
        await browser.close()

asyncio.run(main())
