# Open-Meteo Historical Forecast API: pricing, parameters and code examples

`open-meteo/historical-forecast` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Archived high-resolution weather model forecasts by coordinates and date range, as they were issued.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/historical-forecast", "end_date": "2024-01-07", "latitude": "52.52", "longitude": "13.41", "start_date": "2024-01-01"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/historical-forecast', {'end_date': '2024-01-07', 'latitude': '52.52', 'longitude': '13.41', 'start_date': '2024-01-01'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/historical-forecast", {
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
run, err := c.Run(ctx, "open-meteo/historical-forecast", sandbase.Params{
	"end_date": "2024-01-07",
	"latitude": "52.52",
	"longitude": "13.41",
	"start_date": "2024-01-01",
})
```

Same call via the path form: `POST /v1/api/open-meteo/historical-forecast` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `daily` | string |  | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_mean`, `precipitation_sum`, `rain_sum`, `snowfall_sum`,…  |
| `hourly` | string |  | Comma-separated list of hourly variables to return. Common values: `temperature_2m`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`, `precipitation`, `rain`, `showers`, `snowfall`, `weather_code`,…  |
| `models` | string |  | Comma-separated forecast models to retrieve archived runs for. Default best match.  |
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

Returns archived weather model forecasts for a coordinate pair and a date range, as the models issued them. You send `latitude`, `longitude`, `start_date` and `end_date`, plus the `daily` or `hourly` variables you want.

### Use cases

- Compare what a model predicted for a day with what actually happened, by pairing this data with observed weather.
- Build a training set of past forecast values for a site to test a forecast correction model.
- Check which temperature a forecast showed on a given past date to review a planning decision.
- Pull daily maximum temperatures for several dates at one location to chart forecast trends.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/historical-forecast" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "2024-01-07", "latitude": "52.52", "longitude": "13.41", "start_date": "2024-01-01", "daily": "temperature_2m_max", "timezone": "auto"}'
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
| `models` | string | No | Comma-separated forecast models to retrieve archived runs for. Default best match. |
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
    "temperature_2m_max": [
      7.8
    ],
    "time": [
      "2024-01-01"
    ]
  },
  "daily_units": {
    "temperature_2m_max": "°C",
    "time": "iso8601"
  },
  "elevation": 38.0,
  "generationtime_ms": 31.14795684814453,
  "latitude": 52.512604,
  "longitude": 13.419517,
  "timezone": "Europe/Berlin",
  "timezone_abbreviation": "GMT+1",
  "utc_offset_seconds": 3600
}
```

### Response fields

| Field | Meaning |
|---|---|
| `daily.time` | List of dates in the requested range. Each entry matches the same position in the other `daily` lists. |
| `daily.temperature_2m_max` | List of forecast daily maximum temperatures at 2 m, one value per date. The key name changes with the variables you request in `daily`. |
| `daily_units.temperature_2m_max` | Unit of the daily temperature values, here `°C`. |
| `daily_units.time` | Format of the `daily.time` values, here `iso8601`. |
| `latitude / longitude` | Coordinates of the grid cell used for the answer. They differ slightly from the requested point. |
| `elevation` | Elevation in meters used for the location. |
| `timezone / timezone_abbreviation` | Time zone resolved for the request, such as `Europe/Berlin`, and its short label. |
| `utc_offset_seconds` | Offset of the time zone from UTC, in seconds. |
| `generationtime_ms` | Time the server took to build the response, in milliseconds. |

### Notes

- The `daily` parameter needs `timezone`. Use `auto` to resolve it from the coordinates.
- Use `hourly` for hourly values. The response then has an `hourly` object and an `hourly_units` object instead of the `daily` ones.
- To see how a forecast changed across several runs, call [Open-Meteo Previous Model Runs](/apis/open-meteo/previous-runs).
- For measured past weather rather than forecasts, call [Open-Meteo Historical Weather](/apis/open-meteo/archive).

### Pricing

$0.0001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/open-meteo/historical-forecast.json`](../../../catalog/models/open-meteo/historical-forecast.json) · Store page: https://www.sandbase.ai/model/open-meteo/historical-forecast
