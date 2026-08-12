import { sendJson, methodNotAllowed } from './_lib/http.js';
export default async function handler(req, res) {
  if (req.method !== 'GET') return methodNotAllowed(res, ['GET']);
  sendJson(res, 200, { ok: true, service: 'malach-public-site', timestamp: new Date().toISOString() });
}
