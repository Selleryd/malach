import { sendJson, methodNotAllowed } from './_lib/http.js';
import { priceMap } from './_lib/stripe.js';

export default async function handler(req, res) {
  if (req.method !== 'GET') return methodNotAllowed(res, ['GET']);
  const prices = priceMap();
  const display = {
    core: {
      monthly: { enabled: Boolean(prices.core.monthly), display: process.env.PUBLIC_PRICE_CORE_MONTHLY || '' },
      annual: { enabled: Boolean(prices.core.annual), display: process.env.PUBLIC_PRICE_CORE_ANNUAL || '' }
    },
    autonomous: {
      monthly: { enabled: Boolean(prices.autonomous.monthly), display: process.env.PUBLIC_PRICE_AUTONOMOUS_MONTHLY || '' },
      annual: { enabled: Boolean(prices.autonomous.annual), display: process.env.PUBLIC_PRICE_AUTONOMOUS_ANNUAL || '' }
    },
    portfolio: {
      monthly: { enabled: Boolean(prices.portfolio.monthly), display: process.env.PUBLIC_PRICE_PORTFOLIO_MONTHLY || '' },
      annual: { enabled: Boolean(prices.portfolio.annual), display: process.env.PUBLIC_PRICE_PORTFOLIO_ANNUAL || '' }
    }
  };
  sendJson(res, 200, {
    billingEnabled: Boolean(process.env.STRIPE_SECRET_KEY && Object.values(prices).some(plan => plan.monthly || plan.annual)),
    prices: display,
    appUrl: process.env.APP_URL || 'https://app.malach.app'
  });
}
