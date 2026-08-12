from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]

NAV = [
    ('Product', '/product/'),
    ('Auto Agent', '/auto-agent/'),
    ('Intelligence', '/intelligence/'),
    ('Advantage', '/advantage/'),
    ('Security', '/security/'),
    ('Pricing', '/pricing/'),
]

FOOTER_COLS = [
    ('Product', [
        ('Product', '/product/'), ('Auto Agent', '/auto-agent/'), ('Advantage', '/advantage/'),
        ('Attribution', '/attribution/'), ('Malach Voice', '/voice/'), ('Pricing', '/pricing/')
    ]),
    ('Company', [('About', '/about/'), ('Support', '/support/'), ('Status', '/status/'), ('Changelog', '/changelog/')]),
    ('Legal', [('Privacy', '/privacy/'), ('Terms', '/terms/'), ('Security', '/security/')])
]

COMMAND = '''
<div class="command-palette" data-command-palette aria-hidden="true">
  <div class="command-panel" role="dialog" aria-modal="true" aria-label="Search Malach website">
    <input class="command-input" type="search" placeholder="Search Malach…" aria-label="Search pages">
    <div class="command-results"></div>
  </div>
</div>
'''

def header(current=''):
    links = ''.join(f'<a href="{href}" {"aria-current=\"page\"" if current == href else ""}>{label}</a>' for label, href in NAV)
    return f'''
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="nav-shell">
    <a class="logo-link" href="/" aria-label="Malach home">
      <img src="/assets/media/malach-lockup.png" alt="Malach">
    </a>
    <nav class="main-nav" aria-label="Primary navigation">{links}</nav>
    <div class="nav-actions">
      <button class="theme-toggle" type="button" data-theme-toggle aria-label="Switch theme"></button>
      <button class="nav-link" type="button" data-command-open aria-label="Search Malach">Search <span aria-hidden="true">⌘K</span></button>
      <a class="nav-link" href="https://app.malach.app" data-track="sign_in_clicked">Sign in</a>
      <a class="btn btn-primary btn-small" href="/pricing/" data-track="header_get_malach">Get Malach</a>
      <button class="menu-toggle" type="button" data-menu-toggle aria-label="Open menu" aria-expanded="false"></button>
    </div>
  </div>
</header>
'''

def footer():
    cols = ''.join(
        f'<div class="footer-col"><h4>{title}</h4><nav>{"".join(f"<a href=\"{href}\">{label}</a>" for label, href in links)}</nav></div>'
        for title, links in FOOTER_COLS
    )
    return f'''
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/media/malach-lockup.png" alt="Malach">
        <p>Autonomous commerce intelligence for mathematically informed advertising decisions.</p>
      </div>
      {cols}
    </div>
    <div class="footer-bottom">
      <span>© <span data-year></span> Malach. All rights reserved.</span>
      <span>Advertising intelligence that never stops thinking.</span>
    </div>
  </div>
</footer>
'''

def head(title, description, path='/', extra=''):
    canonical = f'https://malach.app{path}'
    return f'''<!doctype html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <meta name="theme-color" content="#09080a">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Malach">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://malach.app/assets/media/og-image.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(title)}">
  <meta name="twitter:description" content="{escape(description)}">
  <meta name="twitter:image" content="https://malach.app/assets/media/og-image.jpg">
  <link rel="icon" href="/assets/media/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="64x64" href="/assets/media/favicon-64.png">
  <link rel="apple-touch-icon" href="/assets/media/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="stylesheet" href="/assets/css/styles.css">
  {extra}
</head>'''

def page(title, description, path, current, main, scripts=None, body_class=''):
    scripts = scripts or []
    script_tags = '<script type="module" src="/assets/js/site.js"></script>' + ''.join(f'<script type="module" src="{s}"></script>' for s in scripts)
    return f'''{head(title, description, path)}
<body class="{body_class}">
{header(current)}
<main id="main">{main}</main>
{footer()}
{COMMAND}
{script_tags}
</body>
</html>
'''

