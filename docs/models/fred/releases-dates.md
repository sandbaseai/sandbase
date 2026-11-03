# FRED Get Releases Dates API: pricing, parameters and code examples

`fred/releases-dates` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Releases Dates from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/releases-dates"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/releases-dates', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/releases-dates", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/releases-dates", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/fred/releases-dates` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'release_date', 'release_id', 'release_name'. optional, default: release_date one of: `release_date`, `release_id`, `release_name`; default `"release_date"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `sort_order` | string |  | Sort results is ascending or descending release date order. One of the following strings: 'asc', 'desc'. optional, default: desc one of: `asc`, `desc`; default `"desc"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) default `"9999-12-31"` |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: First day of the current year  |
| `include_release_dates_with_no_data` | string |  | Determines whether release dates with no data available are returned. The defalut value 'false' excludes release dates that do not have data. In particular, this excludes future release dates which may be available in… one of: `true`, `false`; default `"false"` |

## Details

Returns release dates for all FRED data releases, one row per release and date, with the release ID and name. It needs no required input. You can page through results and change the sort order and real-time window.

### Use cases

- Build a calendar of upcoming and past economic data releases across FRED.
- Find which releases publish on a given day, such as `2026-11-02`.
- Collect `release_id` values to pass to release-level APIs.
- Sort by `release_name` to list the dates for each release in one place.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/releases-dates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `file_type` | string | No | Response format. Only json is supported. |
| `include_release_dates_with_no_data` | string | No | Determines whether release dates with no data available are returned. The defalut value 'false' excludes release dates that do not have data. In particular, this excludes future release dates which may be available in th |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'release_date', 'release_id', 'release_name'. optional, default: release_date |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: First day of the current year |
| `sort_order` | string | No | Sort results is ascending or descending release date order. One of the following strings: 'asc', 'desc'. optional, default: desc |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 115853,
  "limit": 1000,
  "offset": 0,
  "order_by": "release_date",
  "realtime_end": "9999-12-31",
  "realtime_start": "1776-07-04",
  "release_dates": [
    {
      "date": "2026-11-02",
      "release_id": 488,
      "release_name": "Brave-Butters-Kelley Indexes"
    }
  ],
  "sort_order": "desc"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of release date rows that match the request. Use it to plan paging. |
| `limit / offset` | The page size and starting position used for this response. |
| `order_by / sort_order` | The attribute and direction used to sort the rows. The sample uses `release_date` in `desc` order. |
| `realtime_start / realtime_end` | The real-time period applied to the query, as YYYY-MM-DD dates. |
| `release_dates[].date` | The release date in YYYY-MM-DD format. |
| `release_dates[].release_id` | Numeric ID of the release. Use it to look up that release in other FRED APIs. |
| `release_dates[].release_name` | Name of the release, such as `Commercial Paper`. |

### Notes

- Page through results with `limit` (1 to 1000) and `offset`. Compare `offset` plus `limit` with `count` to know when to stop.
- By default, dates with no data are excluded. Set `include_release_dates_with_no_data` to `true` to include them, such as future dates in the release calendar.
- To get dates for a single release, call [FRED Get Release Dates](/apis/fred/release-dates) with a `release_id` from this response.
- For details on a release, call [FRED Get Release](/apis/fred/release) or [FRED Get Release Series](/apis/fred/release-series).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/releases-dates.json`](../../../catalog/models/fred/releases-dates.json) · Store page: https://www.sandbase.ai/model/fred/releases-dates
