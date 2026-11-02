# Douyin Creator Comparison Trends API: pricing, parameters and code examples

`douyin/index/daren-compare-users-stable` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comparative trend metrics, such as follower growth and engagement, for up to five Douyin creators over a selected 7-day or 30-day timeframe.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/daren-compare-users-stable", "user_list": "<user_list>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/daren-compare-users-stable', {'user_list': '<user_list>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/daren-compare-users-stable", {
  "user_list": "<user_list>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/daren-compare-users-stable", sandbase.Params{
	"user_list": "<user_list>",
})
```

Same call via the path form: `POST /v1/api/douyin/index/daren-compare-users-stable` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `days` | string |  | Comparison period, only 7 or 30 one of: `7`, `30` |
| `user_list` | string | yes | Daren uid list, comma separated, **max 5**  |

## Details

Query comparative performance metrics across multiple Douyin creators using `user_list` for user identifiers and `days` to specify the timeframe.

### Use cases

- Compare follower growth trends between multiple Douyin creators.
- Evaluate relative engagement metrics across competing influencer profiles.
- Benchmark talent performance across 7-day or 30-day reporting windows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/daren-compare-users-stable" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_list": "<user_list>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_list` | string | Yes | Daren uid list, comma separated, max 5 |
| `days` | string | No | Comparison period, only 7 or 30 |

### Notes

- `user_list` accepts a comma-separated list of creator user IDs with a maximum of 5.
- `days` supports values of "7" or "30".

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/daren-compare-users-stable.json`](../../../../catalog/models/douyin/index/daren-compare-users-stable.json) · Store page: https://www.sandbase.ai/model/douyin/index/daren-compare-users-stable
