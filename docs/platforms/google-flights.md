# Google Flights API: 4 endpoints with pricing and code examples

Call 4 Google Flights endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`google-flights/autocomplete`](../models/google-flights/autocomplete.md) | Get Google Flights airport and city suggestions for a partial place name, with IATA codes and location IDs. | $0.01 per call |
| [`google-flights/calendar`](../models/google-flights/calendar.md) | Get the lowest Google Flights fare for each departure date in a range between two airports, for one-way or round trips. | $0.01 per call |
| [`google-flights/deals`](../models/google-flights/deals.md) | Find discounted Google Flights fares from a departure airport, with destination, price, discount, dates and airline. | $0.01 per call |
| [`google-flights/search`](../models/google-flights/search.md) | Google Flights itineraries for a route and date: airlines, times, stops, durations, prices and price insights. | $0.015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-flights/autocomplete", "q": "austin"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
