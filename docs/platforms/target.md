# Target API: 1 endpoints with pricing and code examples

Call 1 Target endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`target/search`](../models/target/search.md) | Search Target products by keyword with TCIN, brand, price, sale price, rating, reviews and pickup, delivery and shipping availability. | $0.015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "target/search", "q": "wireless earbuds"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
