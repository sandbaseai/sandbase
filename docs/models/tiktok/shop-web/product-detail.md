# TikTok Shop Product Details API: pricing, parameters and code examples

`tiktok/shop-web/product-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves full product details and page component information from TikTok Shop by product ID. Supports regional filtering across markets such as the US, UK, and Southeast Asia.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/product-detail", "product_id": "1732108663255959373"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/product-detail', {'product_id': '1732108663255959373'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/product-detail", {
  "product_id": "1732108663255959373"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/product-detail", sandbase.Params{
	"product_id": "1732108663255959373",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/product-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"MY"` |
| `seller_id` | string |  | Seller ID (can be empty string) default `""` |
| `product_id` | string | yes | Product ID (required)  |

## Details

Returns the product page layout and component data for one TikTok Shop product. It needs a `product_id` and accepts an optional `region` and `seller_id`.

### Use cases

- Check which page components, such as top reviewed products, related videos and more-from-shop feeds, a TikTok Shop product page loads.
- Confirm that a `product_id` resolves and see the seller ID attached to it.
- Read the page configuration, such as feed titles and fetch settings, that a product page uses in a given region.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/product-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "1732108663255959373"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Product ID (required) |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |
| `seller_id` | string | No | Seller ID (can be empty string) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "components_map": [
      {
        "component_data": {
          "products": []
        },
        "component_name": "top_reviewed_products",
        "component_type": "top_reviewed_products",
        "fe_config": {
          "data_source": {
            "need_fetch_at_first_screen": false,
            "need_product_info": true,
            "need_split_request": true
          },
          "title": "Top reviewed"
        }
      }
    ],
    "global_api_data": {
      "nova_config": {
        "base_resp": {
          "StatusCode": 400,
          "StatusMessage": "region not supported"
        }
      }
    },
    "global_api_data_config": {
      "nova_config": {
        "api": "nova_config",
        "params": {
          "nova_source_key_list": [
            "view_tts_web_seo_source_key_black_friday_settings"
          ],
          "resource_type_list": [
            1
          ]
        }
      }
    },
    "global_data": {
      "product_info": {
        "categories": [],
        "error_code": 0,
        "product_info": {
          "product_id": "1732108663255959373",
          "product_model": {
            "product_id": "1732108663255959373",
            "seller_id": ""
          },
          "seller_id": ""
        }
      }
    },
    "global_fe_config": {
      "page_name": "product_detail"
    }
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code / message` | Status of the call. `0` and `success` mean the request went through. |
| `data.global_data.product_info.product_info.product_id` | The product ID that was looked up. |
| `data.global_data.product_info.product_info.seller_id` | Seller ID tied to the product. It is an empty string in this example, matching the empty `seller_id` request. |
| `data.global_data.product_info.error_code` | Error code for the product lookup. `0` means no error was reported. |
| `data.global_data.product_info.categories` | List of product categories. It is empty in this example. |
| `data.components_map[].component_name / data.components_map[].component_type` | Name and type of each page component, such as `top_reviewed_products`, `video_list` and `feed_list`. |
| `data.components_map[].component_data` | Content of the component. In this example `products` and `related_videos` are empty lists. |
| `data.components_map[].fe_config.title` | Display title for the component, such as `Top reviewed`. The more-from feed uses a `{s_shopName}` placeholder. |
| `data.components_map[].fe_config.data_source.params` | Request settings for feed components, such as `count`, `product_component` and `shop_page`. |
| `data.global_api_data.nova_config.base_resp.StatusMessage` | Status text for the config sub-request. It shows `region not supported` with code `400` in this example. |

### Notes

- The example request sent only `product_id`, so `region` used its default of `MY`. The nova config sub-response reported `region not supported`, so set `region` to a value such as `SG` or `US` if you need that market.
- Valid `region` values are `US`, `GB`, `SG`, `MY`, `PH`, `TH`, `VN` and `ID`.
- If you only have a share link, call [TikTok Shop Product ID by Share Link](/apis/tiktok/shop-web/product-id-by-share-link) first to get the `product_id`.
- For fuller product data, try [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Shop Product Details (V2)](/apis/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.
- [TikTok Shop Product ID by Share Link](/apis/tiktok/shop-web/product-id-by-share-link): Returns the TikTok Shop product identifier extracted from a provided product share link.

---
Machine-readable: [`catalog/models/tiktok/shop-web/product-detail.json`](../../../../catalog/models/tiktok/shop-web/product-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/product-detail
