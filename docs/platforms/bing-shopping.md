# Bing Shopping API: 2 endpoints with pricing and code examples

Call 2 Bing Shopping endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`bing-shopping/product`](../models/bing-shopping/product.md) | Get a Bing Shopping product by product token with title, specifications, rating, reviews and offers from each merchant. | $0.01 per call |
| [`bing-shopping/search`](../models/bing-shopping/search.md) | Search Bing Shopping by keyword: product title, price, old price, seller, rating, reviews and shipping, with market and filter options. | $0.015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing-shopping/product", "product_token": "<product_token>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
