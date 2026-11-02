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

Retrieves review overview metrics and user feedback for a product on Xiaohongshu (RED) using `sku_id`. An optional `tab` parameter allows filtering by review category tab.

### Use cases

- Analyze customer feedback and sentiment for specific merchandise.
- Display rating distributions and user reviews within product dashboards.
- Monitor feedback trends across different review category tabs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/product-review-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sku_id": "669ddd44e05f3700011067ed"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sku_id` | string | Yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed" |
| `tab` | integer | No | Tab type, default 2 |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "reviews": [
      {
        "reviewInfo": {
          "content": "很透亮 透本甲 需要自己修一下甲型",
          "createTimeDesc": "21/04/2026",
          "create_time_desc": "21/04/2026",
          "itemScore": 0,
          "newSkuScore": 0
        },
        "userInfo": {
          "name": "噜噜狗"
        }
      }
    ]
  }
}
```

### Notes

- `sku_id` is required to identify the target product SKU.
- `tab` specifies the review tab category and defaults to 2.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/model/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/model/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/model/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/product-review-overview.json`](../../../../catalog/models/xiaohongshu/app-v2/product-review-overview.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/product-review-overview
