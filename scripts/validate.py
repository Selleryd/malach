#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import urlparse
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
ROUTES=['/','/product/','/solutions/','/solutions/google-ads/','/solutions/shopify/','/solutions/portfolio/','/intelligence/','/auto-agent/','/advantage/','/attribution/','/voice/','/vision/','/channels/','/pricing/','/security/','/about/','/support/','/contact/','/docs/','/status/','/privacy/','/terms/','/login/']
errors=[]

def route_file(route): return ROOT/'index.html' if route=='/' else ROOT/route.strip('/')/'index.html'

for route in ROUTES:
    if not route_file(route).exists(): errors.append(f'missing route {route}')

files=[ROOT/'404.html',*ROOT.rglob('index.html')]
for file in files:
    if not file.exists(): continue
    text=file.read_text(encoding='utf-8',errors='replace')
    soup=BeautifulSoup(text,'html.parser')
    if not soup.title or not soup.title.string or not soup.title.string.strip(): errors.append(f'{file}: missing title')
    ids=[tag.get('id') for tag in soup.find_all(attrs={'id':True})]
    if len(ids)!=len(set(ids)): errors.append(f'{file}: duplicate ids')
    if len(soup.select('body > a.skip-link'))!=1: errors.append(f'{file}: expected one skip link')
    if not soup.find('h1'): errors.append(f'{file}: missing h1')
    for img in soup.find_all('img'):
        if img.get('alt') is None: errors.append(f'{file}: image missing alt {img.get("src")}')
    for tag in soup.find_all(['a','link','script','img']):
        attr='href' if tag.name in ('a','link') else 'src'
        value=tag.get(attr)
        if not value or value.startswith(('#','mailto:','tel:','data:','javascript:','https://','http://')): continue
        path=urlparse(value).path
        if tag.name=='a':
            if path=='/': target=ROOT/'index.html'
            elif path.endswith('/'): target=ROOT/path.strip('/')/'index.html'
            elif Path(path).suffix: target=ROOT/path.lstrip('/')
            else: target=ROOT/path.strip('/')/'index.html'
        else:
            target=ROOT/path.lstrip('/')
        if not target.exists(): errors.append(f'{file}: missing target {value}')
    for forbidden in ('assets/css/styles.css','assets/css/flagship.css','assets/css/v5.css','assets/css/malach-v6.css','assets/js/site.js','assets/js/flagship.js','assets/js/malach-v6.js','theme-toggle','light-zone','cta-orbit','hero-orbit','orbit-ring'):
        if forbidden in text: errors.append(f'{file}: obsolete artifact {forbidden}')
    if 'assets/css/malach-v7.css' not in text: errors.append(f'{file}: missing V7 design system')
    if 'assets/js/malach-v7.js' not in text: errors.append(f'{file}: missing V7 interaction layer')

home=(ROOT/'index.html').read_text()
for needle in ('No more ad dollars','Your intelligence agency. Your operating force.','Advertising gets expensive when decisions get unclear.','One system. Every critical layer.','From connected data to a measured result.','Every channel through the same profit lens.','Choose exactly how much authority Malach has.','Not another dashboard. An operating system.','Turn better intelligence into better actions—around the clock.'):
    if needle not in home: errors.append(f'home missing {needle}')
for needle in ('Aster Lamp','Sora Carryall','Ember Throw','Drift Shelf','Northstar Home','proprietary algorithms','24/7','Agent Canvas','unfair advantage'):
    if needle not in home: errors.append(f'home missing invented demo entity {needle}')
for forbidden in ('Jura','posterior CVR','Cloud SQL','public interface'):
    if forbidden.lower() in home.lower(): errors.append(f'home exposes forbidden/demo copy {forbidden}')

about=(ROOT/'about/index.html').read_text()
if 'Malach means Angel and Messenger - working for you 24/7 with one goal. Making profitable decisions and actions.' not in about: errors.append('about missing requested Angel and Messenger statement')

pricing=(ROOT/'pricing/index.html').read_text()
for needle in ('$750','$1,500','$5,000','$7,500','$15,000','$50,000','Observe mode only','Priority support','Amazon Ads · coming soon'):
    if needle not in pricing: errors.append(f'pricing missing {needle}')
security=(ROOT/'security/index.html').read_text()
for needle in ('Protected account connections','Each business stays separate','You choose the level of control','Every action is traceable','Stop immediately when needed','Secure payment collection'):
    if needle not in security: errors.append(f'security missing {needle}')
for forbidden in ('Cloud SQL','Worker','Brave','public interface','Secret handling'):
    if forbidden in security: errors.append(f'security exposes internal copy {forbidden}')
status=(ROOT/'status/index.html').read_text()
for needle in ('Malach application','Sign-in &amp; account access','Malach Intelligence','Autonomous operations'):
    if needle not in status: errors.append(f'status missing {needle}')
for forbidden in ('Cloud SQL','Worker','Public website'):
    if forbidden in status: errors.append(f'status exposes {forbidden}')
for backend in ('api/create-checkout-session.js','api/create-portal-session.js','api/stripe-webhook.js','api/contact.js','api/public-config.js'):
    if not (ROOT/backend).exists(): errors.append(f'missing backend {backend}')
for asset in ('assets/css/malach-v7.css','assets/js/malach-v7.js','assets/js/home-v7.js','assets/js/pricing-v7.js','assets/js/status-v7.js'):
    if not (ROOT/asset).exists(): errors.append(f'missing asset {asset}')
if (ROOT/'changelog').exists(): errors.append('changelog should not exist')

# No accidental real-product demo names anywhere in buyer-facing pages.
for file in files:
    if file.exists() and 'Jura' in file.read_text(encoding='utf-8',errors='ignore'):
        errors.append(f'{file}: contains forbidden real product demo name Jura')

if errors:
    print('\n'.join('ERROR '+e for e in errors)); raise SystemExit(1)
print(f'PASS: {len(ROUTES)} routes, links, assets, consumer copy, invented demo data, pricing truth, and preserved APIs')
