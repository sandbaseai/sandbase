# FRED Get Category Series API: pricing, parameters and code examples

`fred/category-series` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Category Series from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/category-series", "category_id": 125}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/category-series', {'category_id': 125})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/category-series", {
  "category_id": 125
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/category-series", sandbase.Params{
	"category_id": 125,
})
```

Same call via the path form: `POST /v1/api/fred/category-series` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated',… one of: `series_id`, `title`, `units`, `frequency`, `seasonal_adjustment`, `realtime_start`, `realtime_end`, `last_updated`, `observation_start`, `observation_end`, `popularity`, `group_popularity`; default `"series_id"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string |  | A semicolon delimited list of tag names that series match all of. String, optional, no filtering by tags by default Example value: 'income;bea'. Filter results to series having both tags 'income' and 'bea'. See the…  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', ' desc '. optional, default: asc one of: `asc`, ` desc `; default `"asc"` |
| `category_id` | integer | yes | The id for a category. integer, required  |
| `filter_value` | string |  | The value of the filter_variable attribute to filter results by. String, optional, no filter by default  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `filter_variable` | string |  | The attribute to filter results by. On of the following strings: 'frequency', 'units', 'seasonal_adjustment'. optional, no filter by default one of: `frequency`, `units`, `seasonal_adjustment` |
| `exclude_tag_names` | string |  | A semicolon delimited list of tag names that series match none of. String, optional, no filtering by tags by default. Example value: 'discontinued;annual'. Filter results to series having neither tag 'discontinued' nor…  |

## Details

Returns the list of FRED data series that belong to one FRED category. It needs a `category_id` and returns each series with its title, units, frequency, seasonal adjustment and observation date range.

### Use cases

- List every series in a trade or economics category to build a catalog of available indicators.
- Filter a category by `frequency` or `seasonal_adjustment` to find only monthly, seasonally adjusted series.
- Sort a category by `popularity` to find the most used series first.
- Spot discontinued series by checking titles and `observation_end` dates before you build on them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/category-series" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_id": 125, "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_id` | integer | Yes | The id for a category. integer, required |
| `exclude_tag_names` | string | No | A semicolon delimited list of tag names that series match none of. String, optional, no filtering by tags by default. Example value: 'discontinued;annual'. Filter results to series having neither tag 'discontinued' nor t |
| `file_type` | string | No | Response format. Only json is supported. |
| `filter_value` | string | No | The value of the filter_variable attribute to filter results by. String, optional, no filter by default |
| `filter_variable` | string | No | The attribute to filter results by. On of the following strings: 'frequency', 'units', 'seasonal_adjustment'. optional, no filter by default |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'observation_start',  |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', ' desc '. optional, default: asc |
| `tag_names` | string | No | A semicolon delimited list of tag names that series match all of. String, optional, no filtering by tags by default Example value: 'income;bea'. Filter results to series having both tags 'income' and 'bea'. See the relat |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 47,
  "limit": 1000,
  "offset": 0,
  "order_by": "series_id",
  "realtime_end": "2026-11-03",
  "realtime_start": "2026-11-03",
  "seriess": [
    {
      "frequency": "Monthly",
      "frequency_short": "M",
      "group_popularity": 26,
      "id": "AITGCBN",
      "last_updated": "2026-10-28 07:32:37-05",
      "notes": "This advance estimate represents the current month statistics of nearly complete…",
      "observation_end": "2026-09-01",
      "observation_start": "2026-09-01",
      "popularity": 6,
      "realtime_end": "2026-11-03",
      "realtime_start": "2026-11-03",
      "seasonal_adjustment": "Not Seasonally Adjusted"
    }
  ],
  "sort_order": "asc"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of series in the category that match the request. Use it with `limit` and `offset` to page through results. |
| `limit / offset / order_by / sort_order` | Echo of the paging and sorting settings applied to this response. |
| `realtime_start / realtime_end` | Real-time period used for the request, as `YYYY-MM-DD` dates. Each series entry repeats them. |
| `seriess[].id` | FRED series ID, such as `AITGCBN`. Pass it to other series APIs. |
| `seriess[].title` | Human readable name of the series. |
| `seriess[].frequency / seriess[].frequency_short` | How often the series is observed, as a full word (`Monthly`) and a short code (`M`). |
| `seriess[].units / seriess[].units_short` | Units of the series values, in long and short form, such as `Millions of Dollars` and `Mil. of $`. |
| `seriess[].seasonal_adjustment / seasonal_adjustment_short` | Whether the series is seasonally adjusted, in long and short form (`SA`, `NSA`). |
| `seriess[].observation_start / seriess[].observation_end` | First and last observation dates of the series, formatted `YYYY-MM-DD`. |
| `seriess[].popularity / seriess[].group_popularity` | Popularity scores for the series and for its group of related series. Higher numbers are more popular. |

### Notes

- The list key is spelled `seriess` in the response.
- `limit` defaults to 1000 and `offset` defaults to 0. Raise `offset` to read further pages when `count` is larger than `limit`.
- `last_updated` uses the format `YYYY-MM-DD HH:MM:SS` followed by a UTC offset. The `notes` field appears only on some series.
- To get values for a series, call [FRED Get Series Observations](/apis/fred/series-observations) with its `id`. To browse subcategories, use [FRED Get Category Children](/apis/fred/category-children).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/category-series.json`](../../../catalog/models/fred/category-series.json) · Store page: https://www.sandbase.ai/model/fred/category-series
