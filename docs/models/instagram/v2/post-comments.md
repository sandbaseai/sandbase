# Instagram Post Comments (V2) API: pricing, parameters and code examples

`instagram/v2/post-comments` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns comments from an Instagram post, including comment text, user details, and like counts. Accepts a post shortcode or URL with options to sort by recent or popular comments and paginate results.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/post-comments", "code_or_url": "DUajw4YkorV"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/post-comments', {'code_or_url': 'DUajw4YkorV'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/post-comments", {
  "code_or_url": "DUajw4YkorV"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/post-comments", sandbase.Params{
	"code_or_url": "DUajw4YkorV",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort_by` | string |  | Sort by "recent" or "popular", default recent default `"recent"` |
| `code_or_url` | string | yes | Post shortcode or full URL  |
| `pagination_token` | string |  | Pagination token from previous response default `""` |

## Details

Returns comments on an Instagram post, including the comment text, like count, reply count and basic details about the commenter. It needs a post shortcode or full post URL in `code_or_url`.

### Use cases

- Read the comments under a brand post to review audience feedback.
- Collect commenter IDs and names from a giveaway post to check entries.
- Find comments with the most likes by calling with `sort_by` set to `popular`.
- Export comment text and timestamps for a social listening report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code_or_url": "DUajw4YkorV"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code_or_url` | string | Yes | Post shortcode or full URL |
| `pagination_token` | string | No | Pagination token from previous response |
| `sort_by` | string | No | Sort by "recent" or "popular", default recent |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "additional_data": {
      "ai_topic_filters": [],
      "caption": {
        "content_type": "comment",
        "created_at": 1770377722,
        "created_at_for_fb_app": 1770377722,
        "created_at_utc": 1770377722,
        "did_report_as_spam": false,
        "hashtags": [],
        "id": "18066362081641928",
        "is_covered": false
      },
      "caption_is_edited": false,
      "comment_cover_pos": "bottom",
      "comment_filter_param": "no_filter",
      "comment_likes_enabled": true,
      "fb_comments": [],
      "filter_options": [],
      "foundation_improvements_enabled": true,
      "geoblocked_comment_notices": [],
      "has_more_headload_fb_comments": false,
      "media_header_display": "none"
    },
    "count": 7,
    "items": [
      {
        "child_comment_count": 0,
        "comment_index": 0,
        "comment_like_count": 2,
        "content_type": "comment",
        "created_at": 1770378260,
        "created_at_for_fb_app": 1770378260,
        "created_at_utc": 1770378260,
        "did_report_as_spam": false,
        "has_disliked_comment": false,
        "has_liked_comment": false,
        "hashtags": [],
        "id": "17970092114852855"
      }
    ],
    "total": 49
  },
  "pagination_token": "GU1VBBoT…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].text` | Text of the comment. It is an empty string when the comment contains only a GIF. |
| `data.items[].id` | ID of the comment. Use it to look up replies to that comment. |
| `data.items[].comment_like_count` | Number of likes on the comment. |
| `data.items[].child_comment_count` | Number of replies to the comment. |
| `data.items[].created_at / data.items[].created_at_utc` | Time the comment was posted, as a Unix timestamp in seconds. |
| `data.items[].user.id / data.items[].user_id` | ID of the account that wrote the comment. |
| `data.items[].user.full_name` | Display name of the commenter. |
| `data.items[].user.is_private / data.items[].user.is_verified` | Flags that show whether the commenter's account is private and whether it is verified. |
| `data.items[].is_pinned` | Shows whether the comment is pinned on the post. |
| `data.items[].giphy_media_info.title` | Title of the GIF when the comment is a GIF. The `images` object holds the GIF file links. |
| `data.total` | Total comment count reported for the post. |
| `pagination_token` | Token that selects the next page of comments. |

### Notes

- Take the shortcode from the post URL. In `https://www.instagram.com/p/DUajw4YkorV/` the shortcode is `DUajw4YkorV`.
- To get the next page, send the returned `pagination_token` with the same `code_or_url` and `sort_by` values.
- `sort_by` accepts `recent` or `popular`. The default is `recent`.
- To read replies to a comment, call [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies) with the comment `id`.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/post-comments.json`](../../../../catalog/models/instagram/v2/post-comments.json) · Store page: https://www.sandbase.ai/model/instagram/v2/post-comments
