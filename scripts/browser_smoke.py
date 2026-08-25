#!/usr/bin/env python3
import asyncio,base64,mimetypes,re
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
ROUTES=['/','/product/','/solutions/','/solutions/google-ads/','/solutions/shopify/','/solutions/portfolio/','/intelligence/','/auto-agent/','/advantage/','/attribution/','/voice/','/vision/','/channels/','/pricing/','/security/','/about/','/support/','/contact/','/docs/','/status/','/privacy/','/terms/','/login/']
CSS=(ROOT/'assets/css/malach-v7.css').read_text(encoding='utf-8')+'\n'+(ROOT/'assets/css/mobile-v72.css').read_text(encoding='utf-8')
SCRIPTS={
    '/assets/js/malach-v7.js':(ROOT/'assets/js/malach-v7.js').read_text(encoding='utf-8'),
    '/assets/js/mobile-v72.js':(ROOT/'assets/js/mobile-v72.js').read_text(encoding='utf-8'),
    '/assets/js/home-v7.js':(ROOT/'assets/js/home-v7.js').read_text(encoding='utf-8'),
    '/assets/js/pricing-v7.js':(ROOT/'assets/js/pricing-v7.js').read_text(encoding='utf-8'),
    '/assets/js/status-v7.js':(ROOT/'assets/js/status-v7.js').read_text(encoding='utf-8'),
}

def route_file(route): return ROOT/'index.html' if route=='/' else ROOT/route.strip('/')/'index.html'

def data_uri(path:Path):
    mime=mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    return f'data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}'

def inline_html(route, with_scripts=True):
    html=route_file(route).read_text(encoding='utf-8')
    html=re.sub(r'<link rel="stylesheet" href="/assets/css/malach-v7\.css\?v=[^"]+">','',html)
    html=re.sub(r'<link rel="stylesheet" href="/assets/css/mobile-v72\.css\?v=[^"]+">',f'<style>{CSS}</style>',html)
    html=re.sub(r'<link rel="(?:icon|apple-touch-icon|manifest)"[^>]*>','',html)
    html=html.replace('<script defer src="/runtime-config.js"></script>','<script>window.MALACH_PUBLIC_CONFIG={appUrl:"https://app.malach.app"};</script>')
    for src,code in SCRIPTS.items():
        pattern=rf'<script type="module" src="{re.escape(src)}\?v=[^"]+"></script>'
        if with_scripts:
            html=re.sub(pattern,lambda _m:f'<script>(()=>{{{code}}})()</script>',html)
        else:
            html=re.sub(pattern,'',html)
    for match in set(re.findall(r'(/assets/media/[^"\']+)',html)):
        clean=match.split('?')[0]
        path=ROOT/clean.lstrip('/')
        if path.exists(): html=html.replace(match,data_uri(path))
    html=html.replace('<head>','<head><base href="https://malach.test/">',1)
    return html

