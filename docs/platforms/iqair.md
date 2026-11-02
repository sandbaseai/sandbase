# IQAir API: 4 endpoints with pricing and code examples

Call 4 IQAir endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`iqair/city-air-quality`](../models/iqair/city-air-quality.md) | Full air quality details for a specific city including current conditions, pollutant breakdown with concentrations, hourly and daily… | $0.01 per call (free daily quota) |
| [`iqair/live-city-ranking`](../models/iqair/live-city-ranking.md) | Real-time global city air quality rankings sorted by AQI descending. Returns up to 122 major cities with current AQI values, geographic… | $0.01 per call (free daily quota) |
| [`iqair/map-data`](../models/iqair/map-data.md) | Air quality station clusters for map visualization. Returns geographic clusters with aggregated AQI values and station counts within the… | $0.01 per call (free daily quota) |
| [`iqair/world-air-quality`](../models/iqair/world-air-quality.md) | Global air quality overview returning the top 15 most polluted and top 15 cleanest major cities worldwide. Each city entry includes… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "iqair/city-air-quality", "city": "new-york-city", "country": "usa", "state": "new-york"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
