# Nextdoor API: 1 endpoints with pricing and code examples

Call 1 Nextdoor endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`nextdoor/business`](../models/nextdoor/business.md) | Fetch one Nextdoor business page by its slug, with phone, email, website, and street address. | about $0.00242 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nextdoor/business", "pageSlug": "radiant-plumbing-air-conditioning-austin-tx"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
