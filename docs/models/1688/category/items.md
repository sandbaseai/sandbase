# 1688 Category Products API: pricing, parameters and code examples

`1688/category/items` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

List 1688 wholesale products in a category with output language, sort, price, dropshipping and factory filters.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/category/items", "catId": "97"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/category/items', {'catId': '97'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/category/items", {
  "catId": "97"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/category/items", sandbase.Params{
	"catId": "97",
})
```

Same call via the path form: `POST /v1/api/1688/category/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Product sort order. one of: `default`, `sales`, `price_up`, `price_down`; default `"default"` |
| `catId` | string | yes | 1688 platform category ID.  |
| `language` | string |  | Output language. one of: `en`, `zh`, `ru`, `vi`, `ja`, `ko`; default `"zh"` |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |
| `priceEnd` | string |  | Maximum price filter in CNY.  |
| `newArrival` | boolean |  | Filter for new products.  |
| `priceStart` | string |  | Minimum price filter in CNY.  |
| `freeShipping` | boolean |  | Filter for free shipping.  |
| `isSuperFactory` | boolean |  | Optional super-factory filter.  |
| `supportDropshipping` | boolean |  | Filter for support for dropshipping.  |

## Details

Returns a page of 1688 wholesale products listed in one category. You send a 1688 category ID as `catId`, and you can set the output language, sort order, and filters such as dropshipping, free shipping and super factory.

### Use cases

- Build a catalog of wholesale products in one 1688 category for a resale store.
- Rank products in a category by `sale_info.sale_quantity_90days` to find fast sellers.
- Shortlist suppliers by shop age, composite score and repurchase rate before contacting them.
- Filter a category for dropshipping or super-factory products and export the product links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/category/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"catId": "97", "language": "en"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `catId` | string | Yes | 1688 platform category ID. |
| `freeShipping` | boolean | No | Filter for free shipping. |
| `isSuperFactory` | boolean | No | Optional super-factory filter. |
| `language` | string | No | Output language. |
| `newArrival` | boolean | No | Filter for new products. |
| `page` | integer | No | Page number, starting at 1. |
| `pageSize` | integer | No | Number of items requested per page. The returned count may differ. |
| `priceEnd` | string | No | Maximum price filter in CNY. |
| `priceStart` | string | No | Minimum price filter in CNY. |
| `sort` | string | No | Product sort order. |
| `supportDropshipping` | boolean | No | Filter for support for dropshipping. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cat_id": 97,
  "filters": {},
  "has_next_page": true,
  "items": [
    {
      "category_path": [
        "97"
      ],
      "currency": "CNY",
      "delivery_info": {
        "area_from": [
          ""
        ],
        "free_shipping": false,
        "ship_in_48h": false
      },
      "img": "https://cbu01.alicdn.com/img/ibank/O1CN01SuQkMOZANnD1bRrY_!!6000000006137-0-cib.…",
      "item_id": 1073789442750,
      "item_repurchase_rate": "100%",
      "low_refund_rate": false,
      "moq": "100",
      "one_piece_min_order": false,
      "price": "0.06",
      "price_info": {
        "origin_price": "",
        "price": "0.06",
        "sale_price": "0.06"
      },
      "product_url": "https://detail.1688.com/offer/1073789442750.html"
    }
  ],
  "keyword": "",
  "page": 1,
  "page_size": 20,
  "sort": "default",
  "total_count": 2000
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].item_id / items[].product_url` | The product ID and the link to its 1688 detail page. |
| `items[].title / items[].title_origin` | The product title in the requested `language`, and the original title in Chinese. |
| `items[].moq / items[].quantity_begin` | The minimum order quantity as a string. |
| `items[].sale_info.sale_quantity_90days` | The sales volume over 90 days, shown as a string such as `100K+`. |
| `items[].item_repurchase_rate` | The product's repurchase rate as a percentage string. |
| `items[].delivery_info.area_from` | The province and city the product ships from. Both values can be empty strings. |
| `items[].delivery_info.free_shipping / items[].ship_in_48h` | Flags for free shipping and for shipping within 48 hours. |
| `items[].shop_info.company_name / items[].shop_info.shop_years` | The seller's company name and the number of years the shop has existed. |
| `items[].shop_info.score_info.composite_score` | The shop's composite score, shown as a string such as `4.0`. |
| `items[].shop_info.is_super_factory` | Flag for the super-factory badge on the shop. |

### Notes

- Set `page` and `pageSize` to move through results. Use `has_next_page` to see if more pages exist. `total_count` gives the total number of matching items.
- Each item has a `category_path` list of category IDs. The first value is the `catId` you requested and the next value is a subcategory ID.
- Pass an `item_id` to [1688 Product Details](/apis/1688/item/detail) to get the full product record.
- Look up category names with [1688 Category Info](/apis/1688/category/info).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/category/items.json`](../../../../catalog/models/1688/category/items.json) · Store page: https://www.sandbase.ai/model/1688/category/items
