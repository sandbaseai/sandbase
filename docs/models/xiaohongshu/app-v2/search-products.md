# Xiaohongshu (RED) Product Search API: pricing, parameters and code examples

`xiaohongshu/app-v2/search-products` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns Xiaohongshu product search results based on a target keyword. Includes product card details, goods identifiers, stock status, and item titles across paginated listings.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/search-products", "keyword": "OpenAI", "page": 1, "search_id": "", "source": "explore_feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/search-products', {'keyword': 'OpenAI', 'page': 1, 'search_id': '', 'source': 'explore_feed'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/search-products", {
  "keyword": "OpenAI",
  "page": 1,
  "search_id": "",
  "source": "explore_feed"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/search-products", sandbase.Params{
	"keyword": "OpenAI",
	"page": 1,
	"search_id": "",
	"source": "explore_feed",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/search-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, start from 1 default `1` |
| `source` | string |  | Source, default "explore_feed" default `"explore_feed"` |
| `keyword` | string | yes | Search keyword  |
| `search_id` | string |  | Search ID, pass value from first search response for pagination default `""` |

## Details

Returns Xiaohongshu (RED) product search results for a keyword. Each result is a goods card with an ID, images, a product type and an in-app link. The only required input is `keyword`.

### Use cases

- Collect product IDs that match a brand or topic keyword, such as `OpenAI`, for market research.
- Build a product image list for a keyword from the card image URLs.
- Page through all goods cards for a keyword to see which listings appear in Xiaohongshu search.
- Feed goods IDs into a product detail lookup to get full listing data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/search-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `page` | integer | No | Page number, start from 1 |
| `search_id` | string | No | Search ID, pass value from first search response for pagination |
| `source` | string | No | Source, default "explore_feed" |

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
              "search_green_tag": "0"
            },
            "goods_type": "normal",
            "has_buyer_explain": false,
            "id": "6a59958bd09fb60001ea5f84",
            "image": [
              {
                "aspect_ratio": 1,
                "height": 540,
                "url": "https://mall-i8.xhscdn.com/arkgoods/1040g0o0322n5l2ie74005oqsg6fm41bf139pt6g?ima…",
                "width": 540
              }
            ],
            "link": "xhsdiscover://goods_detail/6a59958bd09fb60001ea5f84?listing_image=https%3A%2F%2F…",
            "preload": "{\"type\":\"vision\",\"goods_detail_type\":null,\"original\":null,\"vision\":{\"ver\":\"1.0\",…"
          },
          "id": "cosmos_search_goods_card_1",
          "version": "1.0.0"
        }
      ]
    },
    "ver": "1.0"
  },
  "debug_id": "8f02e548",
  "debug_info": "gAAAAABq6ZFsfRsCe9v0VGe69_flRCKq5veSf0YtxlWyUNUG69JxE2Om-5CeYLOAerCqMOXTIWc29dE0…",
  "msg": "成功",
  "next_page": 2,
  "page": 1,
  "search_id": "3e753135d96b4bf9",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.module.data[].content.id` | Goods ID of the product in this card. Use it to look up the product in other APIs. |
| `data.module.data[].content.goods_type` | Type of the goods listing, for example `normal`. |
| `data.module.data[].content.image[].url` | Product image URL. Sibling fields `width`, `height` and `aspect_ratio` give the image size. |
| `data.module.data[].content.link` | In-app deeplink to the goods detail page, in the `xhsdiscover://goods_detail/<id>` format. |
| `data.module.data[].content.has_buyer_explain` | Boolean flag for whether the card has a buyer explanation. |
| `data.module.data[].content.exp_flag_map` | Map of string flags attached to the card, such as `brand_tag` and `help_farmers`. Values are `"0"` or `"1"`. |
| `data.module.data[].id` | Card position ID in the result list, for example `cosmos_search_goods_card_1`. |
| `data.hierarchy.common.load_more` | Shows whether more results can be loaded. |
| `next_page / page` | The next page number and the current page number. |
| `search_id` | ID of this search. Pass it back to get later pages. |

### Notes

- Pagination: take `search_id` from the first response and send it with `page` set to the `next_page` value.
- `page` starts at 1.
- The goods ID is the segment after `goods_detail/` in `content.link`. It matches `content.id`.
- To get full details for a result, call [Xiaohongshu (RED) Product Detail](/apis/xiaohongshu/app-v2/product-detail) with its goods ID.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/search-products.json`](../../../../catalog/models/xiaohongshu/app-v2/search-products.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/search-products
