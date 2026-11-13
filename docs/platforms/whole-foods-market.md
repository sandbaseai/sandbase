# Whole Foods Market API: 2 endpoints with pricing and code examples

Call 2 Whole Foods Market endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`whole-foods/product`](../models/whole-foods/product.md) | Get a Whole Foods Market product by URL with name, brand, price, size, ingredients, nutrition and dietary labels. | $0.00015 per call |
| [`whole-foods/search`](../models/whole-foods/search.md) | Search Whole Foods Market grocery products by keyword with name, brand, price, size and product URL, optionally for a store. | $0.00015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "whole-foods/product", "url": "https://www.wholefoodsmarket.com/product/clover-sonoma-organic-milk-32-fz-b019p8vdyy"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