HOME = r'''
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy reveal">
      <span class="eyebrow">Autonomous commerce intelligence</span>
      <h1>Advertising intelligence that <span class="gradient-text">never stops thinking.</span></h1>
      <p class="lede">Malach continuously studies Google Ads, Shopify economics, attribution, competitors and market signals to find opportunities, contain losses and optimize paid acquisition around contribution profit.</p>
      <div class="hero-actions">
        <a class="btn btn-primary btn-large" href="/pricing/" data-track="hero_get_malach">Get Malach</a>
        <a class="btn btn-large" href="#auto-agent" data-track="hero_watch_think">Watch Malach Think</a>
      </div>
      <div class="hero-trust" aria-label="Product capabilities">
        <span><i></i>Google Ads intelligence</span><span><i></i>Shopify economics</span><span><i></i>24/7 opportunity detection</span><span><i></i>Explainable decision mathematics</span>
      </div>
    </div>
    <div class="hero-stage reveal" aria-label="Illustrative Malach decision demo">
      <div class="hero-orbit"></div><div class="hero-glow"></div>
      <div class="intelligence-card" data-tilt>
        <div class="intelligence-top">
          <div class="malach-chip"><img src="/assets/media/malach-mark.png" alt=""><div><div class="chip-title">MALACH</div><div class="chip-sub">Illustrative decision ledger</div></div></div>
          <div class="live-pill"><i class="live-dot"></i>LIVE</div>
        </div>
        <div class="decision-panel">
          <div class="decision-label">SEARCH OPPORTUNITY</div>
          <div class="decision-title">Controlled commercial-intent test</div>
          <div class="decision-metrics">
            <div class="metric-tile"><span>Probability profitable</span><strong class="positive">78.4%</strong></div>
            <div class="metric-tile"><span>Expected contribution</span><strong>+$3,840</strong></div>
            <div class="metric-tile"><span>Maximum rational CPC</span><strong>$4.28</strong></div>
            <div class="metric-tile"><span>Proposed test budget</span><strong>$420</strong></div>
          </div>
          <div class="equation-strip" data-equation-strip></div>
          <div class="micro-chart">
            <svg viewBox="0 0 500 90" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="heroTrace" x1="0" x2="1"><stop stop-color="#c76535"/><stop offset=".55" stop-color="#35ca93"/><stop offset="1" stop-color="#a68aff"/></linearGradient></defs><path d="M0 70 C45 67 55 57 92 59 S140 35 171 48 S222 23 260 33 S317 17 355 27 S412 10 500 14"/></svg>
          </div>
          <div class="status-row"><span>Confidence 0.81</span><span>Evidence current · 2m ago</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="loop">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">The Malach loop</span><h2>Observe. Calculate. Act. Measure. Learn.</h2><p class="lede">Every decision becomes evidence for the next one.</p></div>
    <div class="glass-card loop-shell reveal">
      <div class="loop-track">
        <article class="loop-node"><span class="loop-number">01</span><h3>Observe</h3><div class="loop-list"><span>Google Ads</span><span>Shopify</span><span>Attribution</span><span>Competitors</span><span>Margins</span></div></article>
        <article class="loop-node"><span class="loop-number">02</span><h3>Calculate</h3><div class="loop-list"><span>Probability</span><span>Expected value</span><span>Risk</span><span>Break-even economics</span><span>Confidence</span></div></article>
        <article class="loop-node"><span class="loop-number">03</span><h3>Decide</h3><div class="loop-list"><span>Scale</span><span>Hold</span><span>Pause</span><span>Test</span><span>Investigate</span></div></article>
        <article class="loop-node"><span class="loop-number">04</span><h3>Verify</h3><div class="loop-list"><span>Read-after-write</span><span>Profit measurement</span><span>Attribution reconciliation</span><span>Rollback evidence</span></div></article>
        <article class="loop-node"><span class="loop-number">05</span><h3>Learn</h3><div class="loop-list"><span>Prediction calibration</span><span>Outcome memory</span><span>Probability adjustment</span><span>New hypothesis</span></div></article>
      </div>
      <div class="loop-footer">A continuous evidence loop—not a one-time recommendation.</div>
    </div>
  </div>
</section>

<section class="section" id="financial-intelligence">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Financial intelligence</span><h2>Optimize advertising around the economics that matter.</h2><p class="lede">Malach connects advertising decisions to the economics behind the order—not just platform-reported ROAS.</p><span class="demo-note">Illustrative product demo</span></div>
    <div class="glass-card financial-shell reveal" data-financial-chart>
      <div class="chart-head">
        <div class="chart-toggles" aria-label="Financial chart series">
          <button class="chart-toggle" data-series="revenue" aria-pressed="true"><i style="background:#c76535"></i>Revenue</button>
          <button class="chart-toggle" data-series="profit" aria-pressed="true"><i style="background:#35ca93"></i>Profit</button>
          <button class="chart-toggle" data-series="spend" aria-pressed="true"><i style="background:#7650d8"></i>Spend</button>
        </div>
        <div class="mode-toggle"><button class="mode-btn" data-chart-mode="shared" aria-pressed="true">Shared $</button><button class="mode-btn" data-chart-mode="compare" aria-pressed="false">Compare trends</button></div>
      </div>
      <div class="chart-wrap"><canvas aria-label="Illustrative revenue, profit and ad spend chart"></canvas><div class="chart-tooltip"></div></div>
      <div class="metric-band">
        <article><small>Contribution profit</small><strong data-count="810" data-prefix="$">$0</strong></article>
        <article><small>POAS</small><strong data-count="2.01" data-decimals="2" data-suffix="×">0×</strong></article>
        <article><small>COGS coverage</small><strong data-count="96" data-suffix="%">0%</strong></article>
        <article><small>Attribution confidence</small><strong data-count="82" data-suffix="%">0%</strong></article>
      </div>
    </div>
  </div>
</section>

<section class="section" id="auto-agent">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">Auto Agent</span><h2>See the mathematics behind every decision.</h2><p class="lede">Malach records the evidence, formulas, thresholds, decisions and outcomes that govern autonomous work.</p></div>
    <div class="glass-card agent-shell reveal" data-agent-demo>
      <aside class="agent-side">
        <div class="agent-tabs" role="tablist"><button class="agent-tab" data-agent-tab="canvas" aria-selected="true">Live Canvas</button><button class="agent-tab" data-agent-tab="algorithm" aria-selected="false">Algorithm</button><button class="agent-tab" data-agent-tab="authority" aria-selected="false">Authority</button></div>
        <div class="agent-authority"><div class="board-status">● OBSERVE</div><p style="font-size:12px;margin-top:9px">Analysis active. Account changes require authorization.</p></div>
      </aside>
      <div class="agent-board" data-agent-view="canvas">
        <div class="board-head"><div><div class="board-status">LIVE DECISION TRACE</div><h3 style="margin-top:10px">Commercial-intent Search opportunity</h3></div><span class="board-time">14:32:08 UTC</span></div>
        <div class="formula-stack">
          <article class="formula-card is-active"><div class="formula-name">Posterior conversion rate</div><div class="formula">Beta(α + conversions, β + clicks − conversions)</div><div class="formula-result"><span>Beta(19 + 7, 481 + 214 − 7)</span><strong>3.72%</strong></div></article>
          <article class="formula-card"><div class="formula-name">Break-even conversion rate</div><div class="formula">CPC ÷ contribution per conversion</div><div class="formula-result"><span>$3.12 ÷ $84.00</span><strong>3.71%</strong></div></article>
          <article class="formula-card"><div class="formula-name">Risk-adjusted expected value</div><div class="formula">EV − λ × downside risk</div><div class="formula-result"><span>$4,680 − 0.38 × $1,140</span><strong>+$4,247</strong></div></article>
        </div>
        <div class="board-decision"><small>DECISION</small><h3>Run controlled Search test</h3><p>Expected value remains positive after risk adjustment. Test budget: $375. Maximum CPC: $3.84.</p></div>
      </div>
      <div class="agent-board" data-agent-view="algorithm" hidden><div class="board-head"><div><div class="board-status">ALGORITHM</div><h3 style="margin-top:10px">Profitability and harm model</h3></div></div><div class="formula-stack"><article class="formula-card"><div class="formula-name">Probability profitable</div><div class="formula">P(profit &gt; 0 | evidence)</div><div class="formula-result"><span>Posterior samples above break-even</span><strong>78.4%</strong></div></article><article class="formula-card"><div class="formula-name">Maximum rational CPC</div><div class="formula">posterior CVR × contribution × safety factor</div><div class="formula-result"><span>3.72% × $84 × 0.82</span><strong>$2.56</strong></div></article></div></div>
      <div class="agent-board" data-agent-view="authority" hidden><div class="board-head"><div><div class="board-status">AUTHORITY</div><h3 style="margin-top:10px">Owner-controlled operating mode</h3></div></div><div class="mode-grid" style="margin-top:32px"><article class="mode-card active"><small>MODE 01</small><h3>Observe</h3><p>Analyze without account changes.</p></article><article class="mode-card"><small>MODE 02</small><h3>Approval</h3><p>Malach proposes; owner approves.</p></article><article class="mode-card"><small>MODE 03</small><h3>Canary Auto</h3><p>Bounded autonomous execution.</p></article><article class="mode-card"><small>MODE 04</small><h3>Full Auto</h3><p>Authorized autonomous operation.</p></article></div></div>
    </div>
  </div>
</section>

<section class="section" id="opportunities">
  <div class="container"><div class="section-head reveal"><span class="eyebrow">Opportunity intelligence</span><h2>Find opportunities humans do not have time to continuously search for.</h2><span class="demo-note">Illustrative product demo</span></div>
    <div class="opportunity-grid" data-opportunity-feed>
      <article class="glass-card opportunity-card reveal"><div class="opportunity-type">KEYWORD OPPORTUNITY</div><h3>commercial espresso machine financing</h3><div class="opportunity-kpis"><div><span>Search volume</span><strong>1,900/mo</strong></div><div><span>Competition</span><strong>Low</strong></div><div><span>Estimated CPC</span><strong>$3.12</strong></div><div><span>Break-even CPC</span><strong>$5.08</strong></div></div><div class="recommendation"><b>74% probability profitable</b><br>Recommended: controlled Search test.</div></article>
      <article class="glass-card opportunity-card reveal"><div class="opportunity-type">PMAX CREATIVE SIGNAL</div><h3>Creative B is separating from the asset group.</h3><div class="opportunity-kpis"><div><span>Observed lift</span><strong>+18%</strong></div><div><span>Persistence</span><strong>82%</strong></div><div><span>Evidence</span><strong>1,842 clicks</strong></div><div><span>Risk</span><strong>Low</strong></div></div><div class="recommendation"><b>Increase exposure</b><br>Run a controlled creative experiment.</div></article>
      <article class="glass-card opportunity-card reveal"><div class="opportunity-type">BUDGET SATURATION</div><h3>Jura Search retains profitable headroom.</h3><div class="opportunity-kpis"><div><span>Current spend</span><strong>$1,050/day</strong></div><div><span>Est. saturation</span><strong>$1,340/day</strong></div><div><span>Marginal contribution</span><strong>+$860/wk</strong></div><div><span>Confidence</span><strong>0.76</strong></div></div><div class="recommendation"><b>Scale carefully</b><br>Increase in bounded steps and verify marginal return.</div></article>
    </div>
  </div>
</section>

<section class="section" id="advantage">
  <div class="container"><div class="section-head center reveal"><span class="eyebrow">Advantage</span><h2>Know the market Malach is competing in.</h2><p class="lede">Competitor pages, keyword economics, search visibility and independent evidence remain source-labeled.</p><span class="demo-note">Illustrative product demo</span></div>
    <div class="glass-card research-shell reveal">
      <div class="research-browser"><div class="browser-chrome"><div class="browser-dots"><i></i><i></i><i></i></div><div class="browser-bar">Malach Research Browser · commercial espresso machine financing</div></div><div class="browser-result"><article class="search-item"><span class="source-badge">MEASURED GOOGLE EVIDENCE</span><h4>Financing language increased across two sponsored competitors</h4><p>Offer capture: “from $189/month” moved into primary headline placement.</p></article><article class="search-item"><span class="source-badge">BRAVE ORGANIC EVIDENCE</span><h4>Competitor landing pages emphasize financing before specifications</h4><p>Independent organic verification across three public pages.</p></article><article class="search-item"><span class="source-badge">MODELED ESTIMATE</span><h4>Clearer monthly economics may improve commercial-intent conversion</h4><p>Estimated probability: 68%. Requires controlled validation.</p></article></div></div>
      <aside class="research-side"><h3>Evidence provenance</h3><div class="provenance"><article><i style="background:#6ba5ff"></i><div><strong>Google Ads</strong><br><span>Account and Keyword Planner evidence</span></div></article><article><i style="background:#ef986b"></i><div><strong>Brave Search</strong><br><span>Independent organic verification</span></div></article><article><i style="background:#35ca93"></i><div><strong>Public web</strong><br><span>Competitor pages and offers</span></div></article><article><i style="background:#a68aff"></i><div><strong>Modeled estimate</strong><br><span>Clearly labeled probabilistic inference</span></div></article></div><a class="btn" style="margin-top:22px;width:100%" href="/advantage/">Explore Advantage</a></aside>
    </div>
  </div>
</section>

<section class="section" id="attribution">
  <div class="container"><div class="section-head reveal"><span class="eyebrow">Attribution</span><h2>Know where profit actually came from.</h2><p class="lede">Revenue, orders, contribution and confidence across every detected Shopify acquisition channel.</p><span class="demo-note">Illustrative product demo</span></div>
    <div class="glass-card attribution-shell reveal"><div class="attribution-summary"><div class="channel-list"><div class="channel-row"><span>Google Ads</span><div class="channel-bar"><i style="width:78%"></i></div><strong>$428k</strong></div><div class="channel-row"><span>Direct</span><div class="channel-bar"><i style="width:51%"></i></div><strong>$278k</strong></div><div class="channel-row"><span>Organic Search</span><div class="channel-bar"><i style="width:34%"></i></div><strong>$186k</strong></div><div class="channel-row"><span>Email</span><div class="channel-bar"><i style="width:26%"></i></div><strong>$142k</strong></div><div class="channel-row"><span>Affiliate</span><div class="channel-bar"><i style="width:18%"></i></div><strong>$97k</strong></div><div class="channel-row"><span>Unattributed</span><div class="channel-bar"><i style="width:8%"></i></div><strong>$42k</strong></div></div><aside class="reconcile-card"><h3>Shopify ↔ Google reconciliation</h3><div class="reconcile-values"><div><span>Shopify attributed</span><strong>$428k</strong></div><div><span>Google reported</span><strong>$451k</strong></div></div><div class="confidence-ring"><strong>82%</strong></div><p style="font-size:12px;text-align:center;margin-top:12px">Attribution confidence</p></aside></div></div>
  </div>
</section>

<section class="section" id="voice">
  <div class="container"><div class="section-head center reveal"><span class="eyebrow">Malach Voice</span><h2>Talk to your advertising intelligence.</h2><p class="lede">Ask concise questions using verified account context, current-page evidence, screenshots or PDFs.</p><span class="demo-note">Illustrative product demo</span></div>
    <div class="glass-card voice-demo reveal" data-voice-demo><div class="voice-copy"><h3>Clear answers. Grounded in your business.</h3><p style="margin-top:14px">Choose a voice, speak in your preferred language, minimize the call and keep working inside Malach.</p><div class="voice-choices"><span>American · Man</span><span>American · Woman</span><span>British · Man</span><span>British · Woman</span><span>Australian · Man</span><span>Australian · Woman</span></div><button class="btn btn-primary" data-voice-action style="margin-top:26px">Hear Malach</button></div><div class="call-ui"><div class="call-head"><div class="call-brand"><img src="/assets/media/malach-mark.png" alt=""><div><strong>MALACH VOICE</strong><div class="chip-sub">Private operating call</div></div></div><span class="live-pill"><i class="live-dot"></i>READY</span></div><div class="call-state"><div class="call-orb"><img src="/assets/media/malach-mark.png" alt=""></div><p style="margin-top:15px">Ask a business question</p></div><div class="transcript" data-voice-transcript><div class="bubble user">Why did profit fall this week?</div><div class="bubble malach">Ad spend rose 21%, but verified contribution fell 8%. Two Search campaigns account for most of the deterioration. I would reduce exposure there before increasing spend elsewhere.</div></div><div class="call-controls"><button class="call-control" aria-label="Microphone">◉</button><button class="call-control" aria-label="Attach screenshot or PDF">＋</button><button class="call-control" aria-label="End call">×</button></div></div></div>
  </div>
</section>

<section class="section" id="chat">
  <div class="container"><div class="section-head reveal"><span class="eyebrow">Malach Chat</span><h2>Ask your business anything.</h2><p class="lede">A modern AI workspace grounded in verified Google Ads, Shopify, profit, attribution and policy data.</p><span class="demo-note">Illustrative product demo</span></div>
    <div class="glass-card chat-demo reveal"><aside class="chat-sidebar"><button class="btn chat-new">＋ New chat</button><div class="thread-list"><div class="thread active">Where am I wasting money?</div><div class="thread">What would you test tomorrow?</div><div class="thread">Why did POAS fall?</div><div class="thread">Which products deserve more spend?</div></div></aside><div class="chat-main"><div class="chat-messages"><article class="chat-message user"><div class="content">What assumptions is Auto Agent making?</div><div class="avatar">YOU</div></article><article class="chat-message"><div class="avatar"><img src="/assets/media/malach-mark.png" alt="" style="width:25px;height:25px;object-fit:contain"></div><div class="content"><strong>Three assumptions matter most.</strong><p style="margin-top:8px;font-size:13px">Contribution per conversion is $84, click quality remains within the trailing 30-day range, and CPC stays below $3.84. If any one breaks, the test should stop.</p></div></article></div><div class="chat-compose"><div class="compose-box"><input aria-label="Ask Malach" placeholder="Ask Malach about profit, campaigns or the next action…"><button class="btn btn-primary btn-small">Send</button></div></div></div></div>
  </div>
</section>

<section class="section" id="evolution">
  <div class="container"><div class="section-head center reveal"><span class="eyebrow">Evolution Studio</span><h2>An intelligence designed to improve.</h2><p class="lede">Malach measures outcomes, recalibrates probability and can engineer approved improvements in an isolated environment.</p></div><div class="evolution-steps reveal"><article class="evolution-step"><b>1</b><h4>Observe</h4><p>Find a recurring failure or opportunity.</p></article><article class="evolution-step"><b>2</b><h4>Propose</h4><p>Document evidence, risk and expected benefit.</p></article><article class="evolution-step"><b>3</b><h4>Engineer</h4><p>Generate bounded edits in an isolated workspace.</p></article><article class="evolution-step"><b>4</b><h4>Validate</h4><p>Compile, test and retain the unified diff.</p></article><article class="evolution-step"><b>5</b><h4>Review</h4><p>Owner approves, rejects or downloads the build.</p></article></div></div>
</section>

<section class="section" id="portfolio">
  <div class="container"><div class="section-head reveal"><span class="eyebrow">Multi-store</span><h2>One intelligence. Your entire portfolio.</h2><p class="lede">Up to 20 independently configured stores, each with separate credentials, economics, attribution and automation state.</p><span class="demo-note">Illustrative product demo</span></div><div class="glass-card portfolio-shell reveal" data-portfolio-demo><div class="store-switch"><button class="active" data-store="portfolio">Portfolio</button><button data-store="upscale">Aurora Coffee</button><button data-store="north">North &amp; Pine</button><button data-store="atelier">Atelier Supply</button></div><div class="portfolio-metrics"><article><span>Revenue</span><strong data-portfolio-value>$2.84m</strong></article><article><span>Profit</span><strong data-portfolio-value>$438k</strong></article><article><span>Spend</span><strong data-portfolio-value>$612k</strong></article><article><span>Orders</span><strong data-portfolio-value>2,814</strong></article><article><span>ROAS</span><strong data-portfolio-value>4.64×</strong></article><article><span>POAS</span><strong data-portfolio-value>0.72×</strong></article></div><div class="store-table"><div class="store-row head"><span>Store</span><span>Revenue</span><span>Profit</span><span>Spend</span><span>ROAS</span><span>Mode</span></div><div class="store-row" data-store-row="upscale"><strong>Aurora Coffee</strong><span>$1.64m</span><span>$284k</span><span>$352k</span><span>4.66×</span><span>Canary</span></div><div class="store-row" data-store-row="north"><strong>North &amp; Pine</strong><span>$742k</span><span>$96k</span><span>$166k</span><span>4.47×</span><span>Approval</span></div><div class="store-row" data-store-row="atelier"><strong>Atelier Supply</strong><span>$458k</span><span>$58k</span><span>$94k</span><span>4.87×</span><span>Observe</span></div></div></div></div>
</section>

<section class="section" id="control">
  <div class="container"><div class="section-head center reveal"><span class="eyebrow">Control and safety</span><h2>Autonomy with visibility.</h2><p class="lede">Choose the operating authority. Inspect the evidence. Stop immediately when needed.</p></div><div class="mode-grid reveal"><article class="mode-card active"><small>MODE 01</small><h3>Observe</h3><p>Analyze without account changes.</p></article><article class="mode-card"><small>MODE 02</small><h3>Approval</h3><p>Malach proposes; owner approves.</p></article><article class="mode-card"><small>MODE 03</small><h3>Canary Auto</h3><p>Bounded autonomous execution.</p></article><article class="mode-card"><small>MODE 04</small><h3>Full Auto</h3><p>Authorized autonomous operation.</p></article></div><div class="glass-card" style="padding:24px;margin-top:18px"><div class="safety-ledger"><div class="safety-row"><code>14:32:08</code><span>Google mutation validation passed</span><b>VERIFIED</b></div><div class="safety-row"><code>14:32:11</code><span>Budget change read back from account</span><b>VERIFIED</b></div><div class="safety-row"><code>14:32:12</code><span>Outcome window and rollback point recorded</span><b>READY</b></div></div></div></div>
</section>

<section class="section" id="system-map">
  <div class="container"><div class="section-head reveal"><span class="eyebrow">System Map</span><h2>Know exactly what Malach can see.</h2><span class="demo-note">Illustrative product demo</span></div><div class="system-grid reveal"><article class="system-node"><div><div class="system-name">Google Ads</div><div class="system-meta">Verified 2m ago</div></div><i class="system-pulse"></i></article><article class="system-node"><div><div class="system-name">Shopify</div><div class="system-meta">Current</div></div><i class="system-pulse"></i></article><article class="system-node"><div><div class="system-name">OpenAI</div><div class="system-meta">Available</div></div><i class="system-pulse"></i></article><article class="system-node"><div><div class="system-name">Brave</div><div class="system-meta">Current</div></div><i class="system-pulse"></i></article><article class="system-node"><div><div class="system-name">Cloud SQL</div><div class="system-meta">Healthy</div></div><i class="system-pulse"></i></article><article class="system-node"><div><div class="system-name">Worker</div><div class="system-meta">Heartbeat 18s</div></div><i class="system-pulse"></i></article><article class="system-node"><div><div class="system-name">Attribution</div><div class="system-meta">82% confidence</div></div><i class="system-pulse"></i></article><article class="system-node"><div><div class="system-name">Knowledge</div><div class="system-meta">12 documents</div></div><i class="system-pulse"></i></article></div></div>
</section>

<section class="section" id="security">
  <div class="container"><div class="section-head center reveal"><span class="eyebrow">Security</span><h2>Your advertising and commerce data remain yours.</h2><p class="lede">Malach uses encrypted transport, secure credential handling, owner-controlled authorization and an auditable action ledger.</p></div><div class="security-grid"><article class="glass-card security-card reveal"><div class="security-icon">◆</div><h3>Secure credentials</h3><p>Secrets are stored outside the public interface and are never returned to the browser after storage.</p></article><article class="glass-card security-card reveal"><div class="security-icon">◎</div><h3>Workspace isolation</h3><p>Each store retains separate connector credentials, data context and operating authority.</p></article><article class="glass-card security-card reveal"><div class="security-icon">↶</div><h3>Auditable control</h3><p>Every action carries evidence, timestamps, validation, outcome measurement and rollback context.</p></article></div></div>
</section>

<section class="section" id="roadmap">
  <div class="container"><div class="section-head reveal"><span class="eyebrow">Coming next</span><h2>The intelligence layer keeps expanding.</h2><p class="lede">Roadmap items are clearly labeled and are not represented as currently available.</p></div><div class="roadmap-grid"><article class="glass-card roadmap-card reveal"><span class="coming-soon">Coming soon</span><h3>Creative Intelligence Studio</h3><p>Generate and validate creative directions against product economics and measured asset outcomes.</p></article><article class="glass-card roadmap-card reveal"><span class="coming-soon">Coming soon</span><h3>Cross-channel expansion</h3><p>Extend contribution-profit intelligence to additional paid acquisition platforms.</p></article><article class="glass-card roadmap-card reveal"><span class="coming-soon">Coming soon</span><h3>Mobile companion</h3><p>Monitor decisions, approve actions and speak with Malach from a native mobile experience.</p></article></div></div>
</section>

<section class="section" id="pricing-preview">
  <div class="container"><div class="section-head center reveal"><span class="eyebrow">Plans</span><h2>Choose the level of intelligence your business needs.</h2><p class="lede">Simple plans for one store, autonomous operation and multi-store portfolios.</p></div><div class="pricing-grid"><article class="glass-card price-card reveal"><span class="plan-badge">CORE</span><h3>Malach Core</h3><p class="plan-copy">For one store that needs a sharper operating picture.</p><div class="price">Private launch</div><ul class="plan-features"><li>One store</li><li>Google Ads and Shopify intelligence</li><li>Profit Center and Attribution</li><li>Malach Chat and Voice</li></ul><a class="btn" href="/pricing/">View plans</a></article><article class="glass-card price-card featured reveal"><span class="plan-badge">AUTONOMOUS</span><h3>Malach Autonomous</h3><p class="plan-copy">For operators ready for governed autonomous optimization.</p><div class="price">Private launch</div><ul class="plan-features"><li>Auto Agent</li><li>Canary and Full Auto authority</li><li>Advantage market intelligence</li><li>Evolution Studio</li></ul><a class="btn btn-primary" href="/pricing/">Request access</a></article><article class="glass-card price-card reveal"><span class="plan-badge">PORTFOLIO</span><h3>Malach Portfolio</h3><p class="plan-copy">For multiple stores, brands and operators.</p><div class="price">Contact sales</div><ul class="plan-features"><li>Up to 20 stores</li><li>Portfolio God View</li><li>Per-store authority</li><li>Custom onboarding</li></ul><a class="btn" href="/support/?topic=sales">Contact sales</a></article></div></div>
</section>

<section class="section section-tight"><div class="container"><div class="glass-card cta-shell reveal"><span class="eyebrow" style="margin:auto">MALACH</span><h2 style="margin-top:20px">Give paid acquisition an intelligence that never sleeps.</h2><p>Connect your commerce data, choose the operating authority and let every decision become evidence for the next one.</p><div class="hero-actions"><a class="btn btn-primary btn-large" href="/pricing/">Get Malach</a><a class="btn btn-large" href="/product/">Explore the product</a></div></div></div></section>
'''

