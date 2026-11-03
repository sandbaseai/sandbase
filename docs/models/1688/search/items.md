# 1688 Product Search API: pricing, parameters and code examples

`1688/search/items` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search 1688 wholesale products by keyword with price, minimum order quantity, tiered prices, sales, repurchase rate and delivery info. Sort and filter by price, MOQ, dropshipping, free shipping and factory.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/search/items", "keyword": "蓝牙耳机"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/search/items', {'keyword': '蓝牙耳机'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/search/items", {
  "keyword": "蓝牙耳机"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/search/items", sandbase.Params{
	"keyword": "蓝牙耳机",
})
```

Same call via the path form: `POST /v1/api/1688/search/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `moq` | integer |  | Minimum order quantity filter.  |
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Product sort order. one of: `default`, `sales`, `price_up`, `price_down`; default `"default"` |
| `keyword` | string | yes | Search keyword.  |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |
| `priceEnd` | string |  | Maximum price filter in CNY.  |
| `newArrival` | boolean |  | Filter for new products.  |
| `priceStart` | string |  | Minimum price filter in CNY.  |
| `freeShipping` | boolean |  | Filter for free shipping.  |
| `isSuperFactory` | boolean |  | Optional super-factory filter.  |
| `supportDropshipping` | boolean |  | Filter for support for dropshipping.  |

## Details

Returns a page of 1688 wholesale products that match a keyword. Each item includes price, sales counts, shop details, delivery origin and tags. The only required input is `keyword`.

### Use cases

- Compare wholesale prices for a product type such as Bluetooth earphones across many sellers.
- Find factory-run shops by checking `shop_info.is_factory` and `shop_info.is_super_factory` in the results.
- Rank products by order volume to spot best sellers in a niche.
- Build a sourcing list of item links, images and shop names for a buyer to review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/search/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "蓝牙耳机"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `freeShipping` | boolean | No | Filter for free shipping. |
| `isSuperFactory` | boolean | No | Optional super-factory filter. |
| `moq` | integer | No | Minimum order quantity filter. |
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
        "10333"
      ],
      "delivery_info": {
        "area_from": [
          "福建"
        ]
      },
      "goods_score": "3.0",
      "img": "https://cbu01.alicdn.com/img/ibank/O1CN01HcxZQF1JWzrRozisJ_!!2219639211037-0-cib…",
      "is_ad": false,
      "item_id": 1051199602311,
      "item_repurchase_rate": "",
      "moq": null,
      "price": "5.01",
      "price_info": {
        "origin_price": null,
        "sale_price": "5.01"
      },
      "product_url": "https://detail.1688.com/offer/1051199602311.html",
      "quantity_begin": null
    }
  ],
  "keyword": "蓝牙耳机",
  "page": 1,
  "page_size": 20,
  "sort": "default",
  "total_count": 2000
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].item_id / items[].product_url` | Product ID and the link to its 1688 detail page. |
| `items[].title / items[].img` | Product title and main image URL. |
| `items[].price / items[].price_info.sale_price` | Listed price as a string. `price_info.origin_price` holds the original price and can be `null`. |
| `items[].moq / items[].quantity_begin / items[].quantity_prices[]` | Minimum order quantity and tiered price data. These are `null` or empty when the listing shows no tiers. |
| `items[].sale_info.orders_count / items[].sale_info.sale_quantity_int` | Order count and numeric sales quantity. `sale_info.sale_quantity` is the display text, such as `已售100+件`. |
| `items[].item_repurchase_rate` | Repurchase rate shown on the listing, such as `33%`. It is an empty string when not shown. |
| `items[].goods_score / items[].rating_star` | Score and star rating for the product, as strings. |
| `items[].shop_info.company_name / items[].shop_info.member_id` | Seller company name and the shop's member ID. |
| `items[].shop_info.is_factory / items[].shop_info.is_super_factory / items[].shop_info.factory_inspection` | Flags that show whether the seller is a factory, a super factory, or has a factory inspection. |
| `items[].delivery_info.area_from / items[].tags` | Province and city the goods ship from, and listing tags such as return shipping coverage. |

### Notes

- Set `page` to move through results. `has_next_page` shows whether another page exists, and `total_count` gives the total match count.
- `item_id` is a number. Pass it to [1688 Product Details](/apis/1688/item/detail) for the full listing.
- Use `shop_info.member_id` with [1688 Shop Info](/apis/1688/shop/info) to look up the seller.
- The response echoes `keyword`, `page`, `page_size` and `sort`. The returned item count may differ from `pageSize`.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/search/items.json`](../../../../catalog/models/1688/search/items.json) · Store page: https://www.sandbase.ai/model/1688/search/items
