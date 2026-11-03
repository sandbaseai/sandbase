# Douyin Material Center Related Videos API: pricing, parameters and code examples

`douyin/creator/creator-material-center-related` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns related videos for a specific topic, hot spot, prop, or music entry from the Douyin creator material center. Supports pagination controls and filtering by billboard type.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-material-center-related", "query_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-material-center-related', {'query_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-material-center-related", {
  "query_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-material-center-related", sandbase.Params{
	"query_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-material-center-related` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Items per page (default 20, range 1-100) range 1–100 |
| `offset` | integer |  | Offset (starting position for pagination) range 0– |
| `query_id` | string | yes | Query ID (topic_id / hot_id obtained from billboard endpoints)  |
| `billboard_type` | integer |  | Billboard type  |

## Details

Fetch videos tied to a topic or trending item using the required `query_id` parameter. You can optionally filter by `billboard_type` and paginate results.

### Use cases

- Discover trending videos linked to a specific hot spot or topic ID.
- Analyze content formats performing well under a designated music track or prop.
- Monitor video engagement patterns across Douyin creator billboard categories.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-material-center-related" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query_id": "2488260"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query_id` | string | Yes | Query ID (topic_id / hot_id obtained from billboard endpoints) |
| `limit` | integer | No | Items per page (default 20, range 1-100) |
| `offset` | integer | No | Offset (starting position for pagination) |
| `billboard_type` | integer | No | Billboard type |

### Notes

- Supply a topic ID or hot spot ID in `query_id` obtained from billboard endpoints.
- The `limit` parameter supports values from 1 to 100 with a default of 20.
- Use `offset` to manage pagination offsets through result sets.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-material-center-related.json`](../../../../catalog/models/douyin/creator/creator-material-center-related.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-material-center-related