# reusable component demos for subpages
AGENT_DEMO = r'''
<div class="glass-card agent-shell" data-agent-demo>
  <aside class="agent-side"><div class="agent-tabs" role="tablist"><button class="agent-tab" data-agent-tab="canvas" aria-selected="true">Live Canvas</button><button class="agent-tab" data-agent-tab="algorithm" aria-selected="false">Algorithm</button><button class="agent-tab" data-agent-tab="authority" aria-selected="false">Authority</button></div><div class="agent-authority"><div class="board-status">● OBSERVE</div><p style="font-size:12px;margin-top:9px">Owner-controlled authority.</p></div></aside>
  <div class="agent-board" data-agent-view="canvas"><div class="board-head"><div><div class="board-status">LIVE DECISION TRACE</div><h3 style="margin-top:10px">Opportunity evaluation</h3></div><span class="board-time">14:32:08 UTC</span></div><div class="formula-stack"><article class="formula-card is-active"><div class="formula-name">Posterior conversion rate</div><div class="formula">Beta(α + conversions, β + clicks − conversions)</div><div class="formula-result"><span>Evidence substituted</span><strong>3.72%</strong></div></article><article class="formula-card"><div class="formula-name">Risk-adjusted EV</div><div class="formula">EV − λ × downside risk</div><div class="formula-result"><span>$4,680 − 0.38 × $1,140</span><strong>+$4,247</strong></div></article></div><div class="board-decision"><small>DECISION</small><h3>Run controlled Search test</h3><p>Expected value remains positive after risk adjustment.</p></div></div>
  <div class="agent-board" data-agent-view="algorithm" hidden><div class="board-head"><div><div class="board-status">ALGORITHM</div><h3 style="margin-top:10px">Probability, economics and evidence</h3></div></div><div class="formula-stack"><article class="formula-card"><div class="formula-name">Maximum rational CPC</div><div class="formula">posterior CVR × contribution × safety factor</div><div class="formula-result"><span>3.72% × $84 × 0.82</span><strong>$2.56</strong></div></article></div></div>
  <div class="agent-board" data-agent-view="authority" hidden><div class="mode-grid" style="margin-top:20px"><article class="mode-card active"><small>MODE 01</small><h3>Observe</h3><p>Analyze without account changes.</p></article><article class="mode-card"><small>MODE 02</small><h3>Approval</h3><p>Owner approves.</p></article><article class="mode-card"><small>MODE 03</small><h3>Canary Auto</h3><p>Bounded execution.</p></article><article class="mode-card"><small>MODE 04</small><h3>Full Auto</h3><p>Authorized autonomy.</p></article></div></div>
</div>
'''

