# Instagram Comment Replies (V2)

`instagram/v2/comment-replies` · api · Instagram

Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/comment-replies", "code_or_url": "DRhvwVLAHAG", "comment_id": "18067775592012345"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/comment-replies', {'code_or_url': 'DRhvwVLAHAG', 'comment_id': '18067775592012345'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/comment-replies", {
  "code_or_url": "DRhvwVLAHAG",
  "comment_id": "18067775592012345"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/comment-replies", sandbase.Params{
	"code_or_url": "DRhvwVLAHAG",
	"comment_id": "18067775592012345",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `comment_id` | string | yes | Comment ID  |
| `code_or_url` | string | yes | Post shortcode or full URL  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Retrieve threaded replies for a specific Instagram comment by providing `code_or_url` and `comment_id`. Use `pagination_token` to navigate through subsequent reply batches.

### Use cases

- Display conversation threads under specific Instagram comments.
- Track user responses and interactions on selected comments.
- Extract threaded replies for community moderation analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code_or_url": "DRhvwVLAHAG", "comment_id": "18067775592012345"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `comment_id` | string | Yes | Comment ID |
| `code_or_url` | string | Yes | Post shortcode or full URL |
| `pagination_token` | string | No | Pagination token from previous response |

### Notes

- Retrieve `comment_id` from the post comments endpoint first.
- Pass `pagination_token` from a previous response to paginate through replies.
- `code_or_url` accepts either an Instagram post shortcode or a full post URL.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.
- [Instagram Highlight Stories](/model/instagram/v2/highlight-stories): Returns all stories contained within a specific Instagram highlight using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v2/comment-replies.json`](../../../../catalog/models/instagram/v2/comment-replies.json) · Store page: https://www.sandbase.ai/model/instagram/v2/comment-replies
