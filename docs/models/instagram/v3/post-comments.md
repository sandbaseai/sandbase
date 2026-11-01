# Instagram Post Comments (V3)

`instagram/v3/post-comments` · api · Instagram

Returns a list of comments for an Instagram post specified by its shortcode. Supports pagination and ordering by popular or newest comments.

## Pricing

- **$0.012 per call** (USD)
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

Retrieve comments on an Instagram post by providing the post shortcode in `code`. You can optionally paginate results using `min_id` and set comment ordering with `sort_order`.

### Use cases

- Analyze user feedback and sentiment on public Instagram posts.
- Monitor engagement and track replies across high-performing media.
- Collect popular or recent viewer discussions for community reporting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code": "DUajw4YkorV"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | string | Yes | Post shortcode (e.g., DUajw4YkorV, required) |
| `min_id` | string | No | Pagination cursor, omit for first request, get from previous response `data.next_min_id` |
| `sort_order` | string | No | Sort order |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "comments": [
    {
      "child_comment_count": 0,
      "comment_like_count": 1,
      "content_type": "comment",
      "media_id": "3826528124109228757",
      "meta_ai_comment_type": "NONE",
      "private_reply_status": 0,
      "status": "Active",
      "text": "So incredibly beautiful ❤️",
      "type": 0,
      "user_id": "<user>",
      "user": {
        "full_name": "jim blaze",
        "id": "78149267796",
        "pk_id": "78149267796",
        "profile_pic_id": "3764395301835210036_78149267796",
        "profile_pic_url": "https://instagram.flas1-1.fna.fbcdn.net/v/t51.82787-19/581679422_178461291216037…",
        "username": "<user>"
      }
    }
  ]
}
```

### Notes

- Use `min_id` from the previous response `data.next_min_id` to paginate through comments.
- Set `sort_order` to either `popular` or `newest`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/post-comments.json`](../../../../catalog/models/instagram/v3/post-comments.json) · Store page: https://www.sandbase.ai/model/instagram/v3/post-comments
