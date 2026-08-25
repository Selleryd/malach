const mobileQuery = matchMedia('(max-width: 900px)');

function rafThrottle(fn){
  let raf = 0;
  return (...args) => {
    if (raf) return;
    raf = requestAnimationFrame(() => {
      raf = 0;
      fn(...args);
    });
  };
}

function setupSnapDeck(selector, label){
  const deck = document.querySelector(selector);
  if (!deck || deck.dataset.v72Enhanced === 'true') return;
  const cards = [...deck.children].filter(el => el.nodeType === 1);
  if (cards.length < 2) return;

  const meta = document.createElement('div');
  meta.className = 'v72-mobile-carousel-meta';
  meta.innerHTML = `<span>${label}</span><div class="v72-mobile-dots" aria-label="${label} position"></div>`;
  deck.insertAdjacentElement('afterend', meta);
  const dots = meta.querySelector('.v72-mobile-dots');

  const buttons = cards.map((card, index) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.setAttribute('aria-label', `${label} ${index + 1} of ${cards.length}`);
    button.addEventListener('click', () => card.scrollIntoView({behavior:'smooth', block:'nearest', inline:'center'}));
    dots.appendChild(button);
    return button;
  });

  const update = rafThrottle(() => {
    if (!mobileQuery.matches) return;
    const box = deck.getBoundingClientRect();
    const center = box.left + box.width / 2;
    let best = 0;
    let distance = Infinity;
    cards.forEach((card, index) => {
      const r = card.getBoundingClientRect();
      const d = Math.abs((r.left + r.width / 2) - center);
      if (d < distance) {
        distance = d;
        best = index;
      }
    });
    buttons.forEach((button, index) => button.classList.toggle('active', index === best));
  });

  deck.addEventListener('scroll', update, {passive:true});
  addEventListener('resize', update, {passive:true});
  deck.dataset.v72Enhanced = 'true';
  update();
}

function setupMobileDetails(){
  const drawer = document.querySelector('[data-mobile-drawer]');
  if (!drawer) return;
  const details = [...drawer.querySelectorAll('details')];
  details.forEach(item => item.addEventListener('toggle', () => {
    if (!item.open) return;
    details.forEach(other => {
      if (other !== item) other.open = false;
    });
  }));
}

function keepActiveTabsVisible(){
  const selectors = ['.v71-canvas-flow', '.v7-channel-nav', '.v71-model-tabs'];
  selectors.forEach(selector => {
    document.querySelectorAll(selector).forEach(scroller => {
      scroller.addEventListener('click', event => {
        if (!mobileQuery.matches) return;
        const button = event.target.closest('button');
        if (!button) return;
        requestAnimationFrame(() => button.scrollIntoView({behavior:'smooth', block:'nearest', inline:'center'}));
      });
    });
  });
}

function setupMobileViewportState(){
  const apply = () => {
    document.documentElement.classList.toggle('v72-mobile', mobileQuery.matches);
    document.documentElement.style.setProperty('--v72-vh', `${innerHeight * 0.01}px`);
  };
  apply();
  mobileQuery.addEventListener?.('change', apply);
  addEventListener('resize', rafThrottle(apply), {passive:true});
}

setupMobileViewportState();
setupMobileDetails();
keepActiveTabsVisible();
setupSnapDeck('.v7-feature-grid', 'Swipe features');
setupSnapDeck('.v7-authority-grid', 'Swipe authority modes');
document.documentElement.dataset.v72MobileReady = 'true';
