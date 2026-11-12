# Etsy API: 4 endpoints with pricing and code examples

Call 4 Etsy endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`etsy/product`](../models/etsy/product.md) | Look up one Etsy listing by id and get its price, images, description, rating, reviews count, shop, category, variations, stock, ship-from… | about $0.00187 per call |
| [`etsy/search`](../models/etsy/search.md) | Search Etsy listings by keyword, the same results an Etsy search or /market page shows, with optional sort, price range and page, and get… | about $0.0009 per call |
| [`etsy/shop`](../models/etsy/shop.md) | Look up one Etsy shop by name and get its id, location, sales, active listings, rating, reviews count, followers, description, logo and… | about $0.0009 per call |
| [`etsy/shop-listings`](../models/etsy/shop-listings.md) | List one Etsy shop's active listings by shop name, a page at a time, and get title, price, original price and image for each listing in… | about $0.0009 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "etsy/product", "listingId": "1810545592"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
