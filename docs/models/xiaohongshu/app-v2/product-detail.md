# Xiaohongshu (RED) Product Detail

`xiaohongshu/app-v2/product-detail` · api · Xiaohongshu

Returns detailed product information for a specified SKU on Xiaohongshu (RED). Supply a product SKU identifier along with optional source page context.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/product-detail", "pre_page": "mall_search", "sku_id": "669ddd44e05f3700011067ed", "source": "mall_search"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/product-detail', {'pre_page': 'mall_search', 'sku_id': '669ddd44e05f3700011067ed', 'source': 'mall_search'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/product-detail", {
  "pre_page": "mall_search",
  "sku_id": "669ddd44e05f3700011067ed",
  "source": "mall_search"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/product-detail", sandbase.Params{
	"pre_page": "mall_search",
	"sku_id": "669ddd44e05f3700011067ed",
	"source": "mall_search",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/product-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sku_id` | string | yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed"  |
| `source` | string |  | Source, default "mall_search" default `"mall_search"` |
| `pre_page` | string |  | Previous page, default "mall_search" default `"mall_search"` |

## Details

Query product detail data from Xiaohongshu (RED) by providing a target `sku_id`. Optional parameters include `source` and `pre_page` to set navigation context.

### Use cases

- Look up SKU-level product information from Xiaohongshu (RED) stores.
- Inspect catalog specifications and visual template elements for items.
- Track merchandise details across Xiaohongshu (RED) e-commerce pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/product-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sku_id": "669ddd44e05f3700011067ed"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sku_id` | string | Yes | Product SKU ID (required), e.g. "669ddd44e05f3700011067ed" |
| `source` | string | No | Source, default "mall_search" |
| `pre_page` | string | No | Previous page, default "mall_search" |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "container": {
      "template": [
        {
          "name": "gd_primary_tag_list",
          "type": "dsl",
          "url": "https://www.xiaohongshu.com"
        }
      ]
    }
  }
}
```

### Notes

- `sku_id` is required to specify the target product item.
- `source` defaults to "mall_search" when omitted.
- `pre_page` defaults to "mall_search" when omitted.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/model/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/model/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/model/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/product-detail.json`](../../../../catalog/models/xiaohongshu/app-v2/product-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/product-detail
