# AliExpress API: 1 endpoints with pricing and code examples

Call 1 AliExpress endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`aliexpress/search/products`](../models/aliexpress/search/products.md) | Search AliExpress products by keyword with sort, category, brand, price, locale, region and currency filters. | $0.014286 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aliexpress/search/products"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