FINANCIAL_DEMO = r'''
<div class="glass-card financial-shell" data-financial-chart><div class="chart-head"><div class="chart-toggles"><button class="chart-toggle" data-series="revenue" aria-pressed="true"><i style="background:#c76535"></i>Revenue</button><button class="chart-toggle" data-series="profit" aria-pressed="true"><i style="background:#35ca93"></i>Profit</button><button class="chart-toggle" data-series="spend" aria-pressed="true"><i style="background:#7650d8"></i>Spend</button></div><div class="mode-toggle"><button class="mode-btn" data-chart-mode="shared" aria-pressed="true">Shared $</button><button class="mode-btn" data-chart-mode="compare" aria-pressed="false">Compare trends</button></div></div><div class="chart-wrap"><canvas></canvas><div class="chart-tooltip"></div></div></div>
'''

RESEARCH_DEMO = r'''
<div class="glass-card research-shell"><div class="research-browser"><div class="browser-chrome"><div class="browser-dots"><i></i><i></i><i></i></div><div class="browser-bar">Malach Research Browser · competitive evidence</div></div><div class="browser-result"><article class="search-item"><span class="source-badge">MEASURED GOOGLE EVIDENCE</span><h4>Commercial-intent keyword gap identified</h4><p>Keyword Planner volume and account economics support a bounded test.</p></article><article class="search-item"><span class="source-badge">PUBLIC WEB</span><h4>Competitor offer changed</h4><p>Financing and delivery language moved above the fold.</p></article><article class="search-item"><span class="source-badge">MODELED ESTIMATE</span><h4>Landing-page response opportunity</h4><p>Probability 68%. Controlled validation required.</p></article></div></div><aside class="research-side"><h3>Evidence sources</h3><div class="provenance"><article><i style="background:#6ba5ff"></i><div><strong>Google Ads</strong><br><span>Account and Keyword Planner</span></div></article><article><i style="background:#ef986b"></i><div><strong>Brave Search</strong><br><span>Independent organic evidence</span></div></article><article><i style="background:#35ca93"></i><div><strong>Public web</strong><br><span>Pages, offers and changes</span></div></article><article><i style="background:#a68aff"></i><div><strong>Modeled estimate</strong><br><span>Probabilistic inference</span></div></article></div></aside></div>
'''

