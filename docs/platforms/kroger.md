# Kroger API: 2 endpoints with pricing and code examples

Call 2 Kroger endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`kroger/product`](../models/kroger/product.md) | Get one Kroger grocery product by URL with title, price, size, images and store availability; pass a store ID for local pricing. | $0.00015 per call |
| [`kroger/search`](../models/kroger/search.md) | Search Kroger grocery products by keyword with price, size and product URL; pass a store ID for local pricing and stock. | $0.00015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kroger/product", "url": "https://www.kroger.com/p/organic-valley-whole-milk-half-gallon/0009396651300"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
