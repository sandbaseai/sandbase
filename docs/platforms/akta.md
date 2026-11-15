# Akta API: 8 endpoints with pricing and code examples

Call 8 Akta endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`akta/companies`](../models/akta/companies.md) | Build a list of companies matching industry, location and funding filters. | about $0.01 per call |
| [`akta/company-headcount-trends`](../models/akta/company-headcount-trends.md) | Get a company's employee count and growth trends by department. | $0.125 per call |
| [`akta/company-website-traffic`](../models/akta/company-website-traffic.md) | Get a company website's monthly visits, engagement and traffic sources. | $0.075 per call |
| [`akta/concise`](../models/akta/concise.md) | Get a condensed all-section company profile at a flat price. | $0.15 per call |
| [`akta/filters-list`](../models/akta/filters-list.md) | List every filter key accepted by company list generation. Free. | from $0 per run, depending on parameters |
| [`akta/filters-options`](../models/akta/filters-options.md) | Get the allowed values for company list filter keys. Free. | from $0 per run, depending on parameters |
| [`akta/markdown`](../models/akta/markdown.md) | Get selected company profile sections as one Markdown document. | about $0.025 per call |
| [`akta/news-by-id`](../models/akta/news-by-id.md) | Fetch complete news article records by their article ids. | about $0.0005 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "akta/companies", "filters": {"location.hq.country": ["USA"], "firmographic.founded_year": {"gte": 2022}}}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
