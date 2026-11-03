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

Returns the danmaku (bullet comment) list for one Douyin video. Each entry has the comment text, the author, a send time and the position in the video where it appears. The only required input is the video `item_id`.

### Use cases

- Read what viewers wrote at each moment of a video to see how the audience reacted.
- Export all danmaku of a video with author IDs and nicknames for text analysis.
- Pull blocked danmaku with `is_blocked` set to `true` to review what was hidden.
- Find the moments in a video that draw the most comments by grouping entries on `offset_time`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/video-danmaku-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7692766887218950514"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video item ID (required, get from video link or API) |
| `count` | integer | No | Items per page (recommended 20, range 1-100) |
| `is_blocked` | boolean | No | Whether to get blocked danmaku (false=normal, true=blocked) |
| `offset` | integer | No | Offset (for pagination, starting position) |
| `order_type` | integer | No | Order type (1=time order, 2=other order) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "danmaku_list": [
    {
      "create_time": 1793372977,
      "danmaku_id": "7702469458682069818",
      "danmaku_logos": null,
      "digg_count": 0,
      "digg_type": 0,
      "extra": {
        "avatar_url": "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_5eec97d8a90d…",
        "big_thumb": [],
        "decorated_emoji_info": null,
        "item_cover": "https://p5-ex-gddgtc-sign.douyinpic.com/tos-cn-p-0015/oA7CULBmC2veLYherVnlA2EC7v…",
        "item_desc": "双子星是吗@过几天",
        "nickname": "记得我的好",
        "style_list": null,
        "unviewed": false
      },
      "item_id": "7692766887218950514",
      "offset_time": 4530,
      "status": 1,
      "text": "王述涵是你吗",
      "text_extra": null,
      "user_id": "99391254676"
    }
  ],
  "has_more": true,
  "status_code": 0,
  "total_count": 145
}
```

### Response fields

| Field | Meaning |
|---|---|
| `danmaku_list[].text` | The text of the bullet comment. |
| `danmaku_list[].danmaku_id` | ID of the danmaku, returned as a string. |
| `danmaku_list[].offset_time` | Position in the video where the danmaku appears. Values such as `4530` and `6778` suggest milliseconds, but the response does not state the unit. |
| `danmaku_list[].create_time` | Unix timestamp in seconds for when the danmaku was posted. |
| `danmaku_list[].digg_count` | Number of likes on the danmaku. |
| `danmaku_list[].user_id` | ID of the user who sent the danmaku. |
| `danmaku_list[].extra.nickname / danmaku_list[].extra.avatar_url` | Nickname and avatar image URL of the sender. |
| `danmaku_list[].extra.item_desc / danmaku_list[].extra.item_cover` | Caption and cover image URL of the video the danmaku belongs to. |
| `danmaku_list[].status` | Status code of the danmaku. All returned entries have the value `1`. |
| `total_count / has_more` | `total_count` is the total number of danmaku. `has_more` is `true` when more pages remain. |

### Notes

- `item_id` is the numeric video ID, for example `7692766887218950514`. Pass it as a string.
- Page through results with `count` (1 to 100) and `offset`. Keep requesting while `has_more` is `true`.
- Set `order_type` to `1` for time order or `2` for the other order. Set `is_blocked` to `true` to list blocked danmaku.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/video-danmaku-list.json`](../../../../catalog/models/douyin/creator/video-danmaku-list.json) · Store page: https://www.sandbase.ai/model/douyin/creator/video-danmaku-list
