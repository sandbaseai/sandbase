# FRED Get Release Series API: pricing, parameters and code examples

`fred/release-series` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Release Series from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/release-series", "release_id": 53}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/release-series', {'release_id': 53})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/release-series", {
  "release_id": 53
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/release-series", sandbase.Params{
	"release_id": 53,
})
```

Same call via the path form: `POST /v1/api/fred/release-series` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated',… one of: `series_id`, `title`, `units`, `frequency`, `seasonal_adjustment`, `realtime_start`, `realtime_end`, `last_updated`, `observation_start`, `observation_end`, `popularity`, `group_popularity`; default `"series_id"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string |  | A semicolon delimited list of tag names that series match all of. String, optional, no filtering by tags by default Example value: 'japan;imports'. Filter results to series having both tags 'japan' and 'imports'. See…  |
| `release_id` | integer | yes | The id for a release. integer, required  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `filter_value` | string |  | The value of the filter_variable attribute to filter results by. String, optional, no filter by default  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `filter_variable` | string |  | The attribute to filter results by. One of the following strings: 'frequency', 'units', 'seasonal_adjustment'. optional, no filter by default one of: `frequency`, `units`, `seasonal_adjustment` |
| `exclude_tag_names` | string |  | A semicolon delimited list of tag names that series match none of. String, optional, no filtering by tags by default. Example value: 'imports;services'. Filter results to series having neither tag 'imports' nor tag…  |

## Details

Returns the list of data series that belong to one FRED release. It needs a `release_id` and returns each series with its title, units, frequency, seasonal adjustment and date range. You can filter by tag, sort, and page through the results.

### Use cases

- List every series in a release to build a catalog of the data it publishes.
- Find the most popular series in a release by sorting on `popularity`.
- Check which series in a release were updated recently using `last_updated`.
- Narrow a release to monthly or seasonally adjusted series with `filter_variable` and `filter_value`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/release-series" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"release_id": 53, "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `release_id` | integer | Yes | The id for a release. integer, required |
| `exclude_tag_names` | string | No | A semicolon delimited list of tag names that series match none of. String, optional, no filtering by tags by default. Example value: 'imports;services'. Filter results to series having neither tag 'imports' nor tag 'serv |
| `file_type` | string | No | Response format. Only json is supported. |
| `filter_value` | string | No | The value of the filter_variable attribute to filter results by. String, optional, no filter by default |
| `filter_variable` | string | No | The attribute to filter results by. One of the following strings: 'frequency', 'units', 'seasonal_adjustment'. optional, no filter by default |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'observation_start',  |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |
| `tag_names` | string | No | A semicolon delimited list of tag names that series match all of. String, optional, no filtering by tags by default Example value: 'japan;imports'. Filter results to series having both tags 'japan' and 'imports'. See the |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 12715,
  "limit": 1000,
  "offset": 0,
  "order_by": "series_id",
  "realtime_end": "2026-11-03",
  "realtime_start": "2026-11-03",
  "seriess": [
    {
      "frequency": "Annual",
      "frequency_short": "A",
      "group_popularity": 7,
      "id": "A001RD3A086NBEA",
      "last_updated": "2026-09-30 07:59:53-05",
      "notes": "BEA Account Code: A001RD\n\nFor more information about this series, please see htt…",
      "observation_end": "2025-01-01",
      "observation_start": "1929-01-01",
      "popularity": 7,
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
| `count` | Total number of series in the release that match the request. Compare it with `limit` and `offset` to see how many pages remain. |
| `seriess[].id` | The FRED series ID, for example `A001RD3A086NBEA`. Use it to look up the series or fetch its observations. |
| `seriess[].title` | Human-readable name of the series. |
| `seriess[].frequency / seriess[].frequency_short` | How often the series has a data point, as a full word (`Annual`) and a short code (`A`). |
| `seriess[].units / seriess[].units_short` | The unit of the series values, in long and short form, for example `Index 2017=100`. |
| `seriess[].seasonal_adjustment / seriess[].seasonal_adjustment_short` | Whether the series is seasonally adjusted, in long and short form, for example `Not Seasonally Adjusted` and `NSA`. |
| `seriess[].observation_start / seriess[].observation_end` | First and last observation dates of the series, in `YYYY-MM-DD` format. |
| `seriess[].popularity / seriess[].group_popularity` | Popularity scores for the series and for its group of related series. Higher numbers mean more popular. |
| `seriess[].last_updated` | Date and time of the last update to the series, with a UTC offset. |
| `seriess[].notes` | Free-text description of the series, often with a source account code and a link. |

### Notes

- Get a `release_id` from [FRED Get Releases](/apis/fred/releases). The sample request uses `release_id` `53`.
- Page through results with `limit` (1 to 1000) and `offset`. This sample has `count` 12715 and returned 1000 per page at most.
- Use `order_by` and `sort_order` to control ordering. The default is `series_id` ascending.
- Pass a series `id` to [FRED Get Series Observations](/apis/fred/series-observations) to get the data values.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/release-series.json`](../../../catalog/models/fred/release-series.json) · Store page: https://www.sandbase.ai/model/fred/release-series
