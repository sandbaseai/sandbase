# 1688 Cross-border Product Search API: pricing, parameters and code examples

`1688/search/cross-border` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search 1688 cross-border products by keyword or category with translated titles, sort and sourcing filters.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/search/cross-border"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/search/cross-border', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/search/cross-border", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/search/cross-border", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/1688/search/cross-border` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Product sort order. one of: `default`, `sales`, `price_up`, `price_down`; default `"default"` |
| `catId` | string |  | 1688 category ID. Supply catId or keyword.  |
| `keyword` | string |  | Search keyword. Supply keyword or catId.  |
| `language` | string |  | Output language. one of: `en`, `zh`, `ru`, `vi`, `ja`, `ko`; default `"en"` |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |
| `priceEnd` | string |  | Maximum price filter in CNY.  |
| `newArrival` | boolean |  | Filter for new products.  |
| `priceStart` | string |  | Minimum price filter in CNY.  |
| `freeShipping` | boolean |  | Filter for free shipping.  |
| `isSuperFactory` | boolean |  | Optional super-factory filter.  |
| `supportDropshipping` | boolean |  | Filter for support for dropshipping.  |

## Details

This API returns a page of 1688 cross-border product listings that match a keyword or a 1688 category ID. Each item has a translated title, minimum order quantity, sales volume and shop details. Send `keyword` or `catId`, and set `language` to pick the title language.

### Use cases

- Find suppliers for a product type such as phone cases and compare their minimum order quantities.
- Rank listings by 90-day sales volume to spot fast-moving products.
- Screen suppliers by shop age, composite score and repurchase rate before you contact them.
- Build a catalog feed with translated titles, images and product links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/search/cross-border" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "phone case", "language": "en"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `catId` | string | No | 1688 category ID. Supply catId or keyword. |
| `freeShipping` | boolean | No | Filter for free shipping. |
| `isSuperFactory` | boolean | No | Optional super-factory filter. |
| `keyword` | string | No | Search keyword. Supply keyword or catId. |
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
  "cat_id": null,
  "filters": {},
  "has_next_page": true,
  "items": [
    {
      "category_path": [
        "7"
      ],
      "currency": "CNY",
      "delivery_info": {
        "area_from": [
          "广东"
        ],
        "free_shipping": false,
        "ship_in_48h": false
      },
      "img": "https://cbu01.alicdn.com/img/ibank/O1CN01ckLnyq1LNUq1BAwUb_!!2220808541287-0-cib…",
      "item_id": 990347938140,
      "item_repurchase_rate": "20%",
      "low_refund_rate": false,
      "moq": "1",
      "one_piece_min_order": false,
      "price": "2.10",
      "price_info": {
        "origin_price": "",
        "price": "2.10",
        "sale_price": "2.10"
      },
      "product_url": "https://detail.1688.com/offer/990347938140.html"
    }
  ],
  "keyword": "phone case",
  "page": 1,
  "page_size": 20,
  "sort": "default",
  "total_count": 2000
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].item_id / items[].product_url` | The 1688 product ID and the link to its product page. |
| `items[].title / items[].title_origin` | The title in the requested `language` and the original Chinese title. |
| `items[].img` | The URL of the main product image. |
| `items[].category_path` | The category IDs for the item, as a list of strings. |
| `items[].moq / items[].quantity_begin` | The minimum order quantity for the item. Both are strings. |
| `items[].sale_info.sale_quantity_90days` | Sales volume over the last 90 days, shown as a rounded string such as `20K+`. |
| `items[].item_repurchase_rate` | The share of buyers who bought the item again, as a percent string such as `20%`. |
| `items[].delivery_info.area_from` | The region the item ships from, as a province and city in Chinese. |
| `items[].delivery_info.free_shipping / items[].ship_in_48h` | Flags for free shipping and for shipping within 48 hours. |
| `items[].shop_info.company_name / items[].shop_info.shop_years` | The seller's company name and the number of years the shop has operated. |

### Notes

- Send either `keyword` or `catId`. The response echoes `keyword`, `page`, `page_size` and `sort`.
- Use `page` and `pageSize` to paginate, and stop when `has_next_page` is `false`. The returned item count may differ from `pageSize`.
- `total_count` gives the number of matches for the query.
- To get full specs for an item, pass its `item_id` to [1688 Product Details](/apis/1688/item/detail). To look up the seller, use [1688 Shop Info](/apis/1688/shop/info).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/search/cross-border.json`](../../../../catalog/models/1688/search/cross-border.json) · Store page: https://www.sandbase.ai/model/1688/search/cross-border
