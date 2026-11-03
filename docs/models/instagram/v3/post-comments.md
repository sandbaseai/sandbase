# Instagram Post Comments (V3) API: pricing, parameters and code examples

`instagram/v3/post-comments` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns a list of comments for an Instagram post specified by its shortcode. Supports pagination and ordering by popular or newest comments.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/post-comments", "code": "DUajw4YkorV"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/post-comments', {'code': 'DUajw4YkorV'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/post-comments", {
  "code": "DUajw4YkorV"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/post-comments", sandbase.Params{
	"code": "DUajw4YkorV",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` | string | yes | Post shortcode (e.g., DUajw4YkorV, required)  |
| `min_id` | string |  | Pagination cursor, omit for first request, get from previous response `data.next_min_id`  |
| `sort_order` | string |  | Sort order one of: `popular`, `newest`; default `"popular"` |

## Details

Returns a list of comments for one Instagram post, plus the post caption and a pagination cursor. It needs the post shortcode in `code`, and you can order results by `popular` or `newest` with `sort_order`.

### Use cases

- Read the top comments on a post to see how viewers react to it.
- Export comment text, authors and like counts for a community or brand report.
- Page through every comment on a post to build a full discussion archive.
- Check whether the post owner pinned or wrote a caption comment and how many comments the post has.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code": "DUajw4YkorV"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | string | Yes | Post shortcode (e.g., DUajw4YkorV, required) |
| `min_id` | string | No | Pagination cursor, omit for first request, get from previous response `data.next_min_id` |
| `sort_order` | string | No | Sort order |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "1ce8f516db888",
  "ai_topic_filters": [],
  "can_view_more_preview_comments": false,
  "caption": {
    "bit_flags": 0,
    "content_type": "comment",
    "created_at": 1770377722,
    "created_at_for_fb_app": 1770377722,
    "created_at_utc": 1770377722,
    "did_report_as_spam": false,
    "is_covered": false,
    "is_created_by_media_owner": true,
    "is_ranked_comment": true,
    "media_id": "3826528124109228757",
    "pk": "18066362081641928",
    "private_reply_status": 0
  },
  "caption_is_edited": false,
  "comment_count": 49,
  "comment_cover_pos": "bottom",
  "comment_filter_param": "no_filter",
  "comment_likes_enabled": true,
  "comments": [
    {
      "bit_flags": 0,
      "child_comment_count": 0,
      "comment_index": 0,
      "comment_like_count": 0,
      "content_type": "comment",
      "created_at": 1786498491,
      "created_at_for_fb_app": 1786498491,
      "created_at_utc": 1786498491,
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
| `comments[]` | List of comments on the post. Each item is one top-level comment. |
| `comments[].text` | The text of the comment. |
| `comments[].pk` | ID of the comment. Use it to identify a single comment. |
| `comments[].comment_like_count / comments[].child_comment_count` | Number of likes on the comment and number of replies under it. |
| `comments[].created_at_utc` | Time the comment was posted, as a Unix timestamp in seconds. |
| `comments[].user.username / comments[].user.full_name / comments[].user_id` | The comment author's handle, display name and numeric account ID. |
| `comments[].user.is_private / comments[].user.is_verified` | Whether the comment author's account is private and whether it is verified. |
| `comment_count` | Total number of comments reported for the post. |
| `caption.text` | The post caption, returned as a comment object written by the post owner. |
| `next_min_id` | Cursor for the next page. Send it as `min_id` in the next request. |
| `has_more_headload_comments` | `true` when more comments are available beyond this page. |

### Notes

- Get the shortcode from a post URL, or use [Instagram Shortcode Extractor](/apis/instagram/v3/extract-shortcode) to pull it out of a link.
- For the next page, pass the `next_min_id` value from the previous response as `min_id`. Leave `min_id` out on the first request.
- `sort_order` accepts `popular` (default) or `newest`.
- To read replies under a comment, call [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/post-comments.json`](../../../../catalog/models/instagram/v3/post-comments.json) · Store page: https://www.sandbase.ai/model/instagram/v3/post-comments
