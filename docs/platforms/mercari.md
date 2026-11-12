# Mercari API: 3 endpoints with pricing and code examples

Call 3 Mercari endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`mercari/product`](../models/mercari/product.md) | Get one Mercari US or Japan listing by item id or URL: title, description, price, original price, status, condition, brand, category,… | about $0.0012 per call |
| [`mercari/search`](../models/mercari/search.md) | Search active Mercari US or Japan listings for sale by keyword with optional price-range, condition, category, brand, and sort filters,… | about $0.0012 per call |
| [`mercari/sold-listings`](../models/mercari/sold-listings.md) | Search Mercari US or Japan sold listings by keyword with optional price-range, condition, category, brand, and sort filters, page by page,… | about $0.0012 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "mercari/product", "itemId": "m73121443159"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
