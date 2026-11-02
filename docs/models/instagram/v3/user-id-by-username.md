# Instagram User ID Lookup API: pricing, parameters and code examples

`instagram/v3/user-id-by-username` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Convert an Instagram username into its numeric user ID, the internal identifier needed by most Instagram profile, posts and followers APIs.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-id-by-username", "username": "nima.vahed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-id-by-username', {'username': 'nima.vahed'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-id-by-username", {
  "username": "nima.vahed"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-id-by-username", sandbase.Params{
	"username": "nima.vahed",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-id-by-username` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username  |

## Details

Pass an Instagram username and get the account's numeric user ID. Use it with the other Instagram APIs that require `user_id`.

### Use cases

- Resolve handles collected from links or bios into stable IDs.
- Track accounts even after they change username.
- First step before fetching posts, reels or followers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-id-by-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "nasa"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "user_id": "528817151"
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bulk translate comments](/model/instagram/v3/bulk-translate-comments): Bulk translate Instagram comments Support translating multiple comments at once for better efficiency Comment IDs can be obtained from get_post_comments API.
- [Get comment replies](/model/instagram/v3/comment-replies): Get Instagram comment's child comments (replies) list Support pagination to fetch all replies Parent comment's comment_id can be obtained from get_post_comment…
- [Get explore feed](/model/instagram/v3/explore): V3 Explore provides a focused capability for applications, automation, and data workflows.

---
Machine-readable: [`catalog/models/instagram/v3/user-id-by-username.json`](../../../../catalog/models/instagram/v3/user-id-by-username.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-id-by-username
