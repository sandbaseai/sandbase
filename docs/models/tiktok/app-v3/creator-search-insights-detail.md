# TikTok Creator Search Insights Detail API: pricing, parameters and code examples

`tiktok/app-v3/creator-search-insights-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Get detailed statistics for a TikTok Creator Search Insights query: popularity over time and audience breakdown by age, gender and country.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/creator-search-insights-detail", "query_id_str": "7449584484497752069", "time_range": "past_30_days"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/creator-search-insights-detail', {'query_id_str': '7449584484497752069', 'time_range': 'past_30_days'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/creator-search-insights-detail", {
  "query_id_str": "7449584484497752069",
  "time_range": "past_30_days"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/creator-search-insights-detail", sandbase.Params{
	"query_id_str": "7449584484497752069",
	"time_range": "past_30_days",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/creator-search-insights-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end_date` | integer |  | End timestamp (seconds), only for custom range  |
| `start_date` | integer |  | Start timestamp (seconds), only for custom range  |
| `time_range` | string |  | Time range (past_7_days/past_30_days/past_60_days/past_6_months/custom)  |
| `query_id_str` | string | yes | Query ID, obtained from fetch_creator_search_insights response  |
| `dimension_list` | string |  | Dimension list, separated by comma, options: gender, age, country  |

## Details

Pass a `query_id_str` from Creator Search Insights and get its popularity trend and searcher demographics.

### Use cases

- Understand who searches for a topic.
- Validate content ideas with demand data.
- Target content by age and country.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/creator-search-insights-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query_id_str": "7449584484497752069", "time_range": "past_30_days"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query_id_str` | string | Yes | Query ID, obtained from fetch_creator_search_insights response |
| `end_date` | integer | No | End timestamp (seconds), only for custom range |
| `start_date` | integer | No | Start timestamp (seconds), only for custom range |
| `time_range` | string | No | Time range (past_7_days/past_30_days/past_60_days/past_6_months/custom) |
| `dimension_list` | string | No | Dimension list, separated by comma, options: gender, age, country |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "demographics": {
    "age": "25-34",
    "gender": "unknown",
    "location": "United Kingdom"
  },
  "age": [
    {
      "category": "total",
      "popularity": 433427
    },
    {
      "category": "others",
      "popularity": 330399
    },
    {
      "category": "25-34",
      "popularity": 49214
    }
  ],
  "gender": [
    {
      "category": "total",
      "popularity": 493646
    },
    {
      "category": "unknown",
      "popularity": 439331
    },
    {
      "category": "male",
      "popularity": 29608
    }
  ],
  "location": [
    {
      "category": "total",
      "popularity": 401003
    },
    {
      "category": "United Kingdom",
      "popularity": 159147
    },
    {
      "category": "United States of America",
      "popularity": 124437
    }
  ]
}
```

### Notes

- Get `query_id_str` from the Creator Search Insights API.
- `time_range`: past_7_days, past_30_days, past_60_days, past_6_months or custom.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Creator Search Insights](/model/tiktok/app-v3/creator-search-insights): Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category a…
- [TikTok Search](/model/tiktok/app-v3/general-search-result): Search TikTok by keyword across videos and users (Top tab).

---
Machine-readable: [`catalog/models/tiktok/app-v3/creator-search-insights-detail.json`](../../../../catalog/models/tiktok/app-v3/creator-search-insights-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/creator-search-insights-detail
