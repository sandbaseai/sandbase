# Realtor.com API: 2 endpoints with pricing and code examples

Call 2 Realtor.com endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`realtor/property`](../models/realtor/property.md) | Get a Realtor.com property by listing URL with price, history, beds, baths, size, lot, year built, schools, agent and photos. | $0.00015 per call |
| [`realtor/search`](../models/realtor/search.md) | Get Realtor.com listings from a search results URL with address, price, beds, baths, size, status and listing link. | $0.00015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "realtor/property", "url": "https://www.realtor.com/realestateandhomes-detail/13409-Madrone-Mountain-Way_Austin_TX_78737_M93328-41646"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
