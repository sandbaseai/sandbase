# Taobao Product Details API: pricing, parameters and code examples

`taobao/item/detail` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get a Taobao or Tmall product by item ID: title, images, price, SKU options, delivery and seller details.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/item/detail", "itemId": "920640959876"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/item/detail', {'itemId': '920640959876'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/item/detail", {
  "itemId": "920640959876"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/item/detail", sandbase.Params{
	"itemId": "920640959876",
})
```

Same call via the path form: `POST /v1/api/taobao/item/detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | Unique product identifier on Taobao/Tmall (item ID).  |

## Details

Returns the details of one Taobao or Tmall product: title, images, price ranges, SKU options, delivery info and shop details. It needs one input, the product `itemId`.

### Use cases

- Track the price and promotion price of a competitor's listing across its SKU options.
- Build a product catalog page with the title, gallery images and description images of an item.
- List every color and bundle option of a product with its stock quantity and per-SKU price.
- Match a product to its shop using `seller.shop_id` and `seller.shop_title`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/item/detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "920640959876"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Unique product identifier on Taobao/Tmall (item ID). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "delivery": {
    "area_id": "110101",
    "delivery_fee": "0.00",
    "from": null,
    "to": "东城区"
  },
  "item": {
    "brandName": null,
    "cat_id": null,
    "cat_name": null,
    "desc_imgs": [
      "//img.alicdn.com/imgextra/i3/835893472/O1CN01gbHmUp1bWECvcBSVR_!!835893472.jpg"
    ],
    "desc_url": "//mdetail.tmall.com/templates/pages/desc?id=920640959876",
    "detail_url": "//item.taobao.com/item.htm?id=920640959876",
    "images": [
      "//img.alicdn.com/bao/uploaded/i2/835893472/O1CN01BI37Zo1bWECZtseXB_!!46116860184…"
    ],
    "num_iid": "920640959876",
    "properties": [
      {
        "name": "品牌",
        "value": "BASEUS/倍思"
      }
    ],
    "properties_cut": "品牌 / 型号 / 使用方式 / 售后服务 / 蓝牙版本 / 保修期 / 耳机类别 / 降噪类型 / 套餐类型 / 是否同时支持两部手机 / 颜色分类",
    "sales": null,
    "sku_base": [
      {
        "activity_price": "139",
        "price": "400",
        "promotion_price": "219",
        "propPath": "1627207:38429888978;5919063:6536025",
        "quantity": "200",
        "skuId": "5964173351608"
      }
    ]
  },
  "seller": {
    "evaluates": null,
    "seller_id": null,
    "seller_title": null,
    "shop_icon": "//img.alicdn.com/imgextra/i1/O1CN01pz5irY1bhDKceJor2_!!6000000003496-2-tps-144-1…",
    "shop_id": "70617482",
    "shop_title": "baseus倍思旗舰店",
    "shop_url": "//store.taobao.com/shop/view_shop.htm?user_number_id=",
    "user_type": "C"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item.title` | Product title as shown on the listing. |
| `item.images[] / item.desc_imgs[]` | Image URLs. `images` holds the main gallery. `desc_imgs` holds the images from the description section. The URLs start with `//`. |
| `item.skus.price / item.skus.promotion_price / item.skus.activity_price` | Price summary across all SKUs. Each value is a string and can be a single number or a range such as `219 - 229`. |
| `item.skus.quantity` | Total stock quantity across all SKUs, as a string. |
| `item.sku_base[]` | One row per SKU combination. Each row has `skuId`, `price`, `promotion_price`, `activity_price`, `quantity` and a `propPath` that points to the chosen option values. |
| `item.sku_props[]` | The option groups, such as color or bundle type. Each group has a `name`, a `pid` and a list of `values` with `vid`, `name` and sometimes `image`. |
| `item.properties[]` | Product attributes as `name` and `value` pairs, such as brand and model. |
| `item.detail_url / item.desc_url` | Links to the product page and to the description page. |
| `delivery.delivery_fee / delivery.to` | Delivery fee and the destination area name. `delivery.area_id` holds the matching area code. |
| `seller.shop_id / seller.shop_title / seller.shop_url` | Shop ID, shop name and shop page link of the seller. |

### Notes

- Use the number in the product page URL (`item.htm?id=...`) as `itemId`. The response returns it as `item.num_iid`.
- Each `propPath` is a list of `pid:vid` pairs joined by `;`. Match them to `item.sku_props[].pid` and `item.sku_props[].values[].vid` to find the option names for a SKU.
- Some fields can be `null` for a given item, such as `item.sales`, `item.video` and `seller.seller_id`.
- To find item IDs, use [Taobao Product Search](/apis/taobao/search/items). For customer feedback on the same item, call [Taobao Product Reviews](/apis/taobao/item/reviews) or [Taobao Product Questions](/apis/taobao/item/questions).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/taobao/item/detail.json`](../../../../catalog/models/taobao/item/detail.json) · Store page: https://www.sandbase.ai/model/taobao/item/detail
