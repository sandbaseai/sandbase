# Douyin Creator Video Danmaku List API: pricing, parameters and code examples

`douyin/creator/video-danmaku-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the danmaku bullet comment list for a specified Douyin video. Filter by blocked status and order results by timestamp or engagement with pagination support.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/video-danmaku-list", "item_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/video-danmaku-list', {'item_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/video-danmaku-list", {
  "item_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/video-danmaku-list", sandbase.Params{
	"item_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/creator/video-danmaku-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Items per page (recommended 20, range 1-100) range 1–100 |
| `offset` | integer |  | Offset (for pagination, starting position) range 0– |
| `item_id` | string | yes | Video item ID (required, get from video link or API)  |
| `is_blocked` | boolean |  | Whether to get blocked danmaku (false=normal, true=blocked)  |
| `order_type` | integer |  | Order type (1=time order, 2=other order)  |

## Details

Retrieve danmaku bullet comments for a Douyin video by providing the `item_id`. Supports filtering for blocked comments and sorting via `order_type`.

### Use cases

- Review audience bullet comments for a specific video.
- Filter blocked danmaku entries to moderate video discussions.
- Analyze audience reaction timing across video playback.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/video-danmaku-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7692766887218950514"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video item ID (required, get from video link or API) |
| `count` | integer | No | Items per page (recommended 20, range 1-100) |
| `offset` | integer | No | Offset (for pagination, starting position) |
| `is_blocked` | boolean | No | Whether to get blocked danmaku (false=normal, true=blocked) |
| `order_type` | integer | No | Order type (1=time order, 2=other order) |

### Notes

- `item_id` is required and can be obtained from the video link or video endpoints.
- Pagination is supported through `offset` and `count`, where `count` ranges between 1 and 100.
- Set `is_blocked` to `true` to view blocked comments, or `false` for normal comments.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/video-danmaku-list.json`](../../../../catalog/models/douyin/creator/video-danmaku-list.json) · Store page: https://www.sandbase.ai/model/douyin/creator/video-danmaku-list
