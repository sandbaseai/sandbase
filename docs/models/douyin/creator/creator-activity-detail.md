# Douyin Creator Activity Details API: pricing, parameters and code examples

`douyin/creator/creator-activity-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specific Douyin creator activity. Queries campaign details using a designated activity identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-activity-detail", "activity_id": "7545335931785450534"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-activity-detail', {'activity_id': '7545335931785450534'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-activity-detail", {
  "activity_id": "7545335931785450534"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-activity-detail", sandbase.Params{
	"activity_id": "7545335931785450534",
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-activity-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `activity_id` | string | yes | Activity ID (obtained from activity list interface)  |

## Details

Look up comprehensive creator activity information by specifying an `activity_id`.

### Use cases

- Review specific Douyin creator campaign information.
- Inspect requirements and guidelines for creator activities.
- Display activity details within creator management dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-activity-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"activity_id": "7545335931785450534"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `activity_id` | string | Yes | Activity ID (obtained from activity list interface) |

### Notes

- Retrieve the required `activity_id` from the creator activity list interface.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.
- [Douyin Creator Content Courses](/apis/douyin/creator/creator-content-course): Returns content development courses from the Douyin creator platform for a specified category.

---
Machine-readable: [`catalog/models/douyin/creator/creator-activity-detail.json`](../../../../catalog/models/douyin/creator/creator-activity-detail.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-activity-detail
