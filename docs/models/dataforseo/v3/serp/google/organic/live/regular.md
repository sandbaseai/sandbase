# DataForSEO Google SERP (Regular) API: pricing, parameters and code examples

`dataforseo/v3/serp/google/organic/live/regular` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.002 per run, depending on parameters · **Modes:** sync

Get live Google organic results for any keyword, location and language in a compact format: rank, title, URL, domain and description for each organic result.

## Pricing

- Depends on parameters (`params.depth`).

| parameters | USD |
|---|---|
| defaults | 0.002 |

Formula: `0.002 * Math.ceil(Math.max(params.depth ?? 10.0, 1.0) / 10.0)`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/organic/live/regular", "depth": 10, "keyword": "qwen 3.8 max", "language_code": "en", "location_code": 2840}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/organic/live/regular', {'depth': 10, 'keyword': 'qwen 3.8 max', 'language_code': 'en', 'location_code': 2840})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/organic/live/regular", {
  "depth": 10,
  "keyword": "qwen 3.8 max",
  "language_code": "en",
  "location_code": 2840
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/organic/live/regular", sandbase.Params{
	"depth": 10,
	"keyword": "qwen 3.8 max",
	"language_code": "en",
	"location_code": 2840,
})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/organic/live/regular` with the body above minus `model`.

## Details

The regular SERP endpoint returns only the organic results (rank, title, URL, description) without SERP feature details, which keeps responses small and fast to process.

### Use cases

- Lightweight rank tracking for many keywords.
- Collect top-ranking URLs for content research.
- Compare rankings across locations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/organic/live/regular" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "running shoes", "location_code": 2840, "language_code": "en", "depth": 20}'
```

### Parameters

The body is passed through to DataForSEO. Common fields:

| Name | Type | Description |
|---|---|---|
| `keyword` | string | Search query, e.g. "openai api". |
| `location_code` | integer | DataForSEO location code, e.g. 2840 for the United States. |
| `language_code` | string | Language code, e.g. "en". |
| `depth` | integer | Number of results to return (default 100). |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "status_code": 20000,
  "tasks": [
    {
      "status_message": "Ok.",
      "result": [
        {
          "keyword": "openai api",
          "se_domain": "google.com",
          "location_code": 2840,
          "language_code": "en",
          "item_types": [
            "ai_overview",
            "organic",
            "video",
            "perspectives",
            "related_searches"
          ],
          "items_count": 7,
          "items": [
            {
              "type": "organic",
              "rank_group": 1,
              "rank_absolute": 2,
              "domain": "addepto.com",
              "title": "How to use OpenAI API and API Key? New Guide for 2026",
              "url": "https://addepto.com/blog/what-is-an-openai-api-and-how-to-use-it/",
              "breadcrumb": "https://addepto.com › blog › what-is-an-openai-api-and...",
              "description": "Jun 11, 2026 — How to use the OpenAI API? · Create an OpenAI account · Generate the OpenA…"
            }
          ]
        }
      ]
    }
  ]
}
```

### Notes

- Need AI Overviews, featured snippets or People Also Ask? Use the Advanced SERP API instead.

### Pricing

$0.002 per page of 10 results. The default depth (10) is one page; for example depth 50 costs 5 pages. Failed calls are not charged. Extra crawled pages, pixel rankings, async AI overview, People Also Ask clicks and search operators (site:, intitle: ...) are not supported.

### Related APIs

- [DataForSEO Google Ads Keyword Search Volume](/model/dataforseo/v3/keywords_data/google_ads/search_volume/live): Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.
- [DataForSEO Google Trends](/model/dataforseo/v3/keywords_data/google_trends/explore/live): Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.
- [DataForSEO Website Screenshot](/model/dataforseo/v3/on_page/page_screenshot): Capture a full-page or viewport screenshot of any URL in desktop, mobile or tablet view.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/organic/live/regular.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/organic/live/regular.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/organic/live/regular
