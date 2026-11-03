# DataForSEO Google SERP (Advanced) API: pricing, parameters and code examples

`dataforseo/v3/serp/google/organic/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Get live Google organic search results for any keyword, location and language, including AI Overviews, featured snippets, People Also Ask and other SERP features, with rank positions and URLs.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

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

## Parameters

| name | type | required | description |
|---|---|---|---|
| `depth` | string |  | Number of results to return (default 100).  |
| `keyword` | string |  | Search query, e.g. "openai api".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | DataForSEO location code, e.g. 2840 for the United States.  |

## Details

Live Google search results for a keyword in any location, language and device: organic results with position, title, URL and snippet, plus the other SERP features on the page such as AI Overview, featured snippets, People Also Ask, local pack and video results.

### Use cases

- Track rankings for your keywords in specific cities or countries.
- Read the AI Overview and its cited sources for a query.
- Feed fresh search results to an agent or a content brief.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/organic/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "running shoes", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `depth` | string | No | Number of results to return (default 100). |
| `keyword` | string | No | Search query, e.g. "openai api". |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | DataForSEO location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "tasks": [
    {
      "result": [
        {
          "keyword": "running shoes",
          "check_url": "https://www.google.com/search?q=running%20shoes&hl=en&gl=US&ie=UTF-8&uule=w+CAIQIFISCQs2MuSEtepUEUK33kOSuTsc",
          "item_types": [
            "ai_overview",
            "organic",
            "local_pack",
            "images",
            "perspectives",
            "product_considerations",
            "related_searches"
          ],
          "se_results_count": 74,
          "items": [
            {
              "type": "organic",
              "rank_group": 3,
              "rank_absolute": 7,
              "domain": "shop.runnersdepot.com",
              "title": "Running and Walking Shoes",
              "url": "https://shop.runnersdepot.com/",
              "description": "Shop online with Runner&#39;s. Running and Walking Shoes. Shop by Category Shoes Insoles S…"
            }
          ]
        }
      ]
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `result[].item_types` | SERP feature types present on the page, e.g. `organic`, `ai_overview`, `people_also_ask`. |
| `result[].items[]` | Every element in page order. Organic rows have `type: "organic"`, `rank_group`, `rank_absolute`, `title`, `url`, `domain` and `description`. |
| `items[] (type ai_overview)` | AI Overview text in `markdown` and its `references` (source title, URL, domain). |
| `result[].check_url` | The Google URL that was searched, for manual checks. |
| `result[].se_results_count` | Google's reported number of results. |

### Notes

- `depth` sets how many results are fetched; the cost grows with the number of result pages.
- Some organic `url` values come back as `google.com/goto?url=...` redirect links, as Google serves them; follow the redirect to get the destination.
- `location_code` 2840 is the United States; use `location_name` such as "London,England,United Kingdom" for cities.
- The response keeps DataForSEO's original JSON; results are under `tasks[0].result[0]`.

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Google Ads Keyword Search Volume](/apis/dataforseo/v3/keywords_data/google_ads/search_volume/live): Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.
- [DataForSEO Google Trends](/apis/dataforseo/v3/keywords_data/google_trends/explore/live): Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.
- [DataForSEO Website Screenshot](/apis/dataforseo/v3/on_page/page_screenshot): Capture a full-page or viewport screenshot of any URL in desktop, mobile or tablet view.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/organic/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/organic/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/organic/live/advanced
