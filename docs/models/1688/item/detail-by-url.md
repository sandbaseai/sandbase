# 1688 Product Details by URL API: pricing, parameters and code examples

`1688/item/detail-by-url` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get 1688 product details from a product URL: prices by quantity, SKUs, MOQ and supplier, in the chosen language.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/item/detail-by-url", "url": "https://detail.1688.com/offer/857511694718.html"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/item/detail-by-url', {'url': 'https://detail.1688.com/offer/857511694718.html'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/item/detail-by-url", {
  "url": "https://detail.1688.com/offer/857511694718.html"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/item/detail-by-url", sandbase.Params{
	"url": "https://detail.1688.com/offer/857511694718.html",
})
```

Same call via the path form: `POST /v1/api/1688/item/detail-by-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | 1688 product URL.  |
| `scene` | string |  | Optional dropshipping pricing scene. one of: `drop_shipping` |
| `language` | string |  | Output language. one of: `en`, `zh`, `ru`, `th`, `pt`, `es`, `tr`, `vi`, `ja`, `ko`; default `"zh"` |
| `optimizeTitle` | boolean |  | Optimize Chinese titles by removing non-core words. default `false` |

## Details

Returns details for one 1688 product, including tiered prices, SKUs with stock, MOQ, shipping data and shop info. It needs a 1688 product URL as `url`. Text can come back in one of ten languages set by `language`.

### Use cases

- Pull tiered prices and MOQ for a 1688 listing to compare sourcing costs.
- Import SKU names, images and stock levels into a dropshipping catalog.
- Check a supplier's shop name and service tags before placing an order.
- Estimate shipping cost per parcel from the SKU package size and weight.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/item/detail-by-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://detail.1688.com/offer/857511694718.html"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | 1688 product URL. |
| `language` | string | No | Output language. |
| `optimizeTitle` | boolean | No | Optimize Chinese titles by removing non-core words. |
| `scene` | string | No | Optional dropshipping pricing scene. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "category_id": 1042207,
  "created_at": 1732704529000,
  "currency": "CNY",
  "delivery_info": {
    "delivery_fee": 2.0,
    "location": "广东省广州市",
    "location_code": "13809818",
    "template_id": "11544552",
    "unit_weight": 0.04
  },
  "detail_url": "https://itemcdn.tmall.com/1688offer/icoss694521994b36ec8ef41ad9e",
  "is_sold_out": false,
  "item_id": 857511694718,
  "main_imgs": [
    "https://cbu01.alicdn.com/img/ibank/O1CN01EGEQPZ2MG03xYboHU_!!3534549799-0-cib.jp…"
  ],
  "mixed_batch": {
    "mix_amount": 5,
    "mix_begin": 0,
    "mix_num": 2
  },
  "moq": 1,
  "offer_unit": "个",
  "price_info": {
    "discount_price": "",
    "origin_price_max": "1.60",
    "origin_price_min": "1.20",
    "price": "1.20",
    "price_max": "1.60",
    "price_min": "1.20"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title` | Product title. Its language follows the `language` parameter. |
| `item_id / product_url` | Numeric 1688 product ID and the canonical product page URL. |
| `moq` | Minimum order quantity for the product. |
| `tiered_price_info.prices[].beginAmount / tiered_price_info.prices[].price` | Price per unit (in `currency`) that applies once the order reaches this quantity. In the sample, the price falls from `1.60` at 1 unit to `1.20` at 2000 units. |
| `price_info.price_min / price_info.price_max` | Lowest and highest listed unit price for the product. |
| `skus[].props_names / skus[].skuid` | Variant name (such as color and model) and the SKU ID for each variant. |
| `skus[].sale_price / skus[].stock` | Unit price and stock count for that SKU. |
| `skus[].package_info` | Length, width, height, weight and volume of the packaged SKU. |
| `sku_props[].prop_name / sku_props[].values[].name` | Variant dimensions (such as color or model) and the option values listed under each. |
| `shop_info.shop_name / shop_info.shop_url` | Supplier shop name and the link to its shop page. |
| `delivery_info.delivery_fee / delivery_info.location` | Shipping fee and the dispatch location of the seller. |
| `sale_info.sale_quantity_year` | Quantity sold over the year. `sale_quantity_90days` can be `null`. |

### Notes

- Copy the `url` from a 1688 product page, in the form `https://detail.1688.com/offer/<item_id>.html`.
- `created_at` and the promotion `start_time` values are Unix timestamps in milliseconds.
- `sku_price_range`, `sale_count` and `discount_price` can be empty, so read tiered prices from `tiered_price_info`.
- To get the product's description images, call [1688 Product Description Images](/apis/1688/item/description-images). For more on the seller, call [1688 Shop Info](/apis/1688/shop/info).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/item/detail-by-url.json`](../../../../catalog/models/1688/item/detail-by-url.json) · Store page: https://www.sandbase.ai/model/1688/item/detail-by-url
