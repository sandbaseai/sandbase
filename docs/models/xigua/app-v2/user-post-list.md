# Xigua User Post List API: pricing, parameters and code examples

`xigua/app-v2/user-post-list` · data API · Xigua · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of posts from a specific Xigua user account. Supports paginated results using timestamp cursor tokens.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/user-post-list", "user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/user-post-list', {'user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/user-post-list", {
  "user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/user-post-list", sandbase.Params{
	"user_id": "example",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/user-post-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User id  |
| `max_behot_time` | string |  | Maximum behavior time, default empty, pass empty for the first request, pass the max_behot_time returned by the previous request for subsequent requests  |

## Details

Returns a page of posts published by one Xigua user. Each post includes its URL, publish time, like and comment counts, categories and cover frame. The only required input is the user's `user_id`.

### Use cases

- Build a timeline of a Xigua creator's uploads with publish times.
- Compare `digg_count` and `comment_count` across a creator's recent videos.
- Check a creator's account for new uploads by comparing `article_url` values between calls.
- Group a creator's output by `categories` to see what topics they post about.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/user-post-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "1922379661976311"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User id |
| `max_behot_time` | string | No | Maximum behavior time, default empty, pass empty for the first request, pass the max_behot_time returned by the previous request for subsequent requests |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "behot_time": 0,
  "curr_min_index": 0,
  "data": [
    {
      "abstract": "",
      "activity_label": null,
      "aggr_type": 1,
      "anchor_info": null,
      "article_sub_type": 0,
      "article_type": 0,
      "article_url": "https://toutiao.com/group/7323614735999042086/",
      "ban_audio_comment": false,
      "ban_audio_comment_reason": "",
      "ban_comment": 0,
      "ban_danmaku": 0,
      "ban_danmaku_reason": ""
    }
  ],
  "has_more": true,
  "has_more_to_refresh": true,
  "message": "success",
  "total_number": 30
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].article_url / data[].display_url` | Link to the post on toutiao.com. In this response both fields hold the same address. |
| `data[].behot_time` | Time value for the post, shown as a Unix timestamp in seconds (for example `1705161932`). Pass the last item's value as `max_behot_time` to get the next page. |
| `data[].cursor` | The same time value as `behot_time`, in milliseconds (for example `1705161932000`). |
| `data[].digg_count / data[].comment_count / data[].bury_count / data[].danmaku_count` | Counts of likes, comments, buries and danmaku (on-screen comments) for the post. |
| `data[].categories` | List of category labels for the post, such as `video_entertainment` and `video_music`. |
| `data[].first_frame_image.url` | Signed URL of the first frame image of the video. `width` and `height` give its size. |
| `data[].ban_comment / data[].ban_download / data[].ban_share` | Flags for whether commenting, downloading or sharing is restricted on the post. `0` means no restriction is set. |
| `has_more` | Whether more posts are available after this page. |
| `total_number` | Number reported with the page. It is `30` in this response. |
| `message` | Status text for the call. It is `success` when the call works. |

### Notes

- Leave `max_behot_time` empty on the first request. For later pages, send the `behot_time` of the last post you received.
- Check `has_more` before asking for another page.
- To find more details about the account itself, call [Xigua User Profile Details](/apis/xigua/app-v2/user-info).
- To read the comments on a post, use [Xigua Video Comment List](/apis/xigua/app-v2/video-comment-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xigua Single Video Information](/apis/xigua/app-v2/one-video): Returns lightweight single video data and associated related video information from Xigua for a specific post by its unique item ID.
- [Xigua Video Play URL](/apis/xigua/app-v2/one-video-play-url): Returns the direct playback URL for a specific Xigua video using its unique item identifier.
- [Xigua Video Search](/apis/xigua/app-v2/search-video): Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.

---
Machine-readable: [`catalog/models/xigua/app-v2/user-post-list.json`](../../../../catalog/models/xigua/app-v2/user-post-list.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/user-post-list
