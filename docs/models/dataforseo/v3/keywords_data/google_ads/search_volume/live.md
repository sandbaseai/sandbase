# DataForSEO Google Ads Keyword Search Volume API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/google_ads/search_volume/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.09 per call · **Modes:** sync

Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.09**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/google_ads/search_volume/live", "keywords": ["AI agents", "AI agent runtime", "multi agent system", "agentic workflow"], "language_code": "en", "location_code": 2840, "sort_by": "search_volume"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/google_ads/search_volume/live', {'keywords': ['AI agents', 'AI agent runtime', 'multi agent system', 'agentic workflow'], 'language_code': 'en', 'location_code': 2840, 'sort_by': 'search_volume'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/google_ads/search_volume/live", {
  "keywords": [
    "AI agents",
    "AI agent runtime",
    "multi agent system",
    "agentic workflow"
  ],
  "language_code": "en",
  "location_code": 2840,
  "sort_by": "search_volume"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/google_ads/search_volume/live", sandbase.Params{
	"keywords": []any{"AI agents", "AI agent runtime", "multi agent system", "agentic workflow"},
	"language_code": "en",
	"location_code": 2840,
	"sort_by": "search_volume",
})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/google_ads/search_volume/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | Keywords to look up (up to 1,000).  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | DataForSEO location code, e.g. 2840 for the United States.  |

## Details

Send a list of keywords with a location and language and get Google Ads data for each: monthly search volume, CPC, competition level and bid ranges, plus monthly history.

### Use cases

- Size demand for keywords in SEO and PPC planning.
- Estimate CPC and competition before launching ads.
- Track seasonality with monthly search history.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/google_ads/search_volume/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840, "language_code": "en"}'
```

### Parameters

The body is passed through to DataForSEO. Common fields:

| Name | Type | Description |
|---|---|---|
| `keywords` | array | Keywords to look up (up to 1,000). |
| `location_code` | integer | DataForSEO location code, e.g. 2840 for the United States. |
| `language_code` | string | Language code, e.g. "en". |

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
          "location_code": 2840,
          "language_code": "en",
          "search_volume": 49500,
          "competition": "LOW",
          "competition_index": 7,
          "cpc": 11.63,
          "low_top_of_page_bid": 4.02,
          "high_top_of_page_bid": 15,
          "monthly_searches": [
            {
              "month": 8,
              "search_volume": 49500,
              "year": 2026
            },
            {
              "month": 7,
              "search_volume": 49500,
              "year": 2026
            }
          ]
        }
      ]
    }
  ]
}
```

### Notes

- Other DataForSEO task fields (e.g. `date_from`, `search_partners`) are passed through as-is.

### Pricing

Billed at the actual cost of each call, about $0.09 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Google Trends](/model/dataforseo/v3/keywords_data/google_trends/explore/live): Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.
- [DataForSEO Website Screenshot](/model/dataforseo/v3/on_page/page_screenshot): Capture a full-page or viewport screenshot of any URL in desktop, mobile or tablet view.
- [DataForSEO Google SERP (Advanced)](/model/dataforseo/v3/serp/google/organic/live/advanced): Get live Google organic search results for any keyword, location and language, including AI Overviews, featured snippets, People Also Ask and other SERP featur…

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/google_ads/search_volume/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/google_ads/search_volume/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/google_ads/search_volume/live
