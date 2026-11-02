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

Get Category Series from FRED. Returns the official FRED API response unchanged.

The response is the official FRED API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/category-series" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_id": 125, "file_type": "json"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_id` | integer | Yes | The id for a category. integer, required |
| `exclude_tag_names` | string | No | A semicolon delimited list of tag names that series match none of. String, optional, no filtering by tags by default. Example value: 'discontinued;annual'. Filt |
| `file_type` | string | No | Response format. Only json is supported. |
| `filter_value` | string | No | The value of the filter_variable attribute to filter results by. String, optional, no filter by default |
| `filter_variable` | string | No | The attribute to filter results by. On of the following strings: 'frequency', 'units', 'seasonal_adjustment'. optional, no filter by default |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_s |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', ' desc '. optional, default: asc |
| `tag_names` | string | No | A semicolon delimited list of tag names that series match all of. String, optional, no filtering by tags by default Example value: 'income;bea'. Filter results  |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/fred/category-series.json`](../../../catalog/models/fred/category-series.json) · Store page: https://www.sandbase.ai/model/fred/category-series
