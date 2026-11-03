# FRED Search Series API: pricing, parameters and code examples

`fred/series-search` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Search Series from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/series-search", "search_text": "unemployment"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/series-search', {'search_text': 'unemployment'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/series-search", {
  "search_text": "unemployment"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/series-search", sandbase.Params{
	"search_text": "unemployment",
})
```

Same call via the path form: `POST /v1/api/fred/series-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'search_rank', 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated',… one of: `search_rank`, `series_id`, `title`, `units`, `frequency`, `seasonal_adjustment`, `realtime_start`, `realtime_end`, `last_updated`, `observation_start`, `observation_end`, `popularity` … |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string |  | A semicolon delimited list of tag names that series match all of. String, optional, no filtering by tags by default Example value: 'usa;m2'. Filter results to series having both tags 'usa' and 'm2'. See the related…  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: If order_by is equal to 'search_rank' or 'popularity', then the… one of: `asc`, `desc` |
| `search_text` | string | yes | The words to match against economic data series.  |
| `search_type` | string |  | Determines the type of search to perform. One of the following strings: 'full_text', 'series_id'. 'full_text' searches series attributes title, units, frequency, and tags by parsing words into stems. This makes it… one of: `full_text`, `series_id`; default `"full_text"` |
| `filter_value` | string |  | The value of the filter_variable attribute to filter results by. String, optional, no filter by default  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `filter_variable` | string |  | The attribute to filter results by. One of the following strings: 'frequency', 'units', 'seasonal_adjustment'. optional, no filter by default one of: `frequency`, `units`, `seasonal_adjustment` |
| `exclude_tag_names` | string |  | A semicolon delimited list of tag names that series match none of. String, optional, no filtering by tags by default. Example value: 'discontinued;m1'. Filter results to series having neither tag 'discontinued' nor tag…  |

## Details

Searches FRED economic data series by keyword or series ID. It returns a list of matching series with title, units, frequency, seasonal adjustment and the dates the data covers. It needs one input, `search_text`.

### Use cases

- Find the FRED series ID for a topic such as unemployment before you pull its data.
- Compare seasonally adjusted and not seasonally adjusted versions of the same series.
- Build a search box for economic indicators that ranks results by `popularity`.
- List all monthly series that match a keyword by using `filter_variable` and `filter_value`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_text": "unemployment", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_text` | string | Yes | The words to match against economic data series. |
| `exclude_tag_names` | string | No | A semicolon delimited list of tag names that series match none of. String, optional, no filtering by tags by default. Example value: 'discontinued;m1'. Filter results to series having neither tag 'discontinued' nor tag ' |
| `file_type` | string | No | Response format. Only json is supported. |
| `filter_value` | string | No | The value of the filter_variable attribute to filter results by. String, optional, no filter by default |
| `filter_variable` | string | No | The attribute to filter results by. One of the following strings: 'frequency', 'units', 'seasonal_adjustment'. optional, no filter by default |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'search_rank', 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'obser |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `search_type` | string | No | Determines the type of search to perform. One of the following strings: 'full_text', 'series_id'. 'full_text' searches series attributes title, units, frequency, and tags by parsing words into stems. This makes it possib |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: If order_by is equal to 'search_rank' or 'popularity', then the de |
| `tag_names` | string | No | A semicolon delimited list of tag names that series match all of. String, optional, no filtering by tags by default Example value: 'usa;m2'. Filter results to series having both tags 'usa' and 'm2'. See the related reque |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 53486,
  "limit": 1000,
  "offset": 0,
  "order_by": "search_rank",
  "realtime_end": "2026-11-03",
  "realtime_start": "2026-11-03",
  "seriess": [
    {
      "frequency": "Monthly",
      "frequency_short": "M",
      "group_popularity": 96,
      "id": "UNRATE",
      "last_updated": "2026-10-02 08:24:37-05",
      "notes": "The unemployment rate represents the number of unemployed as a percentage of the…",
      "observation_end": "2026-09-01",
      "observation_start": "1948-01-01",
      "popularity": 96,
      "realtime_end": "2026-11-03",
      "realtime_start": "2026-11-03",
      "seasonal_adjustment": "Seasonally Adjusted"
    }
  ],
  "sort_order": "desc"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of series that match the search. This can be larger than the number of rows returned in one call. |
| `limit / offset / order_by / sort_order` | Echo of the paging and sorting settings used for this response. In the example, results are sorted by `search_rank` in `desc` order. |
| `seriess[].id` | FRED series ID, such as `UNRATE`. Use it to fetch details or observations for that series. |
| `seriess[].title` | Name of the series. |
| `seriess[].units / seriess[].units_short` | Unit of the series values in long and short form, such as `Percent` and `%`. |
| `seriess[].frequency / seriess[].frequency_short` | How often the series is published, such as `Monthly` and `M`. |
| `seriess[].seasonal_adjustment / seriess[].seasonal_adjustment_short` | Whether the series is seasonally adjusted, such as `Seasonally Adjusted` and `SA`. |
| `seriess[].observation_start / seriess[].observation_end` | First and last observation dates of the series, formatted `YYYY-MM-DD`. |
| `seriess[].popularity / seriess[].group_popularity` | Popularity scores for the series and for its group of related series. Higher values mean more popular. |
| `seriess[].notes` | Description text for the series. Long text may be cut, and the field may be missing for some series. |

### Notes

- The list is in the `seriess` key (with a double s).
- Page through results with `limit` (1 to 1000) and `offset`. Compare `count` with `offset` to see how many results remain.
- `last_updated` uses the format `YYYY-MM-DD HH:MM:SS` followed by a UTC offset, such as `2026-10-02 08:24:37-05`.
- Pass an `id` to [FRED Get Series Observations](/apis/fred/series-observations) to get the data values, or to [FRED Get Series](/apis/fred/series) for series metadata.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/series-search.json`](../../../catalog/models/fred/series-search.json) · Store page: https://www.sandbase.ai/model/fred/series-search
