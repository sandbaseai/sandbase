# AccuWeather API: 3 endpoints with pricing and code examples

Call 3 AccuWeather endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`accuweather/list-cities`](../models/accuweather/list-cities.md) | List all provinces or major administrative divisions within a country by its ISO 2-letter code. Searches across regional browse pages to… | $0.01 per call (free daily quota) |
| [`accuweather/search-locations`](../models/accuweather/search-locations.md) | Search for location keys and metadata by query string. Returns matching cities with their AccuWeather location keys, geographic… | $0.01 per call (free daily quota) |
| [`accuweather/weather`](../models/accuweather/weather.md) | Get comprehensive weather data for a city including current conditions, daily and hourly forecasts, alerts, allergens, and radar metadata.… | $0.05 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "accuweather/list-cities", "country_code": "US"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
