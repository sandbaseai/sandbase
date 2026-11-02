# TikTok Shop API: 8 endpoints with pricing and code examples

Call 8 TikTok Shop endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`tiktok-shop/categories`](../models/tiktok-shop/categories.md) | List the TikTok Shop category tree for a market: top-level categories with ids, slugs, and images, each with its child categories. | about $0.0012 per call |
| [`tiktok-shop/creator`](../models/tiktok-shop/creator.md) | TikTok Shop creator performance by handle: GMV range, promoted product count, brand collaborations, follower age/gender/location… | about $0.0055 per call |
| [`tiktok-shop/product`](../models/tiktok-shop/product.md) | Fetch TikTok Shop product details (title, price, sales, seller, and ratings) from a product URL. | about $0.0012 per call |
| [`tiktok-shop/product-reviews`](../models/tiktok-shop/product-reviews.md) | Fetch customer reviews for a TikTok Shop product by URL (rating, text, reviewer, country, and verified-buyer flag). | about $0.00095 per call |
| [`tiktok-shop/search`](../models/tiktok-shop/search.md) | Search TikTok Shop products by keyword across 15 countries: price, sales, rating, and seller info per product, in one normalized response. | about $0.00095 per call |
| [`tiktok-shop/search-suggestions`](../models/tiktok-shop/search-suggestions.md) | Get TikTok Shop search autocomplete terms for a keyword: the long-tail queries shoppers actually type, for keyword and demand research. | about $0.00095 per call |
| [`tiktok-shop/shop-products`](../models/tiktok-shop/shop-products.md) | List every product of a TikTok Shop store by URL (title, price, sales, and rating per product plus shop-level stats) with cursor pagination. | about $0.0012 per call |
| [`tiktok-shop/user-showcase`](../models/tiktok-shop/user-showcase.md) | List the TikTok Shop products a creator showcases (title, price, rating, and sales per product). | about $0.0012 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/categories"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
