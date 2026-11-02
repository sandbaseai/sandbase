# Douyin Daren Fan Analysis API: pricing, parameters and code examples

`douyin/index/daren-great-user-fans-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns audience and follower analysis data for a specified Douyin influencer. Queries metrics using the influencer's numeric user ID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/daren-great-user-fans-info", "user_id": "1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/daren-great-user-fans-info', {'user_id': '1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/daren-great-user-fans-info", {
  "user_id": "1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/daren-great-user-fans-info", sandbase.Params{
	"user_id": "1",
})
```

Same call via the path form: `POST /v1/api/douyin/index/daren-great-user-fans-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Douyin uid (numeric, e.g. "3100268042915212")  |

## Details

Access Douyin influencer follower analysis data by supplying the account UID in `user_id`.

### Use cases

- Analyze demographic and behavioral profiles of an influencer's audience.
- Evaluate influencer reach and audience alignment before marketing partnerships.
- Track fan base composition metrics for competitive intelligence.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/daren-great-user-fans-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "<user_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Douyin uid (numeric, e.g. "3100268042915212") |

### Notes

- The `user_id` parameter requires the numeric Douyin UID string (e.g., "3100268042915212").

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/daren-great-user-fans-info.json`](../../../../catalog/models/douyin/index/daren-great-user-fans-info.json) · Store page: https://www.sandbase.ai/model/douyin/index/daren-great-user-fans-info
