#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
VERSION = "7.2.0"
APP = "https://app.malach.app"
SUPPORT = "support@malach.app"

ROUTES = [
    "/", "/product/", "/solutions/", "/solutions/google-ads/", "/solutions/shopify/",
    "/solutions/portfolio/", "/intelligence/", "/auto-agent/", "/advantage/",
    "/attribution/", "/voice/", "/vision/", "/channels/", "/pricing/",
    "/security/", "/about/", "/support/", "/contact/", "/docs/", "/status/",
    "/privacy/", "/terms/", "/login/",
]

SEARCH = [
    ("Home", "/", "Profit-first advertising operations"),
    ("Product", "/product/", "One system from signal to outcome"),
    ("Solutions", "/solutions/", "Google Ads, Shopify, portfolio and cross-channel"),
    ("Google Ads", "/solutions/google-ads/", "Connect spend to verified commerce profit"),
    ("Shopify Intelligence", "/solutions/shopify/", "See margin, returns, fees and contribution"),
    ("Portfolio Management", "/solutions/portfolio/", "Operate up to twenty isolated stores"),
    ("Intelligence", "/intelligence/", "24/7 monitoring, competitor watch and decision intelligence"),
    ("Auto Agent", "/auto-agent/", "24/7 execution with Agent Canvas and governed authority"),
    ("Advantage", "/advantage/", "Proprietary models that turn market signals into an unfair advantage"),
    ("Attribution", "/attribution/", "Match platform results to verified sales"),
    ("Malach Voice", "/voice/", "Ask your business a direct question"),
    ("Malach Vision", "/vision/", "One profit view across channels and stores"),
    ("Channels", "/channels/", "Google, Meta, TikTok and Amazon Ads"),
    ("Pricing", "/pricing/", "Core, Autonomous and Portfolio"),
    ("Security", "/security/", "Protected connections and visible control"),
    ("About", "/about/", "Why Malach exists"),
    ("Support", "/support/", "Help with account, billing and connections"),
    ("Contact", "/contact/", "Product, sales and partnership questions"),
    ("Documentation", "/docs/", "Setup and product guidance"),
    ("Status", "/status/", "Live Malach service health"),
]

SOLUTIONS = [
    ("Google Ads", "/solutions/google-ads/", "Connect spend to real contribution profit", "G"),
    ("Shopify Intelligence", "/solutions/shopify/", "See order economics, margin and returns", "S"),
    ("Attribution", "/attribution/", "Match ad-platform claims to verified sales", "A"),
    ("Advantage", "/advantage/", "Track competitors and turn market shifts into profitable moves", "↗"),
    ("Auto Agent", "/auto-agent/", "Agent Canvas plans and carries out the work 24/7", "⚡"),
    ("Malach Vision", "/vision/", "See channels and stores through one profit lens", "V"),
    ("Portfolio", "/solutions/portfolio/", "Operate up to twenty isolated stores", "20"),
    ("Malach Voice", "/voice/", "Ask your advertising operation a direct question", "◉"),
    ("Amazon Ads", "/channels/#amazon", "Portfolio integration planned next", "a"),
]

COMPANY = [
    ("About", "/about/", "Why Malach exists"),
    ("Security", "/security/", "How Malach protects access and control"),
    ("Support", "/support/", "Help with account, billing and connections"),
    ("Contact", "/contact/", "Product, partnership and sales questions"),
]

PLANS = [
    {
        "id": "core", "name": "Malach Core", "label": "INTELLIGENCE", "monthly": "$750", "annual": "$7,500",
        "save": "Save $1,500", "promise": "See. Understand. Decide.",
        "copy": "A profit-first intelligence layer for one commerce operation. Malach analyzes and recommends; you stay in control.",
        "features": ["One Shopify store", "Google Ads + Shopify intelligence", "Profit Center + Attribution", "Chat, Voice and Knowledge", "Observe mode only"],
    },
    {
        "id": "autonomous", "name": "Malach Autonomous", "label": "MOST POPULAR", "monthly": "$1,500", "annual": "$15,000",
        "save": "Save $3,000", "promise": "Decide. Execute. Compound.",
        "copy": "A 24/7 operating layer with Auto Agent, Agent Canvas and governed execution from Approval through Full Auto.",
        "features": ["Everything in Core", "Approval + Auto Agent + Canvas", "Proprietary Algorithm + Master Lab", "Canary + Full Auto", "Advantage + Evolution"],
        "featured": True,
    },
    {
        "id": "portfolio", "name": "Malach Portfolio", "label": "PORTFOLIO SCALE", "monthly": "$5,000", "annual": "$50,000",
        "save": "Save $10,000", "promise": "Govern. Scale. Unify.",
        "copy": "Multi-store and cross-channel command with per-store authority, Malach Vision and priority support.",
        "features": ["Up to 20 isolated stores", "Portfolio God View", "Meta + TikTok + Vision", "Amazon Ads · coming soon", "Priority support"],
    },
]


def attrs(**kwargs: str) -> str:
    return " ".join(f'{key.replace("_", "-")}="{escape(str(value), quote=True)}"' for key, value in kwargs.items() if value is not None)


def route_title(route: str) -> str:
    lookup = {
        "/": "Malach — No More Ad Dollars Wasted",
        "/product/": "Product — Malach",
        "/solutions/": "Solutions — Malach",
        "/solutions/google-ads/": "Google Ads — Malach",
        "/solutions/shopify/": "Shopify Intelligence — Malach",
        "/solutions/portfolio/": "Portfolio Management — Malach",
        "/intelligence/": "Intelligence — Malach",
        "/auto-agent/": "Auto Agent — Malach",
        "/advantage/": "Advantage — Malach",
        "/attribution/": "Attribution — Malach",
        "/voice/": "Malach Voice",
        "/vision/": "Malach Vision",
        "/channels/": "Advertising Channels — Malach",
        "/pricing/": "Pricing — Malach",
        "/security/": "Security — Malach",
        "/about/": "About — Malach",
        "/support/": "Support — Malach",
        "/contact/": "Contact — Malach",
        "/docs/": "Documentation — Malach",
        "/status/": "Status — Malach",
        "/privacy/": "Privacy — Malach",
        "/terms/": "Terms — Malach",
        "/login/": "Sign in — Malach",
        "/404.html": "Page not found — Malach",
    }
    return lookup[route]


def route_description(route: str) -> str:
    lookup = {
        "/": "Malach is your 24/7 autonomous advertising operator, using proprietary algorithms, real business economics and market intelligence to make evidence-based, profit-driven decisions and actions.",
        "/product/": "Explore Malach Intelligence, proprietary decision algorithms, Auto Agent, Agent Canvas, governed execution, attribution, market intelligence and portfolio operations.",
        "/solutions/": "Choose the Malach solution that matches your advertising, commerce and portfolio operating needs.",
        "/solutions/google-ads/": "Connect Google Ads performance to verified Shopify economics, contribution profit and governed execution.",
        "/solutions/shopify/": "See the order economics, margins, returns, fees and contribution behind advertising performance.",
        "/solutions/portfolio/": "Operate up to twenty isolated stores with portfolio intelligence, per-store authority and cross-channel command.",
        "/intelligence/": "Malach Intelligence monitors your business, advertising, competitors and market shifts 24/7, turning signals into evidence-based decisions and clear recommendations.",
        "/auto-agent/": "Auto Agent and Agent Canvas work 24/7 to plan, prepare and execute eligible advertising actions with the authority you choose.",
        "/advantage/": "Use competitor intelligence, probability, statistics and your own economics to turn market movement into an unfair advantage.",
        "/attribution/": "Match platform-reported performance to verified Shopify revenue and contribution profit.",
        "/voice/": "Ask Malach about profit, campaigns, products and the next action through chat and voice.",
        "/vision/": "See stores and advertising channels through one cross-channel contribution-profit lens.",
        "/channels/": "Malach connects Google Ads and Shopify today, adds Meta and TikTok in Portfolio, with Amazon Ads planned next.",
        "/pricing/": "Malach Core, Autonomous and Portfolio pricing with a three-day trial and two months free on annual billing.",
        "/security/": "Understand Malach's account protections, workspace separation, permissions, audit history and emergency controls.",
        "/about/": "Malach means Angel and Messenger—your 24/7 advertising intelligence and execution partner, built to make evidence-based, profitable decisions and actions.",
        "/support/": "Get help with your Malach account, billing, connected accounts and product use.",
        "/contact/": "Contact Malach about product, pricing, partnerships, agencies and portfolio deployments.",
        "/docs/": "Guidance for setting up Malach, connecting accounts, understanding operating modes and managing billing.",
        "/status/": "Check the current availability of the Malach application and key product services.",
        "/privacy/": "Malach privacy policy.",
        "/terms/": "Malach terms of service.",
        "/login/": "Open the Malach application.",
        "/404.html": "The requested Malach page could not be found.",
    }
    return lookup[route]


def head(route: str) -> str:
    title = route_title(route)
    description = route_description(route)
    canonical = "https://malach.app" + route
    json_ld = ""
    if route == "/":
        json_ld = '<script type="application/ld+json">' + json.dumps({
            "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Malach",
            "applicationCategory": "BusinessApplication", "operatingSystem": "Web", "url": "https://malach.app",
            "offers": [{"@type": "Offer", "name": p["name"], "price": p["monthly"].replace("$", "").replace(",", ""), "priceCurrency": "USD"} for p in PLANS],
        }) + "</script>"
    return f'''<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description, quote=True)}">
<meta name="theme-color" content="#07070b">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Malach"><meta property="og:title" content="{escape(title, quote=True)}"><meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://malach.app/assets/media/og-image.jpg">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(title, quote=True)}"><meta name="twitter:description" content="{escape(description, quote=True)}"><meta name="twitter:image" content="https://malach.app/assets/media/og-image.jpg">
<link rel="icon" href="/assets/media/favicon.ico?v={VERSION}" sizes="any">
<link rel="icon" href="/assets/media/favicon-64.png?v={VERSION}" sizes="64x64" type="image/png">
<link rel="apple-touch-icon" href="/assets/media/apple-touch-icon.png?v={VERSION}">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/assets/css/malach-v7.css?v={VERSION}">
<link rel="stylesheet" href="/assets/css/mobile-v72.css?v={VERSION}">
<script defer src="/runtime-config.js"></script>
{json_ld}
</head>'''


