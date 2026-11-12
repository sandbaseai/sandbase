# Target API: 3 endpoints with pricing and code examples

Call 3 Target endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`target/product`](../models/target/product.md) | Fetch a Target.com product by URL and get title, price, brand, rating, description, and images in one normalized response. | about $0.00085 per call |
| [`target/reviews`](../models/target/reviews.md) | Pull a page of 10 customer reviews for any Target.com product by URL, newest first or by helpfulness or rating: rating, title, text, date,… | about $0.00085 per call |
| [`target/search`](../models/target/search.md) | Search Target products by keyword with TCIN, brand, price, sale price, rating, reviews and pickup, delivery and shipping availability. | $0.015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "target/product", "url": "https://www.target.com/p/mr-coffee-12c-programmable-drip-coffee-maker-stainless-steel-finish/-/A-91863920"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
