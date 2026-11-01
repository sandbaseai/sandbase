# Threads User Profile

`threads/web/user-info` · api · Threads

Get a Threads (Meta) user profile by username: name, bio, follower count and verification status.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/user-info", "username": "nasa"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/user-info', {'username': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/user-info", {
  "username": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/user-info", sandbase.Params{
	"username": "nasa",
})
```

Same call via the path form: `POST /v1/api/threads/web/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Username, for example: lilbieber, can be obtained from the user's homepage link, for example: lilbieber in https://www.threads.net/@lilbieber  |

## Details

Pass a Threads username and get the public profile of that account.

### Use cases

- Track follower counts on Threads.
- Vet creators across Meta platforms.
- Enrich handles with profile data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "nasa"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Username, for example: lilbieber, can be obtained from the user's homepage link, for example: lilbieber in https://www.… |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "user": {
    "id": "28829152388",
    "username": "nasa",
    "full_name": "NASA",
    "biography": "Making the seemingly impossible, possible. ✨",
    "follower_count": 12758034,
    "is_verified": true
  }
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Get post detail](/model/threads/web/post-detail): Get Threads post detail.
- [Get post detail V2(supports URL)](/model/threads/web/post-detail-v2): Get Threads post detail (supports short code and full URL).
- [Search profiles](/model/threads/web/search-profiles): Search Threads user profiles.

---
Machine-readable: [`catalog/models/threads/web/user-info.json`](../../../../catalog/models/threads/web/user-info.json) · Store page: https://www.sandbase.ai/model/threads/web/user-info
