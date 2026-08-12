import { readdir, readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const routes = ['/', '/product/', '/auto-agent/', '/intelligence/', '/advantage/', '/attribution/', '/voice/', '/security/', '/pricing/', '/about/', '/support/', '/privacy/', '/terms/', '/login/', '/status/', '/changelog/'];
const failures = [];

function routeFile(route) { return route === '/' ? path.join(root, 'index.html') : path.join(root, route, 'index.html'); }

for (const route of routes) {
  const file = routeFile(route);
  let html = '';
  try { html = await readFile(file, 'utf8'); } catch { failures.push(`Missing route file: ${route}`); continue; }
  if (!/<title>[^<]+<\/title>/.test(html)) failures.push(`Missing title: ${route}`);
  if (!/<meta name="description" content="[^"]+">/.test(html)) failures.push(`Missing description: ${route}`);
  if (!html.includes('class="site-header"')) failures.push(`Missing header: ${route}`);
  if (!html.includes('class="site-footer"') && route !== '/login/') failures.push(`Missing footer: ${route}`);
  if (/TODO|lorem ipsum|your company here/i.test(html)) failures.push(`Placeholder copy found: ${route}`);
  const refs = [...html.matchAll(/(?:src|href)="(\/assets\/[^"?#]+)"/g)].map(m => m[1]);
  for (const ref of refs) {
    const target = path.join(root, ref);
    try { await stat(target); } catch { failures.push(`Broken asset ${ref} in ${route}`); }
  }
}

async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    if (entry.name.startsWith('.') || entry.name === 'node_modules') continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) files.push(...await walk(full)); else files.push(full);
  }
  return files;
}

const all = await walk(root);
for (const file of all.filter(f => f.endsWith('.js') || f.endsWith('.mjs'))) {
  const result = spawnSync(process.execPath, ['--check', file], { encoding: 'utf8' });
  if (result.status !== 0) failures.push(`JavaScript syntax failed: ${path.relative(root, file)}\n${result.stderr}`);
}

const required = ['robots.txt', 'sitemap.xml', 'site.webmanifest', 'vercel.json', '.env.example', 'README.md'];
for (const name of required) {
  try { await stat(path.join(root, name)); } catch { failures.push(`Missing required file: ${name}`); }
}

if (failures.length) {
  console.error(`Validation failed (${failures.length}):`);
  failures.forEach(f => console.error(`- ${f}`));
  process.exit(1);
}
console.log(`Validation passed: ${routes.length} routes, ${all.filter(f => f.endsWith('.js') || f.endsWith('.mjs')).length} JavaScript modules.`);
