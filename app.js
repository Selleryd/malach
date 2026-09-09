(() => {
  'use strict';

  const doc = document.documentElement;
  const body = document.body;
  const header = document.querySelector('[data-header]');
  const menuButton = document.querySelector('[data-menu-button]');
  const menuPanel = document.querySelector('[data-menu-panel]');
  const progress = document.querySelector('[data-page-progress]');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  requestAnimationFrame(() => window.setTimeout(() => document.querySelector('.boot')?.classList.add('is-done'), 120));
  window.setTimeout(() => document.querySelector('.boot')?.classList.add('is-done'), 1200);

  const closeMenu = () => {
    if (!menuButton || !menuPanel) return;
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Open menu');
    menuPanel.setAttribute('aria-hidden', 'true');
    menuPanel.classList.remove('is-open');
    body.classList.remove('menu-open');
    document.querySelector('main')?.removeAttribute('inert');
    document.querySelector('footer')?.removeAttribute('inert');
  };

  menuButton?.addEventListener('click', () => {
    const opening = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(opening));
    menuButton.setAttribute('aria-label', opening ? 'Close menu' : 'Open menu');
    menuPanel?.setAttribute('aria-hidden', String(!opening));
    menuPanel?.classList.toggle('is-open', opening);
    body.classList.toggle('menu-open', opening);
    document.querySelector('main')?.toggleAttribute('inert', opening);
    document.querySelector('footer')?.toggleAttribute('inert', opening);
    if (opening) window.setTimeout(() => menuPanel?.querySelector('a,summary')?.focus(), 60);
  });
  menuPanel?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  const dropdownButton = document.querySelector('[data-dropdown-button]');
  const dropdown = dropdownButton?.closest('.nav-dropdown');
  const dropdownPanel = document.querySelector('[data-dropdown-panel]');
  let dropdownTimer;
  const setDropdown = open => {
    if (!dropdownButton || !dropdown || !dropdownPanel) return;
    dropdownButton.setAttribute('aria-expanded', String(open));
    dropdown.classList.toggle('is-open', open);
  };
  dropdownButton?.addEventListener('click', () => setDropdown(dropdownButton.getAttribute('aria-expanded') !== 'true'));
  dropdown?.addEventListener('pointerenter', () => { window.clearTimeout(dropdownTimer); setDropdown(true); });
  dropdown?.addEventListener('pointerleave', () => { dropdownTimer = window.setTimeout(() => setDropdown(false), 150); });
  dropdown?.addEventListener('focusout', event => { if (!dropdown.contains(event.relatedTarget)) setDropdown(false); });
  document.addEventListener('pointerdown', event => { if (dropdown && !dropdown.contains(event.target)) setDropdown(false); });
  document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    const hadDropdown = dropdownButton?.getAttribute('aria-expanded') === 'true';
    const hadMenu = menuButton?.getAttribute('aria-expanded') === 'true';
    setDropdown(false);
    closeMenu();
    if (hadDropdown) dropdownButton?.focus();
    else if (hadMenu) menuButton?.focus();
  });

  document.querySelectorAll('[data-scroll-to]').forEach(button => {
    button.addEventListener('click', () => {
      document.getElementById(button.dataset.scrollTo)?.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  });

  const revealTargets = document.querySelectorAll('.reveal,.reveal-scale');
  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    revealTargets.forEach(el => revealObserver.observe(el));

    const motionObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => entry.target.classList.toggle('is-inview', entry.isIntersecting));
    }, { rootMargin: '20% 0px 20% 0px', threshold: 0 });
    document.querySelectorAll('section').forEach(section => motionObserver.observe(section));
  } else {
    revealTargets.forEach(el => el.classList.add('is-visible'));
    document.querySelectorAll('section').forEach(section => section.classList.add('is-inview'));
  }

  const wordHeading = document.querySelector('[data-word-reveal]');
  if (wordHeading) {
    const text = wordHeading.textContent.trim();
    wordHeading.textContent = '';
    text.split(/\s+/).forEach(word => {
      const span = document.createElement('span');
      span.className = 'word';
      span.textContent = word;
      wordHeading.appendChild(span);
    });
  }

  const visionData = {
    all: {
      title: 'All live channels', summary: 'Every channel is measured against verified Shopify economics.', barLabel: 'Contribution by live channel',
      metrics: [['Net revenue', '$428,614'], ['Ad spend', '$72,918'], ['Contribution', '$184,290'], ['True ROAS', '5.88×']], confidence: 94, shares: [35, 25, 17, 23]
    },
    google: {
      title: 'Google Ads', summary: 'Search spend and clicks are matched to verified orders, costs, and contribution.', barLabel: 'Selected contribution view',
      metrics: [['Contribution share', '35%'], ['Ad spend', '$28,410'], ['Contribution', '$64,502'], ['Evidence', '1,842 orders']], confidence: 98, shares: [100, 0, 0, 0]
    },
    meta: {
      title: 'Meta Ads', summary: 'Paid social results are checked against the same store-level profit standard.', barLabel: 'Selected contribution view',
      metrics: [['Contribution share', '25%'], ['Ad spend', '$18,760'], ['Contribution', '$46,073'], ['Role', 'Assisted + direct']], confidence: 91, shares: [0, 100, 0, 0]
    },
    tiktok: {
      title: 'TikTok Ads', summary: 'Creative demand signals are connected to orders and contribution before they influence a move.', barLabel: 'Selected contribution view',
      metrics: [['Contribution share', '17%'], ['Ad spend', '$11,940'], ['Contribution', '$31,329'], ['Role', 'Demand discovery']], confidence: 86, shares: [0, 0, 100, 0]
    },
    amazon: {
      title: 'Amazon Ads', summary: 'Sponsored sales are compared with cost, margin, and the rest of the channel portfolio.', barLabel: 'Selected contribution view',
      metrics: [['Contribution share', '23%'], ['Ad spend', '$13,808'], ['Contribution', '$42,386'], ['Status', 'Live · Portfolio']], confidence: 93, shares: [0, 0, 0, 100]
    },
    shopify: {
      title: 'Commerce truth', summary: 'Shopify orders, refunds, products, and visible costs anchor every channel to what the business earned.', barLabel: 'Order evidence · matched / modeled / unresolved',
      metrics: [['Orders', '521'], ['Refunds', '$14,820'], ['Net revenue', '$428,614'], ['Orders matched', '98.2%']], confidence: 98.2, shares: [86, 8, 6, 0]
    }
  };
  document.querySelectorAll('[data-vision-console]').forEach(consoleRoot => {
    const buttons = [...consoleRoot.querySelectorAll('[data-vision-channel]')];
    const contribution = [...consoleRoot.querySelectorAll('[data-vision-contribution] i')];
    const metricSlots = ['a', 'b', 'c', 'd'];
    const setVision = key => {
      const next = visionData[key] || visionData.all;
      consoleRoot.dataset.active = key;
      buttons.forEach(button => {
        const buttonKey = button.dataset.visionChannel;
        const selected = buttonKey === key;
        const supporting = buttonKey !== 'all' && (key === 'all' || (key !== 'shopify' && buttonKey === 'shopify'));
        button.classList.toggle('is-active', selected);
        button.classList.toggle('is-supporting', supporting);
        button.setAttribute('aria-pressed', String(selected));
      });
      const title = consoleRoot.querySelector('[data-vision-title]');
      const summary = consoleRoot.querySelector('[data-vision-summary]');
      const barLabel = consoleRoot.querySelector('[data-vision-bar-label]');
      const confidence = consoleRoot.querySelector('[data-vision-confidence]');
      const confidenceBar = consoleRoot.querySelector('[data-vision-confidence-bar]');
      if (title) title.textContent = next.title;
      if (summary) summary.textContent = next.summary;
      if (barLabel) barLabel.textContent = next.barLabel;
      metricSlots.forEach((slot, index) => {
        const label = consoleRoot.querySelector(`[data-vision-metric-${slot}-label]`);
        const value = consoleRoot.querySelector(`[data-vision-metric-${slot}]`);
        if (label) label.textContent = next.metrics[index][0];
        if (value) value.textContent = next.metrics[index][1];
      });
      contribution.forEach((segment, index) => segment.style.setProperty('--share', `${next.shares[index]}%`));
      if (confidence) confidence.textContent = `${next.confidence}%`;
      confidenceBar?.style.setProperty('--confidence', `${next.confidence}%`);
      consoleRoot.classList.remove('is-routing');
      void consoleRoot.offsetWidth;
      consoleRoot.classList.add('is-routing');
    };
    buttons.forEach(button => button.addEventListener('click', () => setVision(button.dataset.visionChannel)));
    setVision('all');
  });

  document.querySelectorAll('.opportunity-table__row button').forEach(button => {
    button.addEventListener('click', () => {
      const selected = button.classList.toggle('is-selected');
      button.textContent = selected ? 'Selected ✓' : 'Review →';
      button.setAttribute('aria-pressed', String(selected));
    });
  });

  const billingButtons = [...document.querySelectorAll('[data-billing]')];
  billingButtons.forEach(button => button.addEventListener('click', () => {
    const annual = button.dataset.billing === 'annual';
    billingButtons.forEach(item => {
      item.classList.toggle('is-active', item === button);
      item.setAttribute('aria-pressed', String(item === button));
    });
    document.querySelectorAll('[data-price]').forEach(price => {
      price.textContent = annual ? price.dataset.annual : price.dataset.monthly;
    });
    document.querySelectorAll('[data-period]').forEach(period => { period.textContent = annual ? '/ year' : '/ month'; });
  }));

  const usd = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  document.querySelectorAll('[data-math-lab]').forEach(lab => {
    const probability = lab.querySelector('[data-math-prob]');
    const upside = lab.querySelector('[data-math-upside]');
    const downside = lab.querySelector('[data-math-downside]');
    const cost = lab.querySelector('[data-math-cost]');
    const result = lab.querySelector('[data-math-ev]');
    const mode = lab.querySelector('[data-math-mode]');
    const resultPanel = lab.querySelector('.math-simulator__result');
    if (!probability || !upside || !downside || !cost || !result) return;
    const updateMath = () => {
      const p = Number(probability.value) / 100;
      const up = Number(upside.value);
      const down = Number(downside.value);
      const actionCost = Number(cost.value);
      const expectedValue = (p * up) - ((1 - p) * down) - actionCost;
      const rounded = Math.round(expectedValue);
      lab.querySelector('[data-math-prob-output]').textContent = `${probability.value}%`;
      lab.querySelector('[data-math-upside-output]').textContent = usd.format(up);
      lab.querySelector('[data-math-downside-output]').textContent = usd.format(down);
      lab.querySelector('[data-math-cost-output]').textContent = usd.format(actionCost);
      result.textContent = `${rounded >= 0 ? '+' : '−'}${usd.format(Math.abs(rounded))}`;
      resultPanel?.classList.toggle('is-negative', rounded < 0);
      if (mode) mode.textContent = rounded < 0 ? 'Do not advance' : p >= .7 && rounded >= 5000 ? 'Small test allowed' : 'Approval review';
    };
    [probability, upside, downside, cost].forEach(input => input.addEventListener('input', updateMath));
    updateMath();
  });

  const simulatorScenarios = {
    demand: {
      cpc: '$3.60', margin: '$160 / order', cvr: '3.20%', probability: 78, confidence: 78,
      ev: '+$1,010', equation: '$3.60 ÷ $160 = 2.25%', action: 'Increase budget 12%',
      copy: 'Demand is growing and the next dollar remains above break-even.',
      rationale: 'Conversion is 0.95 points above break-even, downside stays inside the active limit, and 1,842 matched orders support the estimate.',
      line: 'M0 160 C80 150 120 135 180 120 S280 115 350 83 S470 72 600 28',
      area: 'M0 160 C80 150 120 135 180 120 S280 115 350 83 S470 72 600 28 L600 190 L0 190Z'
    },
    margin: {
      cpc: '$4.10', margin: '$140 / order', cvr: '2.10%', probability: 18, confidence: 91,
      ev: '−$1,260', equation: '$4.10 ÷ $140 = 2.93%', action: 'Reduce spend 18%',
      copy: 'Current traffic is below break-even, so Malach protects margin before more money leaves the account.',
      rationale: 'Conversion is 0.83 points below break-even, the loss is repeating across three checks, and the reduction remains fully reversible.',
      line: 'M0 40 C80 55 120 48 190 82 S300 86 370 119 S490 130 600 165',
      area: 'M0 40 C80 55 120 48 190 82 S300 86 370 119 S490 130 600 165 L600 190 L0 190Z'
    },
    competitor: {
      cpc: '$2.90', margin: '$118 / order', cvr: '3.05%', probability: 83, confidence: 86,
      ev: '+$5,960', equation: '$2.90 ÷ $118 = 2.46%', action: 'Run a 10% gap test',
      copy: 'Demand rose after a competitor sold out, but Malach keeps the first move small enough to learn safely.',
      rationale: 'Public demand rose 31%, conversion remains above break-even, and a 10% learning window limits downside while the signal is tested.',
      line: 'M0 156 C75 152 115 139 170 135 S260 118 320 108 S425 63 600 35',
      area: 'M0 156 C75 152 115 139 170 135 S260 118 320 108 S425 63 600 35 L600 190 L0 190Z'
    }
  };
  const simulatorModes = {
    approval: { guardrail: 'No action without approval', cta: 'Send for approval', status: 'QUEUED FOR APPROVAL' },
    canary: { guardrail: 'Maximum 10% test · $420 stop limit', cta: 'Start a 10% test', status: 'CANARY STARTED' },
    auto: { guardrail: 'Automatic inside budget and risk limits', cta: 'Execute inside limits', status: 'EXECUTED INSIDE LIMITS' }
  };
  document.querySelectorAll('[data-decision-simulator]').forEach(simulator => {
    const panel = simulator.querySelector('.decision-sim') || simulator;
    const scenarioButtons = [...simulator.querySelectorAll('[data-sim-scenario]')];
    const modeButtons = [...simulator.querySelectorAll('[data-sim-mode]')];
    const path = simulator.querySelector('.decision-sim__path');
    const ledger = simulator.querySelector('.decision-sim__ledger');
    const status = simulator.querySelector('[data-sim-status]');
    const execute = simulator.querySelector('[data-sim-execute]');
    let scenarioKey = scenarioButtons.find(button => button.classList.contains('is-active'))?.dataset.simScenario || 'demand';
    let modeKey = modeButtons.find(button => button.classList.contains('is-active'))?.dataset.simMode || 'approval';
    let timer;
    let actionTimer;
    const setText = (selector, value) => { const node = simulator.querySelector(selector); if (node) node.textContent = value; };
    const resetLedger = () => {
      ledger?.classList.remove('is-recorded');
      execute?.classList.remove('is-complete');
      if (execute) execute.disabled = false;
      path?.classList.remove('is-running');
      path?.querySelectorAll('span').forEach((step, index) => step.classList.toggle('is-complete', index < 2));
      setText('[data-sim-ledger]', 'Signal, formula, probability, rationale, authority, and outcome are ready to be recorded.');
      setText('[data-sim-ledger-state]', 'AWAITING ACTION');
    };
    const render = () => {
      const next = simulatorScenarios[scenarioKey];
      const mode = simulatorModes[modeKey];
      window.clearTimeout(timer);
      window.clearTimeout(actionTimer);
      resetLedger();
      panel.classList.add('is-calculating');
      void panel.offsetWidth;
      path?.classList.add('is-running');
      if (status) status.textContent = 'CALCULATING…';
      setText('[data-sim-cpc]', next.cpc); setText('[data-sim-margin]', next.margin); setText('[data-sim-cvr]', next.cvr);
      setText('[data-sim-probability]', `${next.probability}% chance of profit`); setText('[data-sim-ev]', next.ev);
      setText('[data-sim-equation]', next.equation); setText('[data-sim-action-title]', next.action); setText('[data-sim-action-copy]', next.copy);
      setText('[data-sim-rationale]', next.rationale); setText('[data-sim-confidence]', `${next.confidence}% confidence`);
      setText('[data-sim-guardrail]', mode.guardrail); setText('[data-sim-execute]', mode.cta);
      const executeArrow = document.createElement('span'); executeArrow.textContent = '→'; execute?.appendChild(executeArrow);
      simulator.querySelector('[data-sim-meter]')?.style.setProperty('--confidence', `${next.confidence}%`);
      simulator.querySelector('[data-sim-line]')?.setAttribute('d', next.line);
      simulator.querySelector('[data-sim-area]')?.setAttribute('d', next.area);
      timer = window.setTimeout(() => {
        panel.classList.remove('is-calculating');
        if (status) status.textContent = 'DECISION READY';
      }, reduceMotion ? 0 : 720);
    };
    scenarioButtons.forEach(button => button.addEventListener('click', () => {
      scenarioKey = button.dataset.simScenario;
      scenarioButtons.forEach(item => { const active = item === button; item.classList.toggle('is-active', active); item.setAttribute('aria-pressed', String(active)); });
      render();
    }));
    modeButtons.forEach(button => button.addEventListener('click', () => {
      modeKey = button.dataset.simMode;
      modeButtons.forEach(item => { const active = item === button; item.classList.toggle('is-active', active); item.setAttribute('aria-pressed', String(active)); });
      render();
    }));
    simulator.querySelector('[data-sim-why]')?.addEventListener('click', event => {
      const rationale = simulator.querySelector('[data-sim-rationale]');
      const open = event.currentTarget.getAttribute('aria-expanded') !== 'true';
      event.currentTarget.setAttribute('aria-expanded', String(open));
      const glyph = event.currentTarget.querySelector('span'); if (glyph) glyph.textContent = open ? '−' : '+';
      if (rationale) rationale.hidden = !open;
    });
    execute?.addEventListener('click', () => {
      const next = simulatorScenarios[scenarioKey];
      const mode = simulatorModes[modeKey];
      execute.disabled = true;
      panel.classList.add('is-calculating');
      if (status) status.textContent = modeKey === 'approval' ? 'PREPARING APPROVAL…' : 'OPERATING INSIDE LIMITS…';
      actionTimer = window.setTimeout(() => {
        const awaitingApproval = modeKey === 'approval';
        panel.classList.remove('is-calculating');
        ledger?.classList.add('is-recorded');
        execute.classList.add('is-complete');
        setText('[data-sim-ledger]', awaitingApproval ? `${next.action} — inputs, formula, rationale, and approval request saved.` : `${next.action} — inputs, formula, rationale, authority, and measurement plan saved.`);
        setText('[data-sim-ledger-state]', mode.status);
        setText('[data-sim-status]', awaitingApproval ? 'AWAITING YOUR APPROVAL' : 'OUTCOME MONITORING');
        execute.textContent = awaitingApproval ? 'Approval ready ✓' : 'Action recorded ✓';
        if (!awaitingApproval) setText('[data-sim-confidence]', `${Math.min(99, next.confidence + 4)}% after measurement`);
        path?.querySelectorAll('span').forEach((step, index) => step.classList.toggle('is-complete', index < (awaitingApproval ? 3 : 4)));
      }, reduceMotion ? 0 : 850);
    });
    simulator.querySelector('[data-sim-hold]')?.addEventListener('click', () => {
      window.clearTimeout(actionTimer);
      panel.classList.remove('is-calculating');
      ledger?.classList.add('is-recorded');
      if (execute) {
        execute.disabled = true;
        execute.classList.add('is-complete');
        execute.textContent = 'Action held ✓';
      }
      setText('[data-sim-ledger]', 'Hold recorded with the current evidence, rationale, and next review condition.');
      setText('[data-sim-ledger-state]', 'RECORDED · HOLD');
      setText('[data-sim-status]', 'ACTION HELD');
      path?.querySelectorAll('span').forEach((step, index) => step.classList.toggle('is-complete', index < 3));
    });
    render();
  });

  const conversationCopy = {
    risk: {
      question: 'Brief me on today’s risk.',
      answer: 'Three campaign groups moved below their contribution threshold. One reversible action remains inside policy; two higher-exposure decisions require approval.'
    },
    math: {
      question: 'Show me the mathematics behind that conclusion.',
      answer: 'The leading action has 76% modeled probability of profit and +$8,060 probability-adjusted expected value after downside and action cost. Attribution confidence is 91%.'
    },
    ledger: {
      question: 'Why did Malach choose this action?',
      answer: 'It protected the break-even threshold, preserved the highest-contribution cohort, limited exposure through Canary authority, and attached three invalidation conditions to the decision ledger.'
    }
  };
  document.querySelectorAll('[data-chat-console]').forEach(consoleRoot => {
    const question = consoleRoot.querySelector('[data-chat-question]');
    const answer = consoleRoot.querySelector('[data-chat-answer]');
    const consolePanel = consoleRoot.querySelector('.conversation-console');
    const voiceButton = consoleRoot.querySelector('[data-voice-control]');
    const voiceLabel = consoleRoot.querySelector('[data-voice-label]');
    let voiceTimer;
    const setConversation = key => {
      const next = conversationCopy[key];
      if (!next) return;
      consoleRoot.querySelectorAll('[data-chat-prompt]').forEach(button => button.classList.toggle('is-active', button.dataset.chatPrompt === key));
      if (question) question.textContent = next.question;
      if (answer) answer.textContent = next.answer;
      consoleRoot.querySelectorAll('.conversation-prompts [data-chat-prompt]').forEach(button => {
        button.setAttribute('aria-pressed', String(button.dataset.chatPrompt === key));
      });
    };
    consoleRoot.querySelectorAll('[data-chat-prompt]').forEach(button => button.addEventListener('click', () => {
      window.clearTimeout(voiceTimer);
      voiceButton?.setAttribute('aria-pressed', 'false');
      consolePanel?.classList.remove('is-listening');
      if (voiceLabel) voiceLabel.textContent = 'Ask another question';
      setConversation(button.dataset.chatPrompt);
    }));
    voiceButton?.addEventListener('click', () => {
      window.clearTimeout(voiceTimer);
      const listening = voiceButton.getAttribute('aria-pressed') !== 'true';
      voiceButton.setAttribute('aria-pressed', String(listening));
      consolePanel?.classList.toggle('is-listening', listening);
      if (voiceLabel) voiceLabel.textContent = listening ? 'Listening…' : 'Talk to Malach';
      if (!listening) return;
      voiceTimer = window.setTimeout(() => {
        setConversation('math');
        voiceButton.setAttribute('aria-pressed', 'false');
        consolePanel?.classList.remove('is-listening');
        if (voiceLabel) voiceLabel.textContent = 'Ask another question';
      }, reduceMotion ? 250 : 1600);
    });
  });

  document.querySelectorAll('[data-ledger-row]').forEach(row => {
    row.addEventListener('click', () => {
      const expanded = row.getAttribute('aria-expanded') === 'true';
      row.setAttribute('aria-expanded', String(!expanded));
      const detail = row.querySelector('[data-ledger-detail]');
      if (detail) detail.hidden = expanded;
      const label = row.querySelector('u');
      if (label) label.textContent = expanded ? `${label.textContent.replace('−', '+')}` : `${label.textContent.replace('+', '−')}`;
    });
  });

  document.querySelectorAll('[data-evolution-proposal]').forEach(proposal => {
    const steps = [...proposal.querySelectorAll('[data-learning-step]')];
    const action = proposal.querySelector('.evolution-action');
    const approve = proposal.querySelector('[data-evolution-approve]');
    const status = proposal.querySelector('[data-evolution-status]');
    const selectStep = selected => steps.forEach(item => {
      const active = item === selected;
      item.classList.toggle('is-active', active);
      item.setAttribute('aria-pressed', String(active));
    });
    steps.forEach(step => step.addEventListener('click', () => selectStep(step)));
    approve?.addEventListener('click', () => {
      const approved = approve.getAttribute('aria-pressed') === 'true';
      approve.setAttribute('aria-pressed', String(!approved));
      approve.textContent = approved ? 'Approve into this Malach →' : 'Approved into this Malach ✓';
      action?.classList.toggle('is-approved', !approved);
      if (status) status.textContent = approved ? 'Awaiting decision' : 'Approved by owner';
      const ownerStep = proposal.querySelector('[data-learning-step="approve"]');
      if (!approved && ownerStep) selectStep(ownerStep);
      else selectStep(steps[0]);
    });
  });

  document.querySelectorAll('[data-contact-form]').forEach(form => {
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const values = new FormData(form);
      const kind = form.dataset.formKind === 'support' ? 'Support request' : 'Malach inquiry';
      const subject = `${kind}: ${values.get('topic')}`;
      const message = `Name: ${values.get('name')}\nEmail: ${values.get('email')}\nTopic: ${values.get('topic')}\n\n${values.get('message')}`;
      const status = form.querySelector('[data-form-status]');
      if (status) status.textContent = 'Opening your email app with this message. Review it before sending.';
      window.location.href = `mailto:support@malach.app?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(message)}`;
    });
  });

  const statusPanel = document.querySelector('[data-status-panel]');
  const statusMessage = document.querySelector('[data-status-message]');
  const statusValues = [...document.querySelectorAll('[data-status-value]')];
  const checkStatus = async () => {
    if (!statusPanel) return;
    statusPanel.classList.remove('is-unavailable');
    statusPanel.classList.add('is-checking');
    if (statusMessage) statusMessage.textContent = 'Running a live availability check…';
    statusValues.forEach(value => { value.textContent = 'Checking'; });
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 5000);
    try {
      const response = await fetch(statusPanel.dataset.statusEndpoint, { cache: 'no-store', signal: controller.signal, headers: { Accept: 'application/json' } });
      if (!response.ok) throw new Error('Health endpoint unavailable');
      const data = await response.json();
      const healthy = data.ok === true || ['ok', 'operational', 'healthy'].includes(String(data.status || '').toLowerCase());
      if (!healthy) throw new Error('Health response did not confirm availability');
      statusValues.forEach(value => { value.textContent = 'Responding'; });
      if (statusMessage) statusMessage.textContent = `Live health responded at ${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}.`;
    } catch (_error) {
      statusPanel.classList.add('is-unavailable');
      statusValues.forEach(value => { value.textContent = 'Status unavailable'; });
      if (statusMessage) statusMessage.textContent = 'Live status could not be verified. Check again or contact support@malach.app.';
    } finally {
      window.clearTimeout(timeout);
      statusPanel.classList.remove('is-checking');
    }
  };
  document.querySelector('[data-status-refresh]')?.addEventListener('click', checkStatus);
  if (statusPanel) checkStatus();

  const themedSections = [...document.querySelectorAll('[data-theme]')];
  const chapters = [...document.querySelectorAll('[data-section]')];
  const railLinks = [...document.querySelectorAll('[data-chapter]')];
  const chapterRail = document.querySelector('.chapter-rail');
  const modeSteps = [...document.querySelectorAll('[data-mode-step]')];
  const modeName = document.querySelector('[data-mode-name]');
  const modeValue = document.querySelector('[data-mode-value]');
  const authorityDial = document.querySelector('[data-authority-dial]');
  const modes = [
    { name: 'OBSERVE', value: '0% execution', dial: 5 },
    { name: 'APPROVAL', value: 'Human authorization', dial: 35 },
    { name: 'CANARY', value: 'Controlled execution', dial: 66 },
    { name: 'FULL AUTO', value: '100% inside guardrails', dial: 100 }
  ];
  let lastScroll = window.scrollY;
  let ticking = false;
  let activeMode = -1;

  const setMode = index => {
    if (index === activeMode || !modes[index]) return;
    activeMode = index;
    modeSteps.forEach((step, i) => {
      step.classList.toggle('is-active', i === index);
      step.setAttribute('aria-pressed', String(i === index));
    });
    if (modeName) modeName.textContent = modes[index].name;
    if (modeValue) modeValue.textContent = modes[index].value;
    authorityDial?.style.setProperty('--dial', modes[index].dial);
  };

  modeSteps.forEach((step, index) => {
    step.addEventListener('mouseenter', () => setMode(index));
    step.addEventListener('click', () => setMode(index));
    step.addEventListener('keydown', event => {
      if (!['ArrowDown', 'ArrowRight', 'ArrowUp', 'ArrowLeft'].includes(event.key)) return;
      event.preventDefault();
      const direction = ['ArrowDown', 'ArrowRight'].includes(event.key) ? 1 : -1;
      const next = (index + direction + modeSteps.length) % modeSteps.length;
      setMode(next);
      modeSteps[next]?.focus();
    });
  });
  setMode(0);

  const onScrollFrame = () => {
    const y = window.scrollY;
    const viewportMid = y + window.innerHeight * 0.42;
    const themeProbe = y + Math.max(86, (header?.offsetHeight || 66) + 20);
    const maxScroll = Math.max(1, doc.scrollHeight - window.innerHeight);
    if (progress) progress.style.height = `${Math.min(100, (y / maxScroll) * 100)}%`;

    let currentTheme = 'light';
    themedSections.forEach(section => {
      if (section.offsetTop <= themeProbe && section.offsetTop + section.offsetHeight > themeProbe) {
        currentTheme = section.dataset.theme;
      }
    });
    header?.setAttribute('data-header-theme', ['dark', 'violet', 'copper'].includes(currentTheme) ? 'dark' : 'light');
    header?.classList.toggle('is-hidden', y > 180 && y > lastScroll && Math.abs(y - lastScroll) > 7);

    let currentChapter = '';
    chapters.forEach(section => {
      if (section.offsetTop <= viewportMid && section.offsetTop + section.offsetHeight > viewportMid) currentChapter = section.dataset.section;
    });
    chapterRail?.classList.toggle('is-in-chapters', Boolean(currentChapter));
    railLinks.forEach(link => link.classList.toggle('is-active', link.dataset.chapter === currentChapter));

    if (wordHeading) {
      const rect = wordHeading.getBoundingClientRect();
      const ratio = Math.max(0, Math.min(1, (window.innerHeight * .84 - rect.top) / (window.innerHeight * .75 + rect.height)));
      const words = [...wordHeading.querySelectorAll('.word')];
      const lit = Math.ceil(ratio * words.length * 1.15);
      words.forEach((word, index) => word.classList.toggle('is-lit', index < lit));
    }

    const autonomy = document.getElementById('autonomy');
    if (autonomy) {
      const rect = autonomy.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        const travelled = Math.max(0, Math.min(1, -rect.top / Math.max(1, rect.height - window.innerHeight)));
        setMode(Math.min(3, Math.floor(travelled * 4.25)));
      }
    }

    lastScroll = y;
    ticking = false;
  };

  window.addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(onScrollFrame);
  }, { passive: true });
  window.addEventListener('resize', () => requestAnimationFrame(onScrollFrame), { passive: true });
  onScrollFrame();

  if (!reduceMotion && matchMedia('(pointer:fine)').matches) {
    const stage = document.querySelector('.signal-stage');
    let stageFrame = 0;
    stage?.addEventListener('pointermove', event => {
      if (stageFrame) cancelAnimationFrame(stageFrame);
      stageFrame = requestAnimationFrame(() => {
        const rect = stage.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - .5;
        const y = (event.clientY - rect.top) / rect.height - .5;
        stage.style.setProperty('transform', `perspective(900px) rotateX(${-y * 4}deg) rotateY(${x * 5}deg)`);
      });
    });
    stage?.addEventListener('pointerleave', () => { stage.style.transform = ''; });

    document.querySelectorAll('.feature-card,.control-card,.price-card,.page-card,.page-visual').forEach(card => {
      let frame = 0;
      card.addEventListener('pointermove', event => {
        if (frame) cancelAnimationFrame(frame);
        frame = requestAnimationFrame(() => {
          const rect = card.getBoundingClientRect();
          const x = (event.clientX - rect.left) / rect.width - .5;
          const y = (event.clientY - rect.top) / rect.height - .5;
          card.style.setProperty('--tilt-x', `${-y * 2.2}deg`);
          card.style.setProperty('--tilt-y', `${x * 2.2}deg`);
        });
      });
      card.addEventListener('pointerleave', () => {
        card.style.removeProperty('--tilt-x');
        card.style.removeProperty('--tilt-y');
      });
    });
  }

  const currentPath = location.pathname.replace(/index\.html$/, '');
  document.querySelectorAll('.desktop-nav a,.menu-panel a,.footer a').forEach(link => {
    if (link.origin === location.origin && !link.hash && link.pathname === currentPath) link.setAttribute('aria-current', 'page');
  });
})();
