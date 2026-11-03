# TikTok Post Comments API: pricing, parameters and code examples

`tiktok/post-comment` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get comments for a TikTok post with cursor pagination. Use it to review audience discussion, continue through comment pages, or support comment analysis for a known post.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/post-comment", "awemeId": "7701102965385383199"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/post-comment', {'awemeId': '7701102965385383199'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/post-comment", {
  "awemeId": "7701102965385383199"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/post-comment", sandbase.Params{
	"awemeId": "7701102965385383199",
})
```

Same call via the path form: `POST /v1/api/tiktok/post-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor. Start with '0'. default `"0"` |
| `awemeId` | string | yes | The unique ID of the TikTok post (awemeId).  |

## Details

Returns one page of comments for a TikTok post, including comment text, like counts, creation time, and a short preview of replies. It needs the post's `awemeId`. Use the `cursor` parameter to move through later pages.

### Use cases

- Read what viewers say about a known TikTok video.
- Collect all comments on a post by following the cursor until `has_more` is `0`.
- Find the most liked comments and the ones the creator liked.
- Feed comment text into sentiment or topic analysis for one post.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/post-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"awemeId": "7701102965385383199"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `awemeId` | string | Yes | The unique ID of the TikTok post (awemeId). |
| `cursor` | string | No | Pagination cursor. Start with '0'. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "alias_comment_deleted": false,
  "comments": [
    {
      "allow_download_photo": true,
      "author_pin": false,
      "aweme_id": "7701102965385383199",
      "cid": "7701125977473532702",
      "collect_stat": 0,
      "comment_language": "en",
      "comment_post_item_ids": null,
      "content_type": 1,
      "create_time": 1793058147,
      "digg_count": 7077,
      "fold_status": -1,
      "image_list": null
    }
  ],
  "cursor": 20,
  "extra": {
    "api_debug_info": null,
    "fatal_item_ids": null,
    "now": 1793691847000
  },
  "has_filtered_comments": 0,
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103074407D623CDF3639ECD01CFBD"
  },
  "reply_style": 2,
  "status_code": 0,
  "status_msg": "",
  "top_gifts": null,
  "total": 2755
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[].cid` | ID of the comment. |
| `comments[].text` | Text of the comment. |
| `comments[].create_time` | Time the comment was posted, as a Unix timestamp in seconds. |
| `comments[].digg_count` | Number of likes on the comment. |
| `comments[].is_author_digged / comments[].label_list[].text` | Show whether the post's creator liked the comment. The label reads `Liked by creator` when they did. |
| `comments[].comment_language` | Language code of the comment, such as `en`. |
| `comments[].reply_comment_total` | Total number of replies to the comment. |
| `comments[].reply_comment[]` | A short preview of replies to the comment. It can be `null` when no preview is returned. |
| `comments[].user` | Profile data for the commenter, such as avatar images in `avatar_thumb.url_list`. |
| `total` | Total number of comments reported for the post. |
| `cursor / has_more` | `cursor` is the value for the next page. `has_more` is `1` when more comments remain. |

### Notes

- Get `awemeId` from a video details response, for example from [TikTok Video Details](/apis/tiktok/app-v3/one-video).
- Send `cursor` as `0` for the first page. For the next page, pass the `cursor` value from the previous response.
- Stop paging when `has_more` is `0`.
- Each comment has `reply_comment_total`, but `reply_comment[]` holds only a preview, so it may not list every reply.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tiktok/post-comment.json`](../../../catalog/models/tiktok/post-comment.json) · Store page: https://www.sandbase.ai/model/tiktok/post-comment
