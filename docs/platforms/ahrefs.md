# Ahrefs API: 2 endpoints with pricing and code examples

Call 2 Ahrefs endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`ahrefs/domain-rating`](../models/ahrefs/domain-rating.md) | Return the Ahrefs Domain Rating (0-100 authority score) and Ahrefs Rank for a target domain on a given date. 4xx/5xx are not charged. | $0.08 per call |
| [`ahrefs/metrics`](../models/ahrefs/metrics.md) | Return core Site Explorer metrics for a target domain on a given date: organic and paid keyword counts, top-3 keyword count, organic… | $0.08 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/domain-rating", "date": "2026-08-01", "target": "ahrefs.com"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
