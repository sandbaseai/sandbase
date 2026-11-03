# Xigua Single Video Information API: pricing, parameters and code examples

`xigua/app-v2/one-video` · data API · Xigua · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns lightweight single video data and associated related video information from Xigua for a specific post by its unique item ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/one-video", "item_id": "7354954305222377999"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/one-video', {'item_id': '7354954305222377999'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/one-video", {
  "item_id": "7354954305222377999"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/one-video", sandbase.Params{
	"item_id": "7354954305222377999",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video id  |

## Details

Returns data for one Xigua video: like, repost and danmaku counts, author info, categories, and a list of related videos. It needs the video's `item_id`.

### Use cases

- Track the like and `repin_count` totals of a single Xigua video.
- Pull the author's follower count and video total from the same call as the video stats.
- Collect related videos for a post to map which content Xigua groups together.
- Read the category labels of a video to sort clips by topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/one-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7354954305222377999"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "ban_audio_comment": false,
    "ban_audio_comment_reason": "",
    "ban_comment": 0,
    "ban_danmaku": 0,
    "ban_danmaku_reason": "",
    "ban_danmaku_send": 0,
    "ban_share": 0,
    "content": "<p>\n<p>\n<div class=\"custom-video\" data-sp=\"0\" data-vid=\"v0201ag10000co90nejc77u3…",
    "danmaku_count": 36,
    "delete": 0,
    "digg_control": null,
    "digg_count": 42555
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.digg_count / data.video_like_count` | Like count of the video. Both fields show the same value in this response. |
| `data.repin_count` | Count of saves or reposts for the video, as named by the key. |
| `data.danmaku_count` | Number of danmaku (scrolling comments) on the video. |
| `data.ip_info.address` | Location label shown for the post, such as a province name. |
| `data.user_info.name / data.user_info.user_id` | Display name and numeric ID of the video's author. |
| `data.user_info.follower_count / data.user_info.followers_count_str` | Author follower count as a number and as a short display string such as `118万`. |
| `data.user_info.video_total_count` | Total number of videos the author has posted. |
| `data.video_categories[].level1 / level2 / level3` | Category labels for the video, from broad to narrow. |
| `data.related_video_toutiao[].article_url` | Link to each related video page. |
| `data.related_video_toutiao[].digg_count / comment_count / danmaku_count` | Like, comment and danmaku counts for each related video. |
| `data.share_url` | Share link for the video. |

### Notes

- `item_id` is the numeric video ID. It matches `data.group_id` in the response.
- `data.video_play_info` is a JSON string. For a direct playback URL, call [Xigua Video Play URL](/apis/xigua/app-v2/one-video-play-url).
- To read the comments on this video, use [Xigua Video Comment List](/apis/xigua/app-v2/video-comment-list).
- `data.related_video_toutiao[].behot_time` looks like a Unix timestamp in seconds.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xigua Video Play URL](/apis/xigua/app-v2/one-video-play-url): Returns the direct playback URL for a specific Xigua video using its unique item identifier.
- [Xigua Video Search](/apis/xigua/app-v2/search-video): Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.
- [Xigua User Profile Details](/apis/xigua/app-v2/user-info): Returns profile and personal information for a specified Xigua account.

---
Machine-readable: [`catalog/models/xigua/app-v2/one-video.json`](../../../../catalog/models/xigua/app-v2/one-video.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/one-video