async def mobile_layout_checks(page, route, label, errors):
    metrics=await page.evaluate('''() => ({
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
      viewport: innerWidth,
      scrollHeight: document.documentElement.scrollHeight,
      hiddenHeadings: [...document.querySelectorAll('h1,h2,h3')].filter(el => {
        const s=getComputedStyle(el),r=el.getBoundingClientRect();
        return s.display==='none'||s.visibility==='hidden'||Number(s.opacity)===0||r.width<1||r.height<1;
      }).length,
      escaped: [...document.querySelectorAll('main *')].filter(el => {
        if (el.closest('.v7-feature-grid,.v7-authority-grid,.v71-canvas-flow,.v7-channel-nav,.v71-model-tabs,.v7-signal-marquee')) return false;
        const s=getComputedStyle(el),r=el.getBoundingClientRect();
        if (s.display==='none'||s.visibility==='hidden'||Number(s.opacity)===0||r.width<1||r.height<1) return false;
        if (s.position==='absolute' && (r.left<0||r.right>innerWidth)) return false;
        return r.left < -3 || r.right > innerWidth + 3 || r.width > innerWidth + 3;
      }).slice(0,8).map(el => ({tag:el.tagName,cls:String(el.className).slice(0,80),text:(el.innerText||'').trim().slice(0,60),rect:el.getBoundingClientRect().toJSON()})),
      touchTargets: [...document.querySelectorAll('main .button, .menu-trigger, .mobile-drawer summary, .mobile-actions a')].filter(el => {
        const s=getComputedStyle(el),r=el.getBoundingClientRect();
        return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0&&r.height<40;
      }).slice(0,8).map(el => ({text:(el.innerText||'').trim(),h:Math.round(el.getBoundingClientRect().height)}))
    })''')
    if metrics['scrollWidth'] > metrics['clientWidth'] + 2:
        errors.append(f'{route}: horizontal page overflow at {label} ({metrics["scrollWidth"]}>{metrics["clientWidth"]})')
    if metrics['hiddenHeadings']:
        errors.append(f'{route}: {metrics["hiddenHeadings"]} hidden heading(s) at {label}')
    if metrics['escaped']:
        errors.append(f'{route}: content escaped viewport at {label}: {metrics["escaped"][:3]}')
    if metrics['touchTargets']:
        errors.append(f'{route}: undersized primary touch targets at {label}: {metrics["touchTargets"][:3]}')
    return metrics

