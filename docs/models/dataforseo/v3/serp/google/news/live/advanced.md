# DataForSEO Google News SERP API: pricing, parameters and code examples

`dataforseo/v3/serp/google/news/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Get live Google News results for any keyword, location and language: headlines, sources, URLs, dates and rank.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/news/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/news/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/news/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/news/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/news/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `depth` | string |  | Number of results to return.  |
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | DataForSEO location code, e.g. 2840 for the United States.  |

## Details

Send a keyword with a location and language and get the live Google News results as structured JSON.

### Use cases

- Monitor news coverage of a brand or topic.
- Track which publishers rank for a query.
- Feed fresh news into AI summaries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/news/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "running shoes", "location_code": 2840, "language_code": "en"}'
```

### Parameters

The body is passed through to DataForSEO. Common fields:

| Name | Type | Description |
|---|---|---|
| `keyword` | string | Search query. |
| `location_code` | integer | DataForSEO location code, e.g. 2840 for the United States. |
| `language_code` | string | Language code, e.g. "en". |
| `depth` | integer | Number of results to return. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "status_code": 20000,
  "tasks": [
    {
      "result": [
        {
          "keyword": "openai",
          "location_code": 2840,
          "language_code": "en",
          "items_count": 10,
          "items": [
            {
              "type": "news_search",
              "rank_group": 1,
              "domain": "newsletter.semianalysis.com",
              "title": "Anthropic Subscriptions Offer 5x+ More Value Than OpenAI",
              "url": "https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x",
              "time_published": "15 hours ago",
              "timestamp": "2026-10-05 19:49:37 +00:00"
            }
          ]
        }
      ]
    }
  ]
}
```

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. The cost grows with the number of rows, targets or pages a call returns. `depth` sets how many result pages are fetched. Extra crawled pages, pixel rankings, async AI overview, People Also Ask clicks and search operators (site:, intitle: ...) are not supported. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Google Historical Search Volume](/model/dataforseo/v3/dataforseo_labs/google/historical_search_volume/live): Get historical Google search volume for keywords from DataForSEO Labs: monthly searches, CPC, competition and keyword properties by location and language.
- [DataForSEO Google Ads Keyword Search Volume](/model/dataforseo/v3/keywords_data/google_ads/search_volume/live): Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.
- [DataForSEO Google Trends](/model/dataforseo/v3/keywords_data/google_trends/explore/live): Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/news/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/news/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/news/live/advanced
