# Douyin Activity List API: pricing, parameters and code examples

`douyin/creator/creator-activity-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-activity-list", "end_time": 1, "start_time": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-activity-list', {'end_time': 1, 'start_time': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-activity-list", {
  "end_time": 1,
  "start_time": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-activity-list", sandbase.Params{
	"end_time": 1,
	"start_time": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-activity-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end_time` | integer | yes | End timestamp  |
| `start_time` | integer | yes | Start timestamp  |

## Details

Retrieve Douyin campaign and event activity listings by specifying `start_time` and `end_time` timestamps.

### Use cases

- Track platform events and promotional campaigns within custom date ranges.
- Monitor Douyin campaign participation timelines across specified intervals.
- Audit historical activity records between chosen start and end timestamps.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-activity-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_time": "<end_time>", "start_time": "<start_time>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_time` | integer | Yes | End timestamp |
| `start_time` | integer | Yes | Start timestamp |

### Notes

- Both `start_time` and `end_time` require integer timestamps to define the query window.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/model/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Content Categories](/model/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.
- [Douyin Creator Content Courses](/model/douyin/creator/creator-content-course): Returns content development courses from the Douyin creator platform for a specified category.

---
Machine-readable: [`catalog/models/douyin/creator/creator-activity-list.json`](../../../../catalog/models/douyin/creator/creator-activity-list.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-activity-list