VOICE_DEMO = r'''
<div class="glass-card voice-demo"><div class="voice-copy"><h3>Ask a concise business question.</h3><p style="margin-top:14px">Malach answers from verified account context, current-page evidence and the files you choose to share.</p><div class="voice-choices"><span>American</span><span>British</span><span>Australian</span><span>Male</span><span>Female</span><span>Multiple languages</span></div></div><div class="call-ui"><div class="call-head"><div class="call-brand"><img src="/assets/media/malach-mark.png" alt=""><div><strong>MALACH VOICE</strong><div class="chip-sub">Private operating call</div></div></div><span class="live-pill"><i class="live-dot"></i>READY</span></div><div class="call-state"><div class="call-orb"><img src="/assets/media/malach-mark.png" alt=""></div></div><div class="transcript"><div class="bubble user">Why did contribution profit fall?</div><div class="bubble malach">Ad spend rose while verified margin declined. Two campaigns explain most of the deterioration. I would reduce exposure there first.</div></div></div></div>
'''

PAGES = {}

PAGES['product'] = page(
    'Product — Malach',
    'Explore Malach: Google Ads intelligence, Shopify economics, attribution, Auto Agent, Advantage, Voice and multi-store operations.',
    '/product/', '/product/',
    f'''<section class="subpage-hero"><div class="container"><div class="reveal"><span class="eyebrow">Product</span><h1>One intelligence across paid acquisition and commerce economics.</h1><p>Malach continuously connects advertising evidence to Shopify revenue, costs, attribution, competitor signals and contribution profit.</p><div class="hero-actions"><a class="btn btn-primary btn-large" href="/pricing/">Get Malach</a><a class="btn btn-large" href="/auto-agent/">Explore Auto Agent</a></div></div><div class="glass-card subpage-visual reveal"><img src="/assets/media/malach-mark.png" alt="Malach mark" style="width:280px;filter:drop-shadow(0 30px 70px rgba(118,80,216,.24))"></div></div></section>
<section class="section"><div class="container"><div class="section-head"><span class="eyebrow">The operating system</span><h2>From evidence to measured outcome.</h2></div><div class="detail-grid"><article class="glass-card detail-card reveal"><span class="detail-index">01</span><h3>Connect the economics</h3><p>Google Ads, Shopify, costs, returns, fees, shipping and attribution form one operating ledger.</p></article><article class="glass-card detail-card reveal"><span class="detail-index">02</span><h3>Find the decision</h3><p>Malach evaluates probability, expected contribution, downside and the value of additional evidence.</p></article><article class="glass-card detail-card reveal"><span class="detail-index">03</span><h3>Measure the result</h3><p>Actions are verified, timestamped and compared with subsequent business outcomes.</p></article><article class="glass-card detail-card reveal"><span class="detail-index">04</span><h3>Study the market</h3><p>Advantage monitors keyword economics, competitors, offers and public evidence.</p></article><article class="glass-card detail-card reveal"><span class="detail-index">05</span><h3>Ask Malach</h3><p>Chat and Voice answer concise questions using verified account context and selected documents.</p></article><article class="glass-card detail-card reveal"><span class="detail-index">06</span><h3>Operate a portfolio</h3><p>Up to 20 isolated stores can retain separate credentials, economics and automation authority.</p></article></div></div></section>
<section class="section"><div class="container">{FINANCIAL_DEMO}</div></section>''',
    ['/assets/js/subpage.js']
)

