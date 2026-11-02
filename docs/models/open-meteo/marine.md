# Open-Meteo Marine Forecast API: pricing, parameters and code examples

`open-meteo/marine` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Hourly and daily marine forecast by coordinates: wave height, direction and period, swell and ocean currents.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/marine", "latitude": "54.54", "longitude": "10.23"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/marine', {'latitude': '54.54', 'longitude': '10.23'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/marine", {
  "latitude": "54.54",
  "longitude": "10.23"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/marine", sandbase.Params{
	"latitude": "54.54",
	"longitude": "10.23",
})
```

Same call via the path form: `POST /v1/api/open-meteo/marine` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `daily` | string |  | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `wave_height_max`, `wave_direction_dominant`, `wave_period_max`, `wind_wave_height_max`, `swell_wave_height_max`.  |
| `hourly` | string |  | Comma-separated list of hourly variables to return. Common values: `wave_height`, `wave_direction`, `wave_period`, `wind_wave_height`, `wind_wave_direction`, `wind_wave_period`, `swell_wave_height`,…  |
| `current` | string |  | Comma-separated list of current-condition variables to return. Same variable set as `hourly`.  |
| `end_date` | string |  | End of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `latitude` | string | yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated.  |
| `timezone` | string |  | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`.  |
| `longitude` | string | yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated.  |
| `past_days` | integer |  | Number of past days to include (0-92). Default 0. default `0` |
| `start_date` | string |  | Start of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `timeformat` | string |  | Time output format. Default `iso8601`. one of: `iso8601`, `unixtime`; default `"iso8601"` |
| `length_unit` | string |  | Unit for wave heights. Default `metric`. one of: `metric`, `imperial`; default `"metric"` |
| `forecast_days` | integer |  | Number of forecast days to return (0-8). Default 5. default `5` |
| `cell_selection` | string |  | Grid-cell preference for the coordinate. Default `sea`. one of: `land`, `sea`, `nearest`; default `"sea"` |

## Details

Hourly and daily marine forecast by coordinates: wave height, direction and period, swell and ocean currents.

The result is returned in `outputs[0].data` as the official Open-Meteo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/marine" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": "54.54", "longitude": "10.23", "hourly": "wave_height", "forecast_days": 1}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cell_selection` | string | No | Grid-cell preference for the coordinate. Default `sea`. |
| `current` | string | No | Comma-separated list of current-condition variables to return. Same variable set as `hourly`. |
| `daily` | string | No | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `wave_height_max`, `wave_direction_dominant`, `wave_period_ma |
| `end_date` | string | No | End of the interval, `yyyy-mm-dd` (ISO 8601). |
| `forecast_days` | integer | No | Number of forecast days to return (0-8). Default 5. |
| `hourly` | string | No | Comma-separated list of hourly variables to return. Common values: `wave_height`, `wave_direction`, `wave_period`, `wind_wave_height`, `wind_wave_direction`, `w |
| `latitude` | string | Yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated. |
| `length_unit` | string | No | Unit for wave heights. Default `metric`. |
| `longitude` | string | Yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated. |
| `past_days` | integer | No | Number of past days to include (0-92). Default 0. |
| `start_date` | string | No | Start of the interval, `yyyy-mm-dd` (ISO 8601). |
| `timeformat` | string | No | Time output format. Default `iso8601`. |
| `timezone` | string | No | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/open-meteo/marine.json`](../../../catalog/models/open-meteo/marine.json) · Store page: https://www.sandbase.ai/model/open-meteo/marine
