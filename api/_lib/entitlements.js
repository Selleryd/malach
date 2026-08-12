async function upsertSupabase(record) {
  const url = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !key) return false;
  const response = await fetch(`${url.replace(/\/$/, '')}/rest/v1/subscriptions?on_conflict=stripe_subscription_id`, {
    method: 'POST',
    headers: {
      apikey: key,
      authorization: `Bearer ${key}`,
      'content-type': 'application/json',
      prefer: 'resolution=merge-duplicates,return=minimal'
    },
    body: JSON.stringify(record)
  });
  if (!response.ok) throw new Error(`Supabase entitlement update failed: ${response.status}`);
  return true;
}

async function notifyMalach(record) {
  const endpoint = process.env.MALACH_ENTITLEMENT_WEBHOOK_URL;
  if (!endpoint) return false;
  const headers = { 'content-type': 'application/json' };
  if (process.env.MALACH_ENTITLEMENT_WEBHOOK_TOKEN) headers.authorization = `Bearer ${process.env.MALACH_ENTITLEMENT_WEBHOOK_TOKEN}`;
  const response = await fetch(endpoint, { method: 'POST', headers, body: JSON.stringify(record) });
  if (!response.ok) throw new Error(`Malach entitlement webhook failed: ${response.status}`);
  return true;
}

export async function syncEntitlement(record) {
  const results = await Promise.allSettled([upsertSupabase(record), notifyMalach(record)]);
  const attempted = results.some(result => result.status === 'fulfilled' && result.value === true);
  const failure = results.find(result => result.status === 'rejected');
  if (failure) throw failure.reason;
  if (!attempted && process.env.REQUIRE_ENTITLEMENT_SINK === 'true') {
    throw new Error('No entitlement destination is configured');
  }
}
