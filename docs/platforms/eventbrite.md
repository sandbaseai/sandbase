# Eventbrite API: 1 endpoints with pricing and code examples

Call 1 Eventbrite endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`eventbrite/search`](../models/eventbrite/search.md) | Search Eventbrite events by keyword and location, with title, date, venue, price, organizer and event link. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "eventbrite/search"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
