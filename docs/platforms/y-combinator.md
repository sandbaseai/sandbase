# Y Combinator API: 6 endpoints with pricing and code examples

Call 6 Y Combinator endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`ycombinator/company`](../models/ycombinator/company.md) | Retrieve full details for a YC company by its slug. Returns comprehensive company profile including founders with bios, social links, team… | $0.01 per call (free daily quota) |
| [`ycombinator/partners`](../models/ycombinator/partners.md) | List all current YC Partners. Returns partner profiles with name, slug, title, short bio, and photo URLs. | $0.01 per call (free daily quota) |
| [`ycombinator/person-detail`](../models/ycombinator/person-detail.md) | Get a detailed profile for a YC partner by slug. Returns full biography, achievement stats, associated companies, blog posts, press… | $0.01 per call (free daily quota) |
| [`ycombinator/search-companies`](../models/ycombinator/search-companies.md) | Search and filter the YC company directory via Algolia. Returns paginated results with company metadata including name, batch, industry,… | $0.01 per call (free daily quota) |
| [`ycombinator/search-founders`](../models/ycombinator/search-founders.md) | Search the YC founder directory via Algolia. Returns paginated results with founder metadata including name, current company, title,… | $0.01 per call (free daily quota) |
| [`ycombinator/search-jobs`](../models/ycombinator/search-jobs.md) | List job openings at YC companies from workatastartup.com, filtered by role category. Returns up to 30 jobs per call with title, salary… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ycombinator/company", "slug": "airbnb"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
