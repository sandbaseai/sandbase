# Douyin Xingtu Ranking List Catalog API: pricing, parameters and code examples

`douyin/xingtu-v2/ranking-list-catalog` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the ranking list catalog from Douyin Xingtu, including available leaderboard dates and qualifiers. Accepts optional business scene and classification code filters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/ranking-list-catalog", "biz_scene": "douyin_flow_split_video_author_ranks", "codes": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/ranking-list-catalog', {'biz_scene': 'douyin_flow_split_video_author_ranks', 'codes': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/ranking-list-catalog", {
  "biz_scene": "douyin_flow_split_video_author_ranks",
  "codes": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/ranking-list-catalog", sandbase.Params{
	"biz_scene": "douyin_flow_split_video_author_ranks",
	"codes": "",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/ranking-list-catalog` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `codes` | string |  | Classification codes, default is empty string default `""` |
| `biz_scene` | string |  | Business scene default `"douyin_flow_split_video_author_ranks"` |

## Details

Fetch available leaderboard categories and dates across Douyin Xingtu. Filter the catalog using `biz_scene` and classification `codes`.

### Use cases

- Discover available Douyin Xingtu creator ranking categories and qualifiers.
- Look up supported leaderboard dates for specific business scenes.
- Map qualifier identifiers to corresponding ranking list display names.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/ranking-list-catalog" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `codes` | string | No | Classification codes, default is empty string |
| `biz_scene` | string | No | Business scene |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "catalog": {
    "18": [
      {
        "date": "20260930",
        "display_name": "头部必选榜",
        "qualifier_id": "627"
      }
    ]
  }
}
```

### Notes

- Filter rankings by classification codes using `codes`, which defaults to an empty string.
- Specify the target business context with `biz_scene`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/ranking-list-catalog.json`](../../../../catalog/models/douyin/xingtu-v2/ranking-list-catalog.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/ranking-list-catalog
