# Open-Meteo Ensemble Forecast API: pricing, parameters and code examples

`open-meteo/ensemble` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Ensemble weather forecasts by coordinates with every member of a chosen model, for forecast uncertainty and probabilities.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/ensemble", "latitude": "52.52", "longitude": "13.41", "models": "icon_seamless"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/ensemble', {'latitude': '52.52', 'longitude': '13.41', 'models': 'icon_seamless'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/ensemble", {
  "latitude": "52.52",
  "longitude": "13.41",
  "models": "icon_seamless"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/ensemble", sandbase.Params{
	"latitude": "52.52",
	"longitude": "13.41",
	"models": "icon_seamless",
})
```

Same call via the path form: `POST /v1/api/open-meteo/ensemble` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `daily` | string |  | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_mean`, `precipitation_sum`, `rain_sum`, `snowfall_sum`,…  |
| `hourly` | string |  | Comma-separated list of hourly variables to return. Common values: `temperature_2m`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`, `precipitation`, `rain`, `showers`, `snowfall`, `weather_code`,…  |
| `models` | string | yes | Optional; when omitted, defaults to the best-match global ensemble (a 30-member set). Comma-separated ensemble models, e.g. `icon_seamless`, `gfs_seamless`, `ecmwf_ifs025`, `gem_global`. Each model exposes its own…  |
| `end_date` | string |  | End of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `latitude` | string | yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated.  |
| `timezone` | string |  | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`.  |
| `elevation` | string |  | Manual elevation (meters). Defaults to a 90m DEM.  |
| `longitude` | string | yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated.  |
| `past_days` | integer |  | Number of past days to include (0-92). Default 0. default `0` |
| `start_date` | string |  | Start of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `timeformat` | string |  | Time output format. Default `iso8601`. one of: `iso8601`, `unixtime`; default `"iso8601"` |
| `forecast_days` | integer |  | Number of forecast days to return (0-35). Default 7. default `7` |
| `cell_selection` | string |  | Grid-cell preference for the coordinate. Default `land`. one of: `land`, `sea`, `nearest`; default `"land"` |
| `wind_speed_unit` | string |  | Wind speed unit. Default `kmh`. one of: `kmh`, `ms`, `mph`, `kn`; default `"kmh"` |
| `temperature_unit` | string |  | Temperature unit. Default `celsius`. one of: `celsius`, `fahrenheit`; default `"celsius"` |
| `precipitation_unit` | string |  | Precipitation unit. Default `mm`. one of: `mm`, `inch`; default `"mm"` |

## Details

Returns ensemble weather forecasts for a coordinate, with one series per ensemble member of the chosen model. You send `latitude`, `longitude` and `models`, plus the `hourly` or `daily` variables you want.

### Use cases

