# eBay API: 2 endpoints with pricing and code examples

Call 2 eBay endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`ebay/product`](../models/ebay/product.md) | Get an eBay product by product ID: title, price, condition, quantity sold, item specifics, media, shipping, returns and seller details. | $0.015 per call (free daily quota) |
| [`ebay/search`](../models/ebay/search.md) | Search eBay listings by keyword with price, condition, shipping, bids, time left and seller, plus condition, format, price and location… | $0.015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ebay/product", "product_id": "326405504746"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
