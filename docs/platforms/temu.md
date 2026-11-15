# Temu API: 10 endpoints with pricing and code examples

Call 10 Temu endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`temu/batch-get-products`](../models/temu/batch-get-products.md) | Batch fetch product data for multiple product IDs in one call (up to 40). For each product ID, returns both raw API data and a flat… | $0.03 per call |
| [`temu/batch-get-stores`](../models/temu/batch-get-stores.md) | Batch fetch store products for multiple mall IDs in one call (up to 20). | $0.03 per call |
| [`temu/continue-batch-store-session`](../models/temu/continue-batch-store-session.md) | Continue paginated store sessions started by batch_get_stores. Accepts an array of opaque session tokens (from previous next_session_token… | $0.03 per call |
| [`temu/continue-search-session`](../models/temu/continue-search-session.md) | Continue a paginated search session started by start_search_session. | $0.03 per call |
| [`temu/homepage-featured`](../models/temu/homepage-featured.md) | Retrieve featured/trending products from the Temu homepage. | $0.03 per call |
| [`temu/product-details`](../models/temu/product-details.md) | Retrieve product details for a specific product by its numeric ID, including variant/SKU data. | $0.03 per call |
| [`temu/product-images`](../models/temu/product-images.md) | Retrieve product image URLs for one or more products by their numeric IDs (up to 40 per request). | $0.03 per call |
| [`temu/search-products`](../models/temu/search-products.md) | Full-text search over Temu's product catalog by keyword. | $0.03 per call |
| [`temu/start-search-session`](../models/temu/start-search-session.md) | Start a paginated search session over Temu's product catalog. | $0.03 per call |
| [`temu/store-products`](../models/temu/store-products.md) | Retrieve products listed by a specific store/seller on Temu, identified by mall_id. | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "temu/batch-get-products", "product_ids": "[\"605731197670167\"]"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