- Compute the spread of `temperature_2m` across members to show how uncertain a forecast is.
- Count how many members predict rain above a threshold to estimate a precipitation probability.
- Build a min-to-max temperature band for a chart of the next days at a site.
- Compare member counts and spread between models such as `icon_seamless` and `gfs_seamless` for the same location.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/ensemble" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": "52.52", "longitude": "13.41", "models": "icon_seamless", "hourly": "temperature_2m", "forecast_days": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `latitude` | string | Yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated. |
| `longitude` | string | Yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated. |
| `models` | string | Yes | Optional; when omitted, defaults to the best-match global ensemble (a 30-member set). Comma-separated ensemble models, e.g. `icon_seamless`, `gfs_seamless`, `ecmwf_ifs025`, `gem_global`. Each model exposes its own member |
| `cell_selection` | string | No | Grid-cell preference for the coordinate. Default `land`. |
| `daily` | string | No | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_mean`, `precipitation_sum`, `rain_sum`, `snowfall_sum`, `weat |
| `elevation` | string | No | Manual elevation (meters). Defaults to a 90m DEM. |
| `end_date` | string | No | End of the interval, `yyyy-mm-dd` (ISO 8601). |
| `forecast_days` | integer | No | Number of forecast days to return (0-35). Default 7. |
| `hourly` | string | No | Comma-separated list of hourly variables to return. Common values: `temperature_2m`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`, `precipitation`, `rain`, `showers`, `snowfall`, `weather_code`, `pressu |
| `past_days` | integer | No | Number of past days to include (0-92). Default 0. |
| `precipitation_unit` | string | No | Precipitation unit. Default `mm`. |
| `start_date` | string | No | Start of the interval, `yyyy-mm-dd` (ISO 8601). |
| `temperature_unit` | string | No | Temperature unit. Default `celsius`. |
| `timeformat` | string | No | Time output format. Default `iso8601`. |
| `timezone` | string | No | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`. |
| `wind_speed_unit` | string | No | Wind speed unit. Default `kmh`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "elevation": 38.0,
  "generationtime_ms": 0.32532215118408203,
  "hourly": {
    "temperature_2m": [
      5.9
    ],
    "temperature_2m_member01": [
      6.3
    ],
    "temperature_2m_member02": [
      6.7
    ],
    "temperature_2m_member03": [
      6.7
    ],
    "temperature_2m_member04": [
      6.0
    ],
    "temperature_2m_member05": [
      6.1
    ],
    "temperature_2m_member06": [
      6.3
    ],
    "temperature_2m_member07": [
      5.9
    ],
    "temperature_2m_member08": [
      6.5
    ],
    "temperature_2m_member09": [
      6.7
    ],
    "temperature_2m_member10": [
      6.0
    ],
    "temperature_2m_member11": [
      6.8
    ]
  },
  "hourly_units": {
    "temperature_2m": "°C",
    "temperature_2m_member01": "°C",
    "temperature_2m_member02": "°C",
    "temperature_2m_member03": "°C",
    "temperature_2m_member04": "°C",
    "temperature_2m_member05": "°C",
    "temperature_2m_member06": "°C",
    "temperature_2m_member07": "°C",
    "temperature_2m_member08": "°C",
    "temperature_2m_member09": "°C",
    "temperature_2m_member10": "°C",
    "temperature_2m_member11": "°C"
  },
  "latitude": 52.52871,
  "longitude": 13.419504,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "utc_offset_seconds": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `hourly.time` | List of timestamps for the hourly values. It is not in the trimmed sample, but every hourly series lines up with it by index. |
| `hourly.temperature_2m` | Hourly air temperature at 2 m for the model's main series. Each value matches one timestamp. |
| `hourly.temperature_2m_member01 / temperature_2m_member02 / temperature_2m_member39` | Hourly temperature from each single ensemble member, numbered from `member01`. The request for `icon_seamless` returned members `01` to `39`, so use the spread between them as the uncertainty. |
| `hourly_units.temperature_2m` | Unit of the hourly temperature values, here `°C`. The same unit applies to every member series. |
| `latitude / longitude` | Coordinates of the grid cell used for the forecast. They can differ slightly from the requested point. |
| `elevation` | Elevation in meters used for the forecast point. |
| `timezone / timezone_abbreviation` | Time zone used for the timestamps. It is `GMT` unless you set `timezone`. |
| `utc_offset_seconds` | Offset of the response time zone from UTC, in seconds. |
| `generationtime_ms` | Time the server took to compute the response, in milliseconds. |

### Notes

- Each requested variable returns one main series plus one series per member, named like `temperature_2m_member01`. Member counts vary by model.
- Use `forecast_days` (0-35) or `start_date` and `end_date` to set the time range. `past_days` adds earlier days.
- Daily variables require `timezone`. Set it to an IANA name or `auto`.
- To find coordinates from a place name, call [Open-Meteo Geocoding](/apis/open-meteo/geocoding). For a single deterministic forecast, use [Open-Meteo Weather Forecast](/apis/open-meteo/forecast).

### Pricing

$0.0001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/open-meteo/ensemble.json`](../../../catalog/models/open-meteo/ensemble.json) · Store page: https://www.sandbase.ai/model/open-meteo/ensemble
