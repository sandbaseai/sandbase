# Douyin Comment Replies API: pricing, parameters and code examples

`douyin/video-sub-comment` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get replies to a top-level Douyin (TikTok China) video comment with page-based pagination. Use it to inspect threaded discussions and review feedback under a known comment.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/video-sub-comment", "commentId": "1767587367821390"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/video-sub-comment', {'commentId': '1767587367821390'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/video-sub-comment", {
  "commentId": "1767587367821390"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/video-sub-comment", sandbase.Params{
	"commentId": "1767587367821390",
})
```

Same call via the path form: `POST /v1/api/douyin/video-sub-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (starting from 1). default `1` |
| `commentId` | string | yes | The unique identifier of the top-level comment.  |

## Details

Returns replies to one top-level Douyin comment. It needs the `commentId` of that comment and takes an optional `page` number. Each reply includes its text, timestamp, like count and the video it belongs to.

### Use cases

- Read the full thread under a popular comment to see how viewers respond to it.
- Collect reply text under a known comment for sentiment or feedback review.
- Count replies and likes on a comment to find threads with active discussion.
- Link each reply back to its video and parent comment to rebuild a comment tree.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/video-sub-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"commentId": "7373626964752450315"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `commentId` | string | Yes | The unique identifier of the top-level comment. |
| `page` | integer | No | Page number (starting from 1). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comments": [
    {
      "aweme_id": "7372484719365098803",
      "can_collect": false,
      "cid": "7373632254276944680",
      "comment_reply_total": 6,
      "content_type": 1,
      "create_time": 1716807549,
      "decorated_emoji_info": null,
      "digg_count": 0,
      "image_list": null,
      "is_author_digged": false,
      "is_folded": false,
      "is_hot": false
    }
  ],
  "cursor": 10,
  "extra": {
    "fatal_item_ids": null,
    "now": 1793691144000,
    "scenes": null
  },
  "has_more": 0,
  "log_pb": {
    "impr_id": "202611031532243E3D7BB70E367D24D5ED"
  },
  "merge_cursor": "",
  "status_code": 0,
  "total": 6
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[].cid` | ID of the reply. Use it as a unique key for each reply. |
| `comments[].text` | Text of the reply. Emoji appear as bracket tags such as `[玫瑰]`. |
| `comments[].create_time` | Time the reply was posted, as a Unix timestamp in seconds. |
| `comments[].digg_count` | Number of likes on the reply. |
| `comments[].reply_id` | ID of the top-level comment that this reply belongs to. It matches the `commentId` you sent. |
| `comments[].reply_to_reply_id` | ID of the reply this reply answers. The value `0` means it answers the top-level comment directly. |
| `comments[].aweme_id` | ID of the video that holds the comment thread. |
| `comments[].comment_reply_total` | Reply count shown on each reply item. It matches `total` in this response. |
| `comments[].user` | Profile object of the reply author. It holds avatar image objects and account flags. |
| `has_more / cursor / total` | `has_more` is `0` when no further page exists. `cursor` is the paging offset returned by the platform. `total` is the number of replies to the comment. |

### Notes

- Get `commentId` from the `cid` field of a top-level comment. The [Douyin Video Comments](/apis/douyin/app-v3/video-comments) API lists those comments for a video.
- Set `page` to 1, 2, 3 and so on. Keep requesting the next page while `has_more` is `1`.
- Some `avatar_*` objects come back with an empty `url_list`, so do not rely on them for images.
- An alternative reply endpoint is [Douyin Video Comment Replies (App V3)](/apis/douyin/app-v3/video-comment-replies).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/douyin/video-sub-comment.json`](../../../catalog/models/douyin/video-sub-comment.json) · Store page: https://www.sandbase.ai/model/douyin/video-sub-comment
