# Xiaohongshu (RED) Product Recommendations API: pricing, parameters and code examples

`xiaohongshu/app-v2/product-recommendations` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns a list of recommended products based on a specified product SKU ID. Supports region-based filtering and cursor pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/product-recommendations", "sku_id": "669ddd44e05f3700011067ed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/product-recommendations', {'sku_id': '669ddd44e05f3700011067ed'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/product-recommendations", {
  "sku_id": "669ddd44e05f3700011067ed"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/product-recommendations", sandbase.Params{
	"sku_id": "669ddd44e05f3700011067ed",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/product-recommendations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region, default "US" default `"US"` |
| `sku_id` | string | yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed"  |
| `cursor_score` | string |  | Pagination cursor, leave empty for first request, pass cursor_score value from previous response for next page default `""` |

## Details

Retrieve recommended products for a specific item on Xiaohongshu (RED) using `sku_id`. Supports cursor-based pagination and region filtering.

### Use cases

- Display related product recommendations on item detail pages.
- Analyze suggested product pairings for e-commerce catalog research.
- Explore item recommendation carousels based on specific SKUs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/product-recommendations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sku_id": "669ddd44e05f3700011067ed"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sku_id` | string | Yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed" |
| `region` | string | No | Region, default "US" |
| `cursor_score` | string | No | Pagination cursor, leave empty for first request, pass cursor_score value from previous response for next page |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "components": [
      {
        "component_data": {
          "component_v_o_list": [
            {
              "card_type": "defaultGoodsComponentVO"
            }
          ]
        }
      }
    ]
  }
}
```

### Notes

- Supply `cursor_score` from the previous response to view subsequent pages, or leave it empty for the initial request.
- The `region` parameter defaults to "US" if not specified.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/product-recommendations.json`](../../../../catalog/models/xiaohongshu/app-v2/product-recommendations.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/product-recommendations
