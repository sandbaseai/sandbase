# TikTok Video Comments (App V3) API: pricing, parameters and code examples

`tiktok/app-v3/video-comments` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comments for a specific TikTok video using its video ID. Includes comment engagement metrics, timestamps, author details, and supports pagination controls.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/video-comments", "aweme_id": "7350810998023949599"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/video-comments', {'aweme_id': '7350810998023949599'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/video-comments", {
  "aweme_id": "7350810998023949599"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/video-comments", sandbase.Params{
	"aweme_id": "7350810998023949599",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. default `0` |
| `aweme_id` | string | yes | Video id  |

## Details

Returns a page of comments for one TikTok video. You send the video ID as `aweme_id`, and each comment includes its text, like count, reply count, language and creation time.

### Use cases

- Collect the top comments on a TikTok video to review audience reactions.
- Sort comments by `digg_count` to find the most liked replies on a branded post.
- Filter comments by `comment_language` to see which languages a video's audience writes in.
- Export `text` and `create_time` for a sentiment analysis dataset.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7350810998023949599"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "alias_comment_deleted": false,
  "comments": [
    {
      "allow_download_photo": true,
      "author_pin": false,
      "aweme_id": "7350810998023949599",
      "cid": "7350848249060934442",
      "collect_stat": 0,
      "comment_language": "en",
      "comment_post_item_ids": null,
      "content_type": 1,
      "create_time": 1711502748,
      "digg_count": 28916,
      "fold_status": -1,
      "image_list": null
    }
  ],
  "cursor": 20,
  "extra": {
    "api_debug_info": null,
    "fatal_item_ids": null,
    "now": 1793691842000
  },
  "has_filtered_comments": 0,
  "has_more": 1,
  "log_pb": {
    "impr_id": "2026110307440257575558421DBA018FCF"
  },
  "reply_style": 2,
  "status_code": 0,
  "status_msg": "",
  "top_gifts": null,
  "total": 8098
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[].cid` | ID of the comment. Use it to identify a comment across calls. |
| `comments[].text` | The comment text as written by the user. |
| `comments[].digg_count` | Number of likes on the comment. |
| `comments[].reply_comment_total` | Number of replies to the comment. |
| `comments[].create_time` | When the comment was posted, as a Unix timestamp in seconds. |
| `comments[].comment_language` | Language code of the comment, such as `en`. |
| `comments[].share_info.url` | Link to the video with the comment attached for sharing. |
| `comments[].user` | Profile object of the comment author. |
| `comments[].reply_id` | ID of the parent comment. The value `0` means the item is a top-level comment. |
| `total` | Total number of comments reported for the video. |
| `has_more / cursor` | `has_more` is `1` when more comments exist. `cursor` is the value to send for the next page. |

### Notes

- Set `cursor` to `0` for the first page. For the next page, send the `cursor` value from the previous response.
- Use `count` to set how many comments to request per page. The default is `20`.
- To read the replies under a comment, call [TikTok Video Comment Replies](/apis/tiktok/app-v3/video-comment-replies).
- To translate a comment into another language, use [TikTok Content Translation](/apis/tiktok/app-v3/content-translate).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/video-comments.json`](../../../../catalog/models/tiktok/app-v3/video-comments.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/video-comments
