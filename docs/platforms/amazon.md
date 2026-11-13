# Amazon API: 14 endpoints with pricing and code examples

Call 14 Amazon endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`amazon/asins`](../models/amazon/asins.md) | Look up to 10 Amazon products in one call by ASIN (title, brand, price, ratings, images, and attributes) as normalized JSON. | about $0.0033 per call |
| [`amazon/autocomplete`](../models/amazon/autocomplete.md) | Get Amazon search box suggestions for a partial keyword, optionally for a specific Amazon domain and department. | $0.00015 per call |
| [`amazon/best-sellers`](../models/amazon/best-sellers.md) | Get the Amazon Best Sellers list for a category path in a chosen marketplace country, with rank, title, price, rating and ASIN, page by… | $0.014286 per call (free daily quota) |
| [`amazon/category-products`](../models/amazon/category-products.md) | Get paginated Amazon products for a numeric category node in a selected country marketplace, with configurable result sorting. | $0.014286 per call (free daily quota) |
| [`amazon/deals`](../models/amazon/deals.md) | List today's Amazon deals for one marketplace and get ASIN, title, deal price, list price, discount, deal type, badge and image for each… | about $0.00085 per call |
| [`amazon/fresh`](../models/amazon/fresh.md) | Search Amazon Fresh grocery products for a delivery ZIP code, with title, price, unit price, rating and availability. | $0.01 per call |
| [`amazon/offers`](../models/amazon/offers.md) | List every offer for one Amazon product by ASIN or product URL, the Buy Box first and then the other sellers, and get price, condition,… | about $0.00085 per call |
| [`amazon/product`](../models/amazon/product.md) | Get an Amazon product by ASIN: title, brand, price, rating, reviews, images, variants, availability, purchase options, about-this-item and… | $0.015 per call (free daily quota) |
| [`amazon/product-detail`](../models/amazon/product-detail.md) | Get details for an Amazon product identified by ASIN in a selected country marketplace. Use it to look up a known listing for catalog… | $0.014286 per call (free daily quota) |
| [`amazon/reviews`](../models/amazon/reviews.md) | Pull customer reviews for any Amazon product by ASIN or URL: rating, title, text, date, and verified-buyer badge. | about $0.016 per call |
| [`amazon/search`](../models/amazon/search.md) | Search Amazon by keyword: organic results with ASIN, title, price, old price, rating, reviews, Prime and delivery info, plus sponsored… | $0.015 per call (free daily quota) |
| [`amazon/search-products`](../models/amazon/search-products.md) | Search Amazon marketplace products by keyword or ASIN with country, sort, condition, Prime-only, deals, and page controls. | $0.014286 per call (free daily quota) |
| [`amazon/seller`](../models/amazon/seller.md) | Look up one Amazon seller by seller ID and get its name, star rating, positive feedback percentage, feedback counts for the last 30 days,… | about $0.00085 per call |
| [`amazon/seller-products`](../models/amazon/seller-products.md) | List one Amazon seller's storefront by seller ID, a page at a time, and get ASIN, title, price, list price, rating, reviews count, image,… | about $0.00085 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/asins", "asins": ["B09G9FPHY6"]}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
