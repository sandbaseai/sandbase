# Sprouts Farmers Market API: 2 endpoints with pricing and code examples

Call 2 Sprouts Farmers Market endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`sprouts/product`](../models/sprouts/product.md) | Get a Sprouts Farmers Market product by URL with name, price, size, description and store availability. | $0.00015 per call |
| [`sprouts/search`](../models/sprouts/search.md) | Search Sprouts Farmers Market grocery products by keyword with name, price, size and product URL, optionally for a store. | $0.00015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sprouts/product", "url": "https://shop.sprouts.com/store/sprouts/products/120137222-grazeful-dairy-grassfed-whole-a2-a2-milk-2-gal"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
