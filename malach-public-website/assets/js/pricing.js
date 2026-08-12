const state = {
  interval: 'monthly',
  config: { billingEnabled: false, prices: {} }
};

function setIntervalMode(mode) {
  state.interval = mode;
  document.querySelectorAll('[data-billing-interval]').forEach(btn => btn.classList.toggle('active', btn.dataset.billingInterval === mode));
  document.querySelectorAll('[data-plan]').forEach(card => updateCard(card));
}

function updateCard(card) {
  const id = card.dataset.plan;
  const priceEl = card.querySelector('[data-price]');
  const cadenceEl = card.querySelector('[data-cadence]');
  const cta = card.querySelector('[data-checkout]');
  const price = state.config.prices?.[id]?.[state.interval];
  if (price?.display) {
    priceEl.textContent = price.display;
    cadenceEl.textContent = state.interval === 'annual' ? '/ month, billed annually' : '/ month';
  } else {
    priceEl.textContent = card.dataset.fallbackPrice || 'Private launch';
    cadenceEl.textContent = '';
  }
  if (cta) {
    const available = Boolean(state.config.billingEnabled && price?.enabled);
    cta.textContent = available ? 'Start with Malach' : (card.dataset.contact === 'true' ? 'Contact sales' : 'Request access');
    cta.dataset.available = String(available);
  }
}

async function loadConfig() {
  try {
    const res = await fetch('/api/public-config');
    if (res.ok) state.config = await res.json();
  } catch {
    // Static preview intentionally falls back to early-access CTAs.
  }
  document.querySelectorAll('[data-plan]').forEach(card => updateCard(card));
}

async function startCheckout(button) {
  const card = button.closest('[data-plan]');
  const planId = card.dataset.plan;
  if (button.dataset.available !== 'true') {
    window.malachTrack?.('pricing_request_access', { plan: planId, interval: state.interval });
    location.href = `/support/?topic=pricing&plan=${encodeURIComponent(planId)}`;
    return;
  }
  button.disabled = true;
  const original = button.textContent;
  button.textContent = 'Opening secure checkout…';
  try {
    const res = await fetch('/api/create-checkout-session', {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ planId, interval: state.interval })
    });
    const data = await res.json();
    if (!res.ok || !data.url) throw new Error(data.error || 'Checkout unavailable');
    window.malachTrack?.('checkout_started', { plan: planId, interval: state.interval });
    location.href = data.url;
  } catch (error) {
    button.disabled = false;
    button.textContent = original;
    const status = document.querySelector('[data-pricing-status]');
    if (status) status.textContent = error.message || 'Checkout could not start. Contact support@malach.app.';
  }
}

document.querySelectorAll('[data-billing-interval]').forEach(btn => btn.addEventListener('click', () => setIntervalMode(btn.dataset.billingInterval)));
document.querySelectorAll('[data-checkout]').forEach(btn => btn.addEventListener('click', () => startCheckout(btn)));
setIntervalMode('monthly');
loadConfig();
