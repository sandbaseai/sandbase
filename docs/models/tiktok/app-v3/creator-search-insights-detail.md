# TikTok Creator Search Insights Detail API: pricing, parameters and code examples

`tiktok/app-v3/creator-search-insights-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get detailed statistics for a TikTok Creator Search Insights query: popularity over time and audience breakdown by age, gender and country.

## Pricing

- **$0.001 per call** (USD)
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

Returns audience statistics for one TikTok Creator Search Insights query: popularity scores split by age, gender and country. It needs a `query_id_str` from the Creator Search Insights API and accepts an optional time range.

### Use cases

- Check which age groups search for a topic before planning a video.
- Compare male, female and unknown gender shares of a query's audience.
- Find the top countries where a search topic is popular to choose a posting language or region.
- Compare the same query over `past_7_days` and `past_6_months` to see how its audience changes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/creator-search-insights-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query_id_str": "7449584484497752069", "time_range": "past_30_days"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query_id_str` | string | Yes | Query ID, obtained from fetch_creator_search_insights response |
| `dimension_list` | string | No | Dimension list, separated by comma, options: gender, age, country |
| `end_date` | integer | No | End timestamp (seconds), only for custom range |
| `start_date` | integer | No | Start timestamp (seconds), only for custom range |
| `time_range` | string | No | Time range (past_7_days/past_30_days/past_60_days/past_6_months/custom) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "age": [
    {
      "category": "total",
      "popularity": 355704
    }
  ],
  "demographics": {
    "age": "25-34",
    "gender": "unknown",
    "location": "United Kingdom"
  },
  "extra": {
    "latency": 44,
    "logid": "2026110307435134E8D92AD0DB6B01A3B8",
    "now": 1793691831842,
    "vgeo": "VGeo-US"
  },
  "gender": [
    {
      "category": "total",
      "popularity": 398818
    }
  ],
  "location": [
    {
      "category": "total",
      "popularity": 324781
    }
  ],
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `demographics.age / demographics.gender / demographics.location` | The leading audience group for the query: the top age bucket, gender value and country name. |
| `age[].category` | Age bucket label such as `25-34`. The list also holds `total` and `others` rows. |
| `age[].popularity` | Popularity score for that age bucket. The `total` row is the score for the whole query. |
| `gender[].category` | Gender label such as `male` or `unknown`. The list also holds a `total` row. |
| `gender[].popularity` | Popularity score for that gender value. |
| `location[].category` | Country name such as `United Kingdom`. The list also holds a `total` row. |
| `location[].popularity` | Popularity score for that country. |
| `status_code / status_msg` | Call status. `status_code` is `0` and `status_msg` is empty when the call succeeds. |

### Notes

- Get `query_id_str` from the [TikTok Creator Search Insights](/apis/tiktok/app-v3/creator-search-insights) API.
- `time_range` accepts `past_7_days`, `past_30_days`, `past_60_days`, `past_6_months` or `custom`. Send `start_date` and `end_date` in seconds only with `custom`.
- Set `dimension_list` to a comma-separated mix of `gender`, `age` and `country` to choose which breakdowns you want.
- For the popularity trend of a query over time, see [TikTok Creator Search Insights Trend](/apis/tiktok/app-v3/creator-search-insights-trend).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Creator Search Insights](/apis/tiktok/app-v3/creator-search-insights): Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category a…
- [TikTok Search](/apis/tiktok/app-v3/general-search-result): Search TikTok by keyword across videos and users (Top tab).

---
Machine-readable: [`catalog/models/tiktok/app-v3/creator-search-insights-detail.json`](../../../../catalog/models/tiktok/app-v3/creator-search-insights-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/creator-search-insights-detail
