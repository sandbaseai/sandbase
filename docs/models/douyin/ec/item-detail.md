# Douyin Shop Item Details API: pricing, parameters and code examples

`douyin/ec/item-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.025714 per call · **Modes:** sync

Get a Douyin shop product by item ID: title, price, sales, images, specs and shop information.

## Pricing

- **$0.025714 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/ec/item-detail", "itemId": "3734619545235751048"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/ec/item-detail', {'itemId': '3734619545235751048'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/ec/item-detail", {
  "itemId": "3734619545235751048"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/ec/item-detail", sandbase.Params{
	"itemId": "3734619545235751048",
})
```

Same call via the path form: `POST /v1/api/douyin/ec/item-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | The unique ID of the item on Douyin E-commerce.  |

## Details

Returns the details of one Douyin shop product: title, images, sales count, review rating, service guarantees and shop information. It needs one input, the `itemId` of the product on Douyin E-commerce.

### Use cases

- Track the total sales of a competitor's product by checking `model.product.product_sales.total_sales` over time.
- Download the cover, gallery and detail images of a product for catalog research.
- Check which buyer guarantees a product offers, such as freight insurance and 7-day returns.
- Find the shop behind a product and read its name and ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/ec/item-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "3734619545235751048"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | The unique ID of the item on Douyin E-commerce. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "item_type": 6,
  "label": {
    "service_module": {
      "module_list": [
        {
          "content": {
            "content_list": [
              {
                "content": {
                  "title_list": [
                    {
                      "rich_text": {
                        "rich_text_type": 1,
                        "text": {
                          "font_color": "",
                          "text": "运费险"
                        }
                      },
                      "suffix_type": 3
                    }
                  ]
                },
                "content_type": "privilege",
                "suffix_type": 1
              }
            ]
          },
          "module_type": "privilege",
          "title": {
            "title_list": [
              {
                "rich_text": {
                  "rich_text_type": 1,
                  "text": {
                    "text": "保障"
                  }
                },
                "suffix_type": 1
              }
            ]
          }
        }
      ]
    }
  },
  "model": {
    "author_data": {
      "code": -1
    },
    "comment_data": {
      "code": -1
    },
    "content_data": {
      "code": -1
    },
    "hot_content_data": {
      "code": -1
    },
    "material_data": {
      "code": -1
    },
    "product": {
      "product_base": {
        "big_imgs": [
          "https://p3-aio.ecombdimg.com/obj/ecom-shop-material/jpeg_m_7a451b88b93bf8db3dfc0…"
        ],
        "cover": "https://p9-aio.ecombdimg.com/obj/ecom-shop-material/jpeg_m_e0dd74cc60c22ee927610…",
        "images": [
          "https://p9-aio.ecombdimg.com/obj/ecom-shop-material/jpeg_m_e0dd74cc60c22ee927610…"
        ],
        "is_global_shoping": false,
        "is_sui_xin_tui": true,
        "title": "【美白+补水+隔离+防晒乳】四效合一SPF50+PA++++防水(试用七天)",
        "white_background": "https://p3-aio.ecombdimg.com/obj/ecom-shop-material/jpeg_m_91ba9f58b4d1fa2aab283…"
      },
      "product_comment": {
        "comment_label": {
          "good_ratio": "94.9%"
        },
        "good_ratio": 94.94181904535739
      },
      "product_privilege": {
        "privilege_info_label": {
          "privilege_id": 2,
          "privilege_info_detail": [
            {
              "content": "商家已为您投保，退货成功后保险公司赔付一定金额运费至钱包（保单生效以下单为准）",
              "icon": {
                "url_list": [
                  "https://lf3-cm.ecombdstatic.com/obj/eden-cn/nupfupebo/services/FreightInsurance.…"
                ]
              },
              "tag_id": "insurance_freight",
              "title": "运费险"
            }
          ]
        }
      },
      "product_sales": {
        "product_label": {
          "sales_num": 63976,
          "sales_text": "已售"
        },
        "sell_num": 63976,
        "total_sales": 63976
      }
    },
    "promotion_data": {
      "code": -1
    },
    "shop": {
      "shop_base": {
        "platform_source": 4,
        "shop_logo": "https://p6-ecom-qualification-sign.ecombdimg.com/tos-cn-i-6vegkygxbk/69e0ce1b2d9…",
        "shop_name": "原铭护肤专营店"
      },
      "shop_id": "42853938"
    },
    "shop_product_data": {
      "code": -1
    }
  },
  "product_id": "3734619545235751048",
  "promotion_id": "3734619545235751048"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `model.product.product_base.title` | Product title as shown in the shop listing. |
| `model.product.product_base.cover / model.product.product_base.white_background` | Image URLs for the main cover and the white-background product picture. |
| `model.product.product_base.images[] / model.product.product_base.big_imgs[]` | Image URL lists. `images` holds the gallery pictures. `big_imgs` holds taller images. |
| `model.product.product_base.is_sui_xin_tui` | Boolean flag. `true` when the product carries the 小店随心推 (Xiaodian Suixintui) tag, which also appears in `label.service_module`. |
| `model.product.product_sales.total_sales / model.product.product_sales.sell_num` | Number of units sold. Both hold the same value in this response. |
| `model.product.product_comment.good_ratio` | Share of positive reviews as a number. `comment_label.good_ratio` gives the same value as a text string with a percent sign. |
| `model.product.product_privilege.privilege_info_label.privilege_info_detail[].title / content` | Name and description of each buyer guarantee, such as freight insurance, quick refund and 7-day no-reason returns. |
| `model.shop.shop_id` | ID of the shop that sells the product, as a string. |
| `model.shop.shop_base.shop_name / shop_logo` | Name of the shop and the URL of its logo. |
| `product_id` | ID of the requested product, matching the `itemId` you sent. |

### Notes

- Send the product ID as a string in `itemId`. Do not convert it to a number, because the value is long.
- Several blocks in `model`, such as `comment_data`, `content_data` and `promotion_data`, return only `code` set to `-1` and carry no data for this item.
- To read reviews or SKU options, call [Douyin Shop Item Comments](/apis/douyin/ec/item-comments) or [Douyin Shop Item SKUs](/apis/douyin/ec/item-skus).
- To find more products from the same shop, use `model.shop.shop_id` with [Douyin Shop Items](/apis/douyin/ec/shop-items).

### Pricing

$0.025714 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/ec/item-detail.json`](../../../../catalog/models/douyin/ec/item-detail.json) · Store page: https://www.sandbase.ai/model/douyin/ec/item-detail