PAGES['auto-agent'] = page(
    'Auto Agent — Malach',
    'Inspect Malach’s evidence, formulas, probability, expected value, authority and measured outcomes.',
    '/auto-agent/', '/auto-agent/',
    f'''<section class="subpage-hero"><div class="container"><div class="reveal"><span class="eyebrow">Auto Agent</span><h1>Autonomy with mathematics you can inspect.</h1><p>Live Canvas records evidence and formulas. Algorithm exposes the economic model. Authority defines what Malach may do.</p><div class="hero-actions"><a class="btn btn-primary btn-large" href="/pricing/">Get Malach</a></div></div><div class="glass-card subpage-visual reveal"><div style="font:600 15px/1.8 var(--mono);color:var(--lavender)">P(profit &gt; 0 | evidence) = 78.4%<br>EV = +$4,680<br>Risk-adjusted EV = +$4,247<br>Max CPC = $3.84<br><span style="color:var(--emerald)">→ RUN CONTROLLED TEST</span></div></div></div></section><section class="section"><div class="container">{AGENT_DEMO}</div></section><section class="section"><div class="container"><div class="section-head center"><span class="eyebrow">Operating authority</span><h2>Choose how Malach participates.</h2></div><div class="mode-grid"><article class="mode-card active"><small>OBSERVE</small><h3>Analyze</h3><p>No account changes.</p></article><article class="mode-card"><small>APPROVAL</small><h3>Propose</h3><p>Owner approves each action.</p></article><article class="mode-card"><small>CANARY</small><h3>Bound</h3><p>Limited autonomous action.</p></article><article class="mode-card"><small>FULL AUTO</small><h3>Authorize</h3><p>Autonomous operation within owner controls.</p></article></div></div></section>''',
    ['/assets/js/subpage.js']
)

PAGES['intelligence'] = page(
    'Intelligence — Malach',
    'See how Malach finds opportunities, forecasts outcomes, measures evidence and learns from results.',
    '/intelligence/', '/intelligence/',
    '''<section class="subpage-hero"><div class="container"><div class="reveal"><span class="eyebrow">Intelligence</span><h1>Continuous opportunity detection across the account.</h1><p>Malach studies search demand, creative signals, budget saturation, product economics and measured outcomes—around the clock.</p></div><div class="glass-card subpage-visual reveal"><div class="opportunity-card" style="width:100%;min-height:0"><div class="opportunity-type">LIVE OPPORTUNITY</div><h3>Low-competition commercial terms support a bounded Search test.</h3><div class="opportunity-kpis"><div><span>Probability profitable</span><strong>74%</strong></div><div><span>Expected contribution</span><strong>+$3,840</strong></div></div></div></div></div></section><section class="section"><div class="container"><div class="detail-grid"><article class="glass-card detail-card"><span class="detail-index">FORECAST</span><h3>Expected value</h3><p>Estimate contribution, downside and the value of additional information before committing spend.</p></article><article class="glass-card detail-card"><span class="detail-index">CALIBRATE</span><h3>Outcome learning</h3><p>Compare predicted probability with measured results and recalibrate future estimates.</p></article><article class="glass-card detail-card"><span class="detail-index">PRIORITIZE</span><h3>Opportunity queue</h3><p>Rank ideas by evidence quality, risk-adjusted value and time to learn.</p></article></div></div></section>'''
)

PAGES['advantage'] = page(
    'Advantage — Malach',
    'Monitor competitors, keyword economics, offers, search visibility and source-labeled market evidence.',
    '/advantage/', '/advantage/',
    f'''<section class="subpage-hero"><div class="container"><div class="reveal"><span class="eyebrow">Advantage</span><h1>Market intelligence with evidence provenance.</h1><p>Track competitors, keyword markets, offers, landing-page changes and search visibility without presenting estimates as measured facts.</p></div><div class="glass-card subpage-visual reveal"><div class="provenance" style="width:100%"><article><i style="background:#6ba5ff"></i><div><strong>Google evidence</strong><br><span>Measured account and Keyword Planner signals</span></div></article><article><i style="background:#ef986b"></i><div><strong>Brave evidence</strong><br><span>Independent organic verification</span></div></article><article><i style="background:#35ca93"></i><div><strong>Public web</strong><br><span>Pages, offers and changes</span></div></article></div></div></div></section><section class="section"><div class="container">{RESEARCH_DEMO}</div></section>'''
)

PAGES['attribution'] = page(
    'Attribution — Malach',
    'Understand revenue, orders, contribution and confidence by acquisition channel.',
    '/attribution/', '',
    '''<section class="subpage-hero"><div class="container"><div class="reveal"><span class="eyebrow">Attribution</span><h1>Know where profit actually came from.</h1><p>Malach separates Google-attributed, non-Google and genuinely unattributed revenue, then reconciles Shopify with platform reporting.</p></div><div class="glass-card subpage-visual reveal"><div class="confidence-ring"><strong>82%</strong></div></div></div></section><section class="section"><div class="container"><div class="glass-card attribution-shell"><div class="attribution-summary"><div class="channel-list"><div class="channel-row"><span>Google Ads</span><div class="channel-bar"><i style="width:78%"></i></div><strong>$428k</strong></div><div class="channel-row"><span>Direct</span><div class="channel-bar"><i style="width:51%"></i></div><strong>$278k</strong></div><div class="channel-row"><span>Organic Search</span><div class="channel-bar"><i style="width:34%"></i></div><strong>$186k</strong></div><div class="channel-row"><span>Email</span><div class="channel-bar"><i style="width:26%"></i></div><strong>$142k</strong></div><div class="channel-row"><span>Unattributed</span><div class="channel-bar"><i style="width:8%"></i></div><strong>$42k</strong></div></div><aside class="reconcile-card"><h3>Reconciliation</h3><div class="reconcile-values"><div><span>Shopify attributed</span><strong>$428k</strong></div><div><span>Google reported</span><strong>$451k</strong></div></div><p style="margin-top:18px;font-size:13px">Confidence reflects journey coverage, timing and discrepancy.</p></aside></div></div></div></section>'''
)

