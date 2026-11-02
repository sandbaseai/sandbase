# Douyin Creator Content Courses API: pricing, parameters and code examples

`douyin/creator/creator-content-course` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns content development courses from the Douyin creator platform for a specified category. Results can be sorted by recommendation, popularity, or upload date.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-content-course", "category_id": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-content-course', {'category_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-content-course", {
  "category_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-content-course", sandbase.Params{
	"category_id": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-content-course` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Items per page (recommended 24, range 1-100) range 1–100 |
| `order` | integer |  | Order type (1=recommended order, 2=most popular, 3=latest upload)  |
| `offset` | integer |  | Offset (starting position) range 0– |
| `category_id` | integer | yes | Category ID (for more category IDs, please refer to the content creation category interface)  |

## Details

Fetch creator learning courses for a specific category using `category_id`. Supports pagination via `limit` and `offset` alongside ordering through `order`.

### Use cases

- Display educational courses for Douyin video producers.
- Sort creator academy tutorials by popularity or upload recency.
- Build learning directories segmented by category identifier.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-content-course" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_id": "<category_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_id` | integer | Yes | Category ID (for more category IDs, please refer to the content creation category interface) |
| `limit` | integer | No | Items per page (recommended 24, range 1-100) |
| `order` | integer | No | Order type (1=recommended order, 2=most popular, 3=latest upload) |
| `offset` | integer | No | Offset (starting position) |

### Notes

- The `order` parameter accepts 1 for recommended order, 2 for most popular, and 3 for latest upload.
- `limit` supports values from 1 to 100, with 24 recommended.
- Obtain `category_id` values from the content category endpoint.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/model/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/model/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/model/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-content-course.json`](../../../../catalog/models/douyin/creator/creator-content-course.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-content-course
