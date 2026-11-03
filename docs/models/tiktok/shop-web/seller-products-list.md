# TikTok Seller Products List API: pricing, parameters and code examples

`tiktok/shop-web/seller-products-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns product listings and SKU details for a designated TikTok Shop merchant. Filter items by seller ID, target region, and pagination parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/seller-products-list", "seller_id": "7495150558072178725"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/seller-products-list', {'seller_id': '7495150558072178725'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/seller-products-list", {
  "seller_id": "7495150558072178725"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/seller-products-list", sandbase.Params{
	"seller_id": "7495150558072178725",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/seller-products-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"US"` |
| `seller_id` | string | yes | Seller ID (required)  |
| `search_params` | string |  | Search parameters for pagination (optional) default `""` |

## Details

Returns a page of product listings for one TikTok Shop seller, including title, brand, price, rating, sold count and SKU prices. It needs a `seller_id`. You can add `region` to pick the storefront.

### Use cases

- Pull a seller's full catalog with prices and SKU IDs into a spreadsheet or database.
- Rank a competitor's products by `sold_count` to find their best sellers.
- Track rating and review counts across one shop's listings.
- Collect product IDs for a seller, then fetch full details for each one.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/seller-products-list" \
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
| `search_params` | string | No | Search parameters for pagination (optional) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "has_more": true,
    "load_more_params": {
      "search_params": "30_WzgwNCw2NDAwMDAwMCwxNzQwNzU2MzI0NzM3LCIxNzMwNzc3NTA3NDM1MDI0NDIxIl0="
    },
    "products": [
      {
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
                "da_info": "{\"activity_name\":\"8\",\"is_fbt\":\"0\",\"delivery_tag\":\"free_shipping\",\"placement\":\"DE…",
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
                "da_info": "{\"placement\":\"FREE_SHIPPING\",\"label_type\":\"PRODUCT_FREE_SHIPPING\",\"has_icon\":\"fa…",
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
                      "da_info": "{\"placement\":\"FREE_SHIPPING\",\"label_type\":\"PRODUCT_FREE_SHIPPING\",\"has_icon\":\"fa…",
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
        },
        "sku_info": [
          {
            "PriceInfo": {
              "currency_name": "USD",
              "currency_show_mode": 1,
              "currency_symbol": "$",
              "decimal_point_symbol": ".",
              "promotion_deduction_details": {},
              "raw_origin_price_decimal": "49",
              "raw_origin_price_format": "49.00",
              "sale_price_decimal": "49"
            },
            "SkuId": "1731738033942728741"
          }
        ],
        "sold_info": {
          "sold_count": 49638
        },
        "title": "klassy Braless Off the Shoulder Top-Fitted Women's Top with built in removeable …",
        "transparent_image": {
          "height": 500,
          "uri": "tos-maliva-i-o3syd03w52-us/a25a5d41042a6c9311174b556b96ddc9",
          "url_list": [
            "https://p16-oec-general.ttcdn-us.com/tos-maliva-i-o3syd03w52-us/a25a5d41042a6c93…"
          ],
          "width": 500
        }
      }
    ]
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.products[].product_id` | ID of the product. Use it to look up full product details. |
| `data.products[].title` | Product title as shown on the listing. |
| `data.products[].brand_info.brand_name` | Brand name set on the product. |
| `data.products[].product_price_info.raw_origin_price_format / data.products[].product_price_info.currency_name` | Listing price as a formatted string, and its currency code. `price_prefix` (for example `From`) shows how the price is labeled. |
| `data.products[].sku_info[].SkuId` | ID of one SKU (variant) of the product. |
| `data.products[].sku_info[].PriceInfo.sale_price_decimal / data.products[].sku_info[].PriceInfo.raw_origin_price_decimal` | Sale price and original price of that SKU, as decimal strings. |
| `data.products[].sold_info.sold_count` | Number of units sold for the product. |
| `data.products[].rate_info.score / data.products[].rate_info.review_count` | Average rating and number of reviews for the product. |
| `data.products[].seo_url.canonical_url` | Public product page URL on TikTok Shop. |
| `data.has_more / data.load_more_params.search_params` | `has_more` tells you whether more products exist. `search_params` holds the token for the next page. |

### Notes

- To get the next page, pass `data.load_more_params.search_params` from the response as `search_params` while `data.has_more` is `true`.
- `seller_id` also appears in each product under `seller_info.seller_id`, next to `shop_name`.
- Product and SKU IDs are long numeric strings. Pass a `product_id` to [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail) for full product data.
- `seo_url.updated_at` is a millisecond-style timestamp string such as `1740633104000`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/apis/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/seller-products-list.json`](../../../../catalog/models/tiktok/shop-web/seller-products-list.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/seller-products-list
