# Xigua Video Comment List API: pricing, parameters and code examples

`xigua/app-v2/video-comment-list` · data API · Xigua · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comments for a specified Xigua video. Supports paginating through discussion threads using offset and result count parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/video-comment-list", "item_id": "7354954305222377999"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/video-comment-list', {'item_id': '7354954305222377999'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/video-comment-list", {
  "item_id": "7354954305222377999"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/video-comment-list", sandbase.Params{
	"item_id": "7354954305222377999",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/video-comment-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Quantity, default 20, it is recommended to keep the default.  |
| `offset` | integer |  | Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests  |
| `item_id` | string | yes | Video id  |

## Details

Returns a page of comments for one Xigua video. The only required input is the video's `item_id`. The response also includes the video's author and repost info, plus pagination values.

### Use cases

- Collect viewer comments on a Xigua video for sentiment review.
- Page through the full comment list of a video to archive audience discussion.
- Check whether commenting is turned off for a video before you plan outreach.
- Read the video's author name and title from the same call that returns comments.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/video-comment-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7354954305222377999"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video id |
| `count` | integer | No | Quantity, default 20, it is recommended to keep the default. |
| `offset` | integer | No | Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "at_user_guide_info": null,
  "ban_ai_polish": false,
  "ban_audio_comment": false,
  "ban_comment": false,
  "ban_comment_reason": "写评论",
  "ban_comment_toast": "",
  "ban_face": false,
  "ban_gif_suggest": 0,
  "ban_pic_comment": 0,
  "bottom_tips": null,
  "comment_activity": null,
  "comment_classify_detail": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | The list of comment entries on this page. Each entry has an `id` and a `comment` object. |
| `data[].id` | Numeric ID of the comment entry. |
| `data[].comment.bury_count` | Number of buries (dislikes) on the comment. Other counts and author details sit in the same `comment` object. |
| `has_more` | `true` when more comments remain after this page. |
| `offset` | Offset value to send as `offset` in the next request. In the sample it is `20`. |
| `next_comment_since_ts` | A Unix-style timestamp value (`1793692046` in the sample) tied to the next page of comments. |
| `ban_comment / ban_pic_comment / ban_audio_comment` | Flags that show whether commenting, picture comments or audio comments are blocked for this video. |
| `group.group_id` | ID of the video the comments belong to. It matches the `item_id` you sent. |
| `group.user_name / group.user_id` | Name and numeric ID of the video's author. |
| `repost_params.title` | Title of the video. |

### Notes

- Send `offset` as `0` on the first call. For later pages, pass the `offset` value returned by the previous response and stop when `has_more` is `false`.
- `count` defaults to 20 and the parameter description recommends keeping the default.
- `item_id` is a numeric video ID passed as a string, for example `7354954305222377999`.
- To get the video ID from a keyword, call [Xigua Video Search](/apis/xigua/app-v2/search-video). For video details, call [Xigua Single Video Information](/apis/xigua/app-v2/one-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xigua Single Video Information](/apis/xigua/app-v2/one-video): Returns lightweight single video data and associated related video information from Xigua for a specific post by its unique item ID.
- [Xigua Video Play URL](/apis/xigua/app-v2/one-video-play-url): Returns the direct playback URL for a specific Xigua video using its unique item identifier.
- [Xigua Video Search](/apis/xigua/app-v2/search-video): Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.

---
Machine-readable: [`catalog/models/xigua/app-v2/video-comment-list.json`](../../../../catalog/models/xigua/app-v2/video-comment-list.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/video-comment-list
