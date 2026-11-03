# Open-Meteo Air Quality API: pricing, parameters and code examples

`open-meteo/air-quality` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Hourly air quality forecast for any coordinates: PM2.5, PM10, ozone, NO2, CO, dust, pollen and European/US AQI.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/air-quality", "latitude": "52.52", "longitude": "13.41"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/air-quality', {'latitude': '52.52', 'longitude': '13.41'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/air-quality", {
  "latitude": "52.52",
  "longitude": "13.41"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/air-quality", sandbase.Params{
	"latitude": "52.52",
	"longitude": "13.41",
})
```

Same call via the path form: `POST /v1/api/open-meteo/air-quality` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hourly` | string |  | Comma-separated list of hourly variables to return. Common values: `pm10`, `pm2_5`, `carbon_monoxide`, `nitrogen_dioxide`, `sulphur_dioxide`, `ozone`, `aerosol_optical_depth`, `dust`, `uv_index`, `ammonia`,…  |
| `current` | string |  | Comma-separated list of current-condition variables to return. Same variable set as `hourly`.  |
| `domains` | string |  | Model domain. Default `auto`. one of: `auto`, `cams_europe`, `cams_global`; default `"auto"` |
| `end_date` | string |  | End of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `latitude` | string | yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated.  |
| `timezone` | string |  | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`.  |
| `longitude` | string | yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated.  |
| `past_days` | integer |  | Number of past days to include (0-92). Default 0. default `0` |
| `past_hours` | integer |  | Include a given number of past hours.  |
| `start_date` | string |  | Start of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `timeformat` | string |  | Time output format. Default `iso8601`. one of: `iso8601`, `unixtime`; default `"iso8601"` |
| `forecast_days` | integer |  | Number of forecast days to return (0-7). Default 5. default `5` |
| `cell_selection` | string |  | Grid-cell preference for the coordinate. Default `nearest`. one of: `land`, `sea`, `nearest`; default `"nearest"` |
| `forecast_hours` | integer |  | Limit forecast to a given number of hours.  |

## Details

Returns an hourly air quality forecast for a latitude and longitude. You choose the variables with `hourly`, such as `pm10` and `pm2_5`, and the response gives one value per hour with its unit.

### Use cases

- Show a PM2.5 and PM10 forecast for a city in a health or weather app.
- Warn users when the forecast for ozone or NO2 rises above a limit you set.
- Compare particulate levels across several sites by sending comma-separated coordinates.
- Add pollen or AQI values to a daily outlook for allergy sufferers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/air-quality" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": "52.52", "longitude": "13.41", "hourly": "pm10,pm2_5", "forecast_days": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `latitude` | string | Yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated. |
| `longitude` | string | Yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated. |
| `cell_selection` | string | No | Grid-cell preference for the coordinate. Default `nearest`. |
| `current` | string | No | Comma-separated list of current-condition variables to return. Same variable set as `hourly`. |
| `domains` | string | No | Model domain. Default `auto`. |
| `end_date` | string | No | End of the interval, `yyyy-mm-dd` (ISO 8601). |
| `forecast_days` | integer | No | Number of forecast days to return (0-7). Default 5. |
| `forecast_hours` | integer | No | Limit forecast to a given number of hours. |
| `hourly` | string | No | Comma-separated list of hourly variables to return. Common values: `pm10`, `pm2_5`, `carbon_monoxide`, `nitrogen_dioxide`, `sulphur_dioxide`, `ozone`, `aerosol_optical_depth`, `dust`, `uv_index`, `ammonia`, `european_aqi |
| `past_days` | integer | No | Number of past days to include (0-92). Default 0. |
| `past_hours` | integer | No | Include a given number of past hours. |
| `start_date` | string | No | Start of the interval, `yyyy-mm-dd` (ISO 8601). |
| `timeformat` | string | No | Time output format. Default `iso8601`. |
| `timezone` | string | No | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "elevation": 38.0,
  "generationtime_ms": 0.3840923309326172,
  "hourly": {
    "pm10": [
      15.9
    ],
    "pm2_5": [
      13.0
    ],
    "time": [
      "2026-11-03T00:00"
    ]
  },
  "hourly_units": {
    "pm10": "μg/m³",
    "pm2_5": "μg/m³",
    "time": "iso8601"
  },
  "latitude": 52.5,
  "longitude": 13.400002,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "utc_offset_seconds": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `hourly.time[]` | Timestamp of each hourly step, in ISO 8601 local time for the chosen `timezone`. Each position lines up with the same position in the other `hourly` lists. |
| `hourly.pm10[]` | Forecast concentration of particles up to 10 µm for each hour. The unit is given in `hourly_units.pm10`. |
| `hourly.pm2_5[]` | Forecast concentration of fine particles up to 2.5 µm for each hour. The unit is given in `hourly_units.pm2_5`. |
| `hourly_units.pm10 / hourly_units.pm2_5` | Unit for each requested variable. In this response both are `μg/m³`. |
| `hourly_units.time` | Format of the values in `hourly.time[]`. It is `iso8601` here. |
| `latitude / longitude` | Coordinates of the grid cell the data comes from. They can differ slightly from the coordinates you sent. |
| `elevation` | Elevation of the grid cell, in the same response as the coordinates. The value here is `38.0`. |
| `timezone / timezone_abbreviation / utc_offset_seconds` | Time zone applied to the timestamps and its offset from UTC in seconds. The default is `GMT` with an offset of `0`. |
| `generationtime_ms` | Time taken to generate the response, in milliseconds. |

### Notes

- Each variable you list in `hourly` adds a matching list under `hourly` and an entry under `hourly_units`.
- Use `forecast_days` (0-7) for the forecast length and `past_days` (0-92) to include earlier days. Or set `start_date` and `end_date` as `yyyy-mm-dd`.
- Set `timezone` to an IANA name or `auto` to get local times. Without it, times are in GMT.
- For weather variables at the same coordinates, call [Open-Meteo Weather Forecast](/apis/open-meteo/forecast). To turn a place name into coordinates, use [Open-Meteo Geocoding](/apis/open-meteo/geocoding).

### Pricing

$0.0001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/open-meteo/air-quality.json`](../../../catalog/models/open-meteo/air-quality.json) · Store page: https://www.sandbase.ai/model/open-meteo/air-quality
