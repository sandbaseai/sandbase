# Google Shopping API: 3 endpoints with pricing and code examples

Call 3 Google Shopping endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`google-shopping/immersive-product`](../models/google-shopping/immersive-product.md) | Get the full Google Shopping product view by page token: specifications, ratings, reviews and offers from each store with price and… | $0.01 per call |
| [`google-shopping/product`](../models/google-shopping/product.md) | One Google Shopping product's merchant offers, prices, specifications, reviews and related products. | $0.00015 per call (free daily quota) |
| [`google-shopping/search`](../models/google-shopping/search.md) | Search Google Shopping by keyword: product title, price, old price, store, rating, reviews, delivery and product ID, with price, sort and… | $0.015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-shopping/immersive-product", "page_token": "<page_token>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
