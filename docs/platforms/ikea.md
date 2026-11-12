# IKEA API: 2 endpoints with pricing and code examples

Call 2 IKEA endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`ikea/product`](../models/ikea/product.md) | Get one IKEA product by URL with name, price, images, dimensions, materials, rating and store stock when a store ID is given. | $0.00015 per call |
| [`ikea/search`](../models/ikea/search.md) | Search IKEA's US store by keyword and get title, price, rating, and image for each product in one normalized response. | about $0.00085 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ikea/product", "url": "https://www.ikea.com/us/en/p/billy-bookcase-white-20522046/"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
