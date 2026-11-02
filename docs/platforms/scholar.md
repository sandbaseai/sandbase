# Scholar API: 3 endpoints with pricing and code examples

Call 3 Scholar endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`scholar/search-mixed`](../models/scholar/search-mixed.md) | Returns scholarly and academic search results matching a query. Supports filtering by publication year range and limiting the total number… | $0.0036 per call (free daily quota) |
| [`scholar/search-scholar`](../models/scholar/search-scholar.md) | Search academic papers on Google Scholar: titles, authors, links, citation counts and snippets, with publication-year filters. | $0.0036 per call (free daily quota) |
| [`scholar/search-web`](../models/scholar/search-web.md) | Returns web search results tailored to academic and research topics. Supports filtering by publication year ranges and limiting the total… | $0.0036 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "scholar/search-mixed", "max_num_results": 15, "query": "ferroelectric control of chiral phonons"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
