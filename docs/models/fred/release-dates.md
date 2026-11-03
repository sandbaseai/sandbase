# FRED Get Release Dates API: pricing, parameters and code examples

`fred/release-dates` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Release Dates from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/release-dates", "release_id": 53}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/release-dates', {'release_id': 53})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/release-dates", {
  "release_id": 53
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/release-dates", sandbase.Params{
	"release_id": 53,
})
```

Same call via the path form: `POST /v1/api/fred/release-dates` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 10000, optional, default: 10000 default `10000`; range 1–10000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `release_id` | integer | yes | The id for a release. integer, required  |
| `sort_order` | string |  | Sort results is ascending or descending release date order. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) default `"9999-12-31"` |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: 1776-07-04 (earliest available) default `"1776-07-04"` |
| `include_release_dates_with_no_data` | string |  | Determines whether release dates with no data available are returned. The defalut value 'false' excludes release dates that do not have data. In particular, this excludes future release dates which may be available in… one of: `true`, `false`; default `"false"` |

## Details

Returns the list of dates on which a FRED data release was published or scheduled. It needs a `release_id` and returns one entry per release date, along with the paging and real-time period settings used for the query.

### Use cases

- Build a calendar of past publication dates for a single economic release.
- Measure how often a release is published by comparing consecutive `release_dates[].date` values.
- Check the full publication history of a release before you pull its series data.
- Page through a long release history in chunks using `limit` and `offset`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/release-dates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"release_id": 53, "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `release_id` | integer | Yes | The id for a release. integer, required |
| `file_type` | string | No | Response format. Only json is supported. |
| `include_release_dates_with_no_data` | string | No | Determines whether release dates with no data available are returned. The defalut value 'false' excludes release dates that do not have data. In particular, this excludes future release dates which may be available in th |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 10000, optional, default: 10000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: 1776-07-04 (earliest available) |
| `sort_order` | string | No | Sort results is ascending or descending release date order. One of the following strings: 'asc', 'desc'. optional, default: asc |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 858,
  "limit": 10000,
  "offset": 0,
  "order_by": "release_date",
  "realtime_end": "9999-12-31",
  "realtime_start": "1776-07-04",
  "release_dates": [
    {
      "date": "1947-07-20",
      "release_id": 53
    }
  ],
  "sort_order": "asc"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `release_dates[].date` | The date of one release, formatted as YYYY-MM-DD. |
| `release_dates[].release_id` | The id of the release this date belongs to. It matches the `release_id` you sent. |
| `count` | The total number of release dates that match the query. Use it to decide how many pages to fetch. |
| `limit / offset` | The page size and the starting position used for this response. |
| `order_by` | The field the results are sorted by. In this response it is `release_date`. |
| `sort_order` | The direction of the sort, `asc` or `desc`. |
| `realtime_start / realtime_end` | The real-time period applied to the query, formatted as YYYY-MM-DD. |

### Notes

- `release_id` is required. To find an id, call [FRED Get Releases](/apis/fred/releases) or [FRED Get Series Release](/apis/fred/series-release).
- Page through results with `limit` (1 to 10000) and `offset`. Compare `count` with `offset` to see if more rows remain.
- By default, release dates with no data are excluded, which also leaves out future dates. Set `include_release_dates_with_no_data` to `true` to include them.
- To see details about the release itself, call [FRED Get Release](/apis/fred/release).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/release-dates.json`](../../../catalog/models/fred/release-dates.json) · Store page: https://www.sandbase.ai/model/fred/release-dates
