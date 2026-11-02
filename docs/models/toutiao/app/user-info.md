# Toutiao User Profile API: pricing, parameters and code examples

`toutiao/app/user-info` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Get a Toutiao (Jinri Toutiao) user profile by user ID: name, bio, avatar, follower, following and like counts, and content tabs.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/app/user-info", "user_id": "1352838578180211"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/app/user-info', {'user_id': '1352838578180211'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/app/user-info", {
  "user_id": "1352838578180211"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/app/user-info", sandbase.Params{
	"user_id": "1352838578180211",
})
```

Same call via the path form: `POST /v1/api/toutiao/app/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID, can be obtained from the following API: `toutiao/app/user-id`  |

## Details

Pass a Toutiao user ID and get the public profile of that account, including follower counts and the content tabs it publishes in.

### Use cases

- Profile Toutiao creators and media accounts.
- Track follower growth for accounts you monitor.
- Enrich author IDs from Toutiao search results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/app/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "1352838578180211"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID, can be obtained from the following API: `toutiao/app/user-id` |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "user_id": "1352838578180211",
    "name": "<user>",
    "description": "…",
    "followers_count": "…",
    "followings_count": "…",
    "digg_count": "…",
    "top_tab": [
      {
        "type": "external_ies_video",
        "total_count": "…"
      }
    ]
  }
}
```

### Notes

- Get the user ID from a Toutiao profile link or the Toutiao user ID API.
- The example below shows the response shape; values depend on the account.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Get information of specified article](/model/toutiao/app/article-info): Get information of specified post.
- [Get comments of specified post](/model/toutiao/app/comments): Get comments of specified post.
- [Get user_id from user profile](/model/toutiao/app/user-id): Get user_id from user profile.

---
Machine-readable: [`catalog/models/toutiao/app/user-info.json`](../../../../catalog/models/toutiao/app/user-info.json) · Store page: https://www.sandbase.ai/model/toutiao/app/user-info
