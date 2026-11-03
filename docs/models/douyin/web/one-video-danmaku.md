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

Returns danmaku (scrolling comment) data for one Douyin video over a playback window. You send the video `item_id`, the video's total `duration`, and a `start_time` and `end_time` for the window.

### Use cases

- Check how many danmaku comments a Douyin video has in a chosen time range.
- Pull danmaku for one segment of a video to study viewer reactions at that point.
- Confirm that a video has danmaku data before you build an overlay for it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/one-video-danmaku" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"duration": 15134, "end_time": 15133, "item_id": "7355433624046472498", "start_time": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `duration` | integer | Yes | Video total duration |
| `end_time` | integer | Yes | End time |
| `item_id` | string | Yes | Video id |
| `start_time` | integer | Yes | Start time |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "danmaku_list": null,
  "end_time": 32000,
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611031532288DC7ADE63C0205E3F5CF",
    "now": 1793691148000
  },
  "log_pb": {
    "impr_id": "202611031532288DC7ADE63C0205E3F5CF"
  },
  "start_time": 0,
  "status_code": 0,
  "total": 6
}
```

### Response fields

| Field | Meaning |
|---|---|
| `danmaku_list` | List of danmaku comment records for the requested window. It is `null` in this response, so no records came back for this request. |
| `total` | Count of danmaku comments reported for the video. This response shows `6`. |
| `start_time / end_time` | Start and end of the playback window that the response covers. This response shows `0` and `32000`, which differs from the `end_time` of `15133` in the request. |
| `status_code` | Result code of the call. `0` in this response. |
| `extra.fatal_item_ids` | List of video IDs that failed to load. It is empty here. |
| `extra.logid / log_pb.impr_id` | Request identifiers. They carry the same value in this response. |
| `extra.now` | Server time as a 13-digit number, which looks like a Unix timestamp in milliseconds. |

### Notes

- Get the `item_id` from a Douyin video URL with [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id) or [Douyin Video ID Extractor](/apis/douyin/web/aweme-id).
- Get the video `duration` from [Douyin Single Video Details (V1)](/apis/douyin/web/one-video).
- The response `end_time` can differ from the `end_time` you send, so read it to see the window that was returned.
- `danmaku_list` can be `null` even when `total` is above `0`, so check both fields.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/one-video-danmaku.json`](../../../../catalog/models/douyin/web/one-video-danmaku.json) · Store page: https://www.sandbase.ai/model/douyin/web/one-video-danmaku
