# Apartments.com API: 2 endpoints with pricing and code examples

Call 2 Apartments.com endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`apartments-com/property`](../models/apartments-com/property.md) | Get an Apartments.com rental property by URL with floor plans, rent, availability, amenities, fees, pet policy and contact info. | $0.00015 per call |
| [`apartments-com/search`](../models/apartments-com/search.md) | Get rental listings from an Apartments.com search URL with property name, address, rent range, beds and listing link. | $0.00015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apartments-com/property", "url": "https://www.apartments.com/edison-austin-austin-tx/40n18nj/"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
