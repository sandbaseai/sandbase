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

Search Series from FRED. Returns the official FRED API response unchanged.

The response is the official FRED API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_text": "unemployment", "file_type": "json"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `exclude_tag_names` | string | No | A semicolon delimited list of tag names that series match none of. String, optional, no filtering by tags by default. Example value: 'discontinued;m1'. Filter r |
| `file_type` | string | No | Response format. Only json is supported. |
| `filter_value` | string | No | The value of the filter_variable attribute to filter results by. String, optional, no filter by default |
| `filter_variable` | string | No | The attribute to filter results by. One of the following strings: 'frequency', 'units', 'seasonal_adjustment'. optional, no filter by default |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'search_rank', 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustmen |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `search_text` | string | Yes | The words to match against economic data series. |
| `search_type` | string | No | Determines the type of search to perform. One of the following strings: 'full_text', 'series_id'. 'full_text' searches series attributes title, units, frequency |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: If ord |
| `tag_names` | string | No | A semicolon delimited list of tag names that series match all of. String, optional, no filtering by tags by default Example value: 'usa;m2'. Filter results to s |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/fred/series-search.json`](../../../catalog/models/fred/series-search.json) · Store page: https://www.sandbase.ai/model/fred/series-search
