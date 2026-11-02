# Xiaohongshu (RED) Product Reviews API: pricing, parameters and code examples

`xiaohongshu/app-v2/product-reviews` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns customer reviews for a specified Xiaohongshu e-commerce SKU. Supports pagination, sorting strategy selection, and filtering for reviews with images.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/product-reviews", "from_page": "score_page", "page": 0, "share_pics_only": 0, "sku_id": "669ddd44e05f3700011067ed", "sort_strategy_type": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/product-reviews', {'from_page': 'score_page', 'page': 0, 'share_pics_only': 0, 'sku_id': '669ddd44e05f3700011067ed', 'sort_strategy_type': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/product-reviews", {
  "from_page": "score_page",
  "page": 0,
  "share_pics_only": 0,
  "sku_id": "669ddd44e05f3700011067ed",
  "sort_strategy_type": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/product-reviews", sandbase.Params{
	"from_page": "score_page",
	"page": 0,
	"share_pics_only": 0,
	"sku_id": "669ddd44e05f3700011067ed",
	"sort_strategy_type": 0,
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/product-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, start from 0 default `0` |
| `sku_id` | string | yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed"  |
| `from_page` | string |  | From page, default "score_page" default `"score_page"` |
| `share_pics_only` | integer |  | Show reviews with images only, 0=no, 1=yes default `0` |
| `sort_strategy_type` | integer |  | Sort strategy default `0` |

## Details

Retrieve user reviews and ratings for an item by providing `sku_id`. Optional parameters allow sorting, pagination, and filtering only entries with images.

### Use cases

- Analyze customer feedback and satisfaction scores for specific product SKUs.
- Filter and display user reviews containing uploaded photos.
- Monitor recent product comments and sentiment trends over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/product-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sku_id": "669ddd44e05f3700011067ed"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sku_id` | string | Yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed" |
| `page` | integer | No | Page number, start from 0 |
| `from_page` | string | No | From page, default "score_page" |
| `share_pics_only` | integer | No | Show reviews with images only, 0=no, 1=yes |
| `sort_strategy_type` | integer | No | Sort strategy |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "reviews": [
      {
        "reviewInfo": {
          "commentType": 5,
          "content": "非常貌美，就是甲片是薄的，不是很硬，但是我觉得完全没问题，很闪很好看，嬛嬛甲的回购款，很上镜",
          "createTimeDesc": "2025-09-26",
          "itemScore": 5,
          "likeCount": 3,
          "logisticsScore": 5
        },
        "userInfo": {
          "name": "小Yang"
        }
      }
    ]
  }
}
```

### Notes

- `page` begins numbering at 0.
- Set `share_pics_only` to 1 to show only reviews with images, or 0 for all reviews.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/model/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/model/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/model/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/product-reviews.json`](../../../../catalog/models/xiaohongshu/app-v2/product-reviews.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/product-reviews
