# TikTok Shop Product Search API: pricing, parameters and code examples

`tiktok/shop-web/search-products-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches TikTok Shop listings matching a keyword query and returns product details, seller profiles, ratings, and sales figures. Supports region filtering and pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/search-products-list", "offset": 0, "page_token": "", "region": "VN", "search_word": "áo khoác zip bé"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/search-products-list', {'offset': 0, 'page_token': '', 'region': 'VN', 'search_word': 'áo khoác zip bé'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/search-products-list", {
  "offset": 0,
  "page_token": "",
  "region": "VN",
  "search_word": "áo khoác zip bé"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/search-products-list", sandbase.Params{
	"offset": 0,
	"page_token": "",
	"region": "VN",
	"search_word": "áo khoác zip bé",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/search-products-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Offset for pagination (default 0) default `0` |
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"US"` |
| `page_token` | string |  | Page token for next page default `""` |
| `search_word` | string | yes | Search keyword (required)  |

## Details

Returns a page of TikTok Shop products that match a keyword. Each product has an ID, image, price details, rating summary, seller ID and promotion labels. It needs a `search_word` and takes an optional `region`.

### Use cases

- Compare the sale price and original price of products for a keyword such as `coffee`.
- Find which listings carry labels like free shipping or a limited time deal.
- Collect `product_id` and `seller_id` values to feed into product or seller lookups.
- Read the sort and category filter options TikTok Shop offers for a keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/search-products-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_word": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_word` | string | Yes | Search keyword (required) |
| `offset` | integer | No | Offset for pagination (default 0) |
| `page_token` | string | No | Page token for next page |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "filter_quick_options": [
      {
        "displayName": "Sort by",
        "filterGroupType": 8,
        "filterOptionId": "dropdown:8",
        "quickFilterStyle": "dropdown",
        "sectionTitle": "Sort by"
      }
    ],
    "filter_sections": [
      {
        "filterGroupType": 8,
        "hasAllOption": false,
        "id": "Sort by",
        "isColorSection": false,
        "isOnePerLine": true,
        "options": {
          "Best sellers": "ecom_sold_count",
          "Newest": "ecom_publish_time",
          "Price high to low": "ecom_price|DESC",
          "Price low to high": "ecom_price|ASC"
        },
        "title": "Sort by",
        "type": "radio"
      }
    ],
    "has_more": true,
    "load_more_params": {
      "api_source": 2,
      "offset": 30,
      "page_token": "20261103…"
    },
    "products": [
      {
        "image": {
          "height": 800,
          "uri": "tos-useast5-i-omjb5zjo8w-tx/9f0f6d9b9fe7488c8ddc2553270b5c0f",
          "url_list": [
            "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/9f0f6d9…"
          ],
          "width": 800
        },
        "product_id": "1732811383939568017",
        "product_marketing_info": {
          "placement_labels": {
            "1": [
              {
                "da_info": "{\"limited_time_deal\":\"1\",\"placement\":\"DEFAULT\",\"activity_name\":\"4\",\"has_icon\":\"f…",
                "default_style": 12,
                "feature": [
                  {
                    "property_name": "limited_time_deal",
                    "property_value": "true"
                  }
                ],
                "id": "7703764916251969293",
                "is_show_icon": false,
                "status": 102,
                "text": "Limited time deal",
                "type": 4
              }
            ],
            "10": [
              {
                "da_info": "{\"activity_name\":\"8\",\"has_icon\":\"false\",\"promotion_id\":\"-999\",\"is_free_shipping\"…",
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
                "da_info": "{\"promotion_id\":\"-999\",\"delivery_tag\":\"free_shipping\",\"ranking\":\"1\",\"label_type\"…",
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
                          "styles": "color:{{ theme({ \"light\": \"#E10543\", \"dark\": \"#FF576F\" }) }};font-family:TikTokF…",
                          "type": "Text",
                          "value": "Limited time deal"
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
                      "styles": "display:flex;flex-direction:row;align-items:center;justify-content:flex-start;pa…",
                      "type": "View",
                      "value": ""
                    },
                    "meta": {
                      "da_info": "{\"limited_time_deal\":\"1\",\"placement\":\"DEFAULT\",\"activity_name\":\"4\",\"has_icon\":\"f…",
                      "label_style_id": "191",
                      "label_type": "4"
                    }
                  }
                ],
                "placement": 1
              }
            ]
          }
        },
        "product_price_info": {
          "currency_name": "USD",
          "currency_show_mode": 1,
          "currency_symbol": "$",
          "decimal_point_symbol": ".",
          "promotion_deduction_details": {
            "seller_subtotal_deduction": "14.01",
            "seller_subtotal_deduction_decimal": "14.01"
          },
          "raw_origin_price_decimal": "32",
          "raw_origin_price_format": "32.00",
          "sale_price_decimal": "17.99"
        },
        "rate_info": {
          "review_count": "0",
          "score": 0
        },
        "seller_info": {
          "seller_id": "7495008229870306705",
          "shop_logo": {
            "height": 300,
            "uri": "tos-useast5-i-omjb5zjo8w-tx/587383daaf8a4eaaa4dfb4c8f2b5944f",
            "url_list": [
              "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/587383d…"
            ],
            "width": 300
          },
          "shop_name": "kiradbabeta"
        },
        "seo_url": {
          "canonical_url": "https://shop.tiktok.com/us/pdp/1732811383939568017",
          "slug": "",
          "type": 1,
          "updated_at": "0",
          "version": 2
        },
        "sku_info": [
          {
            "PriceInfo": {
              "currency_name": "USD",
              "currency_show_mode": 1,
              "currency_symbol": "$",
              "decimal_point_symbol": ".",
              "promotion_deduction_details": {
                "seller_subtotal_deduction": "14.01",
                "seller_subtotal_deduction_decimal": "14.01"
              },
              "raw_origin_price_decimal": "32",
              "raw_origin_price_format": "32.00",
              "sale_price_decimal": "17.99"
            },
            "SkuId": "1732811411963744657"
          }
        ],
        "sold_info": {
          "sold_count": 1
        },
        "title": "Mushroom Coffee UsDA Organicwith 6Adaptogenic Mushrooms and McT oilInstant Coffe…"
      }
    ],
    "shops": [
      {
        "seller_id": "7495491684454205698",
        "shop_logo": {
          "height": 300,
          "uri": "tos-useast5-i-omjb5zjo8w-tx/2f7d114e9a93411fbbbd1d91ba2ca264",
          "url_list": [
            "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/2f7d114…"
          ],
          "width": 300
        },
        "shop_name": "RYZE Superfoods",
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
      }
    ]
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.products[].product_id` | ID of the product listing. Use it to look up full product details. |
| `data.products[].product_price_info.sale_price_decimal` | Current selling price as a decimal string, for example `17.99`. |
| `data.products[].product_price_info.raw_origin_price_decimal / raw_origin_price_format` | Original price before the discount, as a decimal string and as a formatted string. |
| `data.products[].product_price_info.promotion_deduction_details.seller_subtotal_deduction` | Amount the seller promotion takes off the original price. |
| `data.products[].product_price_info.currency_name / currency_symbol` | Currency code and symbol for the prices, for example `USD` and `$`. |
| `data.products[].rate_info.review_count / score` | Number of reviews and the rating score. Both are `0` for products with no reviews. |
| `data.products[].seller_info.seller_id` | ID of the shop that sells the product. |
| `data.products[].product_marketing_info.placement_labels` | Promotion labels grouped by placement number. Each label has a `text` such as `Free shipping` or `Limited time deal`. |
| `data.has_more` | Is `true` when more results are available for the same query. |
| `data.load_more_params.offset / page_token` | Values to send in the next request to get the following page. |
| `data.filter_sections[].options` | Maps filter names such as `Best sellers` or `Newest` to TikTok Shop filter IDs. |

### Notes

- To get the next page, send `offset` and `page_token` from `data.load_more_params` with the same `search_word`. Stop when `data.has_more` is `false`.
- `region` defaults to `US`. The schema lists `US`, `GB`, `SG`, `MY`, `PH`, `TH`, `VN` and `ID`.
- Pass a `product_id` from this response to [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail) for full product data.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/apis/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/search-products-list.json`](../../../../catalog/models/tiktok/shop-web/search-products-list.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/search-products-list
