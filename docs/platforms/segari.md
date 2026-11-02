# Segari API: 1 endpoints with pricing and code examples

Call 1 Segari endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`segari/scrape/product`](../models/segari/scrape/product.md) | Extract structured data from a Segari product page URL: price, availability and product details. | $0.024 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "segari/scrape/product", "url": "https://segari.id/p/telur-ayam-kampung-curah"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
