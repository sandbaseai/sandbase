# Taobao API: 5 endpoints with pricing and code examples

Call 5 Taobao endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`taobao/item/detail`](../models/taobao/item/detail.md) | Get a Taobao or Tmall product by item ID: title, images, price, SKU options, delivery and seller details. | $0.020834 per call |
| [`taobao/item/questions`](../models/taobao/item/questions.md) | Get buyer questions and answers for a Taobao or Tmall product by item ID, page by page. | $0.020833 per call |
| [`taobao/item/reviews`](../models/taobao/item/reviews.md) | Get Taobao and Tmall product reviews by item ID with pagination, sorted by latest or default, for customer feedback analysis. | $0.027778 per call |
| [`taobao/search/items`](../models/taobao/search/items.md) | Search Taobao and Tmall products by keyword with titles, prices, images, sales and shop info. Sort by sales or price, filter to Tmall only… | $0.027778 per call |
| [`taobao/shop-item-list`](../models/taobao/shop-item-list.md) | Get products from a Taobao or Tmall shop using both seller or user ID and shop ID, with page-based pagination and sorting by sales, new… | $0.027778 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/item/detail", "itemId": "920640959876"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
