# AutoZone API: 3 endpoints with pricing and code examples

Call 3 AutoZone endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`autozone/product`](../models/autozone/product.md) | Get an AutoZone part by product ID with brand, part number, price, specifications, warranty, vehicle fitment and store availability. | $0.01 per call |
| [`autozone/scrape/category`](../models/autozone/scrape/category.md) | Extract product listings from an AutoZone category page URL with pagination and preferred-store pricing. | $0.012 per call (free daily quota) |
| [`autozone/search`](../models/autozone/search.md) | Search AutoZone auto parts by keyword, optionally for a specific vehicle and store, with part number, brand, price, rating and availability. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "autozone/product", "product_id": "992113"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
