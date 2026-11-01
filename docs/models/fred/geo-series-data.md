# FRED GeoFRED Series Data

`fred/geo-series-data` · api · FRED

GeoFRED Series Data from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/geo-series-data", "series_id": "WIPCPI"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/geo-series-data', {'series_id': 'WIPCPI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/geo-series-data", {
  "series_id": "WIPCPI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/geo-series-data", sandbase.Params{
	"series_id": "WIPCPI",
})
```

Same call via the path form: `POST /v1/api/fred/geo-series-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string |  | The date you want to request series group data from. YYYY-MM-DD formatted string, optional  |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `series_id` | string | yes | The FRED series_id you want to request maps data for. Not all series that are in FRED have geographical data. string, required  |
| `start_date` | string |  | The start date you want to request series group data from. This allows you to pull a range of data YYYY-MM-DD formatted string, optional  |

## Details

GeoFRED Series Data from FRED. Returns the official FRED API response unchanged.

The response is the official FRED API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/geo-series-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "WIPCPI", "file_type": "json"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date` | string | No | The date you want to request series group data from. YYYY-MM-DD formatted string, optional |
| `file_type` | string | No | Response format. Only json is supported. |
| `series_id` | string | Yes | The FRED series_id you want to request maps data for. Not all series that are in FRED have geographical data. string, required |
| `start_date` | string | No | The start date you want to request series group data from. This allows you to pull a range of data YYYY-MM-DD formatted string, optional |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/fred/geo-series-data.json`](../../../catalog/models/fred/geo-series-data.json) · Store page: https://www.sandbase.ai/model/fred/geo-series-data