def header(route: str) -> str:
    def active(prefix: str) -> str:
        return ' aria-current="page"' if (route == prefix or (prefix != "/" and route.startswith(prefix))) else ""

    mega = "".join(
        f'<a class="mega-item" href="{href}"><span class="mega-glyph">{escape(glyph)}</span><span><strong>{escape(name)}</strong><small>{escape(copy)}</small></span></a>'
        for name, href, copy, glyph in SOLUTIONS
    )
    company = "".join(
        f'<a class="company-item" href="{href}"><strong>{escape(name)}</strong><small>{escape(copy)}</small></a>'
        for name, href, copy in COMPANY
    )
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header" data-header>
  <div class="scroll-line" data-scroll-line aria-hidden="true"></div>
  <div class="nav-wrap">
    <a class="brand" href="/" aria-label="Malach home">
      <img src="/assets/media/malach-mark.png" alt="">
      <span><strong>MALACH</strong><small>Advertising operations</small></span>
    </a>
    <nav class="desktop-nav" aria-label="Primary navigation">
      <a href="/product/"{active('/product/')}>Product</a>
      <div class="nav-menu" data-nav-menu>
        <button type="button" data-nav-trigger aria-expanded="false">Solutions <span>⌄</span></button>
        <div class="mega-panel" data-nav-panel aria-hidden="true">
          <div class="mega-head"><span>Solutions</span><a href="/solutions/">View all →</a></div>
          <div class="mega-grid">{mega}</div>
          <div class="mega-foot"><span>Intelligence</span><span>Execution</span><span>Portfolio scale</span></div>
        </div>
      </div>
      <a href="/intelligence/"{active('/intelligence/')}>Intelligence</a>
      <a href="/pricing/"{active('/pricing/')}>Pricing</a>
      <a href="/security/"{active('/security/')}>Security</a>
      <div class="nav-menu" data-nav-menu>
        <button type="button" data-nav-trigger aria-expanded="false">Company <span>⌄</span></button>
        <div class="company-panel" data-nav-panel aria-hidden="true">
          <div class="company-links">{company}</div>
          <aside><small>Ready to see Malach?</small><strong>Start with three days free.</strong><a class="button button-primary" href="{APP}">Open Malach</a></aside>
        </div>
      </div>
    </nav>
    <div class="nav-actions">
      <button class="search-trigger" type="button" data-command-open aria-label="Search Malach">Search <kbd>⌘K</kbd></button>
      <a class="text-link" href="{APP}">Sign in</a>
      <a class="button button-primary button-small" href="{APP}">Start free</a>
      <button class="menu-trigger" type="button" data-menu-trigger aria-label="Open menu" aria-expanded="false"><span></span><span></span></button>
    </div>
  </div>
  <div class="mobile-drawer" data-mobile-drawer aria-hidden="true">
    <nav>
      <a href="/product/">Product</a>
      <details><summary>Solutions</summary><div>{mega}</div></details>
      <a href="/intelligence/">Intelligence</a><a href="/pricing/">Pricing</a><a href="/security/">Security</a>
      <details><summary>Company</summary><div>{company}</div></details>
    </nav>
    <div class="mobile-actions"><a href="{APP}">Sign in</a><a class="button button-primary" href="{APP}">Start 3-day trial</a></div>
  </div>
</header>'''


def footer() -> str:
    return f'''<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-brand"><a class="brand" href="/"><img src="/assets/media/malach-mark.png" alt=""><span><strong>MALACH</strong><small>Advertising operations</small></span></a><p>Your 24/7 intelligence and execution team—built around profitable decisions.</p></div>
    <div><h4>Product</h4><a href="/product/">Product</a><a href="/intelligence/">Intelligence</a><a href="/auto-agent/">Auto Agent</a><a href="/vision/">Vision</a><a href="/pricing/">Pricing</a></div>
    <div><h4>Solutions</h4><a href="/solutions/google-ads/">Google Ads</a><a href="/solutions/shopify/">Shopify Intelligence</a><a href="/attribution/">Attribution</a><a href="/solutions/portfolio/">Portfolio</a><a href="/channels/">Channels</a></div>
    <div><h4>Company</h4><a href="/about/">About</a><a href="/security/">Security</a><a href="/status/">Status</a><a href="/support/">Support</a><a href="/contact/">Contact</a></div>
    <div><h4>Legal</h4><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a><a href="/docs/">Documentation</a></div>
  </div>
  <div class="footer-bottom"><span>© <span data-year></span> Malach. All rights reserved.</span><span>On your team 24/7. Evidence-based decisions. Governed execution.</span></div>
</footer>'''


def command_palette() -> str:
    items = "".join(
        f'<a href="{href}" data-command-item data-search="{escape((name + " " + copy).lower(), quote=True)}"><span>{escape(name)}</span><small>{escape(copy)}</small></a>'
        for name, href, copy in SEARCH
    )
    return f'''<div class="command-palette" data-command-palette aria-hidden="true"><button class="command-backdrop" data-command-close aria-label="Close search"></button><div class="command-dialog" role="dialog" aria-modal="true" aria-label="Search Malach"><div class="command-input-wrap"><span>⌕</span><input class="command-input" type="search" placeholder="Search Malach…" aria-label="Search pages"><kbd>Esc</kbd></div><div class="command-results">{items}</div></div></div>'''


def shell(route: str, body: str, scripts: list[str] | None = None, body_class: str = "") -> str:
    scripts = scripts or []
    script_tags = ''.join(f'<script type="module" src="{src}?v={VERSION}"></script>' for src in scripts)
    return f'''<!doctype html><html lang="en" data-malach-version="{VERSION}">{head(route)}<body class="{escape(body_class)}" data-page="{route}">{header(route)}<main id="main">{body}</main>{footer()}{command_palette()}<script type="module" src="/assets/js/malach-v7.js?v={VERSION}"></script><script type="module" src="/assets/js/mobile-v72.js?v={VERSION}"></script>{script_tags}</body></html>'''


def section_head(eyebrow: str, title: str, copy: str = "", align: str = "") -> str:
    return f'''<div class="section-head {align}"><span class="eyebrow">{escape(eyebrow)}</span><h2>{escape(title)}</h2>{f'<p>{escape(copy)}</p>' if copy else ''}</div>'''


def hero_console() -> str:
    return '''<div class="v7-command-deck" data-hero-console>
      <div class="v7-deck-topbar">
        <div class="v7-deck-brand"><img src="/assets/media/malach-mark.png" alt=""><span><strong>MALACH</strong><small>Northstar Home · Operating simulation</small></span></div>
        <div class="v7-deck-health"><i></i><span>LIVE ECONOMY</span><b>07:30 UTC</b></div>
      </div>
      <div class="v7-deck-grid">
        <aside class="v7-product-rail">
          <div class="v7-panel-label">PRODUCT SIGNALS</div>
          <button class="active" data-product-signal="aster"><span>Aster Lamp</span><small>POAS 3.18×</small><b>↑ 14%</b></button>
          <button data-product-signal="sora"><span>Sora Carryall</span><small>POAS 2.42×</small><b>↑ 7%</b></button>
          <button data-product-signal="ember"><span>Ember Throw</span><small>POAS 1.76×</small><b class="warn">↓ 5%</b></button>
          <button data-product-signal="drift"><span>Drift Shelf</span><small>POAS 2.08×</small><b>↑ 3%</b></button>
          <div class="v7-rail-summary"><small>Verified contribution</small><strong data-live-value data-base="184260">$184,260</strong><span>+18.4%</span></div>
        </aside>
        <section class="v7-deck-center">
          <div class="v7-deck-metrics">
            <div><small>Profit on ad spend</small><strong>2.61×</strong><span>healthy</span></div>
            <div><small>Attribution confidence</small><strong>89%</strong><span>verified</span></div>
            <div><small>Waste contained</small><strong>$18.4k</strong><span>30 days</span></div>
          </div>
          <div class="v7-chart-shell">
            <div class="v7-chart-head"><span>CONTRIBUTION TREND</span><div><i class="revenue"></i>Revenue <i class="profit"></i>Profit <i class="spend"></i>Spend</div></div>
            <svg class="v7-hero-chart" viewBox="0 0 760 300" role="img" aria-label="Illustrative profit and advertising trend for Northstar Home">
              <defs>
                <linearGradient id="v7ProfitFill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#da8054" stop-opacity=".34"/><stop offset="1" stop-color="#da8054" stop-opacity="0"/></linearGradient>
                <linearGradient id="v7ProfitLine" x1="0" x2="1"><stop stop-color="#e18a5d"/><stop offset=".55" stop-color="#b889bf"/><stop offset="1" stop-color="#8a6ee1"/></linearGradient>
                <filter id="v7Glow"><feGaussianBlur stdDeviation="4" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
              </defs>
              <g class="v7-chart-grid"><path d="M0 45H760M0 105H760M0 165H760M0 225H760M0 285H760"/><path d="M126 0V300M252 0V300M378 0V300M504 0V300M630 0V300"/></g>
              <path class="v7-chart-area" d="M0 246 C44 235 58 220 96 226 S155 198 194 206 S250 170 292 180 S348 142 391 150 S449 110 493 121 S552 80 596 90 S662 50 705 58 S742 28 760 22 V300H0Z"/>
              <path class="v7-chart-profit" d="M0 246 C44 235 58 220 96 226 S155 198 194 206 S250 170 292 180 S348 142 391 150 S449 110 493 121 S552 80 596 90 S662 50 705 58 S742 28 760 22"/>
              <path class="v7-chart-spend" d="M0 266 C80 258 142 263 205 254 S327 247 390 251 S520 236 585 241 S690 228 760 225"/>
              <circle class="v7-chart-pulse" cx="760" cy="22" r="5"/>
            </svg>
          </div>
          <div class="v7-deck-footer"><span><i class="google"></i>Google Ads</span><span><i class="shopify"></i>Shopify</span><span><i class="attribution"></i>Attribution reconciled</span><span>Illustrative workspace</span></div>
        </section>
        <aside class="v7-decision-card">
          <div class="v7-panel-label">NEXT EXECUTIVE DECISION</div>
          <span class="v7-decision-id">DECISION 0438 · READY</span>
          <h3>Increase high-intent search while margin remains protected.</h3>
          <p>Conversion quality cleared break-even. Aster Lamp margin and return risk remain inside the approved range.</p>
          <div class="v7-decision-stats"><div><small>Chance profitable</small><strong>82.6%</strong></div><div><small>Estimated upside</small><strong>+$4,760</strong></div><div><small>Max profitable CPC</small><strong>$4.28</strong></div><div><small>Controlled test</small><strong>$480</strong></div></div>
          <div class="authority-switch" data-authority-switch><button class="active" data-mode="observe">Observe</button><button data-mode="approval">Approval</button><button data-mode="canary">Canary</button><button data-mode="full">Full Auto</button></div>
          <div class="authority-note" data-authority-note>Malach recommends. You decide what gets executed.</div>
        </aside>
      </div>
    </div>'''


def home_page() -> str:
    plans = "".join(price_card(p, homepage=True) for p in PLANS)
    faqs = [
        ("What does Malach actually do?", "Malach works like a 24/7 intelligence and operating teammate. It watches your advertising, business economics, attribution and market signals, identifies waste and opportunity, explains the best next move, and—when you authorize it—can prepare or execute the work."),
        ("Is Malach fully autonomous?", "It can be, but only if you choose that level of authority. Start in Observe, move to Approval, test with Canary, or allow certified Full Auto execution within the limits you set."),
        ("What does Malach optimize for?", "Malach uses proprietary decision algorithms that combine your real economics with statistics, probability, attribution confidence, observed outcomes and market context. The goal is simple: make decisions that are evidence-based and profit-driven, not optimized for vanity metrics."),
        ("Which platforms does Malach support?", "Core is built around Google Ads and Shopify. Portfolio adds Meta and TikTok inside Malach Vision. Amazon Ads is the next planned Portfolio integration."),
        ("Do I stay in control?", "Yes. You choose the connected accounts, permissions and operating mode. Every recommendation and action is visible, and autonomous operation can be paused when circumstances change."),
        ("How difficult is setup?", "Malach guides account setup, email verification, billing, Google Ads and Shopify connections, operating authority and the first decision briefing step by step."),
    ]
    faq_html = "".join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in faqs)
    body = f'''
