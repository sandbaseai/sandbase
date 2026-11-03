# FRED Get Series Vintage Dates API: pricing, parameters and code examples

`fred/series-vintagedates` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Series Vintage Dates from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/series-vintagedates", "series_id": "GNPCA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/series-vintagedates', {'series_id': 'GNPCA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/series-vintagedates", {
  "series_id": "GNPCA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/series-vintagedates", sandbase.Params{
	"series_id": "GNPCA",
})
```

Same call via the path form: `POST /v1/api/fred/series-vintagedates` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 10000, optional, default: 10000 default `10000`; range 1–10000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `series_id` | string | yes | The id for a series. string, required  |
| `sort_order` | string |  | Sort results is ascending or descending vintage_date order. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) default `"9999-12-31"` |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: 1776-07-04 (earliest available) default `"1776-07-04"` |

## Details

This API returns the vintage dates for one FRED series. A vintage date is a date on which the series data was revised or newly released. It needs a `series_id`, such as `GNPCA`.

### Use cases

- Find every date on which the values of a series such as `GNPCA` changed, to audit its revision history.
- Pick a vintage date to rebuild what a series looked like at a past point in time.
- Count how many times a series has been revised by reading `count`.
- Page through a long revision history in newest-first order with `sort_order` set to `desc`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series-vintagedates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "GNPCA", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_id` | string | Yes | The id for a series. string, required |
| `file_type` | string | No | Response format. Only json is supported. |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 10000, optional, default: 10000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: 1776-07-04 (earliest available) |
| `sort_order` | string | No | Sort results is ascending or descending vintage_date order. One of the following strings: 'asc', 'desc'. optional, default: asc |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 189,
  "limit": 10000,
  "offset": 0,
  "order_by": "vintage_date",
  "realtime_end": "9999-12-31",
  "realtime_start": "1776-07-04",
  "sort_order": "asc",
  "vintage_dates": [
    "1958-12-21"
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `vintage_dates[]` | List of vintage dates as `YYYY-MM-DD` strings. Each one is a date when the series data was revised or released. The order follows `sort_order`. |
| `count` | Total number of vintage dates found for the series in the real-time period. Use it to know how many pages to request. |
| `limit / offset` | Echo of the page size and starting position used for this response. |
| `order_by` | The field the list is sorted by. It shows `vintage_date`. |
| `sort_order` | Direction of the sort, `asc` or `desc`. |
| `realtime_start / realtime_end` | The real-time period applied to the request. The defaults cover the full range, `1776-07-04` to `9999-12-31`. |

### Notes

- Get the `series_id` from [FRED Search Series](/apis/fred/series-search) or [FRED Get Series](/apis/fred/series).
- To page through results, raise `offset` by `limit` until you have read `count` dates.
- Pass a vintage date as `realtime_start` and `realtime_end` to [FRED Get Series Observations](/apis/fred/series-observations) to see the values as of that date.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/series-vintagedates.json`](../../../catalog/models/fred/series-vintagedates.json) · Store page: https://www.sandbase.ai/model/fred/series-vintagedates
