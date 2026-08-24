import { sendJson, methodNotAllowed } from './_lib/http.js';

const DEFAULT_HEALTH_URL = 'https://app.malach.app/health';

export default async function handler(req, res) {
  if (req.method !== 'GET') return methodNotAllowed(res, ['GET']);

  res.setHeader('Cache-Control', 'no-store, max-age=0');

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 7000);
  const healthUrl = process.env.MALACH_APP_HEALTH_URL || DEFAULT_HEALTH_URL;

  try {
    const response = await fetch(healthUrl, {
      method: 'GET',
      headers: { accept: 'application/json' },
      cache: 'no-store',
      signal: controller.signal,
    });

    if (!response.ok) {
      return sendJson(res, 503, {
        ok: false,
        service: 'malach-application',
        status: 'unavailable',
        checkedAt: new Date().toISOString(),
      });
    }

    const upstream = await response.json().catch(() => ({}));
    if (upstream?.ok === false) {
      return sendJson(res, 503, {
        ok: false,
        service: 'malach-application',
        status: 'degraded',
        checkedAt: new Date().toISOString(),
      });
    }

    return sendJson(res, 200, {
      ok: true,
      service: 'malach-application',
      status: 'operational',
      checkedAt: new Date().toISOString(),
      components: upstream?.components || null,
    });
  } catch {
    return sendJson(res, 503, {
      ok: false,
      service: 'malach-application',
      status: 'unavailable',
      checkedAt: new Date().toISOString(),
    });
  } finally {
    clearTimeout(timeout);
  }
}
