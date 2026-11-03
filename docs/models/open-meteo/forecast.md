# Open-Meteo Weather Forecast API: pricing, parameters and code examples

`open-meteo/forecast` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Up to 16-day hourly, daily and current weather forecast by coordinates: temperature, precipitation, wind, cloud cover and more.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/forecast", "latitude": "52.52", "longitude": "13.41"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/forecast', {'latitude': '52.52', 'longitude': '13.41'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/forecast", {
  "latitude": "52.52",
  "longitude": "13.41"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/forecast", sandbase.Params{
	"latitude": "52.52",
	"longitude": "13.41",
})
```

Same call via the path form: `POST /v1/api/open-meteo/forecast` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `daily` | string |  | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_mean`, `precipitation_sum`, `rain_sum`, `snowfall_sum`,…  |
| `hourly` | string |  | Comma-separated list of hourly variables to return. Common values: `temperature_2m`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`, `precipitation`, `rain`, `showers`, `snowfall`, `weather_code`,…  |
| `models` | string |  | Comma-separated forecast models to use. Default `auto` selects the best model mix per location.  |
| `current` | string |  | Comma-separated list of current-condition variables to return. Common values: `temperature_2m`, `relative_humidity_2m`, `apparent_temperature`, `is_day`, `precipitation`, `weather_code`, `wind_speed_10m`,…  |
| `end_date` | string |  | End of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `latitude` | string | yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated.  |
| `timezone` | string |  | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`.  |
| `elevation` | string |  | Manual elevation (meters) for statistical downscaling. Defaults to a 90m DEM. Use `nan` to disable downscaling.  |
| `longitude` | string | yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated.  |
| `past_days` | integer |  | Number of past days to include (0-92). Default 0. default `0` |
| `past_hours` | integer |  | Include a given number of past hours.  |
| `start_date` | string |  | Start of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `timeformat` | string |  | Time output format. Default `iso8601`. one of: `iso8601`, `unixtime`; default `"iso8601"` |
| `minutely_15` | string |  | Comma-separated 15-minutely variables (Central Europe & North America high-resolution models only).  |
| `forecast_days` | integer |  | Number of forecast days to return (0-16). Default 7. default `7` |
| `cell_selection` | string |  | Grid-cell preference for the coordinate. Default `land`. one of: `land`, `sea`, `nearest`; default `"land"` |
| `forecast_hours` | integer |  | Limit the forecast to a given number of hours from now.  |
| `wind_speed_unit` | string |  | Wind speed unit. Default `kmh`. one of: `kmh`, `ms`, `mph`, `kn`; default `"kmh"` |
| `temperature_unit` | string |  | Temperature unit. Default `celsius`. one of: `celsius`, `fahrenheit`; default `"celsius"` |
| `precipitation_unit` | string |  | Precipitation unit. Default `mm`. one of: `mm`, `inch`; default `"mm"` |

## Details

Returns a weather forecast for one point on Earth. You send `latitude` and `longitude`, plus the variables you want in `current`, `hourly`, `daily` or `minutely_15`. The response holds the values and their units.

### Use cases

- Show the current temperature and wind speed on a city dashboard.
- Plan outdoor events with a daily forecast of rain, wind and temperature highs and lows.
- Feed hourly temperature and precipitation into an energy demand or irrigation model.
- Add a short weather summary to a travel app for a given destination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/forecast" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": "52.52", "longitude": "13.41", "current": "temperature_2m,wind_speed_10m"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `latitude` | string | Yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated. |
| `longitude` | string | Yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated. |
| `cell_selection` | string | No | Grid-cell preference for the coordinate. Default `land`. |
| `current` | string | No | Comma-separated list of current-condition variables to return. Common values: `temperature_2m`, `relative_humidity_2m`, `apparent_temperature`, `is_day`, `precipitation`, `weather_code`, `wind_speed_10m`, `wind_direction |
| `daily` | string | No | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_mean`, `precipitation_sum`, `rain_sum`, `snowfall_sum`, `weat |
| `elevation` | string | No | Manual elevation (meters) for statistical downscaling. Defaults to a 90m DEM. Use `nan` to disable downscaling. |
| `end_date` | string | No | End of the interval, `yyyy-mm-dd` (ISO 8601). |
| `forecast_days` | integer | No | Number of forecast days to return (0-16). Default 7. |
| `forecast_hours` | integer | No | Limit the forecast to a given number of hours from now. |
| `hourly` | string | No | Comma-separated list of hourly variables to return. Common values: `temperature_2m`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`, `precipitation`, `rain`, `showers`, `snowfall`, `weather_code`, `pressu |
| `minutely_15` | string | No | Comma-separated 15-minutely variables (Central Europe & North America high-resolution models only). |
| `models` | string | No | Comma-separated forecast models to use. Default `auto` selects the best model mix per location. |
| `past_days` | integer | No | Number of past days to include (0-92). Default 0. |
| `past_hours` | integer | No | Include a given number of past hours. |
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
  "current": {
    "interval": 900,
    "temperature_2m": 4.6,
    "time": "2026-11-03T07:30",
    "wind_speed_10m": 7.4
  },
  "current_units": {
    "interval": "seconds",
    "temperature_2m": "°C",
    "time": "iso8601",
    "wind_speed_10m": "km/h"
  },
  "elevation": 38.0,
  "generationtime_ms": 0.12421607971191406,
  "latitude": 52.512604,
  "longitude": 13.419517,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "utc_offset_seconds": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `current.time` | Time of the current reading, in the format set by `timeformat`. The example value is `2026-11-03T07:30`, in the time zone given by `timezone`. |
| `current.interval` | Length of the current-conditions interval. The matching entry in `current_units` is `seconds`, so `900` means 15 minutes. |
| `current.temperature_2m / current.wind_speed_10m` | Current air temperature at 2 m and wind speed at 10 m. These keys appear because they were listed in `current`. Each variable you request adds a key here. |
| `current_units` | Unit for each key in `current`, such as `°C` for `temperature_2m` and `km/h` for `wind_speed_10m`. Unit parameters like `temperature_unit` and `wind_speed_unit` change these. |
| `latitude / longitude` | Coordinates of the grid cell the forecast belongs to. They can differ slightly from the coordinates you sent. |
| `elevation` | Elevation of the location in meters. Set the `elevation` parameter to override it. |
| `timezone / timezone_abbreviation` | Time zone used for all timestamps in the response. It is `GMT` unless you set `timezone`. |
| `utc_offset_seconds` | Offset of the response time zone from UTC, in seconds. |
| `generationtime_ms` | Time taken to generate the response, in milliseconds. |

### Notes

- Only the variables you list in `current`, `hourly`, `daily` or `minutely_15` come back. A request with no variable list returns just the location and time zone fields.
- `daily` needs `timezone`. Set it to an IANA name like `Europe/Berlin`, or to `auto` to resolve it from the coordinates.
- Use `forecast_days` (0-16) for the range, or `start_date` and `end_date` in `yyyy-mm-dd` format. Use `past_days` to include earlier days.
- To look up coordinates from a place name, call [Open-Meteo Geocoding](/apis/open-meteo/geocoding). For older dates, use [Open-Meteo Historical Weather](/apis/open-meteo/archive).

### Pricing

$0.0001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/open-meteo/forecast.json`](../../../catalog/models/open-meteo/forecast.json) · Store page: https://www.sandbase.ai/model/open-meteo/forecast
