# Capterra API: 4 endpoints with pricing and code examples

Call 4 Capterra endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`capterra/category-products`](../models/capterra/category-products.md) | Retrieve products listed within a specific software category. Returns product names, numeric IDs, URL slugs, and full URLs. | $0.01 per call (free daily quota) |
| [`capterra/product-details`](../models/capterra/product-details.md) | Retrieve detailed information about a specific software product, including description, overall rating, review count, and feature list.… | $0.01 per call (free daily quota) |
| [`capterra/product-reviews`](../models/capterra/product-reviews.md) | Retrieve user reviews for a software product. Returns paginated reviews with title, date, overall rating, pros, and cons text (up to 25… | $0.01 per call (free daily quota) |
| [`capterra/search-software`](../models/capterra/search-software.md) | Search for software products by keyword. Returns matching products with name, numeric ID, URL slug, and full URL. | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "capterra/category-products", "category_slug": "accounting"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
