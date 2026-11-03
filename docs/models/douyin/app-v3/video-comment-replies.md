# Douyin Video Comment Replies (App V3) API: pricing, parameters and code examples

`douyin/app-v3/video-comment-replies` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns reply comments for a specific comment on a Douyin video based on the video ID and comment ID, with support for cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/video-comment-replies", "comment_id": "example", "item_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/video-comment-replies', {'comment_id': 'example', 'item_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/video-comment-replies", {
  "comment_id": "example",
  "item_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/video-comment-replies", sandbase.Params{
	"comment_id": "example",
	"item_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/video-comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number Please keep the default, otherwise there will be BUG.  |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.  |
| `item_id` | string | yes | Video id  |
| `comment_id` | string | yes | Comment id  |

## Details

Returns the reply comments under one comment on a Douyin video. It needs the video ID (`item_id`) and the parent comment ID (`comment_id`), and it pages through replies with a cursor.

### Use cases

- Read the full reply thread under a popular Douyin comment.
- Collect reply text and like counts to study how viewers react to a specific comment.
- Find which users reply to whom by reading the reply target fields.
- Export a reply thread with timestamps and IP location labels for moderation review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-comment-replies" \
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
| `count` | integer | No | Number Please keep the default, otherwise there will be BUG. |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

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
      "comment_token": "MS4wLjAA…",
      "content_type": 1,
      "create_time": 1712405022,
      "decorated_emoji_info": null,
      "digg_count": 15944,
      "image_list": null,
      "ip_label": "湖南"
    }
  ],
  "cursor": 20,
  "extra": {
    "fatal_item_ids": null,
    "now": 1793691101000,
    "scenes": null
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "202611031531417B52BA2153595311905D"
  },
  "merge_cursor": "",
  "status_code": 0,
  "total": 288
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[].cid` | ID of the reply comment. |
| `comments[].text` | Text of the reply. Emoji appear as bracket codes such as `[再见]`. |
| `comments[].create_time` | Time the reply was posted, as a Unix timestamp in seconds. |
| `comments[].digg_count` | Number of likes on the reply. |
| `comments[].reply_id / comments[].root_comment_id` | ID of the comment being replied to, and the ID of the top level comment of the thread. |
| `comments[].reply_to_username / comments[].reply_to_userid / comments[].reply_to_user_sec_id` | Name and IDs of the user this reply is directed at. These appear when the reply targets another reply. |
| `comments[].ip_label` | Location label shown next to the reply, such as a province name. |
| `comments[].label_text` | Badge shown on the reply. The value `作者` marks a reply with the author label. It is empty when there is no badge. |
| `comments[].user.avatar_thumb.url_list` | Image URLs for the small avatar of the user who wrote the reply. |
| `total / has_more / cursor` | `total` is the number of replies to the comment. `has_more` is `1` when more pages exist. `cursor` is the value to send for the next page. |

### Notes

- Take `item_id` from the video and `comment_id` from a top level comment. Use [Douyin Video Comments](/apis/douyin/app-v3/video-comments) to list those comments first.
- For the first page, send `cursor` as `0`. For the next page, send the `cursor` value from the previous response. Stop when `has_more` is not `1`.
- Leave `count` at its default value. The parameter description warns that other values cause bugs.
- Each reply repeats `comment_reply_total` and `aweme_id`, which is the video ID.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-comment-replies.json`](../../../../catalog/models/douyin/app-v3/video-comment-replies.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-comment-replies
