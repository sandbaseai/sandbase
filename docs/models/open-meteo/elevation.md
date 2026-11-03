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

Returns terrain elevation in meters for one or more coordinates, taken from a 90 m digital elevation model. You send WGS84 `latitude` and `longitude` values, either as single numbers or as comma-separated lists.

### Use cases

- Add ground elevation to a list of store or site locations before analysis.
- Correct a weather forecast or temperature reading for the height of a location.
- Check the elevation of several waypoints on a hiking or cycling route in one request.
- Fill in missing altitude values in a dataset of GPS points.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/elevation" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": "52.52,48.85", "longitude": "13.41,2.35"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `latitude` | string | Yes | WGS84 latitude, or a comma-separated list of up to 100 latitudes. |
| `longitude` | string | Yes | WGS84 longitude, or a comma-separated list of up to 100 longitudes (positions aligned with `latitude`). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "elevation": [
    38.0
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `elevation` | List of terrain elevations in meters, one per requested coordinate. |
| `elevation[0]` | Elevation for the first coordinate pair. For the example request this is `38.0` for `52.52`, `13.41`. |
| `elevation[1]` | Elevation for the second coordinate pair. For the example request this is `46.0` for `48.85`, `2.35`. |

### Notes

- Send up to 100 coordinates in one request. Put them in `latitude` and `longitude` as comma-separated lists.
- Values in `elevation` appear in the same order as the input coordinates. Position 0 in `latitude` pairs with position 0 in `longitude`.
- If you only have a place name, use [Open-Meteo Geocoding](/apis/open-meteo/geocoding) first to get its coordinates.
- To get weather for the same coordinates, use [Open-Meteo Weather Forecast](/apis/open-meteo/forecast).

### Pricing

$0.0001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/open-meteo/elevation.json`](../../../catalog/models/open-meteo/elevation.json) · Store page: https://www.sandbase.ai/model/open-meteo/elevation
