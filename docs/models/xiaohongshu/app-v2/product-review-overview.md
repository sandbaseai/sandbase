# Xiaohongshu (RED) Product Review Overview API: pricing, parameters and code examples

`xiaohongshu/app-v2/product-review-overview` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns product review statistics and feedback details for a specific item on Xiaohongshu (RED), filtered by SKU identifier and tab type.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/product-review-overview", "sku_id": "669ddd44e05f3700011067ed", "tab": 2}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/product-review-overview', {'sku_id': '669ddd44e05f3700011067ed', 'tab': 2})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/product-review-overview", {
  "sku_id": "669ddd44e05f3700011067ed",
  "tab": 2
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/product-review-overview", sandbase.Params{
	"sku_id": "669ddd44e05f3700011067ed",
	"tab": 2,
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/product-review-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tab` | integer |  | Tab type, default 2 default `2` |
| `sku_id` | string | yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed"  |

## Details

Returns review statistics for one Xiaohongshu (RED) product SKU, including the average score, a count of reviews per star rating, and a short list of recent reviews. It needs a `sku_id` and takes an optional `tab` value.

### Use cases

- Show the average score and star distribution of a SKU on a product dashboard.
- Compare the share of 4 and 5 star reviews across competing SKUs.
- Sample the latest review text and dates for a SKU to check buyer feedback.
- Read the filter and sort options offered for a SKU's review list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/product-review-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sku_id": "669ddd44e05f3700011067ed"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sku_id` | string | Yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed" |
| `tab` | integer | No | Tab type, default 2 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "avgScore": "4.7",
    "avgScoreColorInEightDigit": "FF2442",
    "avgScoreDesc": "Excellent",
    "avgScoreLevel": 0,
    "comment_type": "1",
    "expireFlagMap": {
      "badReviewTag": 2,
      "goods_review": 2,
      "newdetail_review": 0,
      "pingjiabiaoqian": 1,
      "pingjiaerjiyegaiban": 0,
      "review_tag_generic_filter": 0
    },
    "filterStrategyList": [
      {
        "name": "With images",
        "type": 0
      }
    ],
    "purchaseHistoryCount": 333,
    "review_sub_title": "",
    "reviews": [
      {
        "reviewInfo": {
          "anonymous": false,
          "content": "很透亮 透本甲 需要自己修一下甲型",
          "createTimeDesc": "21/04/2026",
          "create_time_desc": "21/04/2026",
          "itemScore": 0,
          "newSkuScore": 0,
          "order_id": "",
          "package_review_id": ""
        },
        "translateFlag": true,
        "userInfo": {
          "anonymous": false,
          "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo325t6skhg56005pkcbam0u1d36tj26qg…",
          "name": "噜噜狗",
          "userId": "af4c0846adcc77e2b9f975a414336",
          "visitorFlag": false
        }
      }
    ],
    "scoreDesc": "评分",
    "scoreToCnt": {
      "1": 0,
      "2": 0,
      "3": 0,
      "4": 71,
      "5": 747
    }
  },
  "debug_id": "d210d3cc",
  "debug_info": "gAAAAABq6ZFpt0ODLPUVxslgz08ZeUu6K3c0jyja05FaaypbWjMxgBaSw9VC6QO7MlHF12utWRpMO3vS…",
  "msg": "ok",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.avgScore` | Average review score for the SKU, returned as a string such as `4.7`. |
| `data.avgScoreDesc` | Text label for the average score, such as `Excellent`. |
| `data.total` | Total number of reviews for the SKU. |
| `data.scoreToCnt` | Count of reviews for each star rating. Keys `1` to `5` are star values. |
| `data.purchaseHistoryCount` | Purchase count shown for the SKU. |
| `data.reviews[].reviewInfo.content` | Text of the review. |
| `data.reviews[].reviewInfo.createTimeDesc / data.reviews[].reviewInfo.create_time_desc` | Review date as a `DD/MM/YYYY` string. |
| `data.reviews[].userInfo.name / data.reviews[].userInfo.userId` | Display name and ID of the reviewer. |
| `data.filterStrategyList[].name` | Names of the review filters, such as `With images` and `Styles`. Each has a numeric `type`. |
| `data.sortStrategyList[].name` | Names of the review sort options, such as `Default` and `Latest`. Each has a numeric `type`. |

### Notes

- `sku_id` is a 24-character hex string, for example `669ddd44e05f3700011067ed`. Find SKUs with [Xiaohongshu (RED) Product Search](/apis/xiaohongshu/app-v2/search-products) or [Xiaohongshu (RED) Product Detail](/apis/xiaohongshu/app-v2/product-detail).
- `tab` defaults to `2`. The request above did not set it.
- The `reviews` list in this response is a short sample. Call [Xiaohongshu (RED) Product Reviews](/apis/xiaohongshu/app-v2/product-reviews) to read the reviews themselves.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/product-review-overview.json`](../../../../catalog/models/xiaohongshu/app-v2/product-review-overview.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/product-review-overview
