# AliExpress API: 2 endpoints with pricing and code examples

Call 2 AliExpress endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`aliexpress/reviews`](../models/aliexpress/reviews.md) | Get one page of buyer reviews for an AliExpress product by id, with rating, text, buyer country, date, bought variant and photos for each… | about $0.00085 per call |
| [`aliexpress/search/products`](../models/aliexpress/search/products.md) | Search AliExpress products by keyword with sort, category, brand, price, locale, region and currency filters. | $0.014286 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aliexpress/reviews", "productId": "3256807039224587"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
