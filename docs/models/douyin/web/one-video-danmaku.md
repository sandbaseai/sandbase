# Douyin Video Danmaku API: pricing, parameters and code examples

`douyin/web/one-video-danmaku` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns danmaku comment records for a Douyin video across a specified playback interval. Filter by video ID, total duration, start time, and end time.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/one-video-danmaku", "duration": 15134, "end_time": 15133, "item_id": "7355433624046472498", "start_time": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/one-video-danmaku', {'duration': 15134, 'end_time': 15133, 'item_id': '7355433624046472498', 'start_time': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/one-video-danmaku", {
  "duration": 15134,
  "end_time": 15133,
  "item_id": "7355433624046472498",
  "start_time": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/one-video-danmaku", sandbase.Params{
	"duration": 15134,
	"end_time": 15133,
	"item_id": "7355433624046472498",
	"start_time": 0,
})
```

Same call via the path form: `POST /v1/api/douyin/web/one-video-danmaku` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video id  |
| `duration` | integer | yes | Video total duration  |
| `end_time` | integer | yes | End time  |
| `start_time` | integer | yes | Start time  |

## Details

Retrieve danmaku comment streams for a specific Douyin video using `item_id`. Specify the playback window using `duration`, `start_time`, and `end_time`.

### Use cases

- Analyze viewer real-time reactions across specific video segments.
- Display synchronized danmaku overlays in custom video players.
- Identify audience engagement spikes during video playback.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/one-video-danmaku" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"duration": 15134, "end_time": 15133, "item_id": "7355433624046472498", "start_time": 0}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video id |
| `duration` | integer | Yes | Video total duration |
| `end_time` | integer | Yes | End time |
| `start_time` | integer | Yes | Start time |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "end_time": 32000,
  "start_time": 0,
  "status_code": 0
}
```

### Notes

- Requires `item_id`, `duration`, `start_time`, and `end_time` for each query.
- Time parameters define the video playback window for retrieved danmaku comments.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/one-video-danmaku.json`](../../../../catalog/models/douyin/web/one-video-danmaku.json) · Store page: https://www.sandbase.ai/model/douyin/web/one-video-danmaku
