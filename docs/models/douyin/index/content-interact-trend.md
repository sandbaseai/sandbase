# Douyin Category Content Interaction Trend API: pricing, parameters and code examples

`douyin/index/content-interact-trend` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns engagement rate trends over time for a specific Douyin content category between selected start and end dates.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-interact-trend", "end_date": "20260414", "start_date": "20260314", "tag_id": "601"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-interact-trend', {'end_date': '20260414', 'start_date': '20260314', 'tag_id': '601'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-interact-trend", {
  "end_date": "20260414",
  "start_date": "20260314",
  "tag_id": "601"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-interact-trend", sandbase.Params{
	"end_date": "20260414",
	"start_date": "20260314",
	"tag_id": "601",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-interact-trend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tag_id` | string | yes | Category ID (**required, does NOT support 0=all**, must pass a specific category ID)  |
| `end_date` | string | yes | End date YYYYMMDD (inclusive)  |
| `start_date` | string | yes | Start date YYYYMMDD (inclusive)  |

## Details

Query user interaction rate trends for a specific Douyin category using `tag_id`, `start_date`, and `end_date`.

### Use cases

- Track audience engagement rate changes across specific content categories over time.
- Analyze daily interaction metrics including likes, comments, shares, and favorites.
- Benchmark category performance between specific date ranges.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-interact-trend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "20260414", "start_date": "20260314", "tag_id": "601"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_id` | string | Yes | Category ID (required, does NOT support 0=all, must pass a specific category ID) |
| `end_date` | string | Yes | End date YYYYMMDD (inclusive) |
| `start_date` | string | Yes | Start date YYYYMMDD (inclusive) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "interact_trend": {
    "rate_list": [
      {
        "date": "20260314",
        "rate": 0.02431060923716989
      }
    ]
  }
}
```

### Notes

- `tag_id` requires a specific category ID and does not support 0 for all categories.
- Both `start_date` and `end_date` accept dates formatted as YYYYMMDD and are inclusive.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-interact-trend.json`](../../../../catalog/models/douyin/index/content-interact-trend.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-interact-trend
