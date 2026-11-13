# Zillow API: 6 endpoints with pricing and code examples

Call 6 Zillow endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`zillow/agent-profile`](../models/zillow/agent-profile.md) | Retrieve a real estate agent's full profile by their username/URL slug. Returns sales stats, reviews, listings, service areas, and… | $0.01 per call (free daily quota) |
| [`zillow/mortgage-rates`](../models/zillow/mortgage-rates.md) | Retrieve current mortgage interest rates from Zillow Home Loans. Returns rates for various loan types including conventional fixed… | $0.05 per call |
| [`zillow/open-houses`](../models/zillow/open-houses.md) | Retrieve the scheduled open houses for a property listing by its Zillow property ID (zpid), together with the property's address for… | $0.03 per call |
| [`zillow/property-details`](../models/zillow/property-details.md) | Retrieve full details for a specific property by its Zillow property ID (zpid). Returns comprehensive property information including… | $0.01 per call (free daily quota) |
| [`zillow/search`](../models/zillow/search.md) | Search Zillow listings by region or map bounds with status, price, beds, baths, home type and size filters, returning address, price,… | $0.01 per call |
| [`zillow/zestimate`](../models/zillow/zestimate.md) | Get the Zestimate (automated home value estimate) and rent Zestimate for a property by zpid. | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zillow/agent-profile", "username": "everydoorrealestate"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
