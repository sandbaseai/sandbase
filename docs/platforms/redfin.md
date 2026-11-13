# Redfin API: 2 endpoints with pricing and code examples

Call 2 Redfin endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`redfin/property`](../models/redfin/property.md) | Fetch full details for a single Redfin home by its listing URL (price, beds, baths, square feet, address, listing agent, description and… | about $0.0008 per call |
| [`redfin/search`](../models/redfin/search.md) | Search Redfin home listings by region, map bounds or search URL with price, beds, baths, size, status and property type filters, returning… | $0.00015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "redfin/property", "url": "https://www.redfin.com/TX/Austin/1819-Village-Oak-Ct-78704/home/30981993"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
