# Crunchbase API: 4 endpoints with pricing and code examples

Call 4 Crunchbase endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`crunchbase/investor-profile`](../models/crunchbase/investor-profile.md) | Fetch a comprehensive investor profile by permalink/slug. Makes two API calls: one to retrieve investor-specific data (investment count,… | $0.01 per call (free daily quota) |
| [`crunchbase/organization-profile`](../models/crunchbase/organization-profile.md) | Fetch a single organization's full profile by its slug (permalink). Returns the organization's properties including categories, location,… | $0.02 per call |
| [`crunchbase/search-investors`](../models/crunchbase/search-investors.md) | Full-text search over Crunchbase investors. Returns results with investor details including number of investments, exits, location, and… | $0.02 per call |
| [`crunchbase/search-organizations`](../models/crunchbase/search-organizations.md) | Full-text search over Crunchbase organizations. Returns results with organization details including categories, location, employee count,… | $0.02 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "crunchbase/investor-profile", "slug": "slack"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
