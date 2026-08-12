import { initFinancialCharts } from './chart.js';
initFinancialCharts();

document.querySelectorAll('[data-tab-set]').forEach(shell => {
  const buttons = shell.querySelectorAll('[data-tab]');
  const panels = shell.querySelectorAll('[data-panel]');
  buttons.forEach(button => button.addEventListener('click', () => {
    buttons.forEach(b => b.setAttribute('aria-selected', String(b === button)));
    panels.forEach(panel => panel.hidden = panel.dataset.panel !== button.dataset.tab);
  }));
});
