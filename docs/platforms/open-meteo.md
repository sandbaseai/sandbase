# Open-Meteo API: 12 endpoints with pricing and code examples

Call 12 Open-Meteo endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`open-meteo/air-quality`](../models/open-meteo/air-quality.md) | Hourly air quality forecast for any coordinates: PM2.5, PM10, ozone, NO2, CO, dust, pollen and European/US AQI. | $0.0001 per call (free daily quota) |
| [`open-meteo/archive`](../models/open-meteo/archive.md) | Historical weather by coordinates and date range from the ERA5 reanalysis, back to 1940, with hourly and daily variables. | $0.0001 per call (free daily quota) |
| [`open-meteo/climate`](../models/open-meteo/climate.md) | Daily climate model projections to 2050 for any coordinates, from CMIP6 high-resolution models. | $0.0001 per call (free daily quota) |
| [`open-meteo/elevation`](../models/open-meteo/elevation.md) | Terrain elevation in meters for one or more coordinates, from a 90 m digital elevation model. | $0.0001 per call (free daily quota) |
| [`open-meteo/ensemble`](../models/open-meteo/ensemble.md) | Ensemble weather forecasts by coordinates with every member of a chosen model, for forecast uncertainty and probabilities. | $0.0001 per call (free daily quota) |
| [`open-meteo/flood`](../models/open-meteo/flood.md) | Daily river discharge forecast and history for any coordinates from the GloFAS flood model. | $0.0001 per call (free daily quota) |
| [`open-meteo/forecast`](../models/open-meteo/forecast.md) | Up to 16-day hourly, daily and current weather forecast by coordinates: temperature, precipitation, wind, cloud cover and more. | $0.0001 per call (free daily quota) |
| [`open-meteo/geocoding`](../models/open-meteo/geocoding.md) | Look up places by name and get coordinates, country, timezone, population and elevation for use with the weather APIs. | $0.0001 per call (free daily quota) |
| [`open-meteo/historical-forecast`](../models/open-meteo/historical-forecast.md) | Archived high-resolution weather model forecasts by coordinates and date range, as they were issued. | $0.0001 per call (free daily quota) |
| [`open-meteo/marine`](../models/open-meteo/marine.md) | Hourly and daily marine forecast by coordinates: wave height, direction and period, swell and ocean currents. | $0.0001 per call (free daily quota) |
| [`open-meteo/previous-runs`](../models/open-meteo/previous-runs.md) | Weather forecasts from earlier model runs for the same coordinates, to compare how forecasts changed day by day. | $0.0001 per call (free daily quota) |
| [`open-meteo/seasonal`](../models/open-meteo/seasonal.md) | Seasonal weather forecast up to several months ahead by coordinates, from the ECMWF seasonal model. | $0.0001 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/air-quality", "latitude": "52.52", "longitude": "13.41"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