<section class="v7-hero">
  <div class="v7-hero-atmosphere" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="container v7-hero-layout">
    <div class="v7-hero-copy reveal">
      <span class="eyebrow">Autonomous profit intelligence</span>
      <h1>No more ad dollars <span>wasted.</span></h1>
      <p class="v7-hero-lead">Malach is the AI operator on your team 24/7. It combines your real business economics with proprietary algorithms, statistics, probability, attribution, competitor intelligence and measured outcomes to make evidence-based, profit-driven decisions—and, when authorized, carry them out.</p>
      <p class="v7-hero-mantra">Always watching. Always learning. Always working toward more profitable decisions.</p>
      <div class="hero-actions"><a class="button button-primary" href="{APP}">Start 3-day trial</a><a class="button button-ghost" href="#how-it-works">See how Malach works</a></div>
      <div class="v7-proof-row"><span>Works 24/7</span><span>Proprietary decision algorithms</span><span>Competitor + market intelligence</span><span>Observe → Full Auto</span></div>
    </div>
    <div class="v7-hero-stage reveal" data-hero-stage>{hero_console()}</div>
  </div>
  <div class="v7-signal-marquee" aria-label="Malach operating capabilities"><div><span>PROFIT CENTER</span><i></i><span>ATTRIBUTION</span><i></i><span>AUTO AGENT</span><i></i><span>MALACH VISION</span><i></i><span>ADVANTAGE</span><i></i><span>VOICE + CHAT</span><i></i><span>GOVERNED EXECUTION</span><i></i><span>PROFIT CENTER</span></div></div>
</section>

<section class="section v7-command-section">
  <div class="container">
    <div class="v7-command-intro">{section_head('The Malach doctrine','Your intelligence agency. Your operating force.','Malach watches your business and the market around it, separates signal from noise, models the odds, and when authorized, does the work. Think of it as the intelligence layer that sees the field and the operating layer that moves on it—24/7.','wide')}</div>
    <div class="v7-command-duality" data-command-duality>
      <article class="v7-command-half intelligence">
        <div class="v7-command-number">01</div><span class="v7-command-kicker">INTELLIGENCE COMMAND</span><h3>Know what is happening before it costs you.</h3><p>Malach continuously watches performance, competitors, product economics, attribution and market movement—then tells you what matters, what changed and where the opportunity is.</p>
        <div class="v7-intel-scan"><div><span>Waste signal</span><strong>Search leakage</strong><b>−$6.8k</b></div><div><span>Opportunity signal</span><strong>Aster Lamp demand</strong><b>+$12.4k</b></div><div><span>Risk signal</span><strong>Ember Throw returns</strong><b>watch</b></div></div>
      </article>
      <div class="v7-command-core"><span>ONE PROFIT DOCTRINE</span><strong>Evidence → Decision → Action → Outcome</strong><i></i></div>
      <article class="v7-command-half execution">
        <div class="v7-command-number">02</div><span class="v7-command-kicker">EXECUTION UNIT</span><h3>Turn the right decision into real work.</h3><p>Auto Agent and Agent Canvas turn the recommendation into a real operating plan. Malach can prepare the work, wait for approval, run a controlled test or execute autonomously inside the limits you choose.</p>
        <div class="v7-execution-queue"><div><b>READY</b><span>Increase Northstar Search 12%</span><em>82.6%</em></div><div><b>WATCH</b><span>Hold Ember Throw prospecting</span><em>61.2%</em></div><div><b>TEST</b><span>Expand Sora Carryall remarketing</span><em>74.8%</em></div></div>
      </article>
    </div>
  </div>
</section>

<section class="section v71-always-on-section">
  <div class="container v71-always-on-layout">
    <div>{section_head('Always on your team','Malach never clocks out.','Advertising changes after hours. Competitors move. Costs shift. Opportunities appear and disappear. Malach keeps watching, thinking and working 24/7 so important changes do not have to wait for the next meeting.')}</div>
    <div class="v71-ops-clock" data-ops-clock>
      <div class="v71-ops-head"><span><i></i> LIVE OPERATING WATCH</span><b data-ops-time>07:30:00</b></div>
      <div class="v71-ops-events">
        <article class="active"><time>02:13</time><div><strong>Competitor move detected</strong><small>Category promotion depth increased.</small></div><em>INTELLIGENCE</em></article>
        <article><time>04:48</time><div><strong>Waste contained</strong><small>Search spend crossed the contribution-safe boundary.</small></div><em>PROTECTED</em></article>
        <article><time>07:30</time><div><strong>Decision briefing ready</strong><small>Three material moves ranked by expected profit.</small></div><em>BRIEFED</em></article>
        <article><time>12:16</time><div><strong>Auto Agent work prepared</strong><small>Agent Canvas assembled evidence, decision and action.</small></div><em>READY</em></article>
        <article><time>19:42</time><div><strong>Outcome measured</strong><small>Measured contribution exceeded expected upside.</small></div><em>LEARNED</em></article>
      </div>
    </div>
  </div>
</section>

<section class="section v7-clarity-section" data-clarity-root>
  <div class="container v7-clarity-layout">
    <div class="v7-clarity-copy">{section_head('Why Malach','Advertising gets expensive when decisions get unclear.','Most teams piece together channel dashboards, store performance, attribution noise and campaign behavior by hand. Malach turns that fragmentation into one operating system built around profit.')}
      <div class="v7-clarity-toggle" role="group" aria-label="Compare fragmented tools with Malach"><button class="active" data-clarity="fragmented">Before Malach</button><button data-clarity="unified">With Malach</button></div>
      <p data-clarity-copy>Disconnected dashboards create delayed, reactive decisions.</p>
    </div>
    <div class="v7-clarity-stage">
      <div class="v7-fragmented-view active" data-clarity-panel="fragmented"><article><span>GOOGLE ADS</span><strong>ROAS 4.1×</strong><small>Platform-reported</small></article><article><span>SHOPIFY</span><strong>$842k revenue</strong><small>Margin unclear</small></article><article><span>ATTRIBUTION</span><strong>9% gap</strong><small>Needs reconciliation</small></article><article><span>SPREADSHEET</span><strong>Last updated 2d ago</strong><small>Manual model</small></article><div class="v7-fragment-lines"><i></i><i></i><i></i></div></div>
      <div class="v7-unified-view" data-clarity-panel="unified"><div class="v7-unified-head"><span>MALACH OPERATING PICTURE</span><b>VERIFIED</b></div><strong>$184,260</strong><small>Contribution profit</small><div class="v7-unified-bars"><i style="--w:88%"></i><i style="--w:62%"></i><i style="--w:41%"></i></div><p>One economic model. One decision brief. One measured outcome.</p></div>
    </div>
  </div>
</section>