PAGES['voice'] = page(
    'Malach Voice — Talk to your advertising intelligence',
    'Speak with Malach using verified business context, live transcription, selectable voices, languages, screenshots and PDFs.',
    '/voice/', '',
    f'''<section class="subpage-hero"><div class="container"><div class="reveal"><span class="eyebrow">Malach Voice</span><h1>A private operating call with your business intelligence.</h1><p>Ask concise questions, change voice and language, minimize the call and keep working across Malach.</p></div><div class="glass-card subpage-visual reveal"><img src="/assets/media/malach-mark.png" alt="Malach" style="width:250px"></div></div></section><section class="section"><div class="container">{VOICE_DEMO}</div></section><section class="section"><div class="container"><div class="detail-grid"><article class="glass-card detail-card"><span class="detail-index">CONTEXT</span><h3>Verified account data</h3><p>Answers can use Google Ads, Shopify, profit, attribution, Advantage and operating-state evidence.</p></article><article class="glass-card detail-card"><span class="detail-index">INPUTS</span><h3>Screenshots and PDFs</h3><p>Choose the files and current-page context that Malach may inspect.</p></article><article class="glass-card detail-card"><span class="detail-index">VOICE</span><h3>Clear spoken delivery</h3><p>Concise answers, multiple voice profiles, language choice and live transcription.</p></article></div></div></section>'''
)

PAGES['security'] = page(
    'Security — Malach',
    'Learn how Malach approaches credential handling, workspace isolation, authorization, auditability and billing security.',
    '/security/', '/security/',
    '''<section class="subpage-hero"><div class="container"><div class="reveal"><span class="eyebrow">Security</span><h1>Control, isolation and auditability by design.</h1><p>Malach protects connector credentials, separates store workspaces and records the evidence behind operating decisions.</p></div><div class="glass-card subpage-visual reveal"><div class="system-grid" style="grid-template-columns:1fr 1fr;width:100%"><article class="system-node"><div><div class="system-name">Encrypted transport</div><div class="system-meta">HTTPS</div></div><i class="system-pulse"></i></article><article class="system-node"><div><div class="system-name">Secret handling</div><div class="system-meta">Not exposed in UI</div></div><i class="system-pulse"></i></article><article class="system-node"><div><div class="system-name">Workspace isolation</div><div class="system-meta">Per store</div></div><i class="system-pulse"></i></article><article class="system-node"><div><div class="system-name">Action ledger</div><div class="system-meta">Timestamped</div></div><i class="system-pulse"></i></article></div></div></div></section><section class="section"><div class="container"><div class="security-grid"><article class="glass-card security-card"><div class="security-icon">◆</div><h3>Secure credential handling</h3><p>API keys and OAuth secrets are not displayed back to ordinary browser sessions after storage.</p></article><article class="glass-card security-card"><div class="security-icon">◎</div><h3>Owner authorization</h3><p>Operating authority remains visible, selectable and auditable.</p></article><article class="glass-card security-card"><div class="security-icon">↶</div><h3>Emergency control</h3><p>Emergency Stop, validation, read-after-write checks and rollback context support operational control.</p></article><article class="glass-card security-card"><div class="security-icon">▦</div><h3>Store isolation</h3><p>Each store retains separate connector credentials and data context.</p></article><article class="glass-card security-card"><div class="security-icon">◌</div><h3>Payment security</h3><p>Stripe Checkout handles card collection; Malach does not receive raw card details.</p></article><article class="glass-card security-card"><div class="security-icon">≡</div><h3>Audit ledger</h3><p>Actions, evidence, results and errors can be retained for review.</p></article></div></div></section>'''
)

PAGES['pricing'] = page(
    'Pricing — Malach',
    'Choose Malach Core, Autonomous or Portfolio. Online billing is enabled when Stripe price IDs are configured.',
    '/pricing/', '/pricing/',
    '''<section class="subpage-hero"><div class="container"><div class="reveal"><span class="eyebrow">Pricing</span><h1>Choose the operating level your business needs.</h1><p>Plan architecture is ready for monthly and annual Stripe subscriptions. Launch pricing remains configurable.</p></div><div class="glass-card subpage-visual reveal"><div style="text-align:center"><span class="coming-soon">Private launch</span><h3 style="margin-top:18px;font-size:2rem">Simple plans. Clear authority.</h3><p style="margin-top:12px">No percentage-of-spend pricing is assumed.</p></div></div></div></section><section class="section"><div class="container"><div class="pricing-toggle"><button class="active" data-billing-interval="monthly">Monthly</button><button data-billing-interval="annual">Annual</button></div><p class="form-status" data-pricing-status style="text-align:center;margin-bottom:18px"></p><div class="pricing-grid"><article class="glass-card price-card" data-plan="core" data-fallback-price="Private launch"><span class="plan-badge">CORE</span><h3>Malach Core</h3><p class="plan-copy">For one store that needs a sharper operating picture.</p><div class="price"><span data-price>Private launch</span> <small data-cadence></small></div><ul class="plan-features"><li>One Shopify store</li><li>Google Ads and Shopify intelligence</li><li>Profit Center and Attribution</li><li>Malach Chat and Voice</li><li>Observe and Approval modes</li></ul><button class="btn" data-checkout>Request access</button></article><article class="glass-card price-card featured" data-plan="autonomous" data-fallback-price="Private launch"><span class="plan-badge">AUTONOMOUS</span><h3>Malach Autonomous</h3><p class="plan-copy">For businesses ready for governed autonomous optimization.</p><div class="price"><span data-price>Private launch</span> <small data-cadence></small></div><ul class="plan-features"><li>Everything in Core</li><li>Auto Agent and Agent Canvas</li><li>Canary and Full Auto authority</li><li>Advantage market intelligence</li><li>Evolution Studio</li><li>Priority support</li></ul><button class="btn btn-primary" data-checkout>Request access</button></article><article class="glass-card price-card" data-plan="portfolio" data-fallback-price="Contact sales" data-contact="true"><span class="plan-badge">PORTFOLIO</span><h3>Malach Portfolio</h3><p class="plan-copy">For multiple stores, brands and operators.</p><div class="price"><span data-price>Contact sales</span> <small data-cadence></small></div><ul class="plan-features"><li>Up to 20 isolated stores</li><li>Portfolio-wide God View</li><li>Per-store credentials and authority</li><li>Team governance</li><li>Custom onboarding</li></ul><button class="btn" data-checkout>Contact sales</button></article></div></div></section><section class="section section-tight"><div class="container"><div class="glass-card cta-shell"><h2>Need a custom launch plan?</h2><p>Tell us about your stores, Google Ads accounts and operating requirements.</p><div class="hero-actions"><a class="btn btn-primary" href="/support/?topic=sales">Contact sales</a></div></div></div></section>''',
    ['/assets/js/pricing.js']
)

PAGES['about'] = page(
    'About — Malach',
    'Malach is an autonomous commerce intelligence system built to make paid acquisition more measurable and economically accountable.',
    '/about/', '',
    '''<section class="content-page"><div class="content-narrow"><span class="eyebrow">About Malach</span><h1>Build advertising decisions around evidence and economics.</h1><p class="lede">Malach was created around a simple premise: paid acquisition should be governed by the economics behind the order, not isolated platform metrics.</p><h2>What Malach is</h2><p>Malach is an autonomous commerce intelligence and Google Ads operating system for ecommerce businesses. It brings advertising performance, Shopify economics, attribution, market evidence and operating authority into one decision layer.</p><h2>What Malach is not</h2><p>Malach is not an agency, a generic chatbot or a guaranteed-profit machine. It is software that helps operators observe evidence, calculate tradeoffs, act with defined authority, measure results and learn from outcomes.</p><h2>Why the name</h2><p>Malach means messenger. The product is built to surface the message inside complex account data: what changed, why it matters and what the evidence supports doing next.</p></div></section>'''
)

