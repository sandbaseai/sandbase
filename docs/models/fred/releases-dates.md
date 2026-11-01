# FRED Get Releases Dates

`fred/releases-dates` · api · FRED

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

Get Releases Dates from FRED. Returns the official FRED API response unchanged.

The response is the official FRED API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/releases-dates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"file_type": "json"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `file_type` | string | No | Response format. Only json is supported. |
| `include_release_dates_with_no_data` | string | No | Determines whether release dates with no data available are returned. The defalut value 'false' excludes release dates that do not have data. In particular, thi |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'release_date', 'release_id', 'release_name'. optional, default: release_date |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: First day of the current year |
| `sort_order` | string | No | Sort results is ascending or descending release date order. One of the following strings: 'asc', 'desc'. optional, default: desc |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/fred/releases-dates.json`](../../../catalog/models/fred/releases-dates.json) · Store page: https://www.sandbase.ai/model/fred/releases-dates
