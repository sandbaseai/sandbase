# Open-Meteo Flood Forecast API: pricing, parameters and code examples

`open-meteo/flood` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Daily river discharge forecast and history for any coordinates from the GloFAS flood model.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/flood", "latitude": "52.52", "longitude": "13.41"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/flood', {'latitude': '52.52', 'longitude': '13.41'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/flood", {
  "latitude": "52.52",
  "longitude": "13.41"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/flood", sandbase.Params{
	"latitude": "52.52",
	"longitude": "13.41",
})
```

Same call via the path form: `POST /v1/api/open-meteo/flood` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `daily` | string |  | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `river_discharge`, `river_discharge_mean`, `river_discharge_median`, `river_discharge_max`, `river_discharge_min`,…  |
| `models` | string |  | Comma-separated GloFAS models. Default best match.  |
| `end_date` | string |  | End of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `ensemble` | boolean |  | Return all ensemble members instead of the aggregate. Default `false`. default `false` |
| `latitude` | string | yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated.  |
| `longitude` | string | yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated.  |
| `past_days` | integer |  | Number of past days to include (0-92). Default 0. default `0` |
| `start_date` | string |  | Start of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `timeformat` | string |  | Time output format. Default `iso8601`. one of: `iso8601`, `unixtime`; default `"iso8601"` |
| `forecast_days` | integer |  | Number of forecast days to return (0-210). Default 92. default `92` |
| `cell_selection` | string |  | Grid-cell preference for the coordinate. Default `nearest`. one of: `land`, `sea`, `nearest`; default `"nearest"` |

## Details

Returns daily river discharge values in cubic meters per second for a pair of coordinates, from the GloFAS flood model. It needs `latitude` and `longitude`. Add `daily` to choose which discharge variables come back.

### Use cases

- Chart the expected river flow near a site over the next weeks to spot rising water.
- Compare recent past discharge with the forecast using `past_days` and `forecast_days`.
- Add a river flow value to a flood risk score for a property or a project location.
- Pull the same discharge series for several coordinates by passing comma-separated `latitude` and `longitude` values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/flood" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": "52.52", "longitude": "13.41", "daily": "river_discharge"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `latitude` | string | Yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated. |
| `longitude` | string | Yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated. |
| `cell_selection` | string | No | Grid-cell preference for the coordinate. Default `nearest`. |
| `daily` | string | No | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `river_discharge`, `river_discharge_mean`, `river_discharge_median`, `river_discharge_max`, `river_discharge_min`, `river |
| `end_date` | string | No | End of the interval, `yyyy-mm-dd` (ISO 8601). |
| `ensemble` | boolean | No | Return all ensemble members instead of the aggregate. Default `false`. |
| `forecast_days` | integer | No | Number of forecast days to return (0-210). Default 92. |
| `models` | string | No | Comma-separated GloFAS models. Default best match. |
| `past_days` | integer | No | Number of past days to include (0-92). Default 0. |
| `start_date` | string | No | Start of the interval, `yyyy-mm-dd` (ISO 8601). |
| `timeformat` | string | No | Time output format. Default `iso8601`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "daily": {
    "river_discharge": [
      0.45
    ],
    "time": [
      "2026-11-03"
    ]
  },
  "daily_units": {
    "river_discharge": "m³/s",
    "time": "iso8601"
  },
  "elevation": 38.0,
  "generationtime_ms": 0.18489360809326172,
  "latitude": 52.525,
  "longitude": 13.425003,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "utc_offset_seconds": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `daily.time[]` | Date of each daily value, in `yyyy-mm-dd` format when `timeformat` is `iso8601`. It lines up by position with the values in `daily.river_discharge[]`. |
| `daily.river_discharge[]` | Forecast river discharge for each date in `daily.time[]`. The unit is given in `daily_units.river_discharge`. |
| `daily_units.river_discharge` | Unit of the discharge values, shown as `m³/s` in this response. |
| `latitude / longitude` | Coordinates of the grid cell the data comes from. They can differ slightly from the requested point, for example `52.525` and `13.425003` for a request of `52.52` and `13.41`. |
| `elevation` | Elevation of the selected grid cell, in the same call as the discharge data. |
| `timezone / timezone_abbreviation / utc_offset_seconds` | Time zone used for the daily dates, here `GMT` with an offset of `0` seconds. |
| `generationtime_ms` | Time the server took to build the response, in milliseconds. |

### Notes

- Get coordinates for a place name with [Open-Meteo Geocoding](/apis/open-meteo/geocoding).
- Use `start_date` and `end_date` for a fixed date range, or `past_days` and `forecast_days` for a window around today.
- Other discharge variables for `daily` include `river_discharge_mean`, `river_discharge_median`, `river_discharge_max`, `river_discharge_min`, `river_discharge_p25` and `river_discharge_p75`.
- Set `ensemble` to `true` to get all ensemble members instead of the aggregate.

### Pricing

$0.0001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/open-meteo/flood.json`](../../../catalog/models/open-meteo/flood.json) · Store page: https://www.sandbase.ai/model/open-meteo/flood
