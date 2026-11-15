# H&M API: 12 endpoints with pricing and code examples

Call 12 H&M endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`hm/new-arrivals`](../models/hm/new-arrivals.md) | Fetch new arrivals for a category. Returns recently added products with pricing and availability. Uses the same listing mechanism as… | $0.03 per call |
| [`hm/product-detail`](../models/hm/product-detail.md) | Fetch product details including pricing, availability, color variants, and images for a given article code or product URL. Returns full… | $0.03 per call |
| [`hm/product-details-kr`](../models/hm/product-details-kr.md) | Get full product details for a Korean H&M product including all color variants, size-level online availability, images with type labels,… | $0.03 per call |
| [`hm/product-listing`](../models/hm/product-listing.md) | Fetch paginated product listings for a specific category path. Returns product hits with pricing, images, swatches, sizes, and pagination… | $0.03 per call |
| [`hm/products-kr`](../models/hm/products-kr.md) | List Korean H&M products by category path. Returns paginated products with Korean names, KRW prices, member prices, images, and facets.… | $0.03 per call |
| [`hm/related-products-kr`](../models/hm/related-products-kr.md) | Get styling and pairing recommendations for a Korean H&M product. | $0.03 per call |
| [`hm/sale-products`](../models/hm/sale-products.md) | Fetch sale/discounted products for a category. Returns products with both regular and discounted prices, discount percentages, and… | $0.03 per call |
| [`hm/search-products`](../models/hm/search-products.md) | Search for products by keyword. Returns matching products with pricing, images, facets, and pagination. Uses H&M's search API for reliable… | $0.03 per call |
| [`hm/search-products-kr`](../models/hm/search-products-kr.md) | Search Korean H&M products by keyword. | $0.03 per call |
| [`hm/similar-items`](../models/hm/similar-items.md) | Fetch similar product recommendations for a given article code. Returns multiple recommendation lists (style_with, alternatives, upsell)… | $0.03 per call |
| [`hm/size-guide`](../models/hm/size-guide.md) | Return the H&M size guide shown on a product page: measurement tables (chest, waist, hip, inside leg, etc. | $0.03 per call |
| [`hm/store-finder`](../models/hm/store-finder.md) | Fetch physical H&M store locations in the US. Optionally filter by city name using case-insensitive substring matching. Returns store… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hm/new-arrivals"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
