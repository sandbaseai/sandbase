# Open-Meteo Historical Weather API: pricing, parameters and code examples

`open-meteo/archive` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Historical weather by coordinates and date range from the ERA5 reanalysis, back to 1940, with hourly and daily variables.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/archive", "end_date": "2024-01-07", "latitude": "52.52", "longitude": "13.41", "start_date": "2024-01-01"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/archive', {'end_date': '2024-01-07', 'latitude': '52.52', 'longitude': '13.41', 'start_date': '2024-01-01'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/archive", {
  "end_date": "2024-01-07",
  "latitude": "52.52",
  "longitude": "13.41",
  "start_date": "2024-01-01"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/archive", sandbase.Params{
	"end_date": "2024-01-07",
	"latitude": "52.52",
	"longitude": "13.41",
	"start_date": "2024-01-01",
})
```

Same call via the path form: `POST /v1/api/open-meteo/archive` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `daily` | string |  | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_mean`, `precipitation_sum`, `rain_sum`, `snowfall_sum`,…  |
| `hourly` | string |  | Comma-separated list of hourly variables to return. Common values: `temperature_2m`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`, `precipitation`, `rain`, `showers`, `snowfall`, `weather_code`,…  |
| `models` | string |  | Comma-separated reanalysis models, e.g. `era5`, `era5_land`, `ecmwf_ifs`, `cerra`. Default best match.  |
| `end_date` | string | yes | End of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `latitude` | string | yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated.  |
| `timezone` | string |  | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`.  |
| `elevation` | string |  | Manual elevation (meters). Defaults to a 90m DEM.  |
| `longitude` | string | yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated.  |
| `start_date` | string | yes | Start of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `timeformat` | string |  | Time output format. Default `iso8601`. one of: `iso8601`, `unixtime`; default `"iso8601"` |
| `cell_selection` | string |  | Grid-cell preference for the coordinate. Default `land`. one of: `land`, `sea`, `nearest`; default `"land"` |
| `wind_speed_unit` | string |  | Wind speed unit. Default `kmh`. one of: `kmh`, `ms`, `mph`, `kn`; default `"kmh"` |
| `temperature_unit` | string |  | Temperature unit. Default `celsius`. one of: `celsius`, `fahrenheit`; default `"celsius"` |
| `precipitation_unit` | string |  | Precipitation unit. Default `mm`. one of: `mm`, `inch`; default `"mm"` |

## Details

Returns historical weather for a point location and date range from the ERA5 reanalysis, with data back to 1940. It needs `latitude`, `longitude`, `start_date` and `end_date`, plus the `daily` or `hourly` variables you want.

### Use cases

- Pull daily maximum temperature and precipitation for a city to compare a past week against the seasonal norm.
- Build a training dataset that joins past weather to sales, energy use or crop yield records by date.
- Check what the weather was at a site on a specific day for an insurance or incident report.
- Export long daily series for several coordinates to chart climate trends.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/archive" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "2024-01-07", "latitude": "52.52", "longitude": "13.41", "start_date": "2024-01-01", "daily": "temperature_2m_max,precipitation_sum", "timezone": "auto"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End of the interval, `yyyy-mm-dd` (ISO 8601). |
| `latitude` | string | Yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated. |
| `longitude` | string | Yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated. |
| `start_date` | string | Yes | Start of the interval, `yyyy-mm-dd` (ISO 8601). |
| `cell_selection` | string | No | Grid-cell preference for the coordinate. Default `land`. |
| `daily` | string | No | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_mean`, `precipitation_sum`, `rain_sum`, `snowfall_sum`, `weat |
| `elevation` | string | No | Manual elevation (meters). Defaults to a 90m DEM. |
| `hourly` | string | No | Comma-separated list of hourly variables to return. Common values: `temperature_2m`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`, `precipitation`, `rain`, `showers`, `snowfall`, `weather_code`, `pressu |
| `models` | string | No | Comma-separated reanalysis models, e.g. `era5`, `era5_land`, `ecmwf_ifs`, `cerra`. Default best match. |
| `precipitation_unit` | string | No | Precipitation unit. Default `mm`. |
| `temperature_unit` | string | No | Temperature unit. Default `celsius`. |
| `timeformat` | string | No | Time output format. Default `iso8601`. |
| `timezone` | string | No | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`. |
| `wind_speed_unit` | string | No | Wind speed unit. Default `kmh`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "daily": {
    "precipitation_sum": [
      1.9
    ],
    "temperature_2m_max": [
      7.5
    ],
    "time": [
      "2024-01-01"
    ]
  },
  "daily_units": {
    "precipitation_sum": "mm",
    "temperature_2m_max": "°C",
    "time": "iso8601"
  },
  "elevation": 38.0,
  "generationtime_ms": 0.12195110321044922,
  "latitude": 52.54833,
  "longitude": 13.407822,
  "timezone": "Europe/Berlin",
  "timezone_abbreviation": "GMT+1",
  "utc_offset_seconds": 3600
}
```

### Response fields

| Field | Meaning |
|---|---|
| `daily.time[]` | Date of each daily value, in `yyyy-mm-dd` format. The position matches the same index in the other `daily` lists. |
| `daily.temperature_2m_max[]` | Highest air temperature at 2 m for each day. The unit is in `daily_units.temperature_2m_max`. |
| `daily.precipitation_sum[]` | Total precipitation for each day. The unit is in `daily_units.precipitation_sum`. |
| `daily_units.temperature_2m_max / daily_units.precipitation_sum` | Units for the matching `daily` lists, such as `°C` and `mm`. |
| `latitude / longitude` | Coordinates of the grid cell the data comes from. They can differ slightly from the coordinates you sent. |
| `elevation` | Elevation in meters used for the result. It matches the `elevation` parameter when you set it. |
| `timezone / timezone_abbreviation` | IANA time zone name and its short label used for the daily values. |
| `utc_offset_seconds` | Offset of the time zone from UTC, in seconds. |
| `generationtime_ms` | Time the server took to build the response, in milliseconds. |

### Notes

- The `daily` list needs `timezone`. Use `auto` to resolve it from the coordinates.
- Each key in `daily` or `hourly` is a list with one value per time step. Read it together with the `time` list at the same index.
- Only the variables you request in `daily` or `hourly` appear in the response, along with a matching `daily_units` or `hourly_units` object.
- To find coordinates for a place name, call [Open-Meteo Geocoding](/apis/open-meteo/geocoding). For recent or upcoming days, use [Open-Meteo Weather Forecast](/apis/open-meteo/forecast).

### Pricing

$0.0001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/open-meteo/archive.json`](../../../catalog/models/open-meteo/archive.json) · Store page: https://www.sandbase.ai/model/open-meteo/archive
