# Instagram Post Comments (V2)

`instagram/v2/post-comments` · api · Instagram

Returns comments from an Instagram post, including comment text, user details, and like counts. Accepts a post shortcode or URL with options to sort by recent or popular comments and paginate results.

## Pricing

- **$0.003 per call** (USD)
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

Retrieve comments for an Instagram post using `code_or_url`. Optional parameters include `sort_by` to reorder results and `pagination_token` for navigating through multiple pages.

### Use cases

- Analyze audience sentiment and feedback on specific Instagram posts.
- Track popular or recent discussions under brand and influencer media.
- Extract user replies and interaction counts for social listening reports.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code_or_url": "DUajw4YkorV"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code_or_url` | string | Yes | Post shortcode or full URL |
| `sort_by` | string | No | Sort by "recent" or "popular", default recent |
| `pagination_token` | string | No | Pagination token from previous response |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "child_comment_count": 0,
        "comment_like_count": 2,
        "content_type": "comment",
        "id": "17970092114852855",
        "meta_ai_comment_type": "NONE",
        "private_reply_status": 0,
        "text": "luvvvvvvv🖤🖤🖤",
        "type": 0,
        "user_id": "<user>",
        "user": {
          "full_name": "Lingga S. P.",
          "id": "3558721631",
          "profile_pic_id": "3955241250307294885",
          "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/762008208_18466154488113…",
          "username": "<user>"
        }
      }
    ]
  }
}
```

### Notes

- `sort_by` accepts "recent" or "popular", defaulting to "recent".
- `code_or_url` accepts either an Instagram post shortcode or a full URL.
- Pass `pagination_token` from a previous response to page through additional comments.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/post-comments.json`](../../../../catalog/models/instagram/v2/post-comments.json) · Store page: https://www.sandbase.ai/model/instagram/v2/post-comments
