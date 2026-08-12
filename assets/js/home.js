import { initFinancialCharts } from './chart.js';

const equations = [
  ['Posterior CVR', 'Beta(19 + 7, 481 + 214 − 7)', '3.72% · confidence 0.81'],
  ['Break-even CVR', '$3.12 CPC ÷ $84 contribution', '3.71% threshold'],
  ['Maximum rational CPC', '3.72% × $84 × 0.82 safety factor', '$2.56'],
  ['Risk-adjusted EV', '$4,680 EV − 0.38 × $1,140 downside', '+$4,247'],
  ['Decision', 'P(profit > 0 | evidence) = 78.4%', 'RUN CONTROLLED SEARCH TEST']
];

function setupHeroEquations() {
  const strip = document.querySelector('[data-equation-strip]');
  if (!strip) return;
  let index = 0;
  const render = () => {
    const [name, formula, result] = equations[index];
    strip.innerHTML = `<div class="equation-line"><strong>${name}</strong><br>${formula}<br><span style="color:#35ca93">→ ${result}</span></div>`;
    index = (index + 1) % equations.length;
  };
  render();
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches) setInterval(render, 2700);
}

function setupAgentTabs() {
  document.querySelectorAll('[data-agent-demo]').forEach(shell => {
    const tabs = shell.querySelectorAll('[data-agent-tab]');
    const views = shell.querySelectorAll('[data-agent-view]');
    tabs.forEach(tab => tab.addEventListener('click', () => {
      tabs.forEach(t => t.setAttribute('aria-selected', String(t === tab)));
      views.forEach(view => view.hidden = view.dataset.agentView !== tab.dataset.agentTab);
      window.malachTrack?.('agent_demo_tab', { tab: tab.dataset.agentTab });
    }));
  });
}

function setupFormulaPulse() {
  const cards = [...document.querySelectorAll('.formula-card')];
  if (!cards.length || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let i = 0;
  setInterval(() => {
    cards.forEach((card, idx) => card.classList.toggle('is-active', idx === i));
    i = (i + 1) % cards.length;
  }, 1900);
}

function setupVoiceDemo() {
  const demo = document.querySelector('[data-voice-demo]');
  if (!demo) return;
  const button = demo.querySelector('[data-voice-action]');
  const transcript = demo.querySelector('[data-voice-transcript]');
  const orb = demo.querySelector('.call-orb');
  const exchanges = [
    ['Why did profit fall this week?', 'Ad spend rose 21%, but verified contribution fell 8%. Two Search campaigns account for most of the deterioration. I would reduce exposure there before increasing spend elsewhere.'],
    ['What would you test tomorrow?', 'A controlled Search test around two low-competition commercial terms. The break-even CPC is $5.08; I would cap the first test at $375 and stop if probability drops below 62%.'],
    ['What are competitors changing?', 'Two competitors increased financing visibility and shortened their primary offer. Your strongest counter is a product-specific landing page with clearer monthly-payment economics.']
  ];
  let i = 0;
  button?.addEventListener('click', () => {
    const [q, a] = exchanges[i % exchanges.length];
    i++;
    button.textContent = 'Listening…';
    orb?.classList.add('is-listening');
    setTimeout(() => {
      transcript.innerHTML = `<div class="bubble user">${q}</div><div class="bubble malach">${a}</div>`;
      button.textContent = 'Ask another question';
      orb?.classList.remove('is-listening');
    }, 850);
  });
}

function setupStoreSwitch() {
  const shell = document.querySelector('[data-portfolio-demo]');
  if (!shell) return;
  const buttons = shell.querySelectorAll('[data-store]');
  const rows = shell.querySelectorAll('[data-store-row]');
  const values = {
    portfolio: ['$2.84m', '$438k', '$612k', '2,814', '4.64×', '0.72×'],
    upscale: ['$1.64m', '$284k', '$352k', '1,420', '4.66×', '0.81×'],
    north: ['$742k', '$96k', '$166k', '812', '4.47×', '0.58×'],
    atelier: ['$458k', '$58k', '$94k', '582', '4.87×', '0.62×']
  };
  const metrics = shell.querySelectorAll('[data-portfolio-value]');
  buttons.forEach(btn => btn.addEventListener('click', () => {
    buttons.forEach(b => b.classList.toggle('active', b === btn));
    const key = btn.dataset.store;
    metrics.forEach((el, idx) => el.textContent = values[key][idx]);
    rows.forEach(row => row.hidden = key !== 'portfolio' && row.dataset.storeRow !== key);
  }));
}

function setupOpportunityFeed() {
  const feed = document.querySelector('[data-opportunity-feed]');
  if (!feed || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const cards = [...feed.children];
  let i = 0;
  setInterval(() => {
    cards.forEach((card, idx) => {
      const active = idx === i;
      card.style.borderColor = active ? 'rgba(199,101,53,.38)' : '';
      card.style.transform = active ? 'translateY(-5px)' : '';
    });
    i = (i + 1) % cards.length;
  }, 2600);
}

setupHeroEquations();
setupAgentTabs();
setupFormulaPulse();
setupVoiceDemo();
setupStoreSwitch();
setupOpportunityFeed();
initFinancialCharts();
