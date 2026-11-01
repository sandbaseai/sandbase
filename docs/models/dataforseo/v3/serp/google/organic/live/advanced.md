# DataForSEO Google SERP (Advanced)

`dataforseo/v3/serp/google/organic/live/advanced` · api · DataForSEO

Get live Google organic search results for any keyword, location and language, including AI Overviews, featured snippets, People Also Ask and other SERP features, with rank positions and URLs.

## Pricing

- Depends on parameters (`params.depth`).

| parameters | USD |
|---|---|
| defaults | 0.003 |

Formula: `0.003 * Math.ceil(Math.max(params.depth ?? 10.0, 1.0) / 10.0)`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/organic/live/advanced", "depth": 10, "device": "desktop", "keyword": "dinq.me company product", "language_code": "en", "location_code": 2840}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/organic/live/advanced', {'depth': 10, 'device': 'desktop', 'keyword': 'dinq.me company product', 'language_code': 'en', 'location_code': 2840})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/organic/live/advanced", {
  "depth": 10,
  "device": "desktop",
  "keyword": "dinq.me company product",
  "language_code": "en",
  "location_code": 2840
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/organic/live/advanced", sandbase.Params{
	"depth": 10,
	"device": "desktop",
	"keyword": "dinq.me company product",
	"language_code": "en",
	"location_code": 2840,
})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/organic/live/advanced` with the body above minus `model`.

## Details

Send a keyword with a location and language and get the live Google results page as structured JSON: organic rankings plus SERP features such as AI Overviews, featured snippets and People Also Ask.

### Use cases

- Track keyword rankings for SEO.
- Monitor which SERP features (AI Overview, snippets) appear for your keywords.
- Analyze competitor visibility by location.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/organic/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "running shoes", "location_code": 2840, "language_code": "en"}'
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
            "organic"
          ],
          "items_count": 7,
          "items": [
            {
              "type": "organic",
              "rank_group": 1,
              "rank_absolute": 1,
              "domain": "openai.com",
              "title": "API Platform",
              "url": "https://openai.com/api/",
              "breadcrumb": "https://openai.com › api",
              "description": "Our API platform offers our latest models and guides for safety best practices."
            }
          ]
        }
      ]
    }
  ]
}
```

### Notes

- Use `location_code` / `language_code` (or `location_name` / `language_name`) from DataForSEO's location and language lists.
- Other DataForSEO task fields (e.g. `device`, `os`) are passed through as-is.

### Pricing

$0.003 per page of 10 results. The default depth (10) is one page; for example depth 50 costs 5 pages. Failed calls are not charged. Extra crawled pages, pixel rankings, async AI overview, People Also Ask clicks and search operators (site:, intitle: ...) are not supported.

### Related APIs

- [DataForSEO Google Ads Keyword Search Volume](/model/dataforseo/v3/keywords_data/google_ads/search_volume/live): Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.
- [DataForSEO Google Trends](/model/dataforseo/v3/keywords_data/google_trends/explore/live): Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.
- [DataForSEO Website Screenshot](/model/dataforseo/v3/on_page/page_screenshot): Capture a full-page or viewport screenshot of any URL in desktop, mobile or tablet view.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/organic/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/organic/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/organic/live/advanced
