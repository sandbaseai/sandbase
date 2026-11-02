# FRED Get Series Updates API: pricing, parameters and code examples

`fred/series-updates` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Series Updates from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/series-updates", "end_time": "202610280000", "start_time": "202610270000"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/series-updates', {'end_time': '202610280000', 'start_time': '202610270000'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/series-updates", {
  "end_time": "202610280000",
  "start_time": "202610270000"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/series-updates", sandbase.Params{
	"end_time": "202610280000",
	"start_time": "202610270000",
})
```

Same call via the path form: `POST /v1/api/fred/series-updates` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `end_time` | string | yes | End time for limiting results for a time range, can filter down to minutes YYYYMMDDHhmm formatted string, optional, , start_time is required if end_time is set < Example: 2018-03-02 2:20 would be 201803020220  |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `start_time` | string | yes | Start time for limiting results for a time range, can filter down to minutes YYYYMMDDHhmm formatted string, optional, end_time is required if start_time is set Example: 2018-03-02 14:20 would be 201803021420  |
| `filter_value` | string |  | Limit results by geographic type of economic data series; namely 'macro', 'regional', and 'all'. String, optional, default: 'all' meaning no filter. One of the values: 'macro', 'regional', 'all' 'macro' limits results… default `"all"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Get Series Updates from FRED. Returns the official FRED API response unchanged.

The response is the official FRED API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series-updates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_time": "202610270000", "end_time": "202610280000", "limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_time` | string | Yes | End time for limiting results for a time range, can filter down to minutes YYYYMMDDHhmm formatted string, optional, , start_time is required if end_time is set  |
| `file_type` | string | No | Response format. Only json is supported. |
| `filter_value` | string | No | Limit results by geographic type of economic data series; namely 'macro', 'regional', and 'all'. String, optional, default: 'all' meaning no filter. One of the  |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `start_time` | string | Yes | Start time for limiting results for a time range, can filter down to minutes YYYYMMDDHhmm formatted string, optional, end_time is required if start_time is set  |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/fred/series-updates.json`](../../../catalog/models/fred/series-updates.json) · Store page: https://www.sandbase.ai/model/fred/series-updates
