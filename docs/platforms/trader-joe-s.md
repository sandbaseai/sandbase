# Trader Joe's API: 2 endpoints with pricing and code examples

Call 2 Trader Joe's endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`trader-joes/product`](../models/trader-joes/product.md) | Get a Trader Joe's product by product ID with name, price, size, description, ingredients, nutrition and dietary tags. | $0.01 per call |
| [`trader-joes/search`](../models/trader-joes/search.md) | Search Trader Joe's products by keyword with name, price, size, category and dietary tags, filtered by store and category. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trader-joes/product", "product_id": "097234"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
