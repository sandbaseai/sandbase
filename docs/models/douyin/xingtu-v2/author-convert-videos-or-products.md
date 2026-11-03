# Douyin Xingtu Creator Conversion Details API: pricing, parameters and code examples

`douyin/xingtu-v2/author-convert-videos-or-products` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns conversion details for a creator's videos or associated products on Douyin Xingtu. Filter by creator ID, item type, time range tier, and industry category.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-convert-videos-or-products", "o_author_id": "7589271892177518598"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-convert-videos-or-products', {'o_author_id': '7589271892177518598'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-convert-videos-or-products", {
  "o_author_id": "7589271892177518598"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-convert-videos-or-products", sandbase.Params{
	"o_author_id": "7589271892177518598",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-convert-videos-or-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default 1  |
| `time_range` | integer |  | Time range tier, default 2  |
| `detail_type` | integer |  | Detail type, 1=videos, 2=products, default 1  |
| `industry_id` | integer |  | Industry ID, 0=unlimited, default 0  |
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Query conversion metrics for a specific creator by passing `o_author_id`. Use `detail_type` to switch between returning converted videos or converted products.

### Use cases

- Review conversion-driving videos associated with a specific Douyin creator.
- Inspect product conversion performance across chosen time ranges and industries.
- Compare video and product conversion data across creator campaigns.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-convert-videos-or-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7589271892177518598"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `page` | integer | No | Page number, default 1 |
| `time_range` | integer | No | Time range tier, default 2 |
| `detail_type` | integer | No | Detail type, 1=videos, 2=products, default 1 |
| `industry_id` | integer | No | Industry ID, 0=unlimited, default 0 |
| `platform_source` | integer | No | Platform source, default 1 |
| `platform_channel` | integer | No | Platform channel, default 1 |

### Notes

- Set `detail_type` to `1` for video conversion details or `2` for product conversion details.
- Filter records across industries using `industry_id`, where `0` represents unlimited.
- Paginate through results using `page`, which defaults to `1`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-convert-videos-or-products.json`](../../../../catalog/models/douyin/xingtu-v2/author-convert-videos-or-products.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-convert-videos-or-products
