# TikTok Shop Product Search API: pricing, parameters and code examples

`tiktok/shop/search-products` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search TikTok Shop products by keyword within a selected region, with offset and page-token pagination. Use it to discover regional products and continue through search results.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop/search-products", "keyword": "iphone"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop/search-products', {'keyword': 'iphone'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop/search-products", {
  "keyword": "iphone"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop/search-products", sandbase.Params{
	"keyword": "iphone",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop/search-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Search result offset. default `0` |
| `region` | string |  | Target region for product search. one of: `US`, `GB`, `FR`, `SG`, `MY`, `PH`, `TH`, `VN`, `ID`; default `"US"` |
| `keyword` | string | yes | Search keyword.  |
| `pageToken` | string |  | Pagination token for the next page.  |

## Details

This API returns TikTok Shop products that match a keyword in a chosen region. Each product has a title, price, rating, sold count, seller and SKU list. It needs a `keyword`. You can also set `region`, `offset` and `pageToken`.

### Use cases

- Find which shops sell a product type, such as phone cases, in the US market.
- Compare listed prices and sold counts across competing products for one keyword.
- Collect product IDs and canonical product page URLs to track a catalog over time.
- Check which sellers appear for a keyword in a given region.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop/search-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "phone case"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `offset` | integer | No | Search result offset. |
| `pageToken` | string | No | Pagination token for the next page. |
| `region` | string | No | Target region for product search. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "has_more": false,
    "load_more_params": {
      "api_source": 2,
      "offset": 0,
      "page_token": ""
    },
    "products": [
      {
        "image": {
          "height": 1290,
          "uri": "tos-useast5-i-omjb5zjo8w-tx/94fdba7fde2e4228816fc2f6a1a9705b",
          "url_list": [
            "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/94fdba7…"
          ],
          "width": 1290
        },
        "product_id": "1731987113638072822",
        "product_marketing_info": {
          "placement_labels": {},
          "placement_labels_ui": {
            "ui_list": []
          }
        },
        "product_price_info": {
          "currency_name": "USD",
          "currency_show_mode": 1,
          "currency_symbol": "$",
          "decimal_point_symbol": ".",
          "promotion_deduction_details": {},
          "raw_origin_price_decimal": "20",
          "raw_origin_price_format": "20.00",
          "sale_price_decimal": "20"
        },
        "rate_info": {
          "review_count": "0",
          "score": 0
        },
        "seller_info": {
          "seller_id": "7496085867160504822",
          "shop_logo": {
            "height": 300,
            "uri": "tos-useast5-i-omjb5zjo8w-tx/587383daaf8a4eaaa4dfb4c8f2b5944f",
            "url_list": [
              "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/587383d…"
            ],
            "width": 300
          },
          "shop_name": "jaidaalize"
        },
        "seo_url": {
          "canonical_url": "https://shop.tiktok.com/us/pdp/pink-white-junk-phone-case-stylish-protective-cov…",
          "slug": "pink-white-junk-phone-case-stylish-protective-cover",
          "type": 2,
          "updated_at": "1768407212939",
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
              "raw_origin_price_decimal": "20",
              "raw_origin_price_format": "20.00",
              "sale_price_decimal": "20"
            },
            "SkuId": "1731987120486257142"
          }
        ],
        "sold_info": {
          "sold_count": 0
        },
        "title": "junk phone case",
        "transparent_image": {
          "height": 500,
          "uri": "tos-maliva-i-o3syd03w52-us/25537fd3c1eaabaa7574d646de2e72ef",
          "url_list": [
            "https://p16-oec-general.ttcdn-us.com/tos-maliva-i-o3syd03w52-us/25537fd3c1eaabaa…"
          ],
          "width": 500
        }
      }
    ],
    "shops": []
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.products[].product_id` | ID of the product, returned as a string. |
| `data.products[].title` | Product title as shown in the shop listing. |
| `data.products[].product_price_info.sale_price_decimal / data.products[].product_price_info.raw_origin_price_decimal` | Sale price and original price as decimal strings. Some products have no `sale_price_decimal`. |
| `data.products[].product_price_info.currency_name / data.products[].product_price_info.currency_symbol` | Currency code and symbol for the prices, such as `USD` and `$`. |
| `data.products[].product_price_info.price_prefix` | Label placed before the price, such as `From`. It appears only on some products. |
| `data.products[].sold_info.sold_count` | Number of units sold for the product. |
| `data.products[].rate_info.score / data.products[].rate_info.review_count` | Average rating score and number of reviews. `review_count` is a string. |
| `data.products[].seller_info.seller_id / data.products[].seller_info.shop_name` | ID and display name of the shop that sells the product. |
| `data.products[].seo_url.canonical_url` | Link to the product page on TikTok Shop. |
| `data.products[].sku_info[].SkuId` | ID of one SKU variant. Each SKU has its own `PriceInfo` block with the same price fields. |

### Notes

- Pass the next page with `offset` and `pageToken`. Read the values to use from `data.load_more_params`.
- `data.has_more` tells you whether more results exist. In this response it is `false` and `data.load_more_params.page_token` is empty.
- `region` accepts `US`, `GB`, `FR`, `SG`, `MY`, `PH`, `TH`, `VN` and `ID`. The default is `US`.
- `data.products[].seo_url.updated_at` is a Unix timestamp in milliseconds, shown as a string.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tiktok/shop/search-products.json`](../../../../catalog/models/tiktok/shop/search-products.json) · Store page: https://www.sandbase.ai/model/tiktok/shop/search-products
