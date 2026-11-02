# Douyin Similar Daren Accounts API: pricing, parameters and code examples

`douyin/index/daren-similar-users` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a list of similar Douyin daren accounts based on a specified user profile. Supply a target user identifier to discover comparable talent and content channels across the platform.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/daren-similar-users", "user_id": "<user_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/daren-similar-users', {'user_id': '<user_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/daren-similar-users", {
  "user_id": "<user_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/daren-similar-users", sandbase.Params{
	"user_id": "<user_id>",
})
```

Same call via the path form: `POST /v1/api/douyin/index/daren-similar-users` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Douyin uid (numeric, e.g. "3100268042915212")  |

## Details

Look up related Douyin daren comparable to a target account using the `user_id` parameter.

### Use cases

- Discover alternative Douyin daren within a specific content niche.
- Identify comparable influencer accounts for campaign benchmarking.
- Expand talent research rosters based on existing high-performing profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/daren-similar-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "<user_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Douyin uid (numeric, e.g. "3100268042915212") |

### Notes

- Provide a numeric Douyin user ID for the `user_id` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/daren-similar-users.json`](../../../../catalog/models/douyin/index/daren-similar-users.json) · Store page: https://www.sandbase.ai/model/douyin/index/daren-similar-users
