# Fundable API: 2 endpoints with pricing and code examples

Call 2 Fundable endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`fundable/industry-search`](../models/fundable/industry-search.md) | Search industries and super categories by name | from $0 per run, depending on parameters |
| [`fundable/location-search`](../models/fundable/location-search.md) | Search locations by name and optionally filter by type | from $0 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fundable/industry-search", "name": "fintech"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
