# Douyin Shop Items API: pricing, parameters and code examples

`douyin/ec/shop-items` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

List the products of a Douyin shop by shop ID, page by page, with price and sales for each item.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/ec/shop-items", "shopId": "42853938"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/ec/shop-items', {'shopId': '42853938'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/ec/shop-items", {
  "shopId": "42853938"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/ec/shop-items", sandbase.Params{
	"shopId": "42853938",
})
```

Same call via the path form: `POST /v1/api/douyin/ec/shop-items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for pagination.  |
| `shopId` | string | yes | The unique ID of the shop on Douyin E-commerce.  |

## Details

Returns one page of products listed by a Douyin shop. Each item has a title, price, monthly sales, cover image and ID. The only required input is the shop ID in `shopId`.

### Use cases

- Track a competitor shop's best sellers by comparing `month_sales` across its products.
- Build a price list of every item a shop sells on Douyin E-commerce.
- Collect `product_id` values to feed into item detail, SKU or comment lookups.
- Check which service tags, such as free return shipping insurance, a shop puts on its products.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/ec/shop-items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shopId": "42853938"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shopId` | string | Yes | The unique ID of the shop on Douyin E-commerce. |
| `page` | string | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "page": 1,
  "products": [
    {
      "cover": "https://lf26-cm.ecombdstatic.com/obj/ecom-shop-material/jpeg_m_64c6f372c524bd699…",
      "month_sales": 705482,
      "price": 39.9,
      "product_id": "3680294078299373976",
      "product_tags": [
        "运费险"
      ],
      "promotion_id": "3680296553450441933",
      "title": "娇婵美白补水修颜隔离防晒乳SPF50+PA++++防紫外线补水"
    }
  ],
  "shop_id": "42853938",
  "total": 81,
  "total_pages": 9
}
```

### Response fields

| Field | Meaning |
|---|---|
| `products[].product_id` | ID of the product. Use it to look up the item in other Douyin shop APIs. |
| `products[].title` | Product title as shown in the shop, in Chinese. |
| `products[].price` | Listed price of the product as a number, for example `39.9`. |
| `products[].month_sales` | Sales count for the product, named as a monthly figure. |
| `products[].cover` | URL of the product cover image. |
| `products[].product_tags` | List of tags shown on the product, such as shipping insurance and return policy labels. |
| `products[].promotion_id` | ID of the promotion linked to the product. |
| `page / total_pages` | Current page number and the total number of pages for this shop. |
| `total` | Total number of products found for the shop. |
| `shop_id` | ID of the shop that was queried. |

### Notes

- Pass the page number in `page`. The first request without `page` returns page 1. Stop when `page` reaches `total_pages`.
- `product_id` is a long numeric string. Keep it as a string to avoid rounding.
- Call [Douyin Shop Item Details](/apis/douyin/ec/item-detail) with a `product_id` for full item data, or [Douyin Shop Item SKUs](/apis/douyin/ec/item-skus) for its variants.
- To find items without a shop ID, use [Douyin Shop Product Search](/apis/douyin/ec/search-items).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/ec/shop-items.json`](../../../../catalog/models/douyin/ec/shop-items.json) · Store page: https://www.sandbase.ai/model/douyin/ec/shop-items
