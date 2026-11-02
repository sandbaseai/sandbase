# Apollo API: 8 endpoints with pricing and code examples

Call 8 Apollo endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`apollo/company-bulk-enrich`](../models/apollo/company-bulk-enrich.md) | Enrich up to 10 companies in one call. Body takes `domains`, an array of bare domains. | from $0.01975 per run, depending on parameters |
| [`apollo/company-enrich`](../models/apollo/company-enrich.md) | Enrich one company by domain. `domain` is the only parameter and it must be the bare domain (apple.com), not a full URL. | $0.01975 per call |
| [`apollo/company-job-postings`](../models/apollo/company-job-postings.md) | Live job postings for one company, by Apollo organization id. Each posting carries its title, location, posted date and source URL. Useful… | $0.01975 per call |
| [`apollo/company-news-search`](../models/apollo/company-news-search.md) | News Articles Search from Apollo. Returns the official Apollo API response unchanged. | $0.01975 per call |
| [`apollo/company-record`](../models/apollo/company-record.md) | The complete Apollo record for one company, by Apollo organization id (not by domain). | $0.01975 per call |
| [`apollo/company-search`](../models/apollo/company-search.md) | Find companies matching criteria: name, domain, headcount, industry, location, funding stage and technologies in use. | $0.01975 per call |
| [`apollo/people-match`](../models/apollo/people-match.md) | Enrich one person: give whatever identifiers you have and get back Apollo's full record for them. Send identifiers in the JSON request… | $0.01975 per call |
| [`apollo/people-search`](../models/apollo/people-search.md) | Use the People API Search endpoint to find net new people in the Apollo database. Several filters are available to help narrow your… | $0.012 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/company-bulk-enrich", "domains[]": ["stripe.com", "notion.so"]}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
