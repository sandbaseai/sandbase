# Xiaohongshu (RED) PGY Blogger Fan Profile API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-fans-profile` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns demographic distributions for a blogger's follower base, including gender, age, region, interests, and device types, filtered by user ID.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-fans-profile", "user_id": "60b137080000000001000301"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-fans-profile', {'user_id': '60b137080000000001000301'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-fans-profile", {
  "user_id": "60b137080000000001000301"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-fans-profile", sandbase.Params{
	"user_id": "60b137080000000001000301",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-fans-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |

## Details

Retrieve audience demographic breakdowns for a specific blogger by passing their `user_id`.

### Use cases

- Analyze follower demographics before booking blogger campaigns.
- Verify target audience alignment across regions and age groups.
- Assess device preferences and consumer interest categories of followers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-fans-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "60b137080000000001000301"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "provinces": [
      {
        "name": "广东"
      }
    ]
  }
}
```

### Notes

- Requires a valid blogger `user_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/model/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/model/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/model/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-fans-profile.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-fans-profile.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-fans-profile
