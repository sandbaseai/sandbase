# FRED Get Tags Series API: pricing, parameters and code examples

`fred/tags-series` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Tags Series from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/tags-series", "tag_names": "usa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/tags-series', {'tag_names': 'usa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/tags-series", {
  "tag_names": "usa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/tags-series", sandbase.Params{
	"tag_names": "usa",
})
```

Same call via the path form: `POST /v1/api/fred/tags-series` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated',… one of: `series_id`, `title`, `units`, `frequency`, `seasonal_adjustment`, `realtime_start`, `realtime_end`, `last_updated`, `observation_start`, `observation_end`, `popularity`, `group_popularity`; default `"series_id"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string | yes | A semicolon delimited list of tag names that series match all of. String, required, no default value. Example value: 'slovenia;food'. Filter results to series having both tags 'slovenia' and 'food'. See the related…  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `exclude_tag_names` | string |  | A semicolon delimited list of tag names that series match none of. String, optional, no default value. Example value: 'alchohol;quarterly'. Filter results to series having neither tag 'alchohol' nor tag 'quarterly'.  |

## Details

Returns the FRED data series that carry all of the tags you list. You send one or more tag names in `tag_names`, and the response lists matching series with their title, units, frequency and date range.

### Use cases

- List every FRED series tagged `usa` and `quarterly` to build a catalog of U.S. quarterly indicators.
- Sort matches by `popularity` to find the most used series for a topic.
- Exclude unwanted tags with `exclude_tag_names` to narrow a broad tag down to the series you need.
- Page through all matches to sync series IDs and metadata into your own database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/tags-series" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tag_names": "usa", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_names` | string | Yes | A semicolon delimited list of tag names that series match all of. String, required, no default value. Example value: 'slovenia;food'. Filter results to series having both tags 'slovenia' and 'food'. See the related reque |
| `exclude_tag_names` | string | No | A semicolon delimited list of tag names that series match none of. String, optional, no default value. Example value: 'alchohol;quarterly'. Filter results to series having neither tag 'alchohol' nor tag 'quarterly'. |
| `file_type` | string | No | Response format. Only json is supported. |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'observation_start',  |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 679198,
  "limit": 1000,
  "offset": 0,
  "order_by": "series_id",
  "realtime_end": "2026-11-03",
  "realtime_start": "2026-11-03",
  "seriess": [
    {
      "frequency": "Quarterly",
      "frequency_short": "Q",
      "group_popularity": 1,
      "id": "101458USN",
      "last_updated": "2026-09-08 09:11:33-05",
      "notes": "Further information related to the Quarterly Financial Report survey can be foun…",
      "observation_end": "2026-04-01",
      "observation_start": "2000-10-01",
      "popularity": 1,
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
| `count` | Total number of series that match the tag filter. Use it with `limit` and `offset` to page through results. |
| `limit / offset / order_by / sort_order` | Echo of the paging and sorting settings used for this response. |
| `realtime_start / realtime_end` | The real-time period applied to the request, as `YYYY-MM-DD` dates. Each series item repeats these values. |
| `seriess[].id` | The FRED series ID, for example `101458USN`. Use it to look up the series in other FRED calls. |
| `seriess[].title` | Full name of the series. |
| `seriess[].frequency / seriess[].frequency_short` | How often the series is observed, as a full word (`Quarterly`) and a short code (`Q`). |
| `seriess[].units / seriess[].units_short` | The unit of the values, as a full label (`Millions of Dollars`) and a short label. |
| `seriess[].seasonal_adjustment / seriess[].seasonal_adjustment_short` | Whether the series is seasonally adjusted, as a full label (`Not Seasonally Adjusted`) and a short code (`NSA`). |
| `seriess[].observation_start / seriess[].observation_end` | First and last observation dates of the series. |
| `seriess[].popularity / seriess[].group_popularity` | Popularity scores for the series and for its group of related series. |

### Notes

- The series list is under the key `seriess` (with a double s).
- Use `limit` (1 to 1000) and `offset` to page. Compare `offset` plus `limit` against `count` to know when to stop.
- Get valid tag names from [FRED Get Tags](/apis/fred/tags). Separate several names with a semicolon, for example `usa;quarterly`.
- Pass a series `id` to [FRED Get Series Observations](/apis/fred/series-observations) to fetch the data values.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/tags-series.json`](../../../catalog/models/fred/tags-series.json) · Store page: https://www.sandbase.ai/model/fred/tags-series
