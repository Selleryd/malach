#!/usr/bin/env python3
import asyncio,base64,mimetypes,re
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
ROUTES=['/','/product/','/solutions/','/solutions/google-ads/','/solutions/shopify/','/solutions/portfolio/','/intelligence/','/auto-agent/','/advantage/','/attribution/','/voice/','/vision/','/channels/','/pricing/','/security/','/about/','/support/','/contact/','/docs/','/status/','/privacy/','/terms/','/login/']
CSS=(ROOT/'assets/css/malach-v7.css').read_text(encoding='utf-8')
SCRIPTS={
    '/assets/js/malach-v7.js':(ROOT/'assets/js/malach-v7.js').read_text(encoding='utf-8'),
    '/assets/js/home-v7.js':(ROOT/'assets/js/home-v7.js').read_text(encoding='utf-8'),
    '/assets/js/pricing-v7.js':(ROOT/'assets/js/pricing-v7.js').read_text(encoding='utf-8'),
    '/assets/js/status-v7.js':(ROOT/'assets/js/status-v7.js').read_text(encoding='utf-8'),
}

def route_file(route): return ROOT/'index.html' if route=='/' else ROOT/route.strip('/')/'index.html'

def data_uri(path:Path):
    mime=mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    return f'data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}'

def inline_html(route):
    html=route_file(route).read_text(encoding='utf-8')
    html=re.sub(r'<link rel="stylesheet" href="/assets/css/malach-v7\.css\?v=[^"]+">',f'<style>{CSS}</style>',html)
    html=re.sub(r'<link rel="(?:icon|apple-touch-icon|manifest)"[^>]*>','',html)
    html=html.replace('<script defer src="/runtime-config.js"></script>','<script>window.MALACH_PUBLIC_CONFIG={appUrl:"https://app.malach.app"};</script>')
    for src,code in SCRIPTS.items():
        html=re.sub(rf'<script type="module" src="{re.escape(src)}\?v=[^"]+"></script>',lambda _m:f'<script>(()=>{{{code}}})()</script>',html)
    for match in set(re.findall(r'(/assets/media/[^"\']+)',html)):
        clean=match.split('?')[0]
        path=ROOT/clean.lstrip('/')
        if path.exists(): html=html.replace(match,data_uri(path))
    html=html.replace('<head>','<head><base href="https://malach.test/">',1)
    return html

