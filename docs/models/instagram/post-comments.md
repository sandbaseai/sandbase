# Instagram Post Comment List API: pricing, parameters and code examples

`instagram/post-comments` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get top-level comments for an Instagram post by shortcode, with cursor pagination and popular or newest sorting. Use it to review audience feedback or analyze discussion around a known post.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/post-comments", "code": "DfAOoAXRg3L"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/post-comments', {'code': 'DfAOoAXRg3L'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/post-comments", {
  "code": "DfAOoAXRg3L"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/post-comments", sandbase.Params{
	"code": "DfAOoAXRg3L",
})
```

Same call via the path form: `POST /v1/api/instagram/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` | string | yes | The unique shortcode for the Instagram post.  |
| `minId` | string |  | Pagination cursor returned as next_min_id from the previous response.  |
| `sortOrder` | string |  | Sort order for the comments. one of: `popular`, `newest`; default `"newest"` |

## Details

Returns top-level comments for an Instagram post, plus the post caption and the total comment count. It needs the post shortcode as `code`. You can sort by `popular` or `newest`.

### Use cases

- Pull the latest comments on a known post to review audience feedback.
- Sort by `popular` to find the comments that drew the most likes.
- Collect comment text and commenter names to analyze the discussion around a campaign post.
- Find comments that have replies and fetch those threads with a separate call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code": "DfAOoAXRg3L"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | string | Yes | The unique shortcode for the Instagram post. |
| `minId` | string | No | Pagination cursor returned as next_min_id from the previous response. |
| `sortOrder` | string | No | Sort order for the comments. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "1318fda1bfbe9",
  "ai_topic_filters": [],
  "can_view_more_preview_comments": false,
  "caption": {
    "bit_flags": 0,
    "content_type": "comment",
    "created_at": 1793116772,
    "created_at_for_fb_app": 1793116772,
    "created_at_utc": 1793116772,
    "did_report_as_spam": false,
    "is_covered": false,
    "is_created_by_media_owner": true,
    "is_ranked_comment": true,
    "media_id": "4017275189435174347",
    "pk": "18115995458110011",
    "private_reply_status": 0
  },
  "caption_is_edited": false,
  "comment_count": 14729,
  "comment_cover_pos": "bottom",
  "comment_filter_param": "no_filter",
  "comment_likes_enabled": true,
  "comments": [
    {
      "bit_flags": 0,
      "child_comment_count": 0,
      "comment_index": 0,
      "comment_like_count": 5,
      "content_type": "comment",
      "created_at": 1793544285,
      "created_at_for_fb_app": 1793544285,
      "created_at_utc": 1793544285,
      "did_report_as_spam": false,
      "has_disliked_comment": false,
      "has_liked_comment": false,
      "inline_composer_display_condition": "never"
    }
  ],
  "fb_comments": [],
  "filter_options": []
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[]` | List of top-level comments on the post. |
| `comments[].pk` | ID of the comment, as a string. |
| `comments[].text` | Text of the comment, including emoji. |
| `comments[].created_at_utc` | Time the comment was posted, as a Unix timestamp. |
| `comments[].comment_like_count` | Number of likes on the comment. |
| `comments[].child_comment_count` | Number of replies to the comment. `0` means no replies. |
| `comments[].user.id / comments[].user.full_name` | ID and display name of the person who wrote the comment. |
| `comments[].user.is_verified` | Whether the commenter has a verified account. |
| `comment_count` | Total number of comments on the post. |
| `caption.text` | Caption of the post. The text can be cut short. |
| `next_min_id` | Cursor for the next page. Pass it as `minId` in the next request. |

### Notes

- The shortcode is the part of a post URL after `/p/` or `/reel/`, for example `DfAOoAXRg3L`.
- For the next page, send the `next_min_id` value from the response as `minId`. Keep the same `sortOrder`.
- `next_min_id` is a JSON string. Pass it back as is.
- To read replies under a comment with `child_comment_count` above `0`, use [Instagram Comment Replies](/apis/instagram/comment-replies).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/instagram/post-comments.json`](../../../catalog/models/instagram/post-comments.json) · Store page: https://www.sandbase.ai/model/instagram/post-comments
