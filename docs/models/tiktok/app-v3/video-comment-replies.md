# TikTok Video Comment Replies API: pricing, parameters and code examples

`tiktok/app-v3/video-comment-replies` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns reply threads for a specific comment on a TikTok video. Queries rely on the video identifier and comment identifier, with support for cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/video-comment-replies", "comment_id": "7327061675382260482", "item_id": "7326156045968067873"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/video-comment-replies', {'comment_id': '7327061675382260482', 'item_id': '7326156045968067873'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/video-comment-replies", {
  "comment_id": "7327061675382260482",
  "item_id": "7326156045968067873"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/video-comment-replies", sandbase.Params{
	"comment_id": "7327061675382260482",
	"item_id": "7326156045968067873",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/video-comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number  |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.  |
| `item_id` | string | yes | Video id  |
| `comment_id` | string | yes | Comment id  |

## Details

Returns the replies under one TikTok comment, with text, like count, creation time and reply targets for each reply. It needs the video ID in `item_id` and the parent comment ID in `comment_id`.

### Use cases

- Read the full reply thread under a popular comment on a video.
- Collect reply text for sentiment or topic analysis of a single discussion.
- Track who replies to whom by using the `reply_to_*` fields.
- Count how many replies a comment has by reading `total`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/video-comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"comment_id": "7327061675382260482", "item_id": "7326156045968067873"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `comment_id` | string | Yes | Comment id |
| `item_id` | string | Yes | Video id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comments": [
    {
      "aweme_id": "7326156045968067873",
      "boost": -119,
      "boost_reason": "multilingual_video_report_cmt_model",
      "cid": "7328166746480870146",
      "collect_stat": 0,
      "comment_language": "en",
      "comment_post_item_ids": null,
      "content_type": 1,
      "create_time": 1706221862,
      "digg_count": 204,
      "fold_status": 0,
      "image_list": null
    }
  ],
  "cursor": 20,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103074402F91A1AB72AA5580194FC",
    "now": 1793691842000
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103074402F91A1AB72AA5580194FC"
  },
  "status_code": 0,
  "status_msg": "",
  "total": 113
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[].cid` | ID of the reply. |
| `comments[].text` | Text of the reply. |
| `comments[].create_time` | Time the reply was posted, as a Unix timestamp in seconds. |
| `comments[].digg_count` | Number of likes on the reply. |
| `comments[].reply_id` | ID of the top-level comment this reply belongs to. It matches the `comment_id` you sent. |
| `comments[].reply_to_reply_id` | ID of the comment or reply this reply answers directly. |
| `comments[].reply_to_username / comments[].reply_to_nickname / comments[].reply_to_userid` | Username, display name and user ID of the person being answered. These keys are missing on some replies. |
| `comments[].comment_language` | Language code of the reply, such as `en`. The value `un` appears when the language is not identified. |
| `comments[].share_info.url` | Share link to the reply on TikTok. |
| `total / has_more / cursor` | `total` is the number of replies in the thread. `has_more` is `1` when more pages exist. `cursor` is the value to send for the next page. |

### Notes

- Get `item_id` from the video URL or a video API such as [TikTok Video Details](/apis/tiktok/app-v3/one-video). Get `comment_id` from the `cid` field of a comment in [TikTok Video Comments (App V3)](/apis/tiktok/app-v3/video-comments).
- For paging, send `cursor` as `0` for the first page. For the next page, send the `cursor` value from the previous response while `has_more` is `1`.
- Use `count` to set how many replies to request per page.
- Each reply has a `user` object with the author's account details. Many of its fields are `null` or empty in this response.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/video-comment-replies.json`](../../../../catalog/models/tiktok/app-v3/video-comment-replies.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/video-comment-replies
