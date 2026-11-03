# 1688 Image Search API: pricing, parameters and code examples

`1688/search/by-image` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Find 1688 wholesale products that match an image URL, with prices, minimum order quantity and supplier info. Sort and filter by price, MOQ, factory, verified supplier and shipping.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/search/by-image", "imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01Z5b6Ax1Bs2nVv6E3n_!!2216226597326-0-cib.jpg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/search/by-image', {'imgUrl': 'https://cbu01.alicdn.com/img/ibank/O1CN01Z5b6Ax1Bs2nVv6E3n_!!2216226597326-0-cib.jpg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/search/by-image", {
  "imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01Z5b6Ax1Bs2nVv6E3n_!!2216226597326-0-cib.jpg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/search/by-image", sandbase.Params{
	"imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01Z5b6Ax1Bs2nVv6E3n_!!2216226597326-0-cib.jpg",
})
```

Same call via the path form: `POST /v1/api/1688/search/by-image` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `moq` | integer |  | Minimum order quantity filter.  |
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Product sort order. one of: `default`, `sales`, `price_up`, `price_down`; default `"default"` |
| `imgUrl` | string | yes | Image URL or image reference returned by Image Conversion. Convert external images for the selected search target before searching.  |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |
| `priceEnd` | string |  | Maximum price filter in CNY.  |
| `isFactory` | boolean |  | Filter by factory status.  |
| `newArrival` | boolean |  | Filter for new products.  |
| `priceStart` | string |  | Minimum price filter in CNY.  |
| `freeShipping` | boolean |  | Filter for free shipping.  |
| `verifiedSupplier` | boolean |  | Filter for verified sellers.  |
| `supportDropshipping` | boolean |  | Filter for support for dropshipping.  |

## Details

Returns 1688 wholesale products that look like a given image. It needs an image URL in `imgUrl`. Each result has the minimum order quantity, sales counts and shop details.

### Use cases

- Find other 1688 sources for a product you already see on another store.
- Compare MOQ across factories that make the same item.
- Build a shortlist of suppliers that match a product photo, filtered to factories only.
- Check how well similar products sell by comparing order counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/search/by-image" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01dVDdAa1g2z0YPmnXe_!!2218348464085-0-cib.jpg"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `imgUrl` | string | Yes | Image URL or image reference returned by Image Conversion. Convert external images for the selected search target before searching. |
| `freeShipping` | boolean | No | Filter for free shipping. |
| `isFactory` | boolean | No | Filter by factory status. |
| `moq` | integer | No | Minimum order quantity filter. |
| `newArrival` | boolean | No | Filter for new products. |
| `page` | integer | No | Page number, starting at 1. |
| `pageSize` | integer | No | Number of items requested per page. The returned count may differ. |
| `priceEnd` | string | No | Maximum price filter in CNY. |
| `priceStart` | string | No | Minimum price filter in CNY. |
| `sort` | string | No | Product sort order. |
| `supportDropshipping` | boolean | No | Filter for support for dropshipping. |
| `verifiedSupplier` | boolean | No | Filter for verified sellers. |

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
        "1036898"
      ],
      "delivery_info": {
        "area_from": [
          "江苏"
        ]
      },
      "goods_score": null,
      "img": "https://cbu01.alicdn.com/img/ibank/O1CN01izT11Z1IAizOygYsq_!!934370853-0-cib.jpg",
      "is_ad": true,
      "item_id": 1056868355487,
      "item_repurchase_rate": "79%",
      "moq": 1,
      "price": "22.8",
      "price_info": {
        "origin_price": null,
        "sale_price": "22.8"
      },
      "product_url": "https://detail.1688.com/offer/1056868355487.html",
      "quantity_begin": 1
    }
  ],
  "keyword": "",
  "page": 1,
  "page_size": 20,
  "sort": "default",
  "total_count": 700
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].item_id / items[].product_url` | The 1688 offer ID and the link to the product page. The ID is also the number at the end of the URL. |
| `items[].title / items[].img` | Product title and main image URL. The title is in Chinese. |
| `items[].moq / items[].quantity_begin` | Minimum order quantity for the product. |
| `items[].sale_info.orders_count` | Number of orders for the product. |
| `items[].sale_info.sale_quantity_int` | Units sold as an integer. `sale_quantity` holds the same count as a string. |
| `items[].item_repurchase_rate` | Repurchase rate shown as a percent string, for example `79%`. |
| `items[].shop_info.company_name / items[].shop_info.member_id` | Name of the selling company and its member ID. |
| `items[].shop_info.is_factory / items[].shop_info.is_super_factory / items[].shop_info.factory_inspection` | Flags that show whether the shop is marked as a factory, a super factory, or has a factory inspection. |
| `items[].is_ad` | `true` when the result is an ad placement. |

### Notes

- Set `page` and `pageSize` to page through results. Read `has_next_page` to see if more pages exist, and `total_count` for the total number of matches.
- `imgUrl` should be an image URL or a reference from Image Conversion. Convert external images first.
- `items[].category_path` is a list of category IDs as strings.
- For full product data on a result, pass its `item_id` to [1688 Product Details](/apis/1688/item/detail).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/search/by-image.json`](../../../../catalog/models/1688/search/by-image.json) · Store page: https://www.sandbase.ai/model/1688/search/by-image
