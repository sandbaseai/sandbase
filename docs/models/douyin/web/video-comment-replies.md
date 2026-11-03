# Douyin Video Comment Replies (Web) API: pricing, parameters and code examples

`douyin/web/video-comment-replies` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns reply data for a specific comment on a Douyin video. Supports pagination controls through cursor and count parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/video-comment-replies", "comment_id": "7354669356632638218", "item_id": "7354666303006723354"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/video-comment-replies', {'comment_id': '7354669356632638218', 'item_id': '7354666303006723354'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/video-comment-replies", {
  "comment_id": "7354669356632638218",
  "item_id": "7354666303006723354"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/video-comment-replies", sandbase.Params{
	"comment_id": "7354669356632638218",
	"item_id": "7354666303006723354",
})
```

Same call via the path form: `POST /v1/api/douyin/web/video-comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number  |
| `cursor` | integer |  | Cursor  |
| `item_id` | string | yes | Video id  |
| `comment_id` | string | yes | Comment id  |

## Details

Returns the replies under one comment on a Douyin video. Each reply has its text, like count, post time, IP location label and author info. You send the video `item_id` and the parent `comment_id`.

### Use cases

- Read the full reply thread under a top comment on a Douyin video.
- Collect replies and their `digg_count` values to see which responses get the most likes.
- Map who replies to whom in a thread using the `reply_to_username` and `reply_to_reply_id` fields.
- Export reply text and `ip_label` values for sentiment or regional analysis of one comment thread.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/video-comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"comment_id": "7354669356632638218", "item_id": "7354666303006723354"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `comment_id` | string | Yes | Comment id |
| `item_id` | string | Yes | Video id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comments": [
    {
      "aweme_id": "7354666303006723354",
      "can_collect": false,
      "can_share": true,
      "cid": "7354723548119139098",
      "comment_reply_total": 288,
      "content_type": 1,
      "create_time": 1712405022,
      "decorated_emoji_info": null,
      "digg_count": 15944,
      "image_list": null,
      "ip_label": "湖南",
      "is_author_digged": false
    }
  ],
  "cursor": 20,
  "extra": {
    "fatal_item_ids": null,
    "now": 1793691155000,
    "scenes": null
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103153235436EC061A2EA00CA8DF6"
  },
  "merge_cursor": "",
  "status_code": 0,
  "total": 288
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[].cid` | ID of the reply itself. |
| `comments[].text` | Text of the reply. Emoji appear as bracketed tags such as `[再见]`. |
| `comments[].create_time` | Time the reply was posted, as a Unix timestamp in seconds. |
| `comments[].digg_count` | Number of likes on the reply. |
| `comments[].reply_id / comments[].root_comment_id` | `reply_id` is the parent comment ID you asked about. `root_comment_id` is the root comment of the thread. |
| `comments[].reply_to_reply_id / comments[].reply_to_username` | The reply this one answers, and the name of that user. `reply_to_reply_id` is `0` when the reply goes directly to the parent comment. The `reply_to_*` fields are missing in that case. |
| `comments[].ip_label` | Location label shown next to the reply, such as a province name. |
| `comments[].label_text` | Badge text on the reply. The value `作者` marks a reply with the author label. It is an empty string when there is no badge. |
| `comments[].user` | Profile info of the reply author, including the `avatar_thumb` image URLs. |
| `total / has_more / cursor` | `total` is the number of replies to the comment (`288` here). `has_more` is `1` when more pages exist. `cursor` is the position after this page (`20` here). |

### Notes

- Both `item_id` (video ID) and `comment_id` (parent comment ID) are required. `comment_id` is the same value as `reply_id` in each returned reply.
- To get the next page, send the returned `cursor` value as the `cursor` parameter. Use `count` to set the page size. Stop when `has_more` is not `1`.
- To list top-level comments and find a `comment_id`, call [Douyin Video Comments (Web)](/apis/douyin/web/video-comments).
- To get a video ID from a share link, use [Douyin Video ID Extractor](/apis/douyin/web/aweme-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/video-comment-replies.json`](../../../../catalog/models/douyin/web/video-comment-replies.json) · Store page: https://www.sandbase.ai/model/douyin/web/video-comment-replies
