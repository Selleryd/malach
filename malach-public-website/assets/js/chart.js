const seriesMeta = {
  revenue: { label: 'Revenue', color: '#c76535', fill: 'rgba(199,101,53,.12)' },
  profit: { label: 'Contribution profit', color: '#35ca93', fill: 'rgba(53,202,147,.10)' },
  spend: { label: 'Ad spend', color: '#7650d8', fill: 'rgba(118,80,216,.10)' }
};

const demo = {
  labels: Array.from({ length: 30 }, (_, i) => `Jul ${i + 12}`),
  revenue: [840,920,790,1010,960,1120,1180,1060,1320,1260,1440,1510,1390,1640,1700,1550,1810,1760,1920,2010,1890,2210,2150,2360,2490,2380,2710,2840,2920,3150],
  profit: [112,146,98,180,164,205,226,189,254,240,286,303,274,348,365,326,401,386,430,458,414,520,492,562,610,584,676,720,742,810],
  spend: [205,212,198,220,218,228,240,236,254,249,268,276,270,288,294,291,309,305,318,326,321,342,338,352,360,358,372,381,386,402]
};

function niceNumber(value) {
  const abs = Math.abs(value);
  if (abs >= 1e6) return `$${(value / 1e6).toFixed(abs >= 1e7 ? 0 : 1)}m`;
  if (abs >= 1e3) return `$${(value / 1e3).toFixed(abs >= 1e4 ? 0 : 1)}k`;
  return `$${Math.round(value).toLocaleString()}`;
}

export class MalachFinancialChart {
  constructor(root, data = demo) {
    this.root = root;
    this.canvas = root.querySelector('canvas');
    this.ctx = this.canvas.getContext('2d');
    this.tooltip = root.querySelector('.chart-tooltip');
    this.data = data;
    this.visible = new Set(['revenue', 'profit', 'spend']);
    this.mode = 'shared';
    this.hoverIndex = -1;
    this.dpr = Math.min(devicePixelRatio || 1, 2);
    this.resizeObserver = new ResizeObserver(() => this.resize());
    this.resizeObserver.observe(this.canvas.parentElement);
    this.bind();
    this.resize();
    addEventListener('malach:theme', () => this.draw());
  }

  bind() {
    this.root.querySelectorAll('[data-series]').forEach(button => {
      button.addEventListener('click', () => {
        const key = button.dataset.series;
        if (this.visible.has(key) && this.visible.size === 1) return;
        this.visible.has(key) ? this.visible.delete(key) : this.visible.add(key);
        button.setAttribute('aria-pressed', String(this.visible.has(key)));
        this.draw();
        window.malachTrack?.('chart_series_toggled', { series: key, visible: this.visible.has(key) });
      });
    });
    this.root.querySelectorAll('[data-chart-mode]').forEach(button => {
      button.addEventListener('click', () => {
        this.mode = button.dataset.chartMode;
        this.root.querySelectorAll('[data-chart-mode]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
        this.draw();
      });
    });
    this.canvas.addEventListener('pointermove', e => this.onPointer(e));
    this.canvas.addEventListener('pointerleave', () => { this.hoverIndex = -1; this.tooltip.style.display = 'none'; this.draw(); });
  }

  resize() {
    const rect = this.canvas.getBoundingClientRect();
    if (!rect.width || !rect.height) return;
    this.width = rect.width;
    this.height = rect.height;
    this.canvas.width = Math.round(rect.width * this.dpr);
    this.canvas.height = Math.round(rect.height * this.dpr);
    this.ctx.setTransform(this.dpr, 0, 0, this.dpr, 0, 0);
    this.draw();
  }

  valuesFor(key) {
    const values = this.data[key];
    if (this.mode !== 'compare') return values;
    const base = values[0] || 1;
    return values.map(v => ((v / base) - 1) * 100);
  }

  dimensions() {
    return { left: 60, right: 22, top: 24, bottom: 42, width: this.width - 82, height: this.height - 66 };
  }

  scale() {
    const keys = [...this.visible];
    const all = keys.flatMap(k => this.valuesFor(k));
    let min = Math.min(...all, 0);
    let max = Math.max(...all, 1);
    const range = max - min || 1;
    min -= range * .1;
    max += range * .12;
    return { min, max };
  }

  colors() {
    const light = document.documentElement.dataset.theme === 'light';
    return {
      text: light ? 'rgba(58,44,37,.58)' : 'rgba(224,211,202,.54)',
      grid: light ? 'rgba(58,44,37,.095)' : 'rgba(255,255,255,.065)',
      zero: light ? 'rgba(58,44,37,.22)' : 'rgba(255,255,255,.16)'
    };
  }

  draw() {
    if (!this.width) return;
    const ctx = this.ctx;
    const d = this.dimensions();
    const { min, max } = this.scale();
    const colors = this.colors();
    ctx.clearRect(0, 0, this.width, this.height);

    const y = v => d.top + (max - v) / (max - min) * d.height;
    const x = i => d.left + (i / (this.data.labels.length - 1)) * d.width;

    ctx.save();
    ctx.font = '11px -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif';
    ctx.textBaseline = 'middle';
    ctx.fillStyle = colors.text;
    ctx.strokeStyle = colors.grid;
    ctx.lineWidth = 1;
    const steps = 5;
    for (let i = 0; i <= steps; i++) {
      const value = min + (max - min) * (1 - i / steps);
      const py = d.top + d.height * i / steps;
      ctx.beginPath();
      ctx.moveTo(d.left, py);
      ctx.lineTo(d.left + d.width, py);
      ctx.stroke();
      ctx.textAlign = 'right';
      const label = this.mode === 'compare' ? `${Math.round(value)}%` : niceNumber(value);
      ctx.fillText(label, d.left - 10, py);
    }

    if (min < 0 && max > 0) {
      ctx.strokeStyle = colors.zero;
      ctx.setLineDash([5, 5]);
      ctx.beginPath();
      ctx.moveTo(d.left, y(0));
      ctx.lineTo(d.left + d.width, y(0));
      ctx.stroke();
      ctx.setLineDash([]);
    }

    const xTicks = [0, 7, 14, 21, 29];
    ctx.fillStyle = colors.text;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    xTicks.forEach(i => ctx.fillText(this.data.labels[i], x(i), d.top + d.height + 14));
    ctx.restore();

    [...this.visible].forEach(key => {
      const values = this.valuesFor(key);
      const meta = seriesMeta[key];
      const gradient = ctx.createLinearGradient(0, d.top, 0, d.top + d.height);
      gradient.addColorStop(0, meta.fill.replace(/\.[0-9]+\)/, '.18)'));
      gradient.addColorStop(1, meta.fill.replace(/\.[0-9]+\)/, '0)'));

      ctx.save();
      ctx.beginPath();
      values.forEach((v, i) => {
        const px = x(i), py = y(v);
        if (i === 0) ctx.moveTo(px, py);
        else {
          const prevX = x(i - 1), prevY = y(values[i - 1]);
          const cp = (px - prevX) * .42;
          ctx.bezierCurveTo(prevX + cp, prevY, px - cp, py, px, py);
        }
      });
      ctx.lineTo(x(values.length - 1), d.top + d.height);
      ctx.lineTo(x(0), d.top + d.height);
      ctx.closePath();
      ctx.fillStyle = gradient;
      ctx.fill();

      ctx.beginPath();
      values.forEach((v, i) => {
        const px = x(i), py = y(v);
        if (i === 0) ctx.moveTo(px, py);
        else {
          const prevX = x(i - 1), prevY = y(values[i - 1]);
          const cp = (px - prevX) * .42;
          ctx.bezierCurveTo(prevX + cp, prevY, px - cp, py, px, py);
        }
      });
      ctx.strokeStyle = meta.color;
      ctx.lineWidth = key === 'profit' ? 2.35 : 1.8;
      ctx.lineJoin = 'round';
      ctx.lineCap = 'round';
      ctx.shadowColor = meta.color;
      ctx.shadowBlur = key === 'profit' ? 12 : 7;
      ctx.globalAlpha = key === 'profit' ? 1 : .9;
      ctx.stroke();
      ctx.restore();
    });

