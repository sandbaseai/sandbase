# Meijer API: 1 endpoints with pricing and code examples

Call 1 Meijer endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`meijer/scrape/product`](../models/meijer/scrape/product.md) | Extract structured data from a Meijer product page URL: price, availability and product details, optionally localized by ZIP code. | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meijer/scrape/product", "url": "https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
