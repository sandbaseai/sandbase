# Threads User Reposts API: pricing, parameters and code examples

`threads/web/user-reposts` · data API · Threads · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns a list of reposted threads for a specified Threads user account. Requires the user ID and supports pagination via an optional cursor.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/user-reposts", "user_id": "<user_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/user-reposts', {'user_id': '<user_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/user-reposts", {
  "user_id": "<user_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/user-reposts", sandbase.Params{
	"user_id": "<user_id>",
})
```

Same call via the path form: `POST /v1/api/threads/web/user-reposts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID, for example: 63625256886  |
| `end_cursor` | string |  | Pagination cursor (optional), used to get next page data  |

## Details

Retrieve reposted posts for a specific account using `user_id`. Optional pagination is handled through `end_cursor`.

### Use cases

- Review reposted content from a target Threads account.
- Track sharing activity and community interactions of a profile.
- Archive repost feeds across multiple user profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/user-reposts" \
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

- Supply `end_cursor` to paginate through subsequent pages of reposts.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Threads Post Detail](/model/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Post Detail (V2)](/model/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Profile Search](/model/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.

---
Machine-readable: [`catalog/models/threads/web/user-reposts.json`](../../../../catalog/models/threads/web/user-reposts.json) · Store page: https://www.sandbase.ai/model/threads/web/user-reposts