<section class="section v7-capability-section" id="features">
  <div class="container">
    {section_head('The operating system','One system. Every critical layer.','Each Malach capability uses the same verified commerce context—so intelligence, action and measurement never drift apart.','wide')}
    <div class="v7-feature-grid">
      <article class="v7-feature-card v7-feature-wide" data-tilt-surface><div class="v7-feature-copy"><span>01 · INTELLIGENCE CENTER</span><h3>See the full picture.</h3><p>Malach Intelligence works around the clock, monitoring your numbers, competitors, demand, attribution and meaningful market shifts—then turns the noise into a short list of what deserves your attention.</p><a href="/intelligence/">Explore Intelligence →</a></div><div class="v7-mini-console intelligence"><div class="v7-mini-head"><span>DAILY BRIEFING</span><b>3 decisions</b></div><div class="v7-mini-list"><div><i>01</i><span><strong>Search waste increased</strong><small>Two campaigns explain 76% of the decline.</small></span><em>Investigate</em></div><div><i>02</i><span><strong>Margin-safe headroom</strong><small>Aster Lamp can absorb approximately $290/day.</small></span><em>Opportunity</em></div><div><i>03</i><span><strong>Attribution drift</strong><small>Platform value exceeds verified sales by 9%.</small></span><em>Reconcile</em></div></div></div></article>
      <article class="v7-feature-card" data-tilt-surface><div class="v7-feature-copy"><span>02 · AUTO AGENT</span><h3>Move from insight to action.</h3><p>Auto Agent does more than recommend. It uses Agent Canvas to plan the work, gather the evidence, prepare each step and carry it out 24/7 according to the authority you choose.</p><a href="/auto-agent/">Explore Auto Agent →</a></div><div class="v7-mini-console agent"><div class="v7-agent-state"><span>PROPOSED ACTION</span><b>READY</b></div><strong>Increase high-intent budget 12%</strong><div class="v7-agent-metrics"><span>82.6% profitable</span><span>+$4,760 upside</span></div><div class="v7-agent-mode"><i></i><span>Approval required</span></div></div></article>
      <article class="v7-feature-card" data-tilt-surface><div class="v7-feature-copy"><span>03 · PROFIT CENTER</span><h3>Optimize for what remains.</h3><p>Revenue, product cost, fees, shipping, returns and ad spend come together in one contribution-profit view.</p><a href="/attribution/">Explore Profit Center →</a></div><div class="v7-mini-console profit"><div class="v7-profit-total"><small>CONTRIBUTION PROFIT</small><strong>$184,260</strong><b>+18.4%</b></div><div class="v7-waterfall-mini"><i style="--h:86%"></i><i style="--h:36%"></i><i style="--h:21%"></i><i style="--h:45%"></i><i class="good" style="--h:38%"></i></div></div></article>
      <article class="v7-feature-card" data-tilt-surface><div class="v7-feature-copy"><span>04 · ATTRIBUTION</span><h3>Know what actually drove the result.</h3><p>Malach reconciles platform claims against verified store outcomes and makes uncertainty visible before it influences a decision.</p><a href="/attribution/">Explore Attribution →</a></div><div class="v7-mini-console attribution"><div class="v7-attribution-flow"><span>GOOGLE<br><b>$92k</b></span><i></i><span>MALACH<br><b>89%</b></span><i></i><span>SHOPIFY<br><b>$84k</b></span></div><p>9% reporting gap identified and isolated.</p></div></article>
      <article class="v7-feature-card v7-feature-wide" data-tilt-surface><div class="v7-feature-copy"><span>05 · MALACH VISION</span><h3>See across channels, not in silos.</h3><p>Portfolio connects Google, Meta, TikTok and store economics through one contribution model, with Amazon Ads planned next.</p><a href="/vision/">Explore Vision →</a></div><div class="v7-mini-console vision"><div class="v7-vision-tabs"><button class="active" data-vision-channel="portfolio">Portfolio</button><button data-vision-channel="google">Google</button><button data-vision-channel="meta">Meta</button><button data-vision-channel="tiktok">TikTok</button></div><div class="v7-vision-total"><span>VERIFIED CONTRIBUTION</span><strong data-vision-value>$438,200</strong><b>+12.8%</b></div><div class="v7-vision-bars"><div><span>Google</span><i style="--w:88%"></i><b>$284k</b></div><div><span>Meta</span><i style="--w:54%"></i><b>$96k</b></div><div><span>TikTok</span><i style="--w:34%"></i><b>$58k</b></div></div></div></article>
      <article class="v7-feature-card" data-tilt-surface><div class="v7-feature-copy"><span>06 · CHAT + VOICE</span><h3>Ask like an executive.</h3><p>Ask what changed, what is wasting spend, which products deserve more budget, or what Malach would test next.</p><a href="/voice/">Explore Chat + Voice →</a></div><div class="v7-mini-console chat"><div class="v7-chat-user">Where am I wasting money?</div><div class="v7-chat-answer"><img src="/assets/media/malach-mark.png" alt=""><span><strong>Two campaigns explain most of the waste.</strong><small>Brand Broad and Ember Throw prospecting spent $6,820 above the contribution-safe range.</small></span></div><div class="v7-chat-input">Ask Malach about profit, campaigns or the next action…</div></div></article>
      <article class="v7-feature-card" data-tilt-surface><div class="v7-feature-copy"><span>07 · ADVANTAGE</span><h3>See the market before it moves you.</h3><p>Advantage combines competitor monitoring and market movement with your own economics and Malach’s proprietary decision models—so changes outside your account become an actionable edge, not more noise.</p><a href="/advantage/">Explore Advantage →</a></div><div class="v7-mini-console market"><div class="v7-market-head"><span>MARKET SIGNALS</span><b>3 material shifts</b></div><div class="v7-market-list"><div><i>01</i><span><strong>Competitor promotion accelerated</strong><small>Category discount depth increased 8%.</small></span><em>WATCH</em></div><div><i>02</i><span><strong>High-intent demand expanded</strong><small>Search interest rose across two measured windows.</small></span><em>MOVE</em></div><div><i>03</i><span><strong>Aster Lamp position strengthened</strong><small>Contribution-safe impression share is available.</small></span><em>OPPORTUNITY</em></div></div></div></article>
    </div>
  </div>
</section>

<section class="section v71-algorithm-section" data-model-lab>
  <div class="container">
    {section_head('Proprietary decision engine','Turn math, statistics and your economics into an unfair advantage.','Malach does not make advertising decisions from one metric or a generic AI prompt. Its proprietary algorithms combine your business economics, attribution confidence, statistical patterns, probability, competitor movement and measured outcomes to build an evidence-based case for the next profitable move.','wide')}
    <div class="v71-model-shell">
      <div class="v71-model-tabs" role="tablist" aria-label="Illustrative Malach decision models"><button class="active" data-model-case="aster">Aster Lamp</button><button data-model-case="sora">Sora Carryall</button><button data-model-case="ember">Ember Throw</button></div>
      <div class="v71-model-grid">
        <div class="v71-model-inputs">
          <div><small>Contribution / conversion</small><strong data-model-margin>$84</strong></div>
          <div><small>Attribution confidence</small><strong data-model-confidence>89%</strong></div>
          <div><small>Profit-safe CPC</small><strong data-model-cpc>$3.84</strong></div>
          <div><small>Market pressure</small><strong data-model-market>+12%</strong></div>
          <div class="v71-probability"><span>PROBABILITY MODEL</span><i><b data-model-probability style="--prob:82.6%"></b></i><em data-model-probability-label>82.6% likely profitable</em></div>
        </div>
        <div class="v71-model-decision">
          <span>PROPRIETARY MODEL OUTPUT</span>
          <h3 data-model-title>Increase high-intent search 12%.</h3>
          <p data-model-reason>Margin buffer, verified attribution and demand strength support a controlled expansion.</p>
          <div><small>Estimated contribution</small><strong data-model-upside>+$4,760</strong></div>
          <div class="v71-evidence-chips"><i>Economics</i><i>Probability</i><i>Attribution</i><i>Competitors</i><i>Outcomes</i></div>
        </div>
      </div>
      <footer><span>Illustrative model · invented demonstration data</span><strong>Evidence in. Profitable decisions out.</strong></footer>
    </div>
  </div>
</section>

<section class="section v71-auto-work-section">
  <div class="container v71-auto-work-layout">
    <div>{section_head('Auto Agent + Agent Canvas','Malach does not just tell you what to do. It does the work.','Auto Agent is the 24/7 operator. Agent Canvas is the visible workspace where Malach turns an opportunity into evidence, a decision, an action plan and a measured result. You can watch the work happen and choose how much authority it has.') }<div class="v71-auto-badges"><span>Always on</span><span>Visible work plan</span><span>Approval → Full Auto</span><span>Outcome measured</span></div><a class="text-cta" href="/auto-agent/">See Auto Agent + Canvas →</a></div>
    <div class="v71-canvas compact" data-v71-canvas>
      <div class="v71-canvas-head"><span>AGENT CANVAS · ACTION 0438</span><b>WORKING 24/7</b></div>
      <div class="v71-canvas-flow"><button class="active" data-canvas-step="signal"><i>01</i><strong>Signal</strong><small>Opportunity detected</small></button><button data-canvas-step="evidence"><i>02</i><strong>Evidence</strong><small>Economics verified</small></button><button data-canvas-step="decision"><i>03</i><strong>Decision</strong><small>Move modeled</small></button><button data-canvas-step="action"><i>04</i><strong>Action</strong><small>Prepared / executed</small></button><button data-canvas-step="outcome"><i>05</i><strong>Outcome</strong><small>Result measured</small></button></div>
      <div class="v71-canvas-stage"><span data-canvas-kicker>OPPORTUNITY DETECTED</span><h3 data-canvas-title>Aster Lamp demand moved above the profit-safe threshold.</h3><p data-canvas-copy>Malach is gathering the economics, attribution and market evidence needed to decide whether the opportunity deserves action.</p><div class="v71-canvas-meta"><span>Northstar Home</span><span>Google Ads</span><span>82.6% confidence</span></div></div>
    </div>
  </div>
</section>

<section class="section v7-how-section" id="how-it-works" data-flow-root>
  <div class="container v7-how-layout">
    <div class="v7-how-copy">{section_head('How it works','From connected data to a measured result.','Malach uses one continuous loop so the reasoning behind a decision is preserved all the way through execution and outcome measurement.')}
      <div class="v7-flow-steps"><button class="active" data-flow-step="connect"><i>01</i><span><strong>Connect</strong><small>Link ads and commerce data.</small></span></button><button data-flow-step="analyze"><i>02</i><span><strong>Analyze</strong><small>Use your economics, statistics and probability to model the best move.</small></span></button><button data-flow-step="act"><i>03</i><span><strong>Recommend or act</strong><small>Use the authority you selected.</small></span></button><button data-flow-step="learn"><i>04</i><span><strong>Measure and learn</strong><small>Measure the result and improve the next move.</small></span></button></div>
    </div>
    <div class="v7-flow-stage">
      <div class="v7-flow-orchestration"><div class="v7-flow-node source"><span>GOOGLE ADS</span><b>Spend + demand</b></div><div class="v7-flow-node source"><span>SHOPIFY</span><b>Orders + margin</b></div><div class="v7-flow-node core"><img src="/assets/media/malach-mark.png" alt=""><strong>MALACH</strong><small data-flow-title>CONNECTED ECONOMICS</small></div><div class="v7-flow-node output"><span>NEXT MOVE</span><b data-flow-output>One verified operating picture</b></div><svg viewBox="0 0 800 460" aria-hidden="true"><path d="M160 120 C280 120 280 220 385 220"/><path d="M160 340 C280 340 280 240 385 240"/><path d="M500 230 C610 230 610 230 700 230"/></svg></div>
      <p data-flow-copy>Malach connects channel activity to actual store economics before making a recommendation.</p>
    </div>
  </div>
</section>

<section class="section v7-channel-section">
  <div class="container">
    {section_head('Connected growth stack','Every channel through the same profit lens.','Malach gives each channel context from the rest of the operation, so budget decisions are not made inside isolated platform dashboards.','wide')}
    <div class="v7-channel-command" data-channel-command>
      <div class="v7-channel-nav" role="tablist"><button class="active" data-channel="google">Google Ads</button><button data-channel="shopify">Shopify</button><button data-channel="meta">Meta Ads</button><button data-channel="tiktok">TikTok Ads</button><button data-channel="amazon">Amazon Ads <small>soon</small></button></div>
      <div class="v7-channel-stage"><div class="v7-channel-copy"><span data-channel-tier>CORE FOUNDATION</span><h3 data-channel-title>Google Ads intelligence with real commerce context.</h3><p data-channel-copy>Malach connects campaign behavior, search demand and spend to verified margin, attribution and contribution—not platform ROAS alone.</p><a data-channel-link href="/solutions/google-ads/">Explore Google Ads →</a></div><div class="v7-channel-visual"><div class="v7-channel-screen"><div><small>SEARCH OPPORTUNITY</small><strong data-channel-metric>+$4,760</strong></div><div class="v7-channel-spark"><i></i></div><p data-channel-finding>High-intent demand remains profitable below the rational CPC ceiling.</p></div></div></div>
    </div>
  </div>
