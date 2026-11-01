# FRED GeoFRED Series Group

`fred/geo-series-group` · api · FRED

GeoFRED Series Group from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/geo-series-group", "series_id": "WIPCPI"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/geo-series-group', {'series_id': 'WIPCPI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/geo-series-group", {
  "series_id": "WIPCPI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/geo-series-group", sandbase.Params{
	"series_id": "WIPCPI",
})
```

Same call via the path form: `POST /v1/api/fred/geo-series-group` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `series_id` | string | yes | The FRED series id you want to request maps meta information for. Not all series that are in FRED have geographical data. string, required  |

## Details

GeoFRED Series Group from FRED. Returns the official FRED API response unchanged.

The response is the official FRED API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/geo-series-group" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "WIPCPI", "file_type": "json"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `file_type` | string | No | Response format. Only json is supported. |
| `series_id` | string | Yes | The FRED series id you want to request maps meta information for. Not all series that are in FRED have geographical data. string, required |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/fred/geo-series-group.json`](../../../catalog/models/fred/geo-series-group.json) · Store page: https://www.sandbase.ai/model/fred/geo-series-group
