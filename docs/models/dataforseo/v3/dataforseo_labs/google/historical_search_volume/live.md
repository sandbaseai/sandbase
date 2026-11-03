# DataForSEO Google Historical Search Volume API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/historical_search_volume/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01212 per call · **Modes:** sync

Get historical Google search volume for keywords from DataForSEO Labs: monthly searches, CPC, competition and keyword properties by location and language.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01212**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/historical_search_volume/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/historical_search_volume/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/historical_search_volume/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/historical_search_volume/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/historical_search_volume/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | Keywords to look up.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | DataForSEO location code, e.g. 2840 for the United States.  |

## Details

Send keywords with a location and language and get their search volume history and keyword metrics.

### Use cases

- Analyze seasonality and long-term demand.
- Compare keyword trends year over year.
- Prioritize SEO keywords.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/historical_search_volume/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840, "language_code": "en"}'
```

### Parameters

The body is passed through to DataForSEO. Common fields:

| Name | Type | Description |
|---|---|---|
| `keywords` | array | Keywords to look up. |
| `location_code` | integer | DataForSEO location code, e.g. 2840 for the United States. |
| `language_code` | string | Language code, e.g. "en". |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "status_code": 20000,
  "tasks": [
    {
      "result": [
        {
          "items": [
            {
              "keyword": "openai api",
              "location_code": 2840,
              "keyword_info": {
                "search_volume": 49500,
                "cpc": 11.63,
                "competition": 0.07,
                "competition_level": "LOW",
                "last_updated_time": "2026-09-16 14:09:04 +00:00",
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
            }
          ]
        }
      ]
    }
  ]
}
```

### Pricing

Billed at the actual cost of each call, about $0.01212 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Google Ads Keyword Search Volume](/apis/dataforseo/v3/keywords_data/google_ads/search_volume/live): Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.
- [DataForSEO Google Trends](/apis/dataforseo/v3/keywords_data/google_trends/explore/live): Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.
- [DataForSEO Website Screenshot](/apis/dataforseo/v3/on_page/page_screenshot): Capture a full-page or viewport screenshot of any URL in desktop, mobile or tablet view.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/historical_search_volume/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/historical_search_volume/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/historical_search_volume/live
