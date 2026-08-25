#!/usr/bin/env python3
from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
errors=[]
htmls=[ROOT/'404.html',*ROOT.rglob('index.html')]
for file in htmls:
    text=file.read_text(encoding='utf-8',errors='replace')
    soup=BeautifulSoup(text,'html.parser')
    headings=soup.select('h1,h2,h3')
    if not headings: errors.append(f'{file}: no headings')
    for heading in headings:
        if not heading.get_text(' ',strip=True): errors.append(f'{file}: empty heading')
    if 'malach-v7.css' not in text: errors.append(f'{file}: not on V7 design system')
    if 'mobile-v72.css' not in text: errors.append(f'{file}: missing V7.2 mobile layer')

css=(ROOT/'assets/css/malach-v7.css').read_text()
for forbidden in ('radial-gradient(circle','scroll-behavior:smooth','background-attachment:fixed','.cta-orbit','.hero-orbit','.orbit-ring'):
    if forbidden in css: errors.append(f'css contains forbidden template/performance motif: {forbidden}')
for required in ('.v7-command-deck','.v7-command-duality','.v7-clarity-section','.v7-feature-grid','.v71-always-on-section','.v71-algorithm-section','.v71-canvas','.v7-how-section','.v7-channel-command','.v7-authority-grid','.v7-comparison','@media(max-width:820px)','prefers-reduced-motion'):
    if required not in css: errors.append(f'css missing {required}')

mobile_css=(ROOT/'assets/css/mobile-v72.css').read_text()
for required in ('scrollbar-gutter: auto','.v7-hero-layout','.v7-deck-grid','.v7-feature-grid','.v7-authority-grid','.v71-canvas-flow','.v7-flow-orchestration','env(safe-area-inset-top)'):
    if required not in mobile_css: errors.append(f'mobile css missing {required}')

js=(ROOT/'assets/js/malach-v7.js').read_text()
mobile_js=(ROOT/'assets/js/mobile-v72.js').read_text()
home=(ROOT/'assets/js/home-v7.js').read_text()
for required in ('requestAnimationFrame','IntersectionObserver','malachReady'):
    if required not in js: errors.append(f'global js missing {required}')
for required in ('setupSnapDeck','setupMobileDetails','v72MobileReady'):
    if required not in mobile_js: errors.append(f'mobile js missing {required}')
for required in ('setupHero','setupClarity','setupVision','setupFlow','setupChannels','setupAuthorityCards','setupModelLab','setupOpsClock','setupAgentCanvas','v7HomeReady'):
    if required not in home: errors.append(f'home js missing {required}')

if errors:
    print('\n'.join('ERROR '+e for e in errors)); raise SystemExit(1)
print(f'PASS: visual contract — {len(htmls)} documents, approved desktop V7.1 system plus dedicated V7.2 mobile architecture')
