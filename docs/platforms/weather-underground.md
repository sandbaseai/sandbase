# Weather Underground API: 1 endpoints with pricing and code examples

Call 1 Weather Underground endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`weather-underground/historical-airport-temperature-series`](../models/weather-underground/historical-airport-temperature-series.md) | Retrieve a complete year-scale airport observation temperature series for settlement calibration. Returns every observation within the… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weather-underground/historical-airport-temperature-series", "country_code": "US", "end_date": "20261002", "start_date": "20261001", "station_id": "KJFK", "timezone_name": "America/New_York"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
