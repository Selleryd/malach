import { sendJson, methodNotAllowed, readJson } from './_lib/http.js';
import { stripeRequest } from './_lib/stripe.js';

export default async function handler(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);
  const expected = process.env.MALACH_PORTAL_API_TOKEN;
  const supplied = String(req.headers.authorization || '').replace(/^Bearer\s+/i, '');
  if (!expected || supplied !== expected) return sendJson(res, 401, { error: 'Unauthorized' });
  try {
    const body = await readJson(req);
    if (!body.customerId) return sendJson(res, 400, { error: 'Stripe customer ID is required' });
    const params = {
      customer: body.customerId,
      return_url: body.returnUrl || `${process.env.APP_URL || 'https://app.malach.app'}/settings/billing`
    };
    if (process.env.STRIPE_PORTAL_CONFIGURATION_ID) params.configuration = process.env.STRIPE_PORTAL_CONFIGURATION_ID;
    const session = await stripeRequest('/billing_portal/sessions', params);
    sendJson(res, 200, { url: session.url });
  } catch (error) {
    console.error('portal_session_failed', { message: error.message });
    sendJson(res, 500, { error: 'Billing portal could not be opened' });
  }
}
