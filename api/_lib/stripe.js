import crypto from 'node:crypto';

const STRIPE_API = 'https://api.stripe.com/v1';

export function requireStripe() {
  const key = process.env.STRIPE_SECRET_KEY;
  if (!key) throw new Error('Stripe is not configured');
  return key;
}

export async function stripeRequest(path, params = {}, method = 'POST') {
  const key = requireStripe();
  const body = new URLSearchParams();
  Object.entries(params).forEach(([name, value]) => {
    if (value === undefined || value === null || value === '') return;
    body.append(name, String(value));
  });
  const response = await fetch(`${STRIPE_API}${path}`, {
    method,
    headers: {
      authorization: `Bearer ${key}`,
      'content-type': 'application/x-www-form-urlencoded'
    },
    body: method === 'GET' ? undefined : body
  });
  const data = await response.json();
  if (!response.ok) {
    const error = new Error(data?.error?.message || 'Stripe request failed');
    error.code = data?.error?.code;
    throw error;
  }
  return data;
}

export function priceMap() {
  return {
    core: {
      monthly: process.env.STRIPE_PRICE_CORE_MONTHLY,
      annual: process.env.STRIPE_PRICE_CORE_ANNUAL
    },
    autonomous: {
      monthly: process.env.STRIPE_PRICE_AUTONOMOUS_MONTHLY,
      annual: process.env.STRIPE_PRICE_AUTONOMOUS_ANNUAL
    },
    portfolio: {
      monthly: process.env.STRIPE_PRICE_PORTFOLIO_MONTHLY,
      annual: process.env.STRIPE_PRICE_PORTFOLIO_ANNUAL
    }
  };
}

export function verifyStripeSignature(rawBody, signatureHeader, secret, toleranceSeconds = 300) {
  if (!signatureHeader || !secret) return false;
  const parsed = signatureHeader.split(',').map(part => part.trim().split('='));
  const timestamp = Number(parsed.find(([key]) => key === 't')?.[1] || 0);
  const signatures = parsed.filter(([key]) => key === 'v1').map(([, value]) => value).filter(Boolean);
  if (!timestamp || !signatures.length) return false;
  if (Math.abs(Date.now() / 1000 - timestamp) > toleranceSeconds) return false;
  const signedPayload = `${timestamp}.${rawBody.toString('utf8')}`;
  const expected = Buffer.from(crypto.createHmac('sha256', secret).update(signedPayload).digest('hex'), 'hex');
  return signatures.some(signature => {
    const candidate = Buffer.from(signature, 'hex');
    return expected.length === candidate.length && crypto.timingSafeEqual(expected, candidate);
  });
}
