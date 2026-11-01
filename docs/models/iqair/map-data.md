# IQAir Map Data

`iqair/map-data` · api · IQAir

Air quality station clusters for map visualization. Returns geographic clusters with aggregated AQI values and station counts within the specified bounding box.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "iqair/map-data"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('iqair/map-data', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("iqair/map-data", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "iqair/map-data", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/iqair/map-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bbox` | string |  | Bounding box as comma-separated string: minLng,minLat,maxLng,maxLat (e.g. '-122.5,37.0,-121.5,38.0'). Omitting returns global data.  |
| `zoom` | integer |  | Map zoom level (1-20). Higher values return more granular clusters with fewer stations per cluster. range -9007199254740991–9007199254740991 |

## Details

Air quality station clusters for map visualization. Returns geographic clusters with aggregated AQI values and station counts within the specified bounding box.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/iqair/map-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bbox` | string | No | Bounding box as comma-separated string: minLng,minLat,maxLng,maxLat (e.g. '-122.5,37.0,-121.5,38.0'). Omitting returns global data. |
| `zoom` | integer | No | Map zoom level (1-20). Higher values return more granular clusters with fewer stations per cluster. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/iqair/map-data.json`](../../../catalog/models/iqair/map-data.json) · Store page: https://www.sandbase.ai/model/iqair/map-data
