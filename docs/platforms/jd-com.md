# JD.com API: 5 endpoints with pricing and code examples

Call 5 JD.com endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`jd/item/comments`](../models/jd/item/comments.md) | Get paginated customer comments for a JD.com product by item ID, for buyer feedback and product quality research. | $0.027778 per call |
| [`jd/item/description-images`](../models/jd/item/description-images.md) | Get the description images and product attributes of a JD.com product by item ID. | $0.020833 per call |
| [`jd/item/detail`](../models/jd/item/detail.md) | Get a JD.com product by item ID: title, price, promotion price, brand, shop and images. | $0.027778 per call |
| [`jd/search/items`](../models/jd/search/items.md) | Search JD.com products by keyword with item IDs, titles, images, categories and shop names, with page-based pagination. | $0.020834 per call |
| [`jd/shop/items`](../models/jd/shop/items.md) | List products from a JD.com shop by shop ID, page by page, to collect item IDs for follow-up lookups. | $0.027778 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "jd/item/comments", "itemId": "100207440191"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