</section>

<section class="section v7-authority-section">
  <div class="container">
    {section_head('Governed autonomy','Choose exactly how much authority Malach has.','You keep ownership of the boundary. Malach scales the speed, consistency and discipline inside it.','wide')}
    <div class="v7-authority-grid" data-authority-cards><article class="active" data-authority-card="observe"><span>01</span><h3>Observe</h3><p>Malach watches, analyzes and recommends. You execute every change.</p><b>INTELLIGENCE ONLY</b></article><article data-authority-card="approval"><span>02</span><h3>Approval</h3><p>Malach prepares executable actions and waits for your approval.</p><b>HUMAN IN THE LOOP</b></article><article data-authority-card="canary"><span>03</span><h3>Canary</h3><p>Malach runs a tightly controlled test before broader authority is used.</p><b>LIMITED TEST</b></article><article data-authority-card="full"><span>04</span><h3>Full Auto</h3><p>Malach executes certified actions within the permissions and safeguards you set.</p><b>GOVERNED EXECUTION</b></article></div>
    <div class="v7-authority-status"><span data-authority-status>Observe mode · No ad-platform execution</span><div><i>Emergency stop ready</i><i>Complete action history</i><i>Change confirmation</i></div></div>
  </div>
</section>

<section class="section v7-not-dashboard-section">
  <div class="container v7-not-dashboard-layout">
    <div>{section_head('Why it is different','Not another dashboard. An operating system.','Dashboards show numbers. Malach interprets them, prioritizes them, connects them to profit, and—when authorized—turns them into measured action.')}</div>
    <div class="v7-comparison"><article><span>TYPICAL TOOL</span><div><i>01</i><p>Reports channel metrics in isolation</p></div><div><i>02</i><p>Leaves interpretation to the operator</p></div><div><i>03</i><p>Creates more monitoring work</p></div><div><i>04</i><p>Stops before execution and outcome</p></div></article><article class="malach"><span>MALACH</span><div><i>01</i><p>Connects channels to store economics</p></div><div><i>02</i><p>Explains the signal and the next move</p></div><div><i>03</i><p>Operates within explicit authority</p></div><div><i>04</i><p>Measures what happened afterward</p></div></article></div>
  </div>
</section>

<section class="section pricing-section v7-pricing-section" id="pricing"><div class="container"><div class="section-head center"><span class="eyebrow">Pricing</span><h2>Choose your level of intelligence and authority.</h2><p>Start with three days free. Choose monthly flexibility or receive two months free with annual billing.</p></div><div class="pricing-toggle" role="group" aria-label="Billing interval"><button class="active" data-billing="monthly">Monthly</button><button data-billing="annual">Annual <span>2 months free</span></button></div><div class="pricing-grid">{plans}</div><p class="seat-note">Additional seats: $50/month or $500/year.</p></div></section>

<section class="section faq-section v7-faq-section"><div class="container faq-layout"><div>{section_head('Questions','Straight answers before you connect anything.','Understand what Malach does, how authority works, and which plan fits your operation.')}</div><div class="faq-list">{faq_html}</div></div></section>
<section class="final-cta v7-final-cta"><div class="container"><div class="cta-copy"><span class="eyebrow">Put a 24/7 operator on your team</span><h2>Turn better intelligence into better actions—around the clock.</h2><p>Connect Malach and see what changes when your economics, competitors, algorithms and execution finally work together.</p></div><div class="cta-actions"><a class="button button-primary" href="{APP}">Start 3-day trial</a><a class="button button-ghost" href="/contact/">Talk to Malach</a></div></div></section>
'''
    return shell("/", body, ["/assets/js/home-v7.js", "/assets/js/pricing-v7.js"], "home-page v7-home")


def story_economics() -> str:
    return '''<article class="story-panel active" data-story-panel="economics"><div class="story-panel-head"><span>PROFIT CENTER</span><span>Verified economics</span></div><div class="profit-grid"><div class="profit-primary"><small>Contribution profit</small><strong>$184,260</strong><span>+18.4%</span></div><div><small>Revenue</small><strong>$842,410</strong></div><div><small>Product cost</small><strong>−$306,880</strong></div><div><small>Fees + shipping</small><strong>−$118,470</strong></div><div><small>Ad spend</small><strong>−$232,800</strong></div></div><div class="waterfall"><i style="--h:78%"></i><i style="--h:29%"></i><i style="--h:18%"></i><i style="--h:36%"></i><i class="profit" style="--h:31%"></i></div><div class="story-foot"><span>Revenue</span><span>Costs</span><span>Fees</span><span>Spend</span><span>Profit</span></div></article>'''


def story_briefing() -> str:
    rows = [("01", "Search efficiency deteriorated", "Two campaigns explain 76% of the POAS decline.", "Investigate"), ("02", "Budget headroom remains", "Northstar Search can absorb approximately $290/day.", "Opportunity"), ("03", "Attribution gap widened", "Google-reported value exceeds verified Shopify revenue by 9%.", "Reconcile")]
    return '<article class="story-panel" data-story-panel="briefing"><div class="story-panel-head"><span>DAILY DECISION BRIEFING</span><span>07:30 UTC</span></div><div class="brief-list">' + ''.join(f'<div><b>{n}</b><span><strong>{t}</strong><small>{c}</small></span><em>{a}</em></div>' for n,t,c,a in rows) + '</div></article>'


def story_authority() -> str:
    return '''<article class="story-panel" data-story-panel="authority"><div class="story-panel-head"><span>OPERATING AUTHORITY</span><span>Owner controlled</span></div><div class="authority-ladder"><div class="active"><span>01</span><strong>Observe</strong><p>Analyze and recommend. No ad-platform execution.</p></div><div><span>02</span><strong>Approval</strong><p>Prepare executable actions for human approval.</p></div><div><span>03</span><strong>Canary</strong><p>Test eligible actions in a controlled rollout.</p></div><div><span>04</span><strong>Full Auto</strong><p>Execute certified actions within configured safeguards.</p></div></div></article>'''


def story_outcome() -> str:
    return '''<article class="story-panel" data-story-panel="outcome"><div class="story-panel-head"><span>OUTCOME LEDGER</span><span>Measured after action</span></div><div class="outcome-summary"><div><small>Action</small><strong>Raised search budget 12%</strong></div><div><small>Expected contribution</small><strong>+$3,840</strong></div><div><small>Measured contribution</small><strong>+$4,120</strong></div><div><small>Validation</small><strong class="healthy">Applied correctly</strong></div></div><div class="outcome-trace"><span>Evidence captured</span><i></i><span>Action applied</span><i></i><span>Platform verified</span><i></i><span>Outcome measured</span></div></article>'''


def authority_visual() -> str:
    return '''<div class="authority-visual"><div class="authority-axis"><span>INTELLIGENCE</span><span>EXECUTION</span></div><div class="authority-cards"><article class="active"><span>01</span><h3>Observe</h3><p>Malach sees and recommends. You act.</p></article><article><span>02</span><h3>Approval</h3><p>Malach prepares. You approve.</p></article><article><span>03</span><h3>Canary</h3><p>Malach tests inside a controlled boundary.</p></article><article><span>04</span><h3>Full Auto</h3><p>Malach acts only within the limits you approved.</p></article></div><div class="authority-safety"><span>Emergency stop</span><span>Complete action history</span><span>Change confirmation</span><span>Outcome measurement</span></div></div>'''


def vision_visual() -> str:
    return '''<div class="vision-console"><div class="vision-head"><span>VERIFIED CONTRIBUTION BY CHANNEL</span><strong>$438,200</strong><em>+12.8%</em></div><div class="channel-bars"><div><span>Google Ads</span><i style="--w:88%"></i><b>$284k</b></div><div><span>Meta Ads</span><i style="--w:54%"></i><b>$96k</b></div><div><span>TikTok Ads</span><i style="--w:34%"></i><b>$58k</b></div><div class="muted"><span>Amazon Ads</span><i style="--w:0%"></i><b>Coming soon</b></div></div><div class="vision-findings"><div><span>01</span><p>Meta prospecting is creating assisted Google conversion value.</p></div><div><span>02</span><p>TikTok creative lift held across three measured windows.</p></div><div><span>03</span><p>Branded search is absorbing upper-funnel demand.</p></div></div></div>'''


def price_card(plan: dict, homepage: bool = False) -> str:
    features = ''.join(f'<li>{escape(f)}</li>' for f in plan['features'])
    featured = ' featured' if plan.get('featured') else ''
    cta = f'{APP}/?plan={plan["id"]}&billing=monthly'
    return f'''<article class="price-card{featured}" data-plan-card data-plan="{plan['id']}"><div class="price-label">{escape(plan['label'])}</div><h3>{escape(plan['name'])}</h3><strong class="plan-promise">{escape(plan['promise'])}</strong><p>{escape(plan['copy'])}</p><div class="price"><span data-monthly>{plan['monthly']}</span><span data-annual hidden>{plan['annual']}</span><small data-monthly>/month</small><small data-annual hidden>/year</small></div><div class="annual-copy" data-annual hidden><b>2 months free</b><span>{escape(plan['save'])}</span></div><ul>{features}</ul><a class="button {'button-primary' if plan.get('featured') else 'button-ghost'}" data-plan-cta href="{cta}">{'Start Autonomous free' if plan.get('featured') else 'Explore ' + plan['name'].replace('Malach ', '')}</a></article>'''


def page_hero(eyebrow: str, title: str, copy: str, actions: str = "", visual: str = "") -> str:
    return f'''<section class="subhero"><div class="subhero-beam" aria-hidden="true"></div><div class="container subhero-grid"><div class="subhero-copy reveal"><span class="eyebrow">{escape(eyebrow)}</span><h1>{escape(title)}</h1><p>{escape(copy)}</p>{actions}</div>{visual}</div></section>'''


def feature_rows(items: list[tuple[str,str,str]]) -> str:
    return '<div class="feature-rows">' + ''.join(f'<article><span>{i:02d}</span><h3>{escape(title)}</h3><p>{escape(copy)}</p></article>' for i,(title,copy,_) in enumerate(items,1)) + '</div>'


def generic_page(route: str, eyebrow: str, title: str, copy: str, body: str, visual: str = "", scripts: list[str] | None = None, body_class: str = "subpage") -> str:
    actions = f'<div class="hero-actions"><a class="button button-primary" href="{APP}">Start 3-day trial</a><a class="button button-ghost" href="/pricing/">View pricing</a></div>'
    return shell(route, page_hero(eyebrow,title,copy,actions,visual) + body + closing_cta(), scripts, body_class)


def closing_cta() -> str:
    return f'''<section class="final-cta"><div class="container"><div class="cta-copy"><span class="eyebrow">See Malach in your operation</span><h2>Connect the economics before you delegate the execution.</h2><p>Start with three days free and inspect the intelligence, controls and evidence before billing begins.</p></div><div class="cta-actions"><a class="button button-primary" href="{APP}">Start free</a><a class="button button-ghost" href="/contact/">Talk to Malach</a></div></div></section>'''


def product_page() -> str:
    visual = '<div class="subhero-visual">' + authority_visual() + '</div>'
    body = f'''<section class="section"><div class="container">{section_head('Product structure','One product. Three levels of leverage.','Core gives you the intelligence. Autonomous adds a 24/7 execution team through Auto Agent and Agent Canvas. Portfolio adds multi-store and cross-channel scale.')}<div class="tier-architecture"><article><span>01</span><h3>Core</h3><strong>Intelligence</strong><p>Profit Center, Attribution, forecasts, competitor and market monitoring, Chat, Voice, Knowledge and Observe mode.</p></article><article><span>02</span><h3>Autonomous</h3><strong>24/7 execution</strong><p>Approval, Auto Agent, Agent Canvas, proprietary decision algorithms, Master Lab, Canary and Full Auto authority.</p></article><article><span>03</span><h3>Portfolio</h3><strong>Scale</strong><p>Up to twenty stores, God View, Meta, TikTok, Vision and priority support.</p></article></div></div></section>
