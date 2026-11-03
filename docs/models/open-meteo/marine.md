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

Returns a marine forecast for a latitude and longitude. You choose the hourly, daily or current variables, such as wave height, wave period, swell and ocean current velocity. The request needs `latitude` and `longitude`.

### Use cases

- Show an hourly wave height chart for a harbor or sailing route.
- Check daily maximum wave height and dominant wave direction before a ferry or boat trip.
- Compare wind wave and swell wave height at a surf spot.
- Add ocean current velocity and direction to a navigation or fishing planner.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/marine" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": "54.54", "longitude": "10.23", "hourly": "wave_height", "forecast_days": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `latitude` | string | Yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated. |
| `longitude` | string | Yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated. |
| `cell_selection` | string | No | Grid-cell preference for the coordinate. Default `sea`. |
| `current` | string | No | Comma-separated list of current-condition variables to return. Same variable set as `hourly`. |
| `daily` | string | No | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `wave_height_max`, `wave_direction_dominant`, `wave_period_max`, `wind_wave_height_max`, `swell_wave_height_max`. |
| `end_date` | string | No | End of the interval, `yyyy-mm-dd` (ISO 8601). |
| `forecast_days` | integer | No | Number of forecast days to return (0-8). Default 5. |
| `hourly` | string | No | Comma-separated list of hourly variables to return. Common values: `wave_height`, `wave_direction`, `wave_period`, `wind_wave_height`, `wind_wave_direction`, `wind_wave_period`, `swell_wave_height`, `swell_wave_direction |
| `length_unit` | string | No | Unit for wave heights. Default `metric`. |
| `past_days` | integer | No | Number of past days to include (0-92). Default 0. |
| `start_date` | string | No | Start of the interval, `yyyy-mm-dd` (ISO 8601). |
| `timeformat` | string | No | Time output format. Default `iso8601`. |
| `timezone` | string | No | IANA time zone name (e.g. `Europe/Berlin`) or `auto` to resolve from coordinates. Defaults to `GMT`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "elevation": 0.0,
  "generationtime_ms": 0.10061264038085938,
  "hourly": {
    "time": [
      "2026-11-03T00:00"
    ],
    "wave_height": [
      0.68
    ]
  },
  "hourly_units": {
    "time": "iso8601",
    "wave_height": "m"
  },
  "latitude": 54.541664,
  "longitude": 10.2083435,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "utc_offset_seconds": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `hourly.time` | List of hourly timestamps in ISO 8601 format, such as `2026-11-03T00:00`. The time zone is the one in `timezone`. |
| `hourly.wave_height` | List of wave heights, one value for each entry in `hourly.time`. Other variables you request in `hourly` appear as extra lists with the same length. |
| `hourly_units.wave_height` | Unit for the wave height values. The example response shows `m`. |
| `hourly_units.time` | Format of the time values. The example response shows `iso8601`. |
| `latitude / longitude` | Coordinates of the grid cell that the forecast uses. They can differ slightly from the coordinates you sent. |
| `elevation` | Elevation of the grid cell. The example response shows `0.0` for a sea cell. |
| `timezone / timezone_abbreviation` | Time zone used for the timestamps. The default is `GMT`. |
| `utc_offset_seconds` | Offset of the response time zone from UTC, in seconds. |
| `generationtime_ms` | Time taken to generate the response, in milliseconds. |

### Notes

- Set `daily` together with `timezone` to get daily values such as `wave_height_max`. Use `timezone` set to `auto` to resolve the zone from the coordinates.
- Use `forecast_days` (0-8) and `past_days` (0-92) to set the time range, or use `start_date` and `end_date` in `yyyy-mm-dd` format.
- `cell_selection` defaults to `sea`, so the forecast uses the nearest sea grid cell. Set it to `land` or `nearest` to change this.
- Set `length_unit` to `imperial` for wave heights in feet. Check `hourly_units` for the unit in each response. For land weather at the same point, call [Open-Meteo Weather Forecast](/apis/open-meteo/forecast).

### Pricing

$0.0001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/open-meteo/marine.json`](../../../catalog/models/open-meteo/marine.json) · Store page: https://www.sandbase.ai/model/open-meteo/marine
