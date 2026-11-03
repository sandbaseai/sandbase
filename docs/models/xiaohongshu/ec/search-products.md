# Xiaohongshu Shop Product Search API: pricing, parameters and code examples

`xiaohongshu/ec/search-products` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Search products sold in Xiaohongshu (RedNote) shops by keyword, with price, sales and shop info.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/ec/search-products", "keyword": "防晒霜"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/ec/search-products', {'keyword': '防晒霜'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/ec/search-products", {
  "keyword": "防晒霜"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/ec/search-products", sandbase.Params{
	"keyword": "防晒霜",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/ec/search-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number, starting from 1.  |
| `keyword` | string | yes | Search keyword.  |
| `searchId` | string |  | Search ID returned by the first-page response; required when page is greater than 1.  |

## Details

Returns a page of Xiaohongshu (RedNote) shop product cards that match a keyword. Each card has a product ID, a product image, and a deep link into the app. The only required input is `keyword`.

### Use cases

- Build a list of product IDs that appear for a keyword such as `防晒霜` (sunscreen) to track which items the search shows.
- Collect product image URLs for a category to compare how listings look.
- Page through search results to see how many product cards a keyword returns and in what order.
- Check whether a keyword gets rewritten or has recommended terms attached.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/ec/search-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "防晒霜"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | string | No | Page number, starting from 1. |
| `searchId` | string | No | Search ID returned by the first-page response; required when page is greater than 1. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "biz_info": {
      "common": {
        "recommend_info": {
          "extend_tag": 0,
          "recommend_items": [],
          "recommend_type": 0
        },
        "rewrite_word_info": {
          "current_result_word": "",
          "desc": "",
          "new_result_word": "",
          "rewrite_type": 0
        }
      }
    },
    "container": {
      "template": [
        {
          "extra": {
            "column": 2
          },
          "identityId": "cosmos_search_goods_card_single_span-dsl-1.0.0",
          "name": "cosmos_search_goods_card_single_span",
          "type": "dsl",
          "url": "",
          "version": "1.0.0"
        }
      ]
    },
    "hierarchy": {
      "common": {
        "layout": "slotY",
        "load_more": true,
        "pull_refresh": false,
        "slot": 2
      },
      "structure": {
        "root": [
          "cosmos_search_goods_card_1"
        ]
      }
    },
    "module": {
      "data": [
        {
          "card_name": "cosmos_search_goods_card",
          "card_type": "dsl",
          "content": {
            "display_lines": 0,
            "exp_flag_map": {
              "Genuine_Brand_Product": "0",
              "brand_tag": "0",
              "flag": "0",
              "help_farmers": "1",
              "help_farmers_price_prefix": "1",
              "more_search_tag": "0",
              "search_add_recommend_tag": "0",
              "search_green_tag": "1"
            },
            "goods_type": "normal",
            "has_buyer_explain": false,
            "id": "6a0410185a83230001c2e48d",
            "image": [
              {
                "aspect_ratio": 1,
                "height": 540,
                "url": "https://mall-i8.xhscdn.com/arkgoods/1040g0o03203ln7ock8105o1lr5a086somrc9tog?ima…",
                "width": 540
              }
            ],
            "link": "xhsdiscover://goods_detail/6a0410185a83230001c2e48d?listing_image=https%3A%2F%2F…",
            "preload": "{\"type\":\"vision\",\"goods_detail_type\":null,\"original\":null,\"vision\":{\"ver\":\"1.0\",…"
          },
          "id": "cosmos_search_goods_card_1",
          "version": "1.0.0"
        }
      ]
    },
    "ver": "1.0"
  },
  "debug_id": "8ed43963",
  "debug_info": "gAAAAABq6ZFy9HPqVt-sXazStSYG0i_PgAMfRIv-rXZUZhdqQ_cofaGDGjdcNDBS5IALgbbwdQnCAp55…",
  "msg": "成功",
  "next_page": 2,
  "page": 1,
  "search_id": "4264cd9ba8a64b44",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.module.data[].content.id` | Product ID of the card. Use it to look up the product in other APIs. |
| `data.module.data[].id` | Position ID of the card in this result page, such as `cosmos_search_goods_card_1`. The values in `data.hierarchy.structure.root` use the same IDs. |
| `data.module.data[].content.image[].url` | Product image URL. The same object holds `width`, `height` and `aspect_ratio`. |
| `data.module.data[].content.link` | Deep link that opens the product in the Xiaohongshu app. The `listing_image` query value is the encoded image URL. |
| `data.module.data[].content.goods_type` | Product type label. The sample cards all return `normal`. |
| `data.module.data[].content.preload` | JSON string that holds the card's display data. Parse it to read more details. |
| `data.biz_info.common.rewrite_word_info.new_result_word` | Keyword the search was rewritten to. It is empty when no rewrite happened. |
| `data.hierarchy.common.load_more` | Shows whether the platform says more results can be loaded. |
| `page / next_page` | Current page number and the next page number to request. |
| `search_id` | ID of this search. Send it as `searchId` when you request page 2 or later. |

### Notes

- Send `keyword` alone for the first page. Read `search_id` and `next_page` from the response.
- For page 2 and later, send `page` and the `searchId` from the first-page response.
- Pass `content.id` to [Xiaohongshu (RED) Product Detail](/apis/xiaohongshu/app-v2/product-detail) to get details for one product.
- The `preload` field is a JSON string, so parse it before you read it.

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/ec/search-products.json`](../../../../catalog/models/xiaohongshu/ec/search-products.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/ec/search-products