<section class="section section-copper"><div class="container">{section_head('Proprietary decision engine','Your economics in. Evidence-based decisions out.','Malach combines your margins, costs, attribution, conversion behavior, competitor movement and real outcomes with proprietary statistical and probabilistic models. It does not replace judgment with a black box—it gives your operation a faster, more consistent decision system.')}<div class="v71-model-ribbon"><article><span>01</span><strong>Economics</strong><p>Your true margins, costs and break-even points.</p></article><article><span>02</span><strong>Evidence</strong><p>Attribution, conversion quality, market signals and outcomes.</p></article><article><span>03</span><strong>Probability</strong><p>How likely the move is to produce a profitable result.</p></article><article><span>04</span><strong>Action</strong><p>The highest-value move within the authority you chose.</p></article></div><div class="product-mosaic"><article class="wide">{story_economics()}</article><article>{story_briefing()}</article><article>{story_outcome()}</article></div></div></section>'''
    return generic_page('/product/','Product','Intelligence that thinks. An operating layer that works.','Malach combines proprietary decision algorithms, real business economics and a 24/7 execution system so you can move from signal to measured action without stitching together five different tools.',body,visual)


def solutions_page() -> str:
    cards = ''.join(f'<a class="solution-card" href="{href}"><span class="solution-glyph">{escape(glyph)}</span><div><h3>{escape(name)}</h3><p>{escape(copy)}</p></div><b>→</b></a>' for name,href,copy,glyph in SOLUTIONS)
    body = f'''<section class="section"><div class="container">{section_head('Choose the operating problem','Start where the economics are hardest to see.','Malach solutions share one foundation: verified commerce economics, visible reasoning and explicit authority.')}<div class="solutions-grid">{cards}</div></div></section>'''
    return generic_page('/solutions/','Solutions','A clearer operating picture for every paid-acquisition decision.','Choose the problem Malach should solve first—from Google Ads and Shopify economics to autonomous execution and portfolio command.',body)


def google_page() -> str:
    visual = '<div class="subhero-visual">' + hero_console() + '</div>'
    body = f'''<section class="section"><div class="container">{section_head('Google Ads intelligence','See beyond platform ROAS.','Malach connects spend, clicks, campaigns and product performance to real margin and verified Shopify outcomes.')}<div class="feature-spread"><article><span>01</span><h3>Campaign economics</h3><p>Evaluate Search, Shopping and PMax against contribution—not just platform revenue.</p></article><article><span>02</span><h3>Opportunity detection</h3><p>Find budget headroom, keyword opportunity, creative fatigue and spend saturation.</p></article><article><span>03</span><h3>Governed execution</h3><p>Move from recommendation to Approval, Canary or Full Auto when your plan and authority allow it.</p></article></div></div></section>'''
    return generic_page('/solutions/google-ads/','Google Ads','Connect campaign performance to real profit.','Malach makes Google Ads decisions with Shopify economics, attribution context and explicit execution authority.',body,visual)


def shopify_page() -> str:
    visual = '<div class="subhero-visual">' + story_economics() + '</div>'
    body = f'''<section class="section"><div class="container">{section_head('Commerce economics','Know what is left after the sale.','Revenue becomes useful only after product cost, fees, shipping, returns, discounts and ad spend are accounted for.')}<div class="commerce-grid"><article><strong>Revenue</strong><span>$842,410</span><p>Verified Shopify sales.</p></article><article><strong>Product cost</strong><span>−$306,880</span><p>COGS at product and order level.</p></article><article><strong>Fees + shipping</strong><span>−$118,470</span><p>Processing, fulfillment and shipping economics.</p></article><article><strong>Contribution profit</strong><span>$184,260</span><p>What remained after the operating costs Malach can see.</p></article></div></div></section>'''
    return generic_page('/solutions/shopify/','Shopify Intelligence','See the economics behind every advertising result.','Malach connects order data, margin, fees, shipping, discounts and returns to the campaigns that created the sale.',body,visual)


def portfolio_page() -> str:
    visual = '<div class="subhero-visual">' + vision_visual() + '</div>'
    body = f'''<section class="section"><div class="container">{section_head('Portfolio command','One executive view. Separate authority underneath.','Operate multiple brands or stores without mixing credentials, context or operating permissions.')}<div class="portfolio-grid">{''.join(f'<article><span>STORE {i:02d}</span><h3>{name}</h3><p>{copy}</p><b>{status}</b></article>' for i,(name,copy,status) in enumerate([('North America','Google + Shopify','Healthy'),('Europe','Google + Meta','Healthy'),('Wholesale','Observe only','Review'),('New launch','Canary authority','Learning')],1))}</div></div></section>'''
    return generic_page('/solutions/portfolio/','Portfolio Management','Govern stores and channels without losing isolation.','Portfolio combines cross-channel intelligence, per-store credentials, authority and a shared contribution-profit operating view.',body,visual)


def intelligence_page() -> str:
    visual = '<div class="subhero-visual">' + story_briefing() + '</div>'
    body = f'''<section class="section"><div class="container">{section_head('Always-on intelligence','Your 24/7 watchtower for performance, competitors and opportunity.','Malach Intelligence continuously monitors your business, advertising, competitors, demand and market shifts. It turns all of that movement into a prioritized briefing: what changed, why it matters, and what you should do next.')}<div class="feature-rows"><article><span>01</span><h3>Watch the business</h3><p>Track profit, attribution, products, campaigns and meaningful performance changes around the clock.</p></article><article><span>02</span><h3>Watch the market</h3><p>Monitor competitors, demand shifts and search-market movement before they become obvious in your results.</p></article><article><span>03</span><h3>Find the signal</h3><p>Use proprietary algorithms to separate routine noise from decisions that can materially affect profit.</p></article><article><span>04</span><h3>Brief the operator</h3><p>Get clear, consumer-friendly explanations of what matters, the evidence behind it and the best next move.</p></article></div></div></section>
<section class="section v71-intel-advantage"><div class="container">{section_head('An unfair advantage','Statistics, probability and your economics—working as one.','Malach combines statistical models, probabilistic reasoning, break-even math, attribution confidence and your own operating data. The result is a decision engine that sees more context, evaluates more evidence and reacts faster than a human team working across disconnected dashboards.','wide')}<div class="v71-intel-grid"><article><small>COMPETITOR WATCH</small><strong>3 material changes</strong><p>Pricing, promotional pressure and search overlap monitored continuously.</p></article><article><small>PROFIT MODEL</small><strong>89% confidence</strong><p>Channel claims reconciled against verified commerce outcomes.</p></article><article><small>OPPORTUNITY MODEL</small><strong>82.6% likely profitable</strong><p>Expected upside tested against the economics that actually matter.</p></article></div></div></section>'''
    return generic_page('/intelligence/','Malach Intelligence','Know what changed before everyone else does.','Malach Intelligence works 24/7 across your performance, competitors, economics and market signals—then uses proprietary decision models to turn that evidence into a clear operating advantage.',body,visual)


def auto_agent_page() -> str:
    visual = '<div class="subhero-visual">' + authority_visual() + '</div>'
    body = f'''<section class="section"><div class="container">{section_head('Auto Agent + Agent Canvas','It does the work—not just the analysis.','Auto Agent is Malach’s 24/7 operating layer. Agent Canvas turns each opportunity into a visible work plan: gather evidence, model the decision, prepare the action, respect the authority you chose, execute when allowed and measure what happened next.')}<div class="v71-canvas" data-v71-canvas><div class="v71-canvas-head"><span>AGENT CANVAS · LIVE WORK PLAN</span><b>24/7</b></div><div class="v71-canvas-flow"><button class="active" data-canvas-step="signal"><i>01</i><strong>Signal</strong><small>Opportunity detected</small></button><button data-canvas-step="evidence"><i>02</i><strong>Evidence</strong><small>Economics verified</small></button><button data-canvas-step="decision"><i>03</i><strong>Decision</strong><small>Best move modeled</small></button><button data-canvas-step="action"><i>04</i><strong>Action</strong><small>Prepared or executed</small></button><button data-canvas-step="outcome"><i>05</i><strong>Outcome</strong><small>Result measured</small></button></div><div class="v71-canvas-stage"><span data-canvas-kicker>OPPORTUNITY DETECTED</span><h3 data-canvas-title>High-intent demand moved above the profit-safe threshold.</h3><p data-canvas-copy>Malach is gathering the economics and evidence needed to decide whether the opportunity deserves action.</p><div class="v71-canvas-meta"><span>Northstar Home</span><span>Aster Lamp</span><span>Google Ads</span></div></div></div></div></section>
