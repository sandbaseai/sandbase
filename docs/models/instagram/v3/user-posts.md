# Instagram User Posts (V3) API: pricing, parameters and code examples

`instagram/v3/user-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns a list of posts from a specific Instagram account. Supports bidirectional cursor pagination using the account username.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-posts", "username": "natgeo"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-posts', {'username': 'natgeo'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-posts", {
  "username": "natgeo"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-posts", sandbase.Params{
	"username": "natgeo",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `last` | integer |  | Posts per page for backward pagination, use with `before`  |
| `after` | string |  | Forward pagination cursor, from previous response `page_info.end_cursor`  |
| `count` | integer |  | Number of posts for first request (default 12)  |
| `first` | integer |  | Posts per page for forward pagination (default 12, max 50) range 1–50 |
| `before` | string |  | Backward pagination cursor, from previous response `page_info.start_cursor`  |
| `username` | string | yes | Username string (e.g. `99brasil`), **NOT numeric user_id**  |

## Details

Retrieve posts for an Instagram account by providing a `username`, with optional cursor-based pagination parameters.

### Use cases

- Retrieve historical posts from a public profile.
- Browse user post feeds using forward or backward cursors.
- Monitor recent media uploads from specific accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "<username>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Username string (e.g. |
| `last` | integer | No | Posts per page for backward pagination, use with `before` |
| `after` | string | No | Forward pagination cursor, from previous response `page_info.end_cursor` |
| `count` | integer | No | Number of posts for first request (default 12) |
| `first` | integer | No | Posts per page for forward pagination (default 12, max 50) |
| `before` | string | No | Backward pagination cursor, from previous response `page_info.start_cursor` |

### Notes

- Provide a `username` string rather than a numeric user ID.
- `first` controls forward page size (default 12, max 50) paired with `after`.
- `last` controls backward page size paired with `before`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-posts.json`](../../../../catalog/models/instagram/v3/user-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-posts
