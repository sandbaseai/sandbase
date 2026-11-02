# Google Hotels API: 1 endpoints with pricing and code examples

Call 1 Google Hotels endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`google-hotels/search`](../models/google-hotels/search.md) | Google Hotels results for a destination and stay dates: hotels, nightly rates, ratings, amenities and offers. | $0.015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-hotels/search", "q": "Bali Resorts", "check_in_date": "2026-12-15", "check_out_date": "2026-12-16", "adults": 2}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