    if (this.hoverIndex >= 0) {
      const px = x(this.hoverIndex);
      ctx.save();
      ctx.strokeStyle = colors.zero;
      ctx.lineWidth = 1;
      ctx.setLineDash([3, 4]);
      ctx.beginPath(); ctx.moveTo(px, d.top); ctx.lineTo(px, d.top + d.height); ctx.stroke();
      ctx.setLineDash([]);
      [...this.visible].forEach(key => {
        const py = y(this.valuesFor(key)[this.hoverIndex]);
        ctx.beginPath(); ctx.arc(px, py, 4, 0, Math.PI * 2);
        ctx.fillStyle = seriesMeta[key].color; ctx.fill();
        ctx.lineWidth = 2; ctx.strokeStyle = document.documentElement.dataset.theme === 'light' ? '#fff' : '#0a090d'; ctx.stroke();
      });
      ctx.restore();
    }
  }

  onPointer(event) {
    const rect = this.canvas.getBoundingClientRect();
    const d = this.dimensions();
    const localX = event.clientX - rect.left;
    const ratio = Math.max(0, Math.min(1, (localX - d.left) / d.width));
    this.hoverIndex = Math.round(ratio * (this.data.labels.length - 1));
    const rows = [...this.visible].map(key => {
      const raw = this.data[key][this.hoverIndex];
      const display = this.mode === 'compare' ? `${this.valuesFor(key)[this.hoverIndex].toFixed(1)}%` : niceNumber(raw);
      return `<div class="chart-tooltip-row"><span><i style="display:inline-block;width:7px;height:7px;border-radius:50%;background:${seriesMeta[key].color};margin-right:7px"></i>${seriesMeta[key].label}</span><b>${display}</b></div>`;
    }).join('');
    this.tooltip.innerHTML = `<strong>${this.data.labels[this.hoverIndex]}</strong>${rows}`;
    this.tooltip.style.display = 'block';
    const left = Math.min(this.width - 230, Math.max(8, localX + 16));
    const top = Math.max(10, event.clientY - rect.top - 20);
    this.tooltip.style.left = `${left}px`;
    this.tooltip.style.top = `${top}px`;
    this.draw();
  }
}

export function initFinancialCharts() {
  document.querySelectorAll('[data-financial-chart]').forEach(root => new MalachFinancialChart(root));
}
