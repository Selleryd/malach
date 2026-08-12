const ROUTES = [
  ['Home', '/'],
  ['Product', '/product/'],
  ['Auto Agent', '/auto-agent/'],
  ['Intelligence', '/intelligence/'],
  ['Advantage', '/advantage/'],
  ['Attribution', '/attribution/'],
  ['Malach Voice', '/voice/'],
  ['Security', '/security/'],
  ['Pricing', '/pricing/'],
  ['About', '/about/'],
  ['Support', '/support/'],
  ['Privacy', '/privacy/'],
  ['Terms', '/terms/']
];

const root = document.documentElement;
const safeStorage = {
  get(key) { try { return window.localStorage.getItem(key); } catch { return null; } },
  set(key, value) { try { window.localStorage.setItem(key, value); } catch { /* storage may be unavailable in hardened or preview contexts */ } }
};
const savedTheme = safeStorage.get('malach-theme');
const preferredTheme = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
root.dataset.theme = savedTheme || preferredTheme;

function icon(name) {
  const icons = {
    sun: '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="4" stroke="currentColor"/><path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.65 17.65l1.42 1.42M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.65 6.35l1.42-1.42" stroke="currentColor" stroke-linecap="round"/></svg>',
    moon: '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5 8.5 8.5 0 1 0 20.5 14.3Z" stroke="currentColor" stroke-linejoin="round"/></svg>',
    menu: '<svg aria-hidden="true" width="19" height="19" viewBox="0 0 24 24" fill="none"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-linecap="round"/></svg>',
    close: '<svg aria-hidden="true" width="19" height="19" viewBox="0 0 24 24" fill="none"><path d="m6 6 12 12M18 6 6 18" stroke="currentColor" stroke-linecap="round"/></svg>'
  };
  return icons[name] || '';
}

function syncThemeButtons() {
  document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
    const isLight = root.dataset.theme === 'light';
    btn.innerHTML = isLight ? icon('moon') : icon('sun');
    btn.setAttribute('aria-label', isLight ? 'Switch to dark theme' : 'Switch to light theme');
  });
}

function setupTheme() {
  syncThemeButtons();
  document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
    btn.addEventListener('click', () => {
      root.dataset.theme = root.dataset.theme === 'light' ? 'dark' : 'light';
      safeStorage.set('malach-theme', root.dataset.theme);
      syncThemeButtons();
      window.dispatchEvent(new CustomEvent('malach:theme', { detail: root.dataset.theme }));
    });
  });
}

function setupHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;
  const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 20);
  onScroll();
  addEventListener('scroll', onScroll, { passive: true });

  const menuBtn = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('.main-nav');
  if (menuBtn && nav) {
    menuBtn.innerHTML = icon('menu');
    menuBtn.addEventListener('click', event => {
      event.stopPropagation();
      const open = menuBtn.getAttribute('aria-expanded') !== 'true';
      nav.classList.toggle('mobile-open', open);
      menuBtn.innerHTML = icon(open ? 'close' : 'menu');
      menuBtn.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', e => {
      if (e.target.closest('a') && nav.classList.contains('mobile-open')) {
        nav.classList.remove('mobile-open');
        menuBtn.innerHTML = icon('menu');
        menuBtn.setAttribute('aria-expanded', 'false');
      }
    });
    document.addEventListener('click', e => {
      if (!nav.contains(e.target) && !menuBtn.contains(e.target) && nav.classList.contains('mobile-open')) {
        nav.classList.remove('mobile-open');
        menuBtn.innerHTML = icon('menu');
        menuBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }
}

function setupReveals() {
  const items = [...document.querySelectorAll('.reveal')];
  if (!items.length) return;
  if (!('IntersectionObserver' in window)) {
    items.forEach(el => el.classList.add('visible'));
    return;
  }
  const obs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
  items.forEach((el, i) => {
    el.style.transitionDelay = `${Math.min(i % 5, 4) * 70}ms`;
    obs.observe(el);
  });
}

function setupCounters() {
  const counters = document.querySelectorAll('[data-count]');
  if (!counters.length) return;
  const format = (n, el) => {
    const prefix = el.dataset.prefix || '';
    const suffix = el.dataset.suffix || '';
    const decimals = Number(el.dataset.decimals || 0);
    return `${prefix}${n.toLocaleString(undefined, { minimumFractionDigits: decimals, maximumFractionDigits: decimals })}${suffix}`;
  };
  const animate = el => {
    const target = Number(el.dataset.count || 0);
    const startTime = performance.now();
    const duration = 1200;
    const tick = now => {
      const t = Math.min(1, (now - startTime) / duration);
      const eased = 1 - Math.pow(1 - t, 3);
      el.textContent = format(target * eased, el);
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  const obs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animate(entry.target);
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: .6 });
  counters.forEach(el => obs.observe(el));
}

function setupCursorHalo() {
  if (matchMedia('(pointer: coarse)').matches || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const halo = document.createElement('div');
  halo.className = 'cursor-halo';
  document.body.appendChild(halo);
  let x = innerWidth / 2, y = innerHeight / 2, tx = x, ty = y;
  addEventListener('pointermove', e => { tx = e.clientX; ty = e.clientY; }, { passive: true });
  const frame = () => {
    x += (tx - x) * .075;
    y += (ty - y) * .075;
    halo.style.transform = `translate3d(${x}px, ${y}px, 0)`;
    requestAnimationFrame(frame);
  };
  frame();
}

function setupParallaxCards() {
  if (matchMedia('(pointer: coarse)').matches || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  document.querySelectorAll('[data-tilt]').forEach(card => {
    card.addEventListener('pointermove', e => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - .5;
      const py = (e.clientY - r.top) / r.height - .5;
      card.style.transform = `perspective(1100px) rotateX(${py * -3}deg) rotateY(${px * 4}deg) translateY(-2px)`;
    });
    card.addEventListener('pointerleave', () => { card.style.transform = ''; });
  });
}

function setupCommandPalette() {
  const palette = document.querySelector('[data-command-palette]');
  if (!palette) return;
  const input = palette.querySelector('input');
  const results = palette.querySelector('.command-results');
  const render = query => {
    const q = query.trim().toLowerCase();
    const filtered = ROUTES.filter(([label]) => !q || label.toLowerCase().includes(q));
    results.innerHTML = filtered.map(([label, href], i) => `<a href="${href}" class="${i === 0 ? 'active' : ''}"><span>${label}</span><kbd>↵</kbd></a>`).join('');
  };
  const open = () => { palette.classList.add('open'); render(''); setTimeout(() => input.focus(), 0); };
  const close = () => { palette.classList.remove('open'); input.value = ''; };
  document.querySelectorAll('[data-command-open]').forEach(btn => btn.addEventListener('click', open));
  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); palette.classList.contains('open') ? close() : open(); }
    if (e.key === 'Escape' && palette.classList.contains('open')) close();
    if (e.key === 'Enter' && palette.classList.contains('open')) {
      const active = results.querySelector('.active') || results.querySelector('a');
      if (active) location.href = active.href;
    }
  });
  input.addEventListener('input', () => render(input.value));
  palette.addEventListener('click', e => { if (e.target === palette) close(); });
}

function setupAnalytics() {
  window.malachTrack = (event, properties = {}) => {
    const endpoint = document.documentElement.dataset.analyticsEndpoint;
    if (!endpoint) return;
    const payload = JSON.stringify({ event, properties, path: location.pathname, ts: Date.now() });
    if (navigator.sendBeacon) navigator.sendBeacon(endpoint, payload);
    else fetch(endpoint, { method: 'POST', headers: { 'content-type': 'application/json' }, body: payload, keepalive: true }).catch(() => {});
  };
  document.querySelectorAll('[data-track]').forEach(el => {
    el.addEventListener('click', () => window.malachTrack(el.dataset.track, { href: el.getAttribute('href') || '' }));
  });
}

function setupYear() {
  document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
}

function setupSmoothLinks() {
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (!id || id === '#') return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
      history.pushState(null, '', id);
    });
  });
}

function setupSupportForms() {
  document.querySelectorAll('[data-support-form]').forEach(form => {
    const status = form.querySelector('.form-status');
    form.addEventListener('submit', async e => {
      e.preventDefault();
      const data = Object.fromEntries(new FormData(form));
      if (data.website) return;
      const endpoint = form.dataset.endpoint || '';
      if (!endpoint) {
        const subject = encodeURIComponent(`[Malach support] ${data.topic || 'Website inquiry'}`);
        const body = encodeURIComponent(`Name: ${data.name || ''}\nEmail: ${data.email || ''}\n\n${data.message || ''}`);
        location.href = `mailto:support@malach.app?subject=${subject}&body=${body}`;
        status.textContent = 'Opening your email client…';
        return;
      }
      status.textContent = 'Sending…';
      try {
        const res = await fetch(endpoint, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(data) });
        if (!res.ok) throw new Error('Request failed');
        form.reset();
        status.textContent = 'Message sent. We’ll respond as soon as possible.';
      } catch {
        status.textContent = 'We could not send this message. Email support@malach.app instead.';
      }
    });
  });
}

setupTheme();
setupHeader();
setupReveals();
setupCounters();
setupCursorHalo();
setupParallaxCards();
setupCommandPalette();
setupAnalytics();
setupYear();
setupSmoothLinks();
setupSupportForms();
