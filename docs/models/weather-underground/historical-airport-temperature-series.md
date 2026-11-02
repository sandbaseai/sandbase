# Weather Underground Historical Airport Temperature Series API: pricing, parameters and code examples

`weather-underground/historical-airport-temperature-series` · data API · Weather Underground · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve a complete year-scale airport observation temperature series for settlement calibration. Returns every observation within the requested local-date range (up to 366 days), preserving the full intraday path.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weather-underground/historical-airport-temperature-series", "country_code": "US", "end_date": "20261002", "start_date": "20261001", "station_id": "KJFK", "timezone_name": "America/New_York"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weather-underground/historical-airport-temperature-series', {'country_code': 'US', 'end_date': '20261002', 'start_date': '20261001', 'station_id': 'KJFK', 'timezone_name': 'America/New_York'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weather-underground/historical-airport-temperature-series", {
  "country_code": "US",
  "end_date": "20261002",
  "start_date": "20261001",
  "station_id": "KJFK",
  "timezone_name": "America/New_York"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weather-underground/historical-airport-temperature-series", sandbase.Params{
	"country_code": "US",
	"end_date": "20261002",
	"start_date": "20261001",
	"station_id": "KJFK",
	"timezone_name": "America/New_York",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/weather-underground/historical-airport-temperature-series` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end_date` | string | yes | End date in YYYYMMDD format, inclusive local calendar date.  |
| `start_date` | string | yes | Start date in YYYYMMDD format, interpreted as a local calendar date.  |
| `station_id` | string | yes | Airport station ICAO code (e.g. EFHK, KJFK). Obtain from search endpoint's icaoCode field.  |
| `country_code` | string | yes | Two-letter ISO country code for the station (e.g. FI, US).  |
| `timezone_name` | string | yes | IANA timezone name for local date grouping (e.g. Europe/Helsinki, America/New_York). DST transitions are handled automatically.  |

## Details

Retrieve a complete year-scale airport observation temperature series for settlement calibration. Returns every observation within the requested local-date range (up to 366 days), preserving the full intraday path.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weather-underground/historical-airport-temperature-series" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"station_id": "KJFK", "country_code": "US", "start_date": "20261001", "end_date": "20261002", "timezone_name": "America/New_York"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country_code` | string | Yes | Two-letter ISO country code for the station (e.g. FI, US). |
| `end_date` | string | Yes | End date in YYYYMMDD format, inclusive local calendar date. |
| `start_date` | string | Yes | Start date in YYYYMMDD format, interpreted as a local calendar date. |
| `station_id` | string | Yes | Airport station ICAO code (e.g. EFHK, KJFK). Obtain from search endpoint's icaoCode field. |
| `timezone_name` | string | Yes | IANA timezone name for local date grouping (e.g. Europe/Helsinki, America/New_York). DST transitions are handled automatically. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/weather-underground/historical-airport-temperature-series.json`](../../../catalog/models/weather-underground/historical-airport-temperature-series.json) · Store page: https://www.sandbase.ai/model/weather-underground/historical-airport-temperature-series
