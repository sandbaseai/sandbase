# Xiaohongshu (RED) Product Recommendations API: pricing, parameters and code examples

`xiaohongshu/app-v2/product-recommendations` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns a list of recommended products based on a specified product SKU ID. Supports region-based filtering and cursor pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/product-recommendations", "sku_id": "669ddd44e05f3700011067ed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/product-recommendations', {'sku_id': '669ddd44e05f3700011067ed'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/product-recommendations", {
  "sku_id": "669ddd44e05f3700011067ed"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/product-recommendations", sandbase.Params{
	"sku_id": "669ddd44e05f3700011067ed",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/product-recommendations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region, default "US" default `"US"` |
| `sku_id` | string | yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed"  |
| `cursor_score` | string |  | Pagination cursor, leave empty for first request, pass cursor_score value from previous response for next page default `""` |

## Details

Returns a list of recommended products for a given Xiaohongshu (RED) product SKU. Each item has an image, a price, sales tags and a pagination cursor. The only required input is `sku_id`.

### Use cases

- Show related products next to an item on a shopping comparison page.
- Collect the price and sales tags of items RED suggests alongside a given product.
- Track which new items appear in the recommendations for a SKU over time using `item_on_shelf_time`.
- Page through the full recommendation list for one SKU to study related products.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/product-recommendations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sku_id": "669ddd44e05f3700011067ed"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sku_id` | string | Yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed" |
| `cursor_score` | string | No | Pagination cursor, leave empty for first request, pass cursor_score value from previous response for next page |
| `region` | string | No | Region, default "US" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "components": [
      {
        "component_data": {
          "component_v_o_list": [
            {
              "card_type": "defaultGoodsComponentVO",
              "data": {
                "base_info": {
                  "buyable": true,
                  "display_lines": 0,
                  "distributor_sub": false,
                  "has_explain": false,
                  "image": {
                    "height": 4032,
                    "url": "https://mall-i10.xhscdn.com/arkgoods/1040g3no31p1407j3i60g5p3mul0k3qndsireqh8?im…",
                    "width": 3024
                  },
                  "in_curation": false,
                  "item_id": "691c17cfccb9e00001b25114",
                  "item_on_shelf_time": 1763448869
                },
                "detail_preload": "{\"type\":\"vision\",\"goods_detail_type\":null,\"original\":null,\"vision\":{\"ver\":\"1.0\",…",
                "empty": false,
                "image_card_display": {},
                "marketing_info": {
                  "price_info": {
                    "expected_price": {
                      "currency": "$",
                      "price": 5.89,
                      "price_str": "$5.89",
                      "price_type": 0
                    }
                  }
                },
                "subscribe_info": {
                  "status": 0
                },
                "tag_strategy_map": {
                  "after_price": [
                    {
                      "able_popup": false,
                      "content": "1533 sold",
                      "tag_content": {
                        "content": "1533 sold"
                      },
                      "tag_content_list": [
                        {
                          "content": "1533 sold"
                        }
                      ],
                      "tag_ext_info": {
                        "sold": "1533"
                      },
                      "tag_type": 1,
                      "type": "sold"
                    }
                  ],
                  "behavior": [
                    {
                      "able_popup": false,
                      "content": "6k added to cart",
                      "style_info": {
                        "cornerRadius": "2",
                        "fontColor": "#000000",
                        "fontColorRgba": "rgba(0, 0, 0, 0.45)",
                        "fontSize": "12",
                        "fontTransparency": "0.45",
                        "frameColor": "#000000",
                        "frameColorRgba": "rgba(0, 0, 0, 0.20)",
                        "frameTransparency": "0.2"
                      },
                      "tag_content": {
                        "content": "6k added to cart",
                        "cornerRadius": "2",
                        "fontColor": "#000000",
                        "fontColorRgba": "rgba(0, 0, 0, 0.45)",
                        "fontSize": "12",
                        "fontTransparency": "0.45",
                        "frameColor": "#000000",
                        "frameColorRgba": "rgba(0, 0, 0, 0.20)"
                      },
                      "tag_content_list": [
                        {
                          "content": "6k added to cart",
                          "cornerRadius": "2",
                          "fontColor": "#000000",
                          "fontColorRgba": "rgba(0, 0, 0, 0.45)",
                          "fontSize": "12",
                          "fontTransparency": "0.45",
                          "frameColor": "#000000",
                          "frameColorRgba": "rgba(0, 0, 0, 0.20)"
                        }
                      ],
                      "tag_type": 1,
                      "type": "add_cart_people_threshold"
                    }
                  ],
                  "upon_title": [
                    {
                      "able_popup": false,
                      "content": "“确实好用，洗了两次头感觉油的没以前那么快了，味道也很好闻，客服回应很快会帮忙备注”",
                      "style_info": {
                        "fontColor": "#9F6A37",
                        "fontColorDark": "#BFA177",
                        "fontColorDarkRgba": "rgba(191, 161, 119, 1)",
                        "fontColorRgba": "rgba(159, 106, 55, 1)",
                        "fontDarkTransparency": "1.0",
                        "fontSize": "12.0",
                        "fontTransparency": "1.0"
                      },
                      "tag_content": {
                        "content": "“确实好用，洗了两次头感觉油的没以前那么快了，味道也很好闻，客服回应很快会帮忙备注”",
                        "fontColor": "#9F6A37",
                        "fontColorDark": "#BFA177",
                        "fontColorDarkRgba": "rgba(191, 161, 119, 1)",
                        "fontColorRgba": "rgba(159, 106, 55, 1)",
                        "fontDarkTransparency": 1,
                        "fontSize": 12,
                        "fontTransparency": 1
                      },
                      "tag_content_list": [
                        {
                          "content": "“确实好用，洗了两次头感觉油的没以前那么快了，味道也很好闻，客服回应很快会帮忙备注”",
                          "fontColor": "#9F6A37",
                          "fontColorDark": "#BFA177",
                          "fontColorDarkRgba": "rgba(191, 161, 119, 1)",
                          "fontColorRgba": "rgba(159, 106, 55, 1)",
                          "fontDarkTransparency": 1,
                          "fontSize": 12,
                          "fontTransparency": 1
                        }
                      ],
                      "tag_ext_info": {
                        "commentId": "572376817738793668",
                        "reviewerAvatar": "https://sns-avatar-qc.xhscdn.com/avatar/62580edcd24df9e45cc36aaa.jpg?imageView2/…"
                      },
                      "tag_type": 1,
                      "type": "positive_review_with_profile"
                    }
                  ]
                },
                "track": {
                  "cursor_score": 1793692009,
                  "model_type": "sku",
                  "track_id": "dssmu2i_dssm@52f30abc-2654-400a-b238-ca79a07febc8"
                }
              },
              "empty": false
            }
          ],
          "empty": false,
          "extra_info": {
            "title": "You may also like"
          },
          "general_param": "{\"biz_name\":\"goods_detail\",\"cursor_score\":\"\",\"is_pull_down\":false,\"region\":\"US\",…",
          "has_more": true,
          "total": 0
        },
        "component_name": "DefaultMixCardComponentV2"
      }
    ],
    "result": {
      "success": true
    }
  },
  "debug_id": "663a80bf",
  "debug_info": "gAAAAABq6ZFqoJ2G_JKLzuCuRBvUzFLdBLhe4f3FG8VNAHNQaDMVjp7RVtDWcxwHHMsXR-rAsPUfqkcg…",
  "msg": "ok",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.components[].component_data.component_v_o_list[]` | The list of recommended product cards. Each entry is one product. |
| `data.components[].component_data.component_v_o_list[].data.base_info.item_id` | ID of the recommended product. |
| `data.components[].component_data.component_v_o_list[].data.base_info.image.url` | Product image URL. `width` and `height` sit next to it in the same object. |
| `data.components[].component_data.component_v_o_list[].data.base_info.buyable` | Whether the product can be bought. |
| `data.components[].component_data.component_v_o_list[].data.base_info.item_on_shelf_time` | Unix timestamp in seconds for when the item went on shelf. |
| `data.components[].component_data.component_v_o_list[].data.marketing_info.price_info.expected_price.price / price_str / currency` | Price as a number, as a display string such as `$5.89`, and the currency symbol. |
| `data.components[].component_data.component_v_o_list[].data.tag_strategy_map.after_price[].content` | Sales text shown after the price, such as `1533 sold` or `5005 sold by shop`. The `type` field names the tag kind, for example `sold` or `seller_sales`. |
| `data.components[].component_data.component_v_o_list[].data.tag_strategy_map.upon_title[].content` | Review quote shown above the title on some items. It can be in Chinese. |
| `data.components[].component_data.component_v_o_list[].data.track.cursor_score` | Cursor value for this item. Use the value from the last item to request the next page. |
| `data.components[].component_data.has_more` | Shows whether more recommendations are available. |

### Notes

- Pass the last item's `track.cursor_score` as `cursor_score` to get the next page. Leave `cursor_score` empty on the first request.
- `has_more` is `true` when another page exists.
- `region` defaults to `US`. Prices in the sample response are in `$`.
- Call [Xiaohongshu (RED) Product Detail](/apis/xiaohongshu/app-v2/product-detail) to look up a recommended product, or [Xiaohongshu (RED) Product Reviews](/apis/xiaohongshu/app-v2/product-reviews) for its reviews.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/product-recommendations.json`](../../../../catalog/models/xiaohongshu/app-v2/product-recommendations.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/product-recommendations
