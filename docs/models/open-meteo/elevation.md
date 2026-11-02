# Open-Meteo Elevation API: pricing, parameters and code examples

`open-meteo/elevation` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Terrain elevation in meters for one or more coordinates, from a 90 m digital elevation model.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/elevation", "latitude": "52.52,48.85", "longitude": "13.41,2.35"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/elevation', {'latitude': '52.52,48.85', 'longitude': '13.41,2.35'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/elevation", {
  "latitude": "52.52,48.85",
  "longitude": "13.41,2.35"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/elevation", sandbase.Params{
	"latitude": "52.52,48.85",
	"longitude": "13.41,2.35",
})
```

Same call via the path form: `POST /v1/api/open-meteo/elevation` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `latitude` | string | yes | WGS84 latitude, or a comma-separated list of up to 100 latitudes.  |
| `longitude` | string | yes | WGS84 longitude, or a comma-separated list of up to 100 longitudes (positions aligned with `latitude`).  |

## Details

Terrain elevation in meters for one or more coordinates, from a 90 m digital elevation model.

The result is returned in `outputs[0].data` as the official Open-Meteo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/elevation" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": "52.52,48.85", "longitude": "13.41,2.35"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `latitude` | string | Yes | WGS84 latitude, or a comma-separated list of up to 100 latitudes. |
| `longitude` | string | Yes | WGS84 longitude, or a comma-separated list of up to 100 longitudes (positions aligned with `latitude`). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/open-meteo/elevation.json`](../../../catalog/models/open-meteo/elevation.json) · Store page: https://www.sandbase.ai/model/open-meteo/elevation
