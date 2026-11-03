# Toutiao Profile User ID API: pricing, parameters and code examples

`toutiao/app/user-id` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Resolves a Toutiao user profile URL into numeric and secure user identifiers. Returns the user ID and sec_user_id associated with the provided profile link.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/app/user-id", "user_profile_url": "https://static.sandbase.ai/examples/4494279d-e579-4329-bbf7-b759ee763f46/input/9295e84f-2dcb-46b2-9db8-9e97dabb7c99.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/app/user-id', {'user_profile_url': 'https://static.sandbase.ai/examples/4494279d-e579-4329-bbf7-b759ee763f46/input/9295e84f-2dcb-46b2-9db8-9e97dabb7c99.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/app/user-id", {
  "user_profile_url": "https://static.sandbase.ai/examples/4494279d-e579-4329-bbf7-b759ee763f46/input/9295e84f-2dcb-46b2-9db8-9e97dabb7c99.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/app/user-id", sandbase.Params{
	"user_profile_url": "https://static.sandbase.ai/examples/4494279d-e579-4329-bbf7-b759ee763f46/input/9295e84f-2dcb-46b2-9db8-9e97dabb7c99.bin",
})
```

Same call via the path form: `POST /v1/api/toutiao/app/user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_profile_url` | string | yes | User profile URL  |

## Details

Look up account identifiers from a Toutiao user profile link by passing `user_profile_url`.

### Use cases

- Convert web profile links into Toutiao user IDs for downstream queries.
- Retrieve sec_user_id values needed for Toutiao data integrations.
- Resolve account identifiers from shared Toutiao user links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/app/user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_profile_url": "https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_profile_url` | string | Yes | User profile URL |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "sec_user_id": "<user>",
  "user_id": "<user>"
}
```

### Notes

- Requires the full profile link in `user_profile_url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Toutiao Article Details (App)](/apis/toutiao/app/article-info): Returns details and interface settings for a specified Toutiao post.
- [Toutiao Post Comments](/apis/toutiao/app/comments): Returns user comments and interaction metrics for a specific Toutiao post.
- [Toutiao User Profile](/apis/toutiao/app/user-info): Get a Toutiao (Jinri Toutiao) user profile by user ID: name, bio, avatar, follower, following and like counts, and content tabs.

---
Machine-readable: [`catalog/models/toutiao/app/user-id.json`](../../../../catalog/models/toutiao/app/user-id.json) · Store page: https://www.sandbase.ai/model/toutiao/app/user-id
