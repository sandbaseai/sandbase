# Threads User Info by ID API: pricing, parameters and code examples

`threads/web/user-info-by-id` · data API · Threads · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns detailed Threads user profile information based on a specified user ID. Ideal for retrieving public account metadata directly through web identifiers.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/user-info-by-id", "user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/user-info-by-id', {'user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/user-info-by-id", {
  "user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/user-info-by-id", sandbase.Params{
	"user_id": "example",
})
```

Same call via the path form: `POST /v1/api/threads/web/user-info-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID, for example: 67027868801, can be obtained from user profile API or post data  |

## Details

Fetch Threads user profile information by supplying a target `user_id`.

### Use cases

- Retrieve Threads profile metadata using an internal account identifier.
- Inspect user profile details extracted from post interactions.
- Resolve account information across threads and user directories.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/user-info-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "67027868801"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID, for example: 67027868801, can be obtained from user profile API or post data |

### Notes

- The `user_id` value can be obtained from the user profile API or from post data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Threads Post Detail](/apis/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Post Detail (V2)](/apis/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Profile Search](/apis/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.

---
Machine-readable: [`catalog/models/threads/web/user-info-by-id.json`](../../../../catalog/models/threads/web/user-info-by-id.json) · Store page: https://www.sandbase.ai/model/threads/web/user-info-by-id