async def main():
    async with async_playwright() as p:
        launch_kwargs={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']}
        system_chromium=Path('/usr/bin/chromium')
        if system_chromium.exists(): launch_kwargs['executable_path']=str(system_chromium)
        browser=await p.chromium.launch(**launch_kwargs)
        errors=[]

        for width,height,label in ((1440,1000,'desktop'),(390,844,'mobile')):
            page=await browser.new_page(viewport={'width':width,'height':height})
            await page.route('https://malach.test/api/health',lambda route:route.fulfill(status=200,content_type='application/json',body='{"ok":true}'))
            for route in ROUTES:
                await page.set_content(inline_html(route),wait_until='domcontentloaded',timeout=12000)
                await page.wait_for_timeout(70)
                if await page.evaluate('document.documentElement.scrollWidth > document.documentElement.clientWidth + 2'):
                    errors.append(f'{route}: horizontal overflow at {label}')
                hidden=await page.locator('h1,h2,h3').evaluate_all('els=>els.filter(el=>{const s=getComputedStyle(el),r=el.getBoundingClientRect();return s.display==="none"||s.visibility==="hidden"||Number(s.opacity)===0||r.width<1||r.height<1}).length')
                if hidden: errors.append(f'{route}: {hidden} hidden heading(s) at {label}')
            await page.close()

        page=await browser.new_page(viewport={'width':1440,'height':1000})
        await page.set_content(inline_html('/'),wait_until='domcontentloaded')
        await page.wait_for_timeout(180)
        trigger=page.locator('[data-nav-trigger]').first
        await trigger.hover();await page.wait_for_timeout(100)
        if not await trigger.evaluate('el=>el.closest("[data-nav-menu]").classList.contains("open")'):
            errors.append('/: Solutions menu did not open')
        if await page.evaluate('document.documentElement.dataset.malachReady||""')!='true':
            errors.append('/: V7 interaction layer did not initialize')
        if await page.evaluate('document.documentElement.dataset.v7HomeReady||""')!='true':
            errors.append('/: V7 homepage interaction layer did not initialize')
        if await page.locator('.v7-command-deck').count()!=1: errors.append('/: V7 hero command deck missing')
        if await page.locator('.cta-orbit,.hero-orbit,.orbit-ring').count(): errors.append('/: obsolete circle/orbit markup remains')
        await page.locator('[data-product-signal="ember"]').click()
        if 'return-adjusted profit' not in (await page.locator('.v7-decision-card h3').inner_text()).lower(): errors.append('/: product-level hero simulation did not update')
        await page.locator('[data-authority-switch] button[data-mode="full"]').click()
        if 'certified' not in (await page.locator('[data-authority-note]').inner_text()).lower(): errors.append('/: hero authority simulation did not update')
        await page.locator('[data-clarity="unified"]').click()
        if not await page.locator('[data-clarity-panel="unified"]').evaluate('el=>el.classList.contains("active")'): errors.append('/: clarity transformation did not switch')
        await page.locator('[data-flow-step="learn"]').click()
        if 'outcome loop' not in (await page.locator('[data-flow-title]').inner_text()).lower(): errors.append('/: operating-loop simulation did not update')
        await page.locator('[data-channel="meta"]').click()
        if 'meta' not in (await page.locator('[data-channel-title]').inner_text()).lower(): errors.append('/: channel simulation did not update')
        await page.locator('[data-authority-card="canary"]').click()
        if 'controlled test' not in (await page.locator('[data-authority-status]').inner_text()).lower(): errors.append('/: authority card interaction did not update')
        await page.locator('[data-model-case="sora"]').click()
        if 'remarketing' not in (await page.locator('[data-model-title]').inner_text()).lower(): errors.append('/: proprietary model simulation did not update')
        canvas=page.locator('[data-v71-canvas]').first
        await canvas.locator('[data-canvas-step="decision"]').click()
        if 'increase high-intent' not in (await canvas.locator('[data-canvas-title]').inner_text()).lower(): errors.append('/: Agent Canvas simulation did not update')
        if await page.locator('[data-ops-clock]').count()<1: errors.append('/: 24/7 operations simulation missing')
        await page.close()

        page=await browser.new_page(viewport={'width':390,'height':844})
        await page.set_content(inline_html('/'),wait_until='domcontentloaded')
        toggle=page.locator('[data-menu-trigger]');await toggle.click()
        if await toggle.get_attribute('aria-expanded')!='true': errors.append('/: mobile menu did not open')
        await page.close()

        page=await browser.new_page(viewport={'width':1440,'height':1000})
        await page.set_content(inline_html('/pricing/'),wait_until='domcontentloaded')
        annual=page.locator('[data-billing="annual"]');await annual.click()
        if not await annual.evaluate('el=>el.classList.contains("active")'): errors.append('/pricing/: annual toggle failed')
        if await page.locator('[data-annual]:visible').count()<3: errors.append('/pricing/: annual prices not visible')
        await page.close()

        page=await browser.new_page(viewport={'width':1440,'height':1000})
        await page.route('https://malach.test/api/health',lambda route:route.fulfill(status=200,content_type='application/json',body='{"ok":true}'))
        await page.set_content(inline_html('/status/'),wait_until='domcontentloaded')
        await page.wait_for_timeout(180)
        if 'No issues detected.' not in await page.locator('body').inner_text(): errors.append('/status/: healthy state did not render')
        await page.close();await browser.close()
        if errors: raise AssertionError('\n'.join(errors))
        print(f'Browser smoke passed: {len(ROUTES)} routes at desktop/mobile plus dropdown, product simulation, proprietary model, Agent Canvas, 24/7 operations, clarity, flow, channels, authority, mobile menu, pricing, and live status.')

if __name__=='__main__': asyncio.run(main())
