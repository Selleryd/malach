export function sendJson(res, status, payload) {
  res.statusCode = status;
  res.setHeader('content-type', 'application/json; charset=utf-8');
  res.setHeader('cache-control', 'no-store');
  res.end(JSON.stringify(payload));
}

export function methodNotAllowed(res, allowed) {
  res.setHeader('allow', allowed.join(', '));
  sendJson(res, 405, { error: 'Method not allowed' });
}

export async function readJson(req, limit = 32_768) {
  if (req.body && typeof req.body === 'object') return req.body;
  const chunks = [];
  let size = 0;
  for await (const chunk of req) {
    size += chunk.length;
    if (size > limit) throw new Error('Request body too large');
    chunks.push(chunk);
  }
  if (!chunks.length) return {};
  return JSON.parse(Buffer.concat(chunks).toString('utf8'));
}

export async function readRaw(req, limit = 1_048_576) {
  const chunks = [];
  let size = 0;
  for await (const chunk of req) {
    size += chunk.length;
    if (size > limit) throw new Error('Request body too large');
    chunks.push(chunk);
  }
  return Buffer.concat(chunks);
}

export function safeOrigin(req) {
  const configured = process.env.SITE_URL || 'https://malach.app';
  const origin = req.headers.origin || '';
  if (!origin) return configured;
  const allowed = new Set([
    configured,
    process.env.APP_URL || 'https://app.malach.app',
    'http://localhost:3000',
    'http://127.0.0.1:3000'
  ]);
  return allowed.has(origin) ? origin : configured;
}
