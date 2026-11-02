# Open-Meteo Previous Model Runs API: pricing, parameters and code examples

`open-meteo/previous-runs` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Weather forecasts from earlier model runs for the same coordinates, to compare how forecasts changed day by day.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/previous-runs", "latitude": "52.52", "longitude": "13.41"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/previous-runs', {'latitude': '52.52', 'longitude': '13.41'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/previous-runs", {
  "latitude": "52.52",
  "longitude": "13.41"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/previous-runs", sandbase.Params{
	"latitude": "52.52",
	"longitude": "13.41",
})
```

Same call via the path form: `POST /v1/api/open-meteo/previous-runs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `daily` | string |  | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_mean`, `precipitation_sum`, `rain_sum`, `snowfall_sum`,…  |
| `hourly` | string |  | Comma-separated list of hourly variables to return. Common values: `temperature_2m`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`, `precipitation`, `rain`, `showers`, `snowfall`, `weather_code`,…  |
| `models` | string |  | Comma-separated forecast models. Default best match.  |
| `end_date` | string |  | End of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `latitude` | string | yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated.  |
| `timezone` | string |  | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`.  |
| `longitude` | string | yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated.  |
| `past_days` | integer |  | Number of past days to include (0-92). Default 0. default `0` |
| `start_date` | string |  | Start of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `timeformat` | string |  | Time output format. Default `iso8601`. one of: `iso8601`, `unixtime`; default `"iso8601"` |
| `forecast_days` | integer |  | Number of forecast days to return (0-16). Default 7. default `7` |
| `cell_selection` | string |  | Grid-cell preference for the coordinate. Default `land`. one of: `land`, `sea`, `nearest`; default `"land"` |
| `wind_speed_unit` | string |  | Wind speed unit. Default `kmh`. one of: `kmh`, `ms`, `mph`, `kn`; default `"kmh"` |
| `temperature_unit` | string |  | Temperature unit. Default `celsius`. one of: `celsius`, `fahrenheit`; default `"celsius"` |
| `precipitation_unit` | string |  | Precipitation unit. Default `mm`. one of: `mm`, `inch`; default `"mm"` |

## Details

Weather forecasts from earlier model runs for the same coordinates, to compare how forecasts changed day by day.

The result is returned in `outputs[0].data` as the official Open-Meteo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/previous-runs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": "52.52", "longitude": "13.41", "hourly": "temperature_2m_previous_day1", "forecast_days": 1}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cell_selection` | string | No | Grid-cell preference for the coordinate. Default `land`. |
| `daily` | string | No | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_m |
| `end_date` | string | No | End of the interval, `yyyy-mm-dd` (ISO 8601). |
| `forecast_days` | integer | No | Number of forecast days to return (0-16). Default 7. |
| `hourly` | string | No | Comma-separated list of hourly variables to return. Common values: `temperature_2m`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`, `precipitat |
| `latitude` | string | Yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated. |
| `longitude` | string | Yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated. |
| `models` | string | No | Comma-separated forecast models. Default best match. |
| `past_days` | integer | No | Number of past days to include (0-92). Default 0. |
| `precipitation_unit` | string | No | Precipitation unit. Default `mm`. |
| `start_date` | string | No | Start of the interval, `yyyy-mm-dd` (ISO 8601). |
| `temperature_unit` | string | No | Temperature unit. Default `celsius`. |
| `timeformat` | string | No | Time output format. Default `iso8601`. |
| `timezone` | string | No | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`. |
| `wind_speed_unit` | string | No | Wind speed unit. Default `kmh`. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/open-meteo/previous-runs.json`](../../../catalog/models/open-meteo/previous-runs.json) · Store page: https://www.sandbase.ai/model/open-meteo/previous-runs
