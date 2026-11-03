# TikTok Shop Seller Products (V2) API: pricing, parameters and code examples

`tiktok/shop-web/seller-products-list-v2` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a streamlined product list with SKU details and catalog information from TikTok Shop. Filter listings by seller identifier, region, and search terms.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/seller-products-list-v2", "seller_id": "7495150558072178725"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/seller-products-list-v2', {'seller_id': '7495150558072178725'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/seller-products-list-v2", {
  "seller_id": "7495150558072178725"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/seller-products-list-v2", sandbase.Params{
	"seller_id": "7495150558072178725",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/seller-products-list-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"US"` |
| `seller_id` | string | yes | Seller ID (required)  |
| `searchParams` | string |  | Search parameters (optional) default `""` |

## Details

Returns a page of products for one TikTok Shop seller, including title-level catalog data such as price, rating, brand, images and product page URL. It needs a `seller_id` and accepts an optional `region` and `searchParams`.

### Use cases

- Pull a seller's full product list to monitor which items they sell and at what starting price.
- Compare review counts and ratings across a seller's products to find the best performers.
- Collect product IDs and canonical URLs for a seller, then fetch each product in detail.
- Check which of a seller's products show free shipping labels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/seller-products-list-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"seller_id": "7495150558072178725"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `seller_id` | string | Yes | Seller ID (required) |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |
| `searchParams` | string | No | Search parameters (optional) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "component_data": {
      "BaseResp": {
        "StatusCode": 0,
        "StatusMessage": ""
      },
      "has_more": true,
      "next_search_param": "10_WzE4MjcsNTIwMDAwMDAsMTcyODgzMTA1NDgwMiwiMTcyOTcwNjY4MDQ2OTAwMDIyOSJd",
      "products": [
        {
          "enter_shop_pdp_schema": "aweme://ec/pdp?biz_type=0&fullScreen=false&orderRequestParams=%7B%7D&requestPara…",
          "product": {
            "brand_info": {
              "brand_name": "Klassy Network"
            },
            "image": {
              "height": 1000,
              "uri": "tos-useast5-i-omjb5zjo8w-tx/02e09f245e6d4c0e8cf096fa265a7ecd",
              "url_list": [
                "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/02e09f2…"
              ],
              "width": 1000
            },
            "product_id": "1729599452982906917",
            "product_marketing_info": {
              "placement_labels": {
                "10": [
                  {
                    "da_info": "{\"is_free_shipping\":\"1\",\"delivery_tag\":\"free_shipping\",\"placement\":\"DEFAULT_SPLI…",
                    "default_style": 10,
                    "feature": [
                      {
                        "property_name": "shipping_fee",
                        "property_value": "0"
                      }
                    ],
                    "id": "8",
                    "is_show_icon": true,
                    "text": "Free shipping",
                    "type": 8
                  }
                ],
                "3": [
                  {
                    "da_info": "{\"label_type\":\"PRODUCT_FREE_SHIPPING\",\"has_icon\":\"false\",\"promotion_id\":\"-999\",\"…",
                    "default_style": 10,
                    "feature": [
                      {
                        "property_name": "shipping_fee",
                        "property_value": "0"
                      }
                    ],
                    "id": "8",
                    "is_show_icon": true,
                    "text": "Free shipping",
                    "type": 8
                  }
                ]
              },
              "placement_labels_ui": {
                "ui_list": [
                  {
                    "divider": {
                      "styles": "width:2rpx;height:16rpx;background:rgba(0,0,0,0.12);margin-left:8rpx;margin-righ…",
                      "value": ""
                    },
                    "labels": [
                      {
                        "lom": {
                          "children": [
                            {
                              "children": [],
                              "click_event": {
                                "arguments": {
                                  "schema": ""
                                },
                                "type": ""
                              },
                              "extra": "",
                              "hidden": false,
                              "strictMode": "",
                              "styles": "color:#fff;font-family:TikTokFont;font-size:11rpx;white-space:nowrap;text-overfl…",
                              "type": "Text",
                              "value": "Free shipping"
                            }
                          ],
                          "click_event": {
                            "arguments": {
                              "schema": ""
                            },
                            "type": ""
                          },
                          "extra": "",
                          "hidden": false,
                          "strictMode": "",
                          "styles": "padding:0rpx 4rpx 2rpx 4rpx;background-color:#007B7B;border-radius:4rpx;",
                          "type": "View",
                          "value": ""
                        },
                        "meta": {
                          "da_info": "{\"label_type\":\"PRODUCT_FREE_SHIPPING\",\"has_icon\":\"false\",\"promotion_id\":\"-999\",\"…",
                          "label_style_id": "199",
                          "label_type": "8"
                        }
                      }
                    ],
                    "placement": 3
                  }
                ]
              }
            },
            "product_price_info": {
              "currency_name": "USD",
              "currency_show_mode": 1,
              "currency_symbol": "$",
              "decimal_point_symbol": ".",
              "price_prefix": "From",
              "promotion_deduction_details": {},
              "raw_origin_price_decimal": "49",
              "raw_origin_price_format": "49.00"
            },
            "rate_info": {
              "review_count": "3195",
              "score": 4.7
            },
            "seller_info": {
              "seller_id": "7495150558072178725",
              "shop_logo": {
                "height": 300,
                "uri": "tos-useast5-i-omjb5zjo8w-tx/a7ee1642b0a84ce7b18a9ec60189b3df",
                "url_list": [
                  "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/a7ee164…"
                ],
                "width": 300
              },
              "shop_name": "Klassynetwork",
              "store_blueV_label": {
                "label_image_dark": {
                  "height": 36,
                  "uri": "tos-maliva-i-acgf4d7es9-us/store_blue_v_fixed.png",
                  "url_list": [
                    "https://p16-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/store_blue_v_fix…"
                  ],
                  "width": 36
                },
                "label_image_light": {
                  "height": 36,
                  "uri": "tos-maliva-i-acgf4d7es9-us/store_blue_v_fixed.png",
                  "url_list": [
                    "https://p16-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/store_blue_v_fix…"
                  ],
                  "width": 36
                }
              }
            },
            "seo_url": {
              "canonical_url": "https://shop.tiktok.com/us/pdp/off-the-shoulder-long-sleeve-top-by-klassy-networ…",
              "slug": "off-the-shoulder-long-sleeve-top-by-klassy-network-built-in-bra-padding",
              "type": 2,
              "updated_at": "1740633104000",
              "version": 2
            }
          }
        }
      ],
      "total_product_count": 195
    },
    "component_name": "shop_products",
    "component_type": "shop_products",
    "fe_config": {}
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.component_data.products[].product.product_id` | ID of the product. Use it to look up the product in the product detail APIs. |
| `data.component_data.products[].product.seo_url.canonical_url` | Public TikTok Shop page URL of the product. The `slug` field next to it holds the URL-friendly product name. |
| `data.component_data.products[].product.product_price_info.raw_origin_price_format` | Product price as a formatted number string, for example `49.00`. Read it together with `currency_name` and `currency_symbol`. `price_prefix` holds text such as `From`. |
| `data.component_data.products[].product.rate_info.score / review_count` | Average rating of the product and the number of reviews it has. |
| `data.component_data.products[].product.brand_info.brand_name` | Brand name shown on the product. |
| `data.component_data.products[].product.seller_info.seller_id / shop_name` | ID and display name of the shop that sells the product. |
| `data.component_data.products[].product.image.url_list[]` | Image URLs for the product's main picture. `width` and `height` give its size. |
| `data.component_data.products[].product.product_marketing_info.placement_labels` | Marketing labels on the product, grouped by placement number. Each label has a `text` value such as `Free shipping`. |
| `data.component_data.has_more` | Is `true` when more products are available after this page. |
| `data.component_data.next_search_param` | Cursor string for the next page of results. |

### Notes

- Pass the value of `next_search_param` as `searchParams` in the next request to get the following page. Keep going while `has_more` is `true`.
- `region` accepts `US`, `GB`, `SG`, `MY`, `PH`, `TH`, `VN` and `ID`. The default is `US`.
- Product IDs are long numeric strings. Send them to [TikTok Shop Product Details (V2)](/apis/tiktok/shop-web/product-detail-v2) or [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3) for more data on one product.
- If you only have a shop share link, use [TikTok Shop ID by Share Link](/apis/tiktok/shop-web/shop-id-by-share-link) to find the seller ID.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/apis/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/seller-products-list-v2.json`](../../../../catalog/models/tiktok/shop-web/seller-products-list-v2.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/seller-products-list-v2
