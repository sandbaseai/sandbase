# Threads User Posts API: pricing, parameters and code examples

`threads/web/user-posts` · data API · Threads · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns a list of posts from a specified Threads account. Accepts a user identifier and an optional pagination cursor to retrieve subsequent pages of data.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/user-posts", "user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/user-posts', {'user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/user-posts", {
  "user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/user-posts", sandbase.Params{
	"user_id": "example",
})
```

Same call via the path form: `POST /v1/api/threads/web/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID, for example: 63625256886, can be obtained from user profile API  |
| `end_cursor` | string |  | Pagination cursor (optional), used to get next page data  |

## Details

Fetch posts for a target account using `user_id`. You can navigate multi-page timelines by providing an `end_cursor`.

### Use cases

- Retrieve historical posts from a specific Threads profile.
- Page through account activity feeds using pagination tokens.
- Collect post content and metadata for social media monitoring.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "63625256886"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID, for example: 63625256886, can be obtained from user profile API |
| `end_cursor` | string | No | Pagination cursor (optional), used to get next page data |

### Notes

- `user_id` can be obtained from the user profile API.
- `end_cursor` is used to navigate to the next page of results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Threads Post Detail](/apis/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Post Detail (V2)](/apis/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Profile Search](/apis/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.

---
Machine-readable: [`catalog/models/threads/web/user-posts.json`](../../../../catalog/models/threads/web/user-posts.json) · Store page: https://www.sandbase.ai/model/threads/web/user-posts
