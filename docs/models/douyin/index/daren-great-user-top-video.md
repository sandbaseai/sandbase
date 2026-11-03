# Douyin Creator Top Videos API: pricing, parameters and code examples

`douyin/index/daren-great-user-top-video` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a Douyin creator's top-performing video list across a specified date range, based on creator ID and date filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/daren-great-user-top-video", "end_date": "<end_date>", "start_date": "<start_date>", "user_id": "<user_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/daren-great-user-top-video', {'end_date': '<end_date>', 'start_date': '<start_date>', 'user_id': '<user_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/daren-great-user-top-video", {
  "end_date": "<end_date>",
  "start_date": "<start_date>",
  "user_id": "<user_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/daren-great-user-top-video", sandbase.Params{
	"end_date": "<end_date>",
	"start_date": "<start_date>",
	"user_id": "<user_id>",
})
```

Same call via the path form: `POST /v1/api/douyin/index/daren-great-user-top-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Douyin uid (numeric, e.g. "3100268042915212")  |
| `end_date` | string | yes | End date, format YYYYMMDD  |
| `start_date` | string | yes | Start date, format YYYYMMDD  |

## Details

Query top-performing videos for a target creator using `user_id`, `start_date`, and `end_date`.

### Use cases

- Analyze a creator's highest-performing content over a specific campaign period.
- Benchmark top video metrics across different Douyin influencers.
- Audit popular video performance trends within designated date windows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/daren-great-user-top-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "<end_date>", "start_date": "<start_date>", "user_id": "<user_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Douyin uid (numeric, e.g. "3100268042915212") |
| `end_date` | string | Yes | End date, format YYYYMMDD |
| `start_date` | string | Yes | Start date, format YYYYMMDD |

### Notes

- `user_id` requires a numeric Douyin user identifier.
- `start_date` and `end_date` must follow the YYYYMMDD format.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/daren-great-user-top-video.json`](../../../../catalog/models/douyin/index/daren-great-user-top-video.json) · Store page: https://www.sandbase.ai/model/douyin/index/daren-great-user-top-video
