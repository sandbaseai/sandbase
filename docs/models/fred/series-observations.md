# FRED Get Series Observations API: pricing, parameters and code examples

`fred/series-observations` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Series Observations from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/series-observations", "series_id": "GNPCA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/series-observations', {'series_id': 'GNPCA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/series-observations", {
  "series_id": "GNPCA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/series-observations", sandbase.Params{
	"series_id": "GNPCA",
})
```

Same call via the path form: `POST /v1/api/fred/series-observations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 100000, optional, default: 100000 default `100000`; range 1–100000 |
| `units` | string |  | A key that indicates a data value transformation. string, optional, default: lin (No transformation) One of the following values: 'lin', 'chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log' lin = Levels (No… one of: `lin`, `chg`, `ch1`, `pch`, `pc1`, `pca`, `cch`, `cca`, `log`; default `"lin"` |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `frequency` | string |  | An optional parameter that indicates a lower frequency to aggregate values to. The FRED frequency aggregation feature converts higher frequency data series into lower frequency data series (e.g. converts a monthly data… one of: `d`, `w`, `bw`, `m`, `q`, `sa`, `a`, `wef`, `weth`, `wew`, `wetu`, `wem` … |
| `series_id` | string | yes | The id for a series. string, required  |
| `sort_order` | string |  | Sort results is ascending or descending observation_date order. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `output_type` | integer |  | An integer that indicates an output type. integer, optional, default: 1 One of the following values: '1', '2', '3', '4' 1 = Observations by Real-Time Period 2 = Observations by Vintage Date, All Observations 3 =… one of: `1`, `2`, `3`, `4`; default `1` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods , vintage_dates . YYYY-MM-DD formatted string, optional, default: today's date  |
| `vintage_dates` | string |  | A comma separated string of YYYY-MM-DD formatted dates in history (e.g. 2000-01-01,2005-02-24). Vintage dates are used to download data as it existed on these specified dates in history. Vintage dates can be specified…  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods , vintage_dates . YYYY-MM-DD formatted string, optional, default: today's date  |
| `observation_end` | string |  | The end of the observation period. YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) default `"9999-12-31"` |
| `observation_start` | string |  | The start of the observation period. YYYY-MM-DD formatted string, optional, default: 1776-07-04 (earliest available) default `"1776-07-04"` |
| `aggregation_method` | string |  | A key that indicates the aggregation method used for frequency aggregation. This parameter has no affect if the frequency parameter is not set. string, optional, default: avg One of the following values: 'avg', 'sum',… one of: `avg`, `sum`, `eop`; default `"avg"` |

## Details

Returns the observations (date and value pairs) for one FRED data series. It needs a `series_id`, such as `GNPCA`, and can filter by date range, change the units, or aggregate to a lower frequency.

### Use cases

- Pull the full history of a series such as `GNPCA` to chart it or load it into a spreadsheet.
- Request `units` such as `pch` or `pc1` to get percent changes without calculating them yourself.
- Convert a monthly series to annual values with `frequency` and `aggregation_method`.
- Fetch a series as it looked on past dates with `vintage_dates` or `realtime_start` and `realtime_end` to test models on the data known at that time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series-observations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "GNPCA", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_id` | string | Yes | The id for a series. string, required |
| `aggregation_method` | string | No | A key that indicates the aggregation method used for frequency aggregation. This parameter has no affect if the frequency parameter is not set. string, optional, default: avg One of the following values: 'avg', 'sum', 'e |
| `file_type` | string | No | Response format. Only json is supported. |
| `frequency` | string | No | An optional parameter that indicates a lower frequency to aggregate values to. The FRED frequency aggregation feature converts higher frequency data series into lower frequency data series (e.g. converts a monthly data s |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 100000, optional, default: 100000 |
| `observation_end` | string | No | The end of the observation period. YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) |
| `observation_start` | string | No | The start of the observation period. YYYY-MM-DD formatted string, optional, default: 1776-07-04 (earliest available) |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `output_type` | integer | No | An integer that indicates an output type. integer, optional, default: 1 One of the following values: '1', '2', '3', '4' 1 = Observations by Real-Time Period 2 = Observations by Vintage Date, All Observations 3 = Observat |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods , vintage_dates . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods , vintage_dates . YYYY-MM-DD formatted string, optional, default: today's date |
| `sort_order` | string | No | Sort results is ascending or descending observation_date order. One of the following strings: 'asc', 'desc'. optional, default: asc |
| `units` | string | No | A key that indicates a data value transformation. string, optional, default: lin (No transformation) One of the following values: 'lin', 'chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log' lin = Levels (No transformat |
| `vintage_dates` | string | No | A comma separated string of YYYY-MM-DD formatted dates in history (e.g. 2000-01-01,2005-02-24). Vintage dates are used to download data as it existed on these specified dates in history. Vintage dates can be specified in |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 97,
  "file_type": "json",
  "limit": 100000,
  "observation_end": "9999-12-31",
  "observation_start": "1776-07-04",
  "observations": [
    {
      "date": "1929-01-01",
      "realtime_end": "2026-10-30",
      "realtime_start": "2026-10-30",
      "value": "1202.659"
    }
  ],
  "offset": 0,
  "order_by": "observation_date",
  "output_type": 1,
  "realtime_end": "2026-10-30",
  "realtime_start": "2026-10-30",
  "sort_order": "asc"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of observations that match the request. In the example it is `97`. |
| `observations[].date` | Date of the observation in `YYYY-MM-DD` format. For this annual series each date is January 1 of a year. |
| `observations[].value` | Value of the observation as a string. Convert it to a number before you calculate with it. |
| `observations[].realtime_start / observations[].realtime_end` | Start and end of the real-time period in which this value was the current one. Both are `YYYY-MM-DD` dates. |
| `observation_start / observation_end` | Observation date range used for the request. The defaults `1776-07-04` and `9999-12-31` mean no limit. |
| `units` | Transformation applied to the values. `lin` means levels with no transformation. |
| `sort_order / order_by` | Sort direction and the field used to sort the observations. The example uses `asc` and `observation_date`. |
| `limit / offset` | Page size and starting position used for this response. Use them to page through long series. |
| `output_type` | Output type used for the response. The example uses `1`, which is observations by real-time period. |

### Notes

- `series_id` is required. To find an ID, use [FRED Search Series](/apis/fred/series-search).
- Page through long series with `limit` (1 to 100000) and `offset`. Compare `offset` plus the number of returned rows with `count` to know when to stop.
- To see the title, units and frequency of a series, call [FRED Get Series](/apis/fred/series).
- To see the dates on which past values were revised, call [FRED Get Series Vintage Dates](/apis/fred/series-vintagedates).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/series-observations.json`](../../../catalog/models/fred/series-observations.json) · Store page: https://www.sandbase.ai/model/fred/series-observations
