# Kelley Blue Book API: 3 endpoints with pricing and code examples

Call 3 Kelley Blue Book endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`kbb/lease-deals`](../models/kbb/lease-deals.md) | Retrieve the current '10 Best Lease Deals Around $200' editorial list from Kelley Blue Book in one round trip. Each deal carries the… | $0.01 per call (free daily quota) |
| [`kbb/obd-codes`](../models/kbb/obd-codes.md) | Retrieve OBD-II diagnostic trouble code descriptions from KBB. Currently supports powertrain (P) codes only. | $0.01 per call (free daily quota) |
| [`kbb/years`](../models/kbb/years.md) | Retrieve all available vehicle model years from Kelley Blue Book in one round trip. Returns an array of integer years in descending order,… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kbb/lease-deals"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
