# Home Depot API: 3 endpoints with pricing and code examples

Call 3 Home Depot endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`home-depot/product`](../models/home-depot/product.md) | Get a Home Depot product by product ID: title, brand, model number, UPC, price, specifications, images, fulfillment and ratings, localized… | $0.015 per call (free daily quota) |
| [`home-depot/product-reviews`](../models/home-depot/product-reviews.md) | Get Home Depot product reviews by product ID: overall rating, ratings histogram, recommendation counts, and reviews with filters and… | $0.015 per call (free daily quota) |
| [`home-depot/search`](../models/home-depot/search.md) | Search Home Depot products by keyword with price, brand, model number, rating, delivery and pickup availability, filters and pagination. | $0.015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "home-depot/product", "product_id": "310009453"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
