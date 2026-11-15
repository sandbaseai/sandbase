# Zoopla API: 5 endpoints with pricing and code examples

Call 5 Zoopla endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`zoopla/property-listing-details`](../models/zoopla/property-listing-details.md) | Get full details of a specific property listing by its Zoopla listing ID. Tries for-sale first, then to-rent if not found. Returns… | $0.09 per call |
| [`zoopla/search-estate-agents`](../models/zoopla/search-estate-agents.md) | Search for estate agents in a specific location. Returns a paginated list of agents with contact details, logo, display address, and… | $0.03 per call |
| [`zoopla/search-properties-for-sale`](../models/zoopla/search-properties-for-sale.md) | Search properties for sale in a specific UK location. | $0.09 per call |
| [`zoopla/search-properties-to-rent`](../models/zoopla/search-properties-to-rent.md) | Search properties to rent in a specific UK location. Returns paginated results including featured and regular rental listings with monthly… | $0.03 per call |
| [`zoopla/search-sold-house-prices`](../models/zoopla/search-sold-house-prices.md) | Search sold house prices in a specific area. Returns paginated results with property sale history including last sale price and date, full… | $0.06 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zoopla/property-listing-details", "listing_id": "67501148"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
