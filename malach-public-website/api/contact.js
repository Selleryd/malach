import { sendJson, methodNotAllowed, readJson } from './_lib/http.js';

export default async function handler(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);
  try {
    const body = await readJson(req, 16_384);
    if (body.website) return sendJson(res, 200, { ok: true });
    const email = String(body.email || '').trim();
    const message = String(body.message || '').trim();
    if (!email.includes('@') || message.length < 10) return sendJson(res, 400, { error: 'A valid email and message are required' });
    const endpoint = process.env.CONTACT_WEBHOOK_URL;
    if (!endpoint) return sendJson(res, 503, { error: 'Contact delivery is not configured. Email support@malach.app.' });
    const headers = { 'content-type': 'application/json' };
    if (process.env.CONTACT_WEBHOOK_TOKEN) headers.authorization = `Bearer ${process.env.CONTACT_WEBHOOK_TOKEN}`;
    const response = await fetch(endpoint, {
      method: 'POST',
      headers,
      body: JSON.stringify({
        source: 'malach.app',
        name: String(body.name || '').slice(0, 120),
        email: email.slice(0, 240),
        topic: String(body.topic || 'Website inquiry').slice(0, 120),
        message: message.slice(0, 5000),
        timestamp: new Date().toISOString()
      })
    });
    if (!response.ok) throw new Error(`Contact webhook returned ${response.status}`);
    sendJson(res, 200, { ok: true });
  } catch (error) {
    console.error('contact_failed', { message: error.message });
    sendJson(res, 500, { error: 'Message could not be delivered. Email support@malach.app.' });
  }
}
