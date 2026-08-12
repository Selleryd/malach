import http from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const port = Number(process.env.PORT || 3000);
const types = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml', '.ico': 'image/x-icon', '.xml': 'application/xml; charset=utf-8', '.txt': 'text/plain; charset=utf-8'
};

function safePath(urlPath) {
  const decoded = decodeURIComponent(urlPath.split('?')[0]);
  const candidate = path.normalize(path.join(root, decoded));
  if (!candidate.startsWith(root)) throw new Error('Invalid path');
  return candidate;
}

const server = http.createServer(async (req, res) => {
  try {
    if (req.url === '/api/public-config') {
      res.setHeader('content-type', 'application/json');
      res.end(JSON.stringify({ billingEnabled: false, prices: {}, appUrl: 'https://app.malach.app' }));
      return;
    }
    let file = safePath(req.url || '/');
    let info;
    try { info = await stat(file); } catch { info = null; }
    if (info?.isDirectory()) file = path.join(file, 'index.html');
    if (!info && !path.extname(file)) file = path.join(file, 'index.html');
    let data;
    try { data = await readFile(file); }
    catch { data = await readFile(path.join(root, '404.html')); res.statusCode = 404; }
    res.setHeader('content-type', types[path.extname(file)] || 'application/octet-stream');
    res.setHeader('cache-control', 'no-store');
    res.end(data);
  } catch (error) {
    res.statusCode = 500;
    res.end('Server error');
  }
});
server.listen(port, '127.0.0.1', () => console.log(`Malach website preview: http://127.0.0.1:${port}`));