<section class="section section-copper"><div class="container">{section_head('Governed execution','Authority is a setting—not an assumption.','Start with Observe. Add human approval. Use Canary for controlled tests. Grant Full Auto only when you are ready. Auto Agent keeps operating inside that boundary 24/7.')}<div class="agent-sequence"><article><span>01</span><h3>Evidence</h3><p>Malach gathers the business economics, performance signals and market context behind the opportunity.</p></article><article><span>02</span><h3>Decision</h3><p>Proprietary models evaluate probability, expected upside, downside and the evidence required to act.</p></article><article><span>03</span><h3>Authority</h3><p>Agent Canvas routes the work according to Observe, Approval, Canary or Full Auto.</p></article><article><span>04</span><h3>Outcome</h3><p>Malach confirms the change, measures the result and feeds the evidence back into the next decision.</p></article></div></div></section>'''
    return generic_page('/auto-agent/','Auto Agent','A 24/7 operator that can actually do the work.','Auto Agent and Agent Canvas turn Malach intelligence into a visible operating plan, then prepare or execute the work according to the authority you choose.',body,visual,['/assets/js/home-v7.js'])


def advantage_page() -> str:
    visual = '''<div class="subhero-visual"><div class="market-console"><div class="market-head"><span>ADVANTAGE MARKET WATCH</span><b>LIVE · 24/7</b></div><div class="market-list"><article><span>01</span><div><h3>Competitor promotion accelerated.</h3><p>Discount depth and search overlap increased across the category.</p></div><em>WATCH</em></article><article><span>02</span><div><h3>High-intent demand is expanding.</h3><p>Search interest and product engagement moved together.</p></div><em>MOVE</em></article><article><span>03</span><div><h3>Category CPC rose faster than value.</h3><p>Protect break-even before expanding coverage.</p></div><em>CONTAIN</em></article></div></div></div>'''
    body = f'''<section class="section"><div class="container">{section_head('Your unfair advantage','See the market. Know the odds. Move before the opportunity disappears.','Advantage watches competitors, pricing pressure, demand and search-market movement 24/7. Malach then runs those signals through the same proprietary algorithms and economics powering your account decisions.')}<div class="feature-spread"><article><span>01</span><h3>Competitor intelligence</h3><p>Track visible shifts in competitors, promotions, positioning and search pressure without living in research tabs.</p></article><article><span>02</span><h3>Market probability</h3><p>Use statistics and probability to distinguish a durable opportunity from a temporary spike.</p></article><article><span>03</span><h3>Economic filter</h3><p>Market movement matters only when it creates a profitable move for your business. Malach keeps your margins and break-even points in the decision.</p></article></div></div></section>'''
    return generic_page('/advantage/','Advantage','Turn outside intelligence into an unfair advantage.','Malach monitors competitors and market movement, combines those signals with your own economics, and helps you act when the evidence says the opportunity is worth it.',body,visual)


def attribution_page() -> str:
    visual = '''<div class="subhero-visual"><div class="reconcile-console"><div class="reconcile-head"><span>ATTRIBUTION RECONCILIATION</span><strong>89% confidence</strong></div><div class="reconcile-grid"><div><small>Google reported</small><strong>$516,400</strong></div><div><small>Shopify verified</small><strong>$472,180</strong></div><div><small>Reconciled value</small><strong>$481,760</strong></div><div><small>Unresolved gap</small><strong>−$34,640</strong></div></div><div class="reconcile-note">Malach separates platform claims, verified orders and the value that can be reconciled with confidence.</div></div></div>'''
    body = f'''<section class="section"><div class="container">{section_head('Attribution with a confidence level','Know which numbers are verified, estimated or unresolved.','Malach compares acquisition-channel claims to Shopify orders and carries uncertainty into the decision instead of hiding it.')}<div class="feature-rows"><article><span>01</span><h3>Platform view</h3><p>What the advertising platform claims it influenced.</p></article><article><span>02</span><h3>Commerce view</h3><p>What Shopify confirms was actually sold.</p></article><article><span>03</span><h3>Reconciled view</h3><p>The value Malach can responsibly use in a decision.</p></article></div></div></section>'''
    return generic_page('/attribution/','Attribution','Match advertising results to verified sales.','Malach reconciles platform-reported performance with Shopify orders and shows the confidence behind the result.',body,visual)


def voice_page() -> str:
    visual = '''<div class="subhero-visual"><div class="chat-console"><aside><button>+ New chat</button><span>Where am I wasting money?</span><span>What would you test tomorrow?</span><span>Why did POAS fall?</span><span>Which products deserve more spend?</span></aside><main><div class="chat-user">What assumptions is Auto Agent making?</div><div class="chat-answer"><img src="/assets/media/malach-mark.png" alt=""><div><strong>Three assumptions matter most.</strong><p>Contribution per conversion is $84, click quality remains within the trailing range, and CPC stays below $3.84. If one breaks, the test should stop.</p></div></div><div class="chat-input">Ask Malach about profit, campaigns or the next action… <button>Send</button></div></main></div></div>'''
    body = f'''<section class="section"><div class="container">{section_head('Conversational intelligence','Ask the question you would ask an analyst.','Malach Chat and Voice work with the same verified business context used by Profit Center, Attribution and Auto Agent.')}<div class="feature-spread"><article><span>01</span><h3>Grounded answers</h3><p>Responses use connected account and commerce context—not generic advice.</p></article><article><span>02</span><h3>Selected-file context</h3><p>Bring operating documents into a focused question when needed.</p></article><article><span>03</span><h3>Direct action context</h3><p>Ask why Malach recommended an action and what would invalidate it.</p></article></div></div></section>'''
    return generic_page('/voice/','Malach Voice','Ask your advertising operation a direct question.','Use chat or voice to investigate profit, campaigns, products, assumptions and the next recommended action.',body,visual)


def vision_page() -> str:
    visual = '<div class="subhero-visual">' + vision_visual() + '</div>'
    body = f'''<section class="section"><div class="container">{section_head('Cross-channel intelligence','Evaluate the system, not each channel in isolation.','Vision helps Portfolio operators understand assisted value, demand transfer and the contribution each channel creates across stores.')}<div class="feature-spread"><article><span>01</span><h3>Shared economics</h3><p>Every channel is evaluated through the same contribution model.</p></article><article><span>02</span><h3>Assisted value</h3><p>See when one channel creates demand another channel later captures.</p></article><article><span>03</span><h3>Portfolio context</h3><p>Compare stores without mixing credentials or operating authority.</p></article></div></div></section>'''
    return generic_page('/vision/','Malach Vision','One profit view across channels and stores.','Portfolio brings Google, Meta and TikTok into one cross-channel contribution model, with Amazon Ads planned next.',body,visual)


def channels_page() -> str:
    cards = [('Google Ads','Core','Live','Campaign intelligence, Profit Center and execution authority.'),('Shopify','Core','Live','Orders, margin, returns, fees and contribution economics.'),('Meta Ads','Portfolio','Live','Cross-channel performance and assisted-value context.'),('TikTok Ads','Portfolio','Live','Creative and demand signals inside Malach Vision.'),('Amazon Ads','Portfolio','Coming soon','Planned Portfolio integration using the same profit lens.')]
    visual = '<div class="subhero-visual"><div class="channel-matrix">' + ''.join(f'<article><span>{tier}</span><h3>{name}</h3><p>{copy}</p><b class="{("upcoming" if status != "Live" else "")}">{status}</b></article>' for name,tier,status,copy in cards) + '</div></div>'
    body = f'''<section class="section"><div class="container">{section_head('One operating model','Different channels. The same economic standard.','Malach evaluates advertising activity through verified commerce economics and the authority configured for each workspace.')}<div class="channel-detail-grid">{''.join(f'<article id="{name.lower().replace(" ","-")}"><span>{tier}</span><h3>{name}</h3><strong>{status}</strong><p>{copy}</p></article>' for name,tier,status,copy in cards)}</div></div></section>'''
    return generic_page('/channels/','Channels','Every paid channel through the same profit lens.','Google Ads and Shopify form the Core foundation. Portfolio adds Meta and TikTok, with Amazon Ads planned next.',body,visual)


def pricing_page() -> str:
    cards = ''.join(price_card(p) for p in PLANS)
    faqs = [
        ("When does billing begin?", "Billing begins after the three-day trial at the timestamp shown during Stripe Checkout unless the subscription is canceled first."),
        ("Is Core autonomous?", "No. Core is the intelligence layer and includes Observe mode only. Malach analyzes and recommends, while you execute changes yourself."),
        ("What execution controls are included in Autonomous?", "Autonomous includes Approval, Auto Agent, Canary and Full Auto authority, plus Algorithm, Master Lab, Advantage and Evolution Studio."),
        ("Who is Portfolio for?", "Portfolio is designed for multi-store, multi-brand or agency operations that need isolated credentials, cross-channel intelligence, Portfolio God View and priority support."),
        ("Can I change plans later?", "Yes. Billing and plan changes are managed through Malach and Stripe. The available product surfaces and authority update with the active entitlement."),
        ("Is Amazon Ads active?", "Not yet. Amazon Ads is planned for Portfolio and remains labeled coming soon until the integration is ready."),
    ]
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)
    body = f'''<section class="pricing-hero"><div class="container"><div class="section-head center"><span class="eyebrow">Pricing</span><h1>Choose the level of intelligence and authority.</h1><p>Start with three days free. Choose monthly flexibility or receive two months free with annual billing.</p></div><div class="pricing-toggle" role="group" aria-label="Billing interval"><button class="active" data-billing="monthly">Monthly</button><button data-billing="annual">Annual <span>2 months free</span></button></div><div class="pricing-grid">{cards}</div><p class="seat-note">Additional seats: $50/month or $500/year.</p></div></section><section class="section faq-section"><div class="container faq-layout"><div>{section_head('Pricing questions','Understand the trial, plans and authority before you begin.','')}</div><div class="faq-list">{faq}</div></div></section>'''
    return shell('/pricing/',body + closing_cta(),['/assets/js/pricing-v7.js'],'pricing-page')


def security_page() -> str:
    visual = '''<div class="subhero-visual"><div class="security-console"><div class="security-row"><span>Account connections</span><b>Protected</b></div><div class="security-row"><span>Workspace separation</span><b>Active</b></div><div class="security-row"><span>Action history</span><b>Recording</b></div><div class="security-row"><span>Operating authority</span><b>Owner controlled</b></div><div class="security-stop">Emergency stop <strong>Ready</strong></div></div></div>'''
    body = f'''<section class="section"><div class="container">{section_head('Security that supports control','Protected access. Separate workspaces. Visible actions.','Malach is designed so operators can understand who has access, what authority is active and what the system changed.')}<div class="security-principles"><article><span>01</span><h3>Protected account connections</h3><p>Saved connection details stay protected and hidden after setup.</p></article><article><span>02</span><h3>Each business stays separate</h3><p>Every store keeps its own data, connections, permissions and settings.</p></article><article><span>03</span><h3>You choose the level of control</h3><p>Observe, Approval, Canary and Full Auto are explicit operating settings.</p></article><article><span>04</span><h3>Every action is traceable</h3><p>See what Malach changed, why it changed it and what happened afterward.</p></article><article><span>05</span><h3>Stop immediately when needed</h3><p>Emergency controls let you pause autonomous operation when circumstances change.</p></article><article><span>06</span><h3>Secure payment collection</h3><p>Stripe handles card information on its hosted checkout experience.</p></article></div></div></section>'''
    return generic_page('/security/','Security','High authority requires visible safeguards.','Malach protects connected accounts, separates workspaces, records actions and gives operators clear authority and emergency controls.',body,visual)


def about_page() -> str:
    body = f'''<section class="section v71-about-meaning"><div class="container"><div class="v71-meaning-card"><span class="eyebrow">The name</span><h2>Malach means Angel and Messenger.</h2><p class="v71-meaning-exact">Malach means Angel and Messenger - working for you 24/7 with one goal. Making profitable decisions and actions.</p><p>That is the product philosophy: always watching, always carrying the signal forward, and always working as part of your team. Malach is built to understand what is happening, explain the evidence, decide what deserves action and—when you allow it—do the work.</p><div class="v71-team-pulse"><i></i><span>ON YOUR TEAM</span><strong>24 / 7 / 365</strong></div></div></div></section>
