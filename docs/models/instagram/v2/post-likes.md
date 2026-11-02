# Instagram Post Likes (V2) API: pricing, parameters and code examples

`instagram/v2/post-likes` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Returns the list of users who liked an Instagram post by shortcode or URL. Supports cursor-based pagination to retrieve subsequent pages.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/post-likes", "code_or_url": "DRhvwVLAHAG"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/post-likes', {'code_or_url': 'DRhvwVLAHAG'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/post-likes", {
  "code_or_url": "DRhvwVLAHAG"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/post-likes", sandbase.Params{
	"code_or_url": "DRhvwVLAHAG",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/post-likes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end_cursor` | string |  | Pagination cursor from previous response  |
| `code_or_url` | string | yes | Post shortcode or full URL  |

## Details

Retrieve user profiles that liked a specific Instagram post using `code_or_url`. Pass `end_cursor` to paginate through the complete list of likes.

### Use cases

- Analyze user engagement on specific Instagram posts.
- Identify active followers and audience members who like content.
- Audit interaction metrics across individual Instagram media entries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/post-likes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code_or_url": "DRhvwVLAHAG"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code_or_url` | string | Yes | Post shortcode or full URL |
| `end_cursor` | string | No | Pagination cursor from previous response |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "id": "68058278483",
        "profile_pic_id": "3425253659352004517",
        "profile_pic_url": "https://instagram.frix7-1.fna.fbcdn.net/v/t51.2885-19/453639237_482505544728262_…",
        "username": "<user>"
      }
    ]
  }
}
```

### Notes

- Provide either a post shortcode or a full Instagram post URL to `code_or_url`.
- Use `end_cursor` from the previous response to fetch the next page of results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/post-likes.json`](../../../../catalog/models/instagram/v2/post-likes.json) · Store page: https://www.sandbase.ai/model/instagram/v2/post-likes