async def main():
    async with async_playwright() as p:
        launch_kwargs={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']}
        system_chromium=Path('/usr/bin/chromium')
        if system_chromium.exists(): launch_kwargs['executable_path']=str(system_chromium)
        browser=await p.chromium.launch(**launch_kwargs)
        errors=[]

        # Desktop contract remains intact.
        page=await browser.new_page(viewport={'width':1440,'height':1000})
        await page.route('https://malach.test/api/health',lambda route:route.fulfill(status=200,content_type='application/json',body='{"ok":true}'))
        for route in ROUTES:
            await page.set_content(inline_html(route,False),wait_until='domcontentloaded',timeout=12000)
            if await page.evaluate('document.documentElement.scrollWidth > document.documentElement.clientWidth + 2'):
                errors.append(f'{route}: horizontal overflow at desktop')
            hidden=await page.locator('h1,h2,h3').evaluate_all('els=>els.filter(el=>{const s=getComputedStyle(el),r=el.getBoundingClientRect();return s.display==="none"||s.visibility==="hidden"||Number(s.opacity)===0||r.width<1||r.height<1}).length')
            if hidden: errors.append(f'{route}: {hidden} hidden heading(s) at desktop')
        await page.close()

        # Responsive matrix. Audit every route at core phone + tablet widths,
        # then stress the highest-risk screens at the smallest and largest phones.
        core_viewports=[
            (390,844,'iphone-15',ROUTES),
            (768,1024,'tablet-portrait',ROUTES),
        ]
        critical_routes=['/','/product/','/auto-agent/','/intelligence/','/vision/','/channels/','/pricing/','/security/','/about/','/contact/','/status/']
        stress_viewports=[
            (320,568,'iphone-se',critical_routes),
            (360,800,'compact-phone',critical_routes),
            (430,932,'large-phone',critical_routes),
        ]
        mobile_heights={}
        for width,height,label,routes in core_viewports+stress_viewports:
            page=await browser.new_page(viewport={'width':width,'height':height})
            await page.route('https://malach.test/api/health',lambda route:route.fulfill(status=200,content_type='application/json',body='{"ok":true}'))
            for route in routes:
                await page.set_content(inline_html(route,False),wait_until='domcontentloaded',timeout=12000)
                metrics=await mobile_layout_checks(page,route,label,errors)
                if route=='/': mobile_heights[label]=metrics['scrollHeight']
            await page.close()

        # Mobile home must be a genuine mobile composition, not clipped desktop content.
        page=await browser.new_page(viewport={'width':390,'height':844})
        await page.set_content(inline_html('/'),wait_until='domcontentloaded')
        await page.wait_for_timeout(160)
        if await page.evaluate('document.documentElement.dataset.v72MobileReady||""')!='true':
            errors.append('/: V7.2 mobile interaction layer did not initialize')
        hero=await page.locator('.v7-hero-copy').evaluate('el=>{const r=el.getBoundingClientRect();return {left:r.left,right:r.right,width:r.width}}')
        if hero['left'] < -1 or hero['right'] > 391 or hero['width'] > 360:
            errors.append(f'/: mobile hero copy is not contained: {hero}')
        deck=await page.locator('.v7-command-deck').evaluate('el=>{const r=el.getBoundingClientRect();return {left:r.left,right:r.right,width:r.width}}')
        if deck['left'] < -1 or deck['right'] > 391:
            errors.append(f'/: mobile command deck is not contained: {deck}')
        grid_cols=await page.locator('.v7-deck-grid').evaluate('el=>getComputedStyle(el).gridTemplateColumns')
        if ' ' in grid_cols.strip(): errors.append(f'/: mobile command deck retained multiple desktop columns: {grid_cols}')
        if await page.locator('.v72-mobile-carousel-meta').count()<2:
            errors.append('/: mobile feature/authority carousel indicators missing')
        feature=page.locator('.v7-feature-grid')
        if await feature.evaluate('el=>getComputedStyle(el).overflowX') not in ('auto','scroll'):
            errors.append('/: mobile feature deck is not touch-scrollable')
        if mobile_heights.get('iphone-15',99999) > 21500:
            errors.append(f'/: mobile homepage remains excessively long: {mobile_heights.get("iphone-15")}px')
        toggle=page.locator('[data-menu-trigger]'); await toggle.click()
        if await toggle.get_attribute('aria-expanded')!='true': errors.append('/: mobile menu did not open')
        drawer=page.locator('[data-mobile-drawer]')
        if await drawer.get_attribute('aria-hidden')!='false': errors.append('/: mobile drawer remained hidden')
        if await page.evaluate('document.body.style.overflow')!='hidden': errors.append('/: mobile menu did not lock background scroll')
        await page.close()

        # Homepage desktop interactivity.
        page=await browser.new_page(viewport={'width':1440,'height':1000})
        await page.set_content(inline_html('/'),wait_until='domcontentloaded')
        await page.wait_for_timeout(160)
        trigger=page.locator('[data-nav-trigger]').first
        await trigger.hover(); await page.wait_for_timeout(80)
        if not await trigger.evaluate('el=>el.closest("[data-nav-menu]").classList.contains("open")'):
            errors.append('/: Solutions menu did not open')
        if await page.evaluate('document.documentElement.dataset.malachReady||""')!='true': errors.append('/: V7 interaction layer did not initialize')
        if await page.evaluate('document.documentElement.dataset.v7HomeReady||""')!='true': errors.append('/: V7 homepage interaction layer did not initialize')
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
        await page.close()

        # Pricing and status functionality.
        page=await browser.new_page(viewport={'width':390,'height':844})
        await page.set_content(inline_html('/pricing/'),wait_until='domcontentloaded')
        annual=page.locator('[data-billing="annual"]'); await annual.click()
        if not await annual.evaluate('el=>el.classList.contains("active")'): errors.append('/pricing/: annual toggle failed on mobile')
        if await page.locator('[data-annual]:visible').count()<3: errors.append('/pricing/: annual prices not visible on mobile')
        await page.close()

        page=await browser.new_page(viewport={'width':390,'height':844})
        await page.route('https://malach.test/api/health',lambda route:route.fulfill(status=200,content_type='application/json',body='{"ok":true}'))
        await page.set_content(inline_html('/status/'),wait_until='domcontentloaded')
        await page.wait_for_timeout(150)
        if 'No issues detected.' not in await page.locator('body').inner_text(): errors.append('/status/: healthy state did not render on mobile')
        await page.close()

        await browser.close()
        if errors: raise AssertionError('\n'.join(errors))
        print(f'Browser smoke passed: 23 routes on desktop, all routes at phone/tablet widths, and critical screens stress-tested from 320–430px with touch containment, mobile hero/deck reflow, carousel UI, menu, pricing, status, and V7 interactions.')

if __name__=='__main__': asyncio.run(main())
