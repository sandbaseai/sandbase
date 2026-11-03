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

Google Ads search volume for up to 1,000 keywords per request: average monthly searches, 12-month trend, CPC, competition level and top-of-page bid range, for any location and language Google Ads supports.

### Use cases

- Size keyword demand before writing content or launching ads.
- Compare CPC and competition across a keyword list.
- Spot seasonality from the monthly trend.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/google_ads/search_volume/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No | Keywords to look up (up to 1,000). |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | DataForSEO location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "keywords_data",
        "function": "search_volume",
        "keywords": [
          "running shoes"
        ],
        "language_code": "en",
        "location_code": 2840,
        "se": "google_ads"
      },
      "id": "11030141-2190-0367-0000-9041552b839f",
      "path": [
        "v3"
      ],
      "result": [
        {
          "competition": "HIGH",
          "competition_index": 100,
          "cpc": 1.09,
          "high_top_of_page_bid": 2.07,
          "keyword": "running shoes",
          "language_code": "en",
          "location_code": 2840,
          "low_top_of_page_bid": 0.48
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0294 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0978 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[]` | One row per keyword. |
| `search_volume` | Average monthly searches over the last 12 months. |
| `monthly_searches[]` | Searches per month (`year`, `month`, `search_volume`). |
| `cpc / low_top_of_page_bid / high_top_of_page_bid` | Average cost per click and the top-of-page bid range, in USD. |
| `competition / competition_index` | Advertiser competition as LOW/MEDIUM/HIGH and 0-100. |

### Notes

- Google Ads groups close variants, so similar keywords can return the same volume.
- `location_code` 2840 is the United States; `language_code` "en" is English. Low-volume keywords may return null volume.

### Pricing

Billed at the actual cost of each call, about $0.09 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Google Trends](/apis/dataforseo/v3/keywords_data/google_trends/explore/live): Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.
- [DataForSEO Website Screenshot](/apis/dataforseo/v3/on_page/page_screenshot): Capture a full-page or viewport screenshot of any URL in desktop, mobile or tablet view.
- [DataForSEO Google SERP (Advanced)](/apis/dataforseo/v3/serp/google/organic/live/advanced): Get live Google organic search results for any keyword, location and language, including AI Overviews, featured snippets, People Also Ask and other SERP featur…

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/google_ads/search_volume/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/google_ads/search_volume/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/google_ads/search_volume/live
