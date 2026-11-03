# Xiaohongshu (RED) Product Detail API: pricing, parameters and code examples

`xiaohongshu/app-v2/product-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns detailed product information for a specified SKU on Xiaohongshu (RED). Supply a product SKU identifier along with optional source page context.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/product-detail", "pre_page": "mall_search", "sku_id": "669ddd44e05f3700011067ed", "source": "mall_search"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/product-detail', {'pre_page': 'mall_search', 'sku_id': '669ddd44e05f3700011067ed', 'source': 'mall_search'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/product-detail", {
  "pre_page": "mall_search",
  "sku_id": "669ddd44e05f3700011067ed",
  "source": "mall_search"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/product-detail", sandbase.Params{
	"pre_page": "mall_search",
	"sku_id": "669ddd44e05f3700011067ed",
	"source": "mall_search",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/product-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sku_id` | string | yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed"  |
| `source` | string |  | Source, default "mall_search" default `"mall_search"` |
| `pre_page` | string |  | Previous page, default "mall_search" default `"mall_search"` |

## Details

Returns the detail page data for one Xiaohongshu (RED) product SKU. The response includes the image carousel, the style and size variants with their SKU IDs and stock status, the seller shop button, and the page layout. You pass a `sku_id`.

### Use cases

- Pull all color and size variants of a product, with each variant's `sku_id` and stock status.
- Collect product image URLs and image sizes for a catalog or comparison sheet.
- Find the seller ID of a shop from the product's shop link.
- Check the displayed deal price and currency data for an overseas listing.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/product-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sku_id": "669ddd44e05f3700011067ed"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sku_id` | string | Yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed" |
| `pre_page` | string | No | Previous page, default "mall_search" |
| `source` | string | No | Source, default "mall_search" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "biz_info": {
      "common": {
        "bottom_bar": {
          "btn_benefit": 0,
          "coupon_infos": [],
          "deal_in_price_template_id": [],
          "delivery_info": {
            "able_to_delivery": true
          },
          "func_buttons": [
            {
              "id": "6405c8953a4a690001a944f6",
              "image": "https://sns-avatar-qc.xhscdn.com/avatar/seller_68d9032542140f000105a04f?imageVie…",
              "link": "xhsdiscover://shop_detail?seller_id=6405c8953a4a690001a944f6&general_param=%7B%2…",
              "name": "Shop",
              "type": "seller"
            }
          ],
          "half_shadow_height": "0.75",
          "instant_buy_jump_page": "checkoutPage",
          "is_single_variant": false
        },
        "common": {
          "app_language": "en",
          "auto_refresh": false,
          "cache_timestamp_ms": 1793692008923,
          "current_content_language": "en",
          "deal_price": 599,
          "extra_info": "{\"showShippingDiscountCoupon\":false,\"user_ip_country\":\"SG\",\"is_rds\":true,\"price_…",
          "fancy_ui": "2",
          "goods_detail_big_video": "big"
        },
        "nav_bar": {
          "has_followed": true,
          "has_more_button": true,
          "has_placeholder": true,
          "is_followed": false,
          "nav_bar_type": "default",
          "share_info": {
            "component_name": "goods_detail",
            "content": "",
            "extension": {
              "friend": "{\"type\":\"goodsDetail\",\"avatar\":\"https://sns-avatar-qc.xhscdn.com/avatar/seller_6…",
              "items": [
                {
                  "title": "Report",
                  "type": "report",
                  "url": "https://www.xiaohongshu.com/evaluation/tip-offs?goodsId=669ddd44e05f3700011067ed"
                }
              ]
            },
            "extra": "{\"link\":\"xhsdiscover://mini_goods_detail/669ddd44e05f3700011067ed?trade_ext=eyJj…",
            "image": "https://mall-i10.xhscdn.com/arkgoods/1040g0o031tjjss2l6o005p00kpfqhaj8r09rlu8?im…",
            "imageurl": "https://mall-i10.xhscdn.com/arkgoods/1040g0o031tjjss2l6o005p00kpfqhaj8r09rlu8?im…",
            "instance_id": "669ddd44e05f3700011067ed",
            "is_from_buyer": false
          },
          "title": "更多功能",
          "translation_info": {
            "target_content_language": "zh-Hans",
            "translation_state": 0
          }
        }
      }
    },
    "container": {
      "template": [
        {
          "extra": {
            "column": 2
          },
          "identityId": "gd_primary_tag_list-dsl-1.0.0",
          "name": "gd_primary_tag_list",
          "type": "dsl",
          "url": "https://www.xiaohongshu.com",
          "version": "1.0.0"
        }
      ]
    },
    "hierarchy": {
      "common": {
        "layout": "autoY",
        "load_more": false,
        "pull_refresh": false
      },
      "structure": {
        "atmosphere_1": [
          "oversea_promotion_atmosphere_1"
        ],
        "gd_comments_1": [
          "gd_show_notes_comment_v3_1"
        ],
        "gd_shop_1": [
          "gd_shop_header_v2_en_1"
        ],
        "primary_1": [
          "atmosphere_1"
        ],
        "primary_content_1": [
          "gd_price_view_oversea_1"
        ],
        "root": [
          "header_carousel_1"
        ]
      }
    },
    "module": {
      "data": [
        {
          "card_attributes": {
            "padding": {
              "bottom": 12,
              "top": 12
            }
          },
          "card_name": "header_carousel",
          "card_type": "native",
          "content": {
            "asset": [
              {
                "asset_content": {
                  "list": [
                    {
                      "container": {
                        "ratio": 1
                      },
                      "image": {
                        "goods_search_route": "xhsdiscover://search/result?mode=goods_image&source=goods_detail&keyword=%E3%80%…",
                        "height": 3024,
                        "image_search_route": "xhsdiscover://search/imagesearch?source=goods_detail&file_id=arkgoods/1040g0o031…",
                        "url": "https://mall-i10.xhscdn.com/arkgoods/1040g0o031tjjss2l6o005p00kpfqhaj8r09rlu8?im…",
                        "width": 3024
                      },
                      "type": "image"
                    }
                  ],
                  "tab_name": "Images"
                },
                "asset_type": "image"
              }
            ],
            "header_ext": {},
            "style": {
              "sku_list": [
                {
                  "header_image": {
                    "height": 3024,
                    "image_id": "arkgoods/1040g3no31guespk73c0g5p00kpfqhaj855vkf2g",
                    "thumbnail": "https://qimg.xiaohongshu.com/arkgoods/1040g3no31guespk73c0g5p00kpfqhaj855vkf2g?i…",
                    "url": "https://mall-i10.xhscdn.com/arkgoods/1040g3no31guespk73c0g5p00kpfqhaj855vkf2g?im…",
                    "width": 3024
                  },
                  "sku_id": "669ddd44e05f3700011067ed",
                  "stock_status": 1,
                  "value": "H03",
                  "variants": [
                    {
                      "id": "5a60c42f69bd891ed8939bc0",
                      "name": "Size",
                      "value": "m"
                    }
                  ]
                }
              ],
              "spec_total_title": "All 3 styles"
            }
          },
          "id": "header_carousel_1",
          "version": "1.0.0"
        }
      ]
    },
    "ver": "1.0"
  },
  "debug_id": "e6a13d04",
  "debug_info": "gAAAAABq6ZFpP58s01s094CiGXHecQFAIdQjFncKr_zSBov7iLwAO41HEb7KwT4JOOMlOAS-2yuSjuVQ…",
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.module.data[].card_name` | Name of each page card, such as `header_carousel`. Use it to find the card you need in the list. |
| `data.module.data[].content.asset[].asset_content.list[].image.url` | Image URL for each carousel item. The `Images` tab holds product photos and the `Styles` tab holds one image per variant. |
| `data.module.data[].content.asset[].asset_content.list[].sku_id` | SKU ID of the variant shown in the `Styles` tab. |
| `data.module.data[].content.style.sku_list[].sku_id` | SKU ID of each variant of this product. |
| `data.module.data[].content.style.sku_list[].stock_status` | Stock flag for the variant. The value `1` appears for the variants in this response. |
| `data.module.data[].content.style.sku_list[].variants[].name / data.module.data[].content.style.sku_list[].variants[].value` | Variant attribute name and its value, for example `Size` with `m` or `Color` with `H03`. |
| `data.biz_info.common.bottom_bar.func_buttons[]` | Bottom bar buttons for `seller`, `service` and `cart`. The `seller` entry has the seller `id`, shop avatar `image` and shop `link`. |
| `data.biz_info.common.common.deal_price` | Deal price value for the product. The currency shows in the `extra_info` string as `price_currency_origin`, which is `GBP` here. |
| `data.biz_info.common.bottom_bar.delivery_info.able_to_delivery` | Whether delivery is available (`true` or `false`). |
| `data.container.template[].name` | Names of the page templates used to render the detail page, such as `gd_price_view_oversea`. |

### Notes

- Take `sku_id` from a product search result. [Xiaohongshu (RED) Product Search](/apis/xiaohongshu/app-v2/search-products) is a good starting point.
- SKU IDs are 24-character hex strings. Variants of one product have close but different IDs.
- `source` and `pre_page` both default to `mall_search` and can be left out.
- For reviews of the same product, call [Xiaohongshu (RED) Product Reviews](/apis/xiaohongshu/app-v2/product-reviews).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/product-detail.json`](../../../../catalog/models/xiaohongshu/app-v2/product-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/product-detail
