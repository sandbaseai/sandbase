# Amazon API: 6 endpoints with pricing and code examples

Call 6 Amazon endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`amazon/best-sellers`](../models/amazon/best-sellers.md) | Get the Amazon Best Sellers list for a category path in a chosen marketplace country, with rank, title, price, rating and ASIN, page by… | $0.014286 per call (free daily quota) |
| [`amazon/category-products`](../models/amazon/category-products.md) | Get paginated Amazon products for a numeric category node in a selected country marketplace, with configurable result sorting. | $0.014286 per call (free daily quota) |
| [`amazon/product`](../models/amazon/product.md) | Get an Amazon product by ASIN: title, brand, price, rating, reviews, images, variants, availability, purchase options, about-this-item and… | $0.015 per call (free daily quota) |
| [`amazon/product-detail`](../models/amazon/product-detail.md) | Get details for an Amazon product identified by ASIN in a selected country marketplace. Use it to look up a known listing for catalog… | $0.014286 per call (free daily quota) |
| [`amazon/search`](../models/amazon/search.md) | Search Amazon by keyword: organic results with ASIN, title, price, old price, rating, reviews, Prime and delivery info, plus sponsored… | $0.015 per call (free daily quota) |
| [`amazon/search-products`](../models/amazon/search-products.md) | Search Amazon marketplace products by keyword or ASIN with country, sort, condition, Prime-only, deals, and page controls. | $0.014286 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/best-sellers", "category": "electronics"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