<section class="section"><div class="container">{section_head('Why Malach exists','Better advertising decisions should not depend on staring at dashboards all day.','Malach was built to give commerce operators a persistent intelligence and execution teammate—one that uses real economics, proprietary algorithms and measured outcomes to make better decisions around the clock.')}<div class="manifesto-grid"><article><span>01</span><h3>Profit is the objective</h3><p>Revenue and platform ROAS are inputs. The real question is what remains after the costs that make the sale possible.</p></article><article><span>02</span><h3>Evidence earns action</h3><p>Malach uses statistics, probability, attribution and your own economics to build an evidence-based case before a recommendation becomes action.</p></article><article><span>03</span><h3>We are on your team</h3><p>Malach operates 24/7—monitoring the business, competitors and market, preparing work, executing when authorized and measuring what happened afterward.</p></article></div></div></section>'''
    return generic_page('/about/','Company','An intelligence and execution teammate that never clocks out.','Malach means Angel and Messenger. It is built to work for you 24/7 with one goal: making profitable decisions and actions.',body)


def support_page(contact=False) -> str:
    route = '/contact/' if contact else '/support/'
    eyebrow = 'Contact' if contact else 'Support'
    title = 'Talk with Malach.' if contact else 'Get help with Malach.'
    copy = 'Product, sales, partnership and portfolio questions.' if contact else 'Help with account access, billing, connected accounts and product use.'
    topic_options = '<option>Product question</option><option>Pricing and sales</option><option>Account access</option><option>Billing</option><option>Connected accounts</option><option>Partnership or agency</option>'
    body = f'''<section class="support-hero"><div class="container support-grid"><div><div class="section-head"><span class="eyebrow">{escape(eyebrow)}</span><h1>{escape(title)}</h1><p>{escape(copy)}</p></div><div class="support-contact"><span>Email</span><a href="mailto:{SUPPORT}">{SUPPORT}</a><p>Include the workspace name and a concise description of the issue. Never send passwords, access keys or authentication codes.</p></div></div><form class="support-form" data-support-form data-endpoint="/api/contact"><input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"><label>Name<input required name="name" autocomplete="name"></label><label>Email<input required type="email" name="email" autocomplete="email"></label><label>Topic<select name="topic">{topic_options}</select></label><label>Message<textarea required name="message" rows="6"></textarea></label><button class="button button-primary" type="submit">Send message</button><p class="form-status" aria-live="polite"></p></form></div></section>'''
    return shell(route,body,[], 'support-page')


def docs_page() -> str:
    guides = [('01','Create your account','Verify your email, choose a plan and complete the three-day trial checkout.'),('02','Connect Google Ads','Authorize the Google Ads account Malach should analyze and, where allowed, operate.'),('03','Connect Shopify','Bring order, product, margin, fee, shipping and return context into Profit Center.'),('04','Choose operating authority','Start with Observe. Add Approval, Canary or Full Auto only when appropriate.'),('05','Read the decision briefing','Review the evidence, expected upside, assumptions and invalidation conditions.'),('06','Manage billing and access','Use Settings and Stripe to manage your plan, seats, payment method and cancellation.')]
    body = f'''<section class="docs-hero"><div class="container"><div class="section-head"><span class="eyebrow">Documentation</span><h1>Set up Malach and understand how it operates.</h1><p>A practical path from account creation to connected economics and governed execution.</p></div><div class="docs-grid">{''.join(f'<article><span>{n}</span><h3>{title}</h3><p>{copy}</p></article>' for n,title,copy in guides)}</div></div></section>'''
    return shell('/docs/',body + closing_cta(),[], 'docs-page')


def status_page() -> str:
    body = '''<section class="status-hero"><div class="container"><span class="eyebrow">Status</span><div class="status-title"><i class="status-dot checking" data-status-dot></i><div><h1 data-status-title>Checking Malach…</h1><p data-status-summary>Running a live availability check.</p></div><button class="button button-ghost" type="button" data-status-refresh>Check again</button></div><div class="status-panel"><div class="status-overview"><span data-status-state>Checking systems</span><strong data-status-detail>Confirming application availability.</strong><small data-status-checked>Checking now</small></div><div class="status-services"><article><span>Malach application</span><b data-service-state>Checking</b></article><article><span>Sign-in &amp; account access</span><b data-service-state>Checking</b></article><article><span>Connected accounts</span><b data-service-state>Checking</b></article><article><span>Malach Intelligence</span><b data-service-state>Checking</b></article><article><span>Intelligence &amp; workspace</span><b data-service-state>Checking</b></article><article><span>Autonomous operations</span><b data-service-state>Checking</b></article></div></div></div></section>'''
    return shell('/status/',body,['/assets/js/status-v7.js'],'status-page')


def legal_page(route: str, title: str, sections: list[tuple[str,str]]) -> str:
    content = ''.join(f'<section><h2>{escape(h)}</h2><p>{escape(p)}</p></section>' for h,p in sections)
    body = f'''<section class="legal-hero"><div class="container"><span class="eyebrow">Legal</span><h1>{escape(title)}</h1><p>Last updated August 2026.</p><article class="legal-document">{content}</article></div></section>'''
    return shell(route,body,[], 'legal-page')


def login_page() -> str:
    body = f'''<section class="login-page"><div class="login-card"><img src="/assets/media/malach-mark.png" alt="Malach"><span class="eyebrow">Malach application</span><h1>Open your workspace.</h1><p>Sign in, create an account, or continue a trial in the Malach application.</p><a class="button button-primary" href="{APP}">Continue to Malach</a><a class="text-cta" href="/support/">Need help?</a></div></section>'''
    return shell('/login/',body,[], 'login-page')


def error_404() -> str:
    body = '''<section class="login-page"><div class="login-card"><img src="/assets/media/malach-mark.png" alt="Malach"><span class="eyebrow">404</span><h1>Page not found.</h1><p>The page you requested does not exist or has moved.</p><a class="button button-primary" href="/">Return home</a></div></section>'''
    return shell('/404.html',body,[], 'login-page')


PAGES = {
    '/': home_page(),
    '/product/': product_page(),
    '/solutions/': solutions_page(),
    '/solutions/google-ads/': google_page(),
    '/solutions/shopify/': shopify_page(),
    '/solutions/portfolio/': portfolio_page(),
    '/intelligence/': intelligence_page(),
    '/auto-agent/': auto_agent_page(),
    '/advantage/': advantage_page(),
    '/attribution/': attribution_page(),
    '/voice/': voice_page(),
    '/vision/': vision_page(),
    '/channels/': channels_page(),
    '/pricing/': pricing_page(),
    '/security/': security_page(),
    '/about/': about_page(),
    '/support/': support_page(False),
    '/contact/': support_page(True),
    '/docs/': docs_page(),
    '/status/': status_page(),
    '/privacy/': legal_page('/privacy/','Privacy Policy',[
        ('Information Malach receives','Malach receives account information you provide, connected advertising and commerce data you authorize, product-use information, and billing status supplied by Stripe.'),
        ('How information is used','Information is used to provide the service, secure accounts, connect advertising and commerce data, calculate product outputs, support users, and improve reliability.'),
        ('Connected accounts','You control which accounts are connected. Closing the account or removing connections should revoke the related operating access according to the product controls available to you.'),
        ('Service providers','Malach may use infrastructure, authentication, email, payment and analytics providers to operate the service. These providers receive only the information required for their role.'),
        ('Your choices','You may request account assistance, connection removal, or account closure through Malach Support.'),
    ]),
    '/terms/': legal_page('/terms/','Terms of Service',[
        ('Using Malach','You are responsible for the accounts you connect, the authority you grant, the data you provide, and the decisions you make using Malach.'),
        ('Autonomous operation','Malach may recommend or execute advertising actions according to your plan and configured authority. You must monitor connected accounts and use emergency controls when appropriate.'),
        ('Billing','Paid access is billed through Stripe according to the selected plan and interval. Trial, renewal and cancellation timing are shown during checkout and in billing management.'),
        ('No guaranteed outcome','Advertising performance and commerce outcomes are uncertain. Malach does not guarantee revenue, profit, return on ad spend or any specific business result.'),
        ('Account security','You are responsible for protecting account credentials, authentication methods and authorized users. Notify support promptly if you suspect unauthorized access.'),
    ]),
    '/login/': login_page(),
}

for route, html in PAGES.items():
    target = ROOT / 'index.html' if route == '/' else ROOT / route.strip('/') / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding='utf-8')

(ROOT / '404.html').write_text(error_404(), encoding='utf-8')
(ROOT / 'site.webmanifest').write_text(json.dumps({
    'name': 'Malach — Advertising Operations', 'short_name': 'Malach', 'start_url': '/', 'display': 'standalone',
    'background_color': '#07070b', 'theme_color': '#07070b',
    'icons': [
        {'src': '/assets/media/favicon-64.png', 'sizes': '64x64', 'type': 'image/png'},
        {'src': '/assets/media/apple-touch-icon.png', 'sizes': '180x180', 'type': 'image/png'},
        {'src': '/assets/media/malach-app-icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
    ]
}, indent=2), encoding='utf-8')

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>https://malach.app{route}</loc></url>\n' for route in ROUTES) + '</urlset>\n'
(ROOT / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
(ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\nDisallow: /api/\nSitemap: https://malach.app/sitemap.xml\n', encoding='utf-8')

print(f'Generated {len(PAGES)} pages + 404 for Malach V{VERSION}')
