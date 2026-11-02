# Firecrawl API: 5 endpoints with pricing and code examples

Call 5 Firecrawl endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`firecrawl/batch/scrape`](../models/firecrawl/batch/scrape.md) | Scrape multiple URLs in a single batch job. Submit a list of URLs and poll for results as each page completes. | from $0.0075 per run, depending on parameters |
| [`firecrawl/crawl`](../models/firecrawl/crawl.md) | Crawl an entire website starting from a URL. Discovers and scrapes all reachable pages, returning clean markdown for each. Runs… | from $0.0075 per run, depending on parameters |
| [`firecrawl/map`](../models/firecrawl/map.md) | Discovers and returns URLs found across a target website. Provide an HTTPS target address and define the maximum link count to map site… | $0.0075 per call (free daily quota) |
| [`firecrawl/scrape`](../models/firecrawl/scrape.md) | Scrapes content from target web pages with automatic handling of JavaScript rendering. Returns extracted page data based on specified… | $0.0075 per call (free daily quota) |
| [`firecrawl/search`](../models/firecrawl/search.md) | Searches the web using a text query and returns relevant pages with their titles, descriptions, and source URLs. Supports adjusting result… | $0.015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "firecrawl/batch/scrape", "urls": "<urls>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
