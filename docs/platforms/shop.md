# Shop API: 8 endpoints with pricing and code examples

Call 8 Shop endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`shop-app/categories`](../models/shop-app/categories.md) | Returns all top-level shopping categories available on shop.app. Categories include a Shopify GID, display name, and whether they have… | $0.03 per call |
| [`shop-app/homepage-featured-products`](../models/shop-app/homepage-featured-products.md) | Retrieves featured products from the shop.app homepage feed (the product shelves shown to an anonymous visitor, such as trending stores,… | $0.03 per call |
| [`shop-app/merchant-info`](../models/shop-app/merchant-info.md) | Retrieves merchant profile information including name, website, reviews, contacts, store sections, and visual theme. Returns the full shop… | $0.03 per call |
| [`shop-app/merchant-products`](../models/shop-app/merchant-products.md) | Retrieves one page of a merchant's in-stock product listing, sorted by the site's most-sales order, in a single upstream request. | $0.03 per call |
| [`shop-app/product-details`](../models/shop-app/product-details.md) | Retrieves full details for a single product including current price, original price (if discounted), images, rating, review count, and… | $0.03 per call |
| [`shop-app/search-autocomplete`](../models/shop-app/search-autocomplete.md) | Fetches search autocomplete suggestions for a query prefix. Returns both query suggestions (text completions) and matching shop… | $0.03 per call |
| [`shop-app/search-merchants-by-category`](../models/shop-app/search-merchants-by-category.md) | Searches for merchants within a shop.app category page. | $0.03 per call |
| [`shop-app/search-products`](../models/shop-app/search-products.md) | Searches shop.app products globally by a free-text keyword and returns one page of matching products from the site's global search results… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shop-app/categories"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
