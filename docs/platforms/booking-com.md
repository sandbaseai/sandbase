# Booking.com API: 1 endpoints with pricing and code examples

Call 1 Booking.com endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`booking/search`](../models/booking/search.md) | Search Booking.com properties by destination and dates, with property name, price, rating, review score, address and photos. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "booking/search", "q": "Austin"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
