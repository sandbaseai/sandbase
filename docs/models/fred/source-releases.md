# FRED Get Source Releases

`fred/source-releases` · api · FRED

Get Source Releases from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/source-releases", "source_id": 1}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/source-releases', {'source_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/source-releases", {
  "source_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/source-releases", sandbase.Params{
	"source_id": 1,
})
```

Same call via the path form: `POST /v1/api/fred/source-releases` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'release_id', 'name', 'press_release', 'realtime_start', 'realtime_end'. optional, default: release_id one of: `release_id`, `name`, `press_release`, `realtime_start`, `realtime_end`; default `"release_id"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `source_id` | integer | yes | The id for a source. integer, required  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Get Source Releases from FRED. Returns the official FRED API response unchanged.

The response is the official FRED API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/source-releases" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"source_id": 1, "file_type": "json"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `file_type` | string | No | Response format. Only json is supported. |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'release_id', 'name', 'press_release', 'realtime_start', 'realtime_end'. optio |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |
| `source_id` | integer | Yes | The id for a source. integer, required |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/fred/source-releases.json`](../../../catalog/models/fred/source-releases.json) · Store page: https://www.sandbase.ai/model/fred/source-releases
