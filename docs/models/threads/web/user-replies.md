# Threads User Replies

`threads/web/user-replies` · api · Threads

Returns a list of replies posted by a specific Threads user. Query replies using a target user identifier and an optional pagination cursor.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/user-replies", "user_id": "63625256886"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/user-replies', {'user_id': '63625256886'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/user-replies", {
  "user_id": "63625256886"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/user-replies", sandbase.Params{
	"user_id": "63625256886",
})
```

Same call via the path form: `POST /v1/api/threads/web/user-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID, for example: 63625256886  |
| `end_cursor` | string |  | Pagination cursor (optional), used to get next page data  |

## Details

Retrieve replies posted by an account on Threads by supplying the `user_id`. Supports subsequent pages of results via `end_cursor`.

### Use cases

- Monitor recent replies posted by a specific user.
- Track user conversation history across different threads.
- Ingest reply activity into an engagement tracking dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/user-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "<user_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID, for example: 63625256886 |
| `end_cursor` | string | No | Pagination cursor (optional), used to get next page data |

### Notes

- Pass `end_cursor` to paginate through subsequent pages of reply data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Threads Post Detail](/model/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Post Detail (V2)](/model/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Profile Search](/model/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.

---
Machine-readable: [`catalog/models/threads/web/user-replies.json`](../../../../catalog/models/threads/web/user-replies.json) · Store page: https://www.sandbase.ai/model/threads/web/user-replies
