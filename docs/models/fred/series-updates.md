# FRED Get Series Updates API: pricing, parameters and code examples

`fred/series-updates` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Series Updates from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/series-updates", "end_time": "202610280000", "start_time": "202610270000"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/series-updates', {'end_time': '202610280000', 'start_time': '202610270000'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/series-updates", {
  "end_time": "202610280000",
  "start_time": "202610270000"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/series-updates", sandbase.Params{
	"end_time": "202610280000",
	"start_time": "202610270000",
})
```

Same call via the path form: `POST /v1/api/fred/series-updates` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `end_time` | string | yes | End time for limiting results for a time range, can filter down to minutes YYYYMMDDHhmm formatted string, optional, , start_time is required if end_time is set < Example: 2018-03-02 2:20 would be 201803020220  |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `start_time` | string | yes | Start time for limiting results for a time range, can filter down to minutes YYYYMMDDHhmm formatted string, optional, end_time is required if start_time is set Example: 2018-03-02 14:20 would be 201803021420  |
| `filter_value` | string |  | Limit results by geographic type of economic data series; namely 'macro', 'regional', and 'all'. String, optional, default: 'all' meaning no filter. One of the values: 'macro', 'regional', 'all' 'macro' limits results… default `"all"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns the FRED economic data series that were updated within a time window, newest first. You must pass `start_time` and `end_time`. Each result includes the series ID, title, frequency, units and the date it was last updated.

### Use cases

- Poll for FRED series changed in the last day to refresh a local copy of economic data.
- Build a feed of newly updated regional or macro series by setting `filter_value`.
- Find which series to re-pull after a data release by listing updates in a time range.
- Page through all updated series with `limit` and `offset` to audit what changed in a given period.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series-updates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_time": "202610270000", "end_time": "202610280000", "limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_time` | string | Yes | End time for limiting results for a time range, can filter down to minutes YYYYMMDDHhmm formatted string, optional, , start_time is required if end_time is set < Example: 2018-03-02 2:20 would be 201803020220 |
| `start_time` | string | Yes | Start time for limiting results for a time range, can filter down to minutes YYYYMMDDHhmm formatted string, optional, end_time is required if start_time is set Example: 2018-03-02 14:20 would be 201803021420 |
| `file_type` | string | No | Response format. Only json is supported. |
| `filter_value` | string | No | Limit results by geographic type of economic data series; namely 'macro', 'regional', and 'all'. String, optional, default: 'all' meaning no filter. One of the values: 'macro', 'regional', 'all' 'macro' limits results to |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 74753,
  "filter_value": "all",
  "filter_variable": "geography",
  "limit": 2,
  "offset": 0,
  "order_by": "last_updated",
  "realtime_end": "2026-11-03",
  "realtime_start": "2026-11-03",
  "seriess": [
    {
      "frequency": "Monthly",
      "frequency_short": "M",
      "id": "LARE748BPPRIVSA",
      "last_updated": "2026-10-27 19:07:29-05",
      "notes": "This series represents the total number of building permits for all structure ty…",
      "observation_end": "2026-09-01",
      "observation_start": "1988-01-01",
      "popularity": 1,
      "realtime_end": "2026-11-03",
      "realtime_start": "2026-11-03",
      "seasonal_adjustment": "Seasonally Adjusted",
      "seasonal_adjustment_short": "SA"
    }
  ],
  "sort_order": "desc"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of updated series that match the time range and filter. Use it to plan paging. |
| `seriess[].id` | FRED series ID, such as `LARE748BPPRIVSA`. Pass it to other FRED APIs to get the series itself. |
| `seriess[].title` | Full name of the series, including the geography when there is one. |
| `seriess[].last_updated` | Timestamp of the latest update to the series, with a UTC offset such as `-05`. Results are sorted by this field. |
| `seriess[].observation_start / seriess[].observation_end` | Dates of the first and last data points in the series. |
| `seriess[].frequency / seriess[].frequency_short` | How often the series reports, as a full word (`Monthly`) and a short code (`M`). |
| `seriess[].units / seriess[].units_short` | The unit the series values are measured in, such as `Units`. |
| `seriess[].seasonal_adjustment / seriess[].seasonal_adjustment_short` | Whether the series is seasonally adjusted, as full text and a short code (`SA`). |
| `seriess[].popularity` | FRED popularity score for the series. |
| `seriess[].notes` | Description of the series. Long text may be cut. |

### Notes

- Format `start_time` and `end_time` as `YYYYMMDDHhmm`, for example `202610270000`. Both are required.
- Page with `limit` (1 to 1000) and `offset`. Compare `offset` plus `limit` against `count` to know when to stop.
- `filter_value` accepts `macro`, `regional` or `all`. The response echoes it with `filter_variable` set to `geography`.
- Call [FRED Get Series Observations](/apis/fred/series-observations) with a series `id` to get its data values, or [FRED Get Series](/apis/fred/series) for its metadata.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/series-updates.json`](../../../catalog/models/fred/series-updates.json) · Store page: https://www.sandbase.ai/model/fred/series-updates