PAGES['support'] = page(
    'Support — Malach',
    'Contact Malach support, request pricing or find help with billing, Google Ads, Shopify and account access.',
    '/support/', '',
    '''<section class="content-page"><div class="container"><div class="section-head"><span class="eyebrow">Support</span><h1>How can we help?</h1><p class="lede">For account access, billing, connectors or product questions, send a message or email support@malach.app.</p></div><div class="support-layout"><aside class="glass-card support-card"><h3>Useful paths</h3><div class="support-links"><a href="https://app.malach.app">Open Malach</a><a href="/pricing/">Plans and billing</a><a href="/security/">Security</a><a href="mailto:support@malach.app">support@malach.app</a></div></aside><form class="glass-card support-form form-grid" data-support-form data-endpoint="/api/contact"><input type="text" name="website" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px"><div class="field"><label for="name">Name</label><input id="name" name="name" required></div><div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required></div><div class="field"><label for="topic">Topic</label><select id="topic" name="topic"><option>Product question</option><option>Pricing</option><option>Billing</option><option>Google Ads</option><option>Shopify</option><option>Account access</option><option>Security</option></select></div><div class="field"><label for="message">Message</label><textarea id="message" name="message" required></textarea></div><button class="btn btn-primary" type="submit">Send message</button><div class="form-status" aria-live="polite"></div></form></div></div></section>'''
)

PRIVACY = '''<section class="content-page"><div class="content-narrow"><span class="eyebrow">Legal</span><h1>Privacy Policy</h1><p class="content-meta">Effective date: August 12, 2026</p><p>This Privacy Policy explains how Malach collects, uses and protects information when you visit malach.app or use the Malach application.</p><h2>Information you provide</h2><p>We may receive account registration information, support messages, billing contact information and configuration details you choose to provide. Payment card details are collected by Stripe Checkout and are not provided to Malach as raw card data.</p><h2>Connected services</h2><p>When you authorize Google Ads, Shopify, OpenAI, Brave Search or another supported service, Malach processes the data required to provide the features you enable. Access is governed by the permissions you grant and may be revoked through the connected service.</p><h2>How information is used</h2><ul><li>Provide and secure the service.</li><li>Process subscriptions and account entitlements.</li><li>Operate requested analytics, synchronization and automation features.</li><li>Respond to support requests.</li><li>Maintain audit, reliability and security records.</li></ul><h2>Data sharing</h2><p>Malach does not sell personal information. Information may be processed by infrastructure, payment and service providers that support the product, subject to their agreements and applicable law.</p><h2>Retention and deletion</h2><p>Information is retained as needed to provide the service, satisfy legal obligations and maintain security or audit records. Account deletion requests may be submitted to support@malach.app.</p><h2>Security</h2><p>Malach uses encrypted HTTPS transport, controlled access to credentials and workspace isolation. No internet service can guarantee absolute security.</p><h2>Contact</h2><p>Questions or requests: <a href="mailto:support@malach.app">support@malach.app</a>.</p></div></section>'''
PAGES['privacy'] = page('Privacy Policy — Malach', 'Malach privacy policy for the public website and application.', '/privacy/', '', PRIVACY)

TERMS = '''<section class="content-page"><div class="content-narrow"><span class="eyebrow">Legal</span><h1>Terms of Service</h1><p class="content-meta">Effective date: August 12, 2026</p><p>These Terms govern access to malach.app and the Malach software service. By using Malach, you agree to these Terms.</p><h2>Authorized use</h2><p>You are responsible for the accounts, stores, advertising properties and credentials you connect, and for ensuring you have authority to use them.</p><h2>Advertising decisions</h2><p>Malach provides analysis, recommendations and optional automation based on available evidence. Advertising outcomes cannot be guaranteed. Markets, attribution, inventory, pricing and customer behavior may change.</p><h2>Operating authority</h2><p>You control the operating mode and are responsible for the financial limits, policies and permissions you configure. Emergency controls, validation and audit features reduce risk but do not eliminate it.</p><h2>Subscriptions and billing</h2><p>Paid subscriptions are processed by Stripe. Plan terms, renewal, cancellation and refund rules shown at checkout form part of these Terms. Access may be limited when payment is overdue or the subscription ends.</p><h2>Acceptable use</h2><p>You may not misuse the service, attempt unauthorized access, disrupt other users, introduce malicious code or use Malach in violation of law or third-party platform rules.</p><h2>Intellectual property</h2><p>Malach and its software, design, branding and documentation are protected by applicable intellectual-property laws. These Terms do not transfer ownership.</p><h2>Availability and changes</h2><p>Features may evolve. Malach may perform maintenance, change functionality or discontinue features when reasonably necessary.</p><h2>Disclaimer and limitation</h2><p>Malach is provided on an “as available” basis to the extent permitted by law. Liability is limited to the maximum extent permitted by applicable law.</p><h2>Contact</h2><p>Questions: <a href="mailto:support@malach.app">support@malach.app</a>.</p></div></section>'''
PAGES['terms'] = page('Terms of Service — Malach', 'Terms governing the Malach website and software service.', '/terms/', '', TERMS)

PAGES['login'] = page(
    'Sign in — Malach', 'Open the Malach application.', '/login/', '',
    '''<section class="login-shell"><div class="glass-card login-card"><img src="/assets/media/malach-lockup.png" alt="Malach"><h1>Open Malach</h1><p>Sign in to your autonomous commerce intelligence workspace.</p><a class="btn btn-primary btn-large" href="https://app.malach.app">Continue to app.malach.app</a><a class="nav-link" href="/support/" style="display:inline-block;margin-top:14px">Need help?</a></div></section>'''
)

PAGES['status'] = page('Status — Malach', 'Malach service status page.', '/status/', '', '''<section class="content-page"><div class="content-narrow"><span class="eyebrow">Status</span><h1>Malach service status</h1><div class="glass-card" style="padding:28px;margin-top:30px"><div class="system-node"><div><div class="system-name">Public website</div><div class="system-meta">Operational</div></div><i class="system-pulse"></i></div><p style="margin-top:20px">A dedicated live status service can be connected here before public launch.</p></div></div></section>''')
PAGES['changelog'] = page('Changelog — Malach', 'Product updates and release notes for Malach.', '/changelog/', '', '''<section class="content-page"><div class="content-narrow"><span class="eyebrow">Changelog</span><h1>What is new in Malach</h1><article class="glass-card" style="padding:28px;margin-top:30px"><span class="coming-soon">Launch preparation</span><h2 style="margin-top:18px">Public website foundation</h2><p>New product pages, pricing architecture, billing integration, legal routes and launch-ready brand system.</p></article></div></section>''')

# Home with structured data
home_extra = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareApplication","name":"Malach","applicationCategory":"BusinessApplication","operatingSystem":"Web","url":"https://malach.app","description":"Autonomous commerce intelligence for mathematically informed advertising decisions."}</script>'''
home_html = f'''{head('Malach — Autonomous Commerce Intelligence', 'Malach continuously analyzes Google Ads, Shopify economics, attribution and market signals to turn commerce data into mathematically informed advertising decisions.', '/', home_extra)}
<body>
{header('')}
<main id="main">{HOME}</main>
{footer()}
{COMMAND}
<script type="module" src="/assets/js/site.js"></script>
<script type="module" src="/assets/js/home.js"></script>
</body></html>'''

(ROOT / 'index.html').write_text(home_html, encoding='utf-8')
for slug, html in PAGES.items():
    d = ROOT / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / 'index.html').write_text(html, encoding='utf-8')

# 404
(ROOT / '404.html').write_text(page('Page not found — Malach', 'The requested Malach page could not be found.', '/404.html', '', '''<section class="login-shell"><div class="glass-card login-card"><img src="/assets/media/malach-mark.png" alt="Malach" style="width:130px"><h1>Page not found</h1><p>The page you requested does not exist or has moved.</p><a class="btn btn-primary btn-large" href="/">Return home</a></div></section>'''), encoding='utf-8')
print('Generated', 1 + len(PAGES), 'pages')
