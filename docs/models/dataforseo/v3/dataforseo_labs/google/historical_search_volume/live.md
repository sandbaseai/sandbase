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

Returns Google search volume history for each keyword you send, with monthly searches, CPC, competition and keyword properties. It needs a list of `keywords`, a `location_code` and a `language_code`.

### Use cases

- Plot month-by-month search volume for a keyword to spot seasonal peaks.
- Compare `cpc` and top-of-page bid ranges to estimate the cost of paid ads for a keyword.
- Rank a keyword list by `keyword_difficulty` and `competition_level` to pick SEO targets.
- Check the average backlink profile of pages that rank for a keyword to judge how hard it is to compete.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/historical_search_volume/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No | Keywords to look up. |
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
        "api": "dataforseo_labs",
        "function": "historical_search_volume",
        "keywords": [
          "running shoes"
        ],
        "language_code": "en",
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030828-2190-0401-0000-d294af51f4c3",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "avg_backlinks_info": {
                "backlinks": 368.9,
                "dofollow": 204.9,
                "last_updated_time": "2026-08-03 09:50:34 +00:00",
                "main_domain_rank": 569.7,
                "rank": 224.9,
                "referring_domains": 96.8,
                "referring_main_domains": 87.3,
                "referring_pages": 264.8
              },
              "clickstream_keyword_info": null,
              "keyword": "running shoes",
              "keyword_info": {
                "categories": [
                  10014
                ],
                "competition": 1,
                "competition_level": "HIGH",
                "cpc": 1.09,
                "high_top_of_page_bid": 2.07,
                "last_updated_time": "2026-10-18 15:02:03 +00:00",
                "low_top_of_page_bid": 0.48,
                "monthly_searches": [
                  {
                    "month": 9,
                    "search_volume": 246000,
                    "year": 2026
                  }
                ]
              },
              "keyword_info_normalized_with_bing": null,
              "keyword_info_normalized_with_clickstream": null,
              "keyword_properties": {
                "core_keyword": null,
                "detected_language": "en",
                "is_another_language": false,
                "keyword_difficulty": 43,
                "se_type": "google",
                "synonym_clustering_algorithm": "text_processing"
              },
              "language_code": "en"
            }
          ],
          "items_count": 1,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0287 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0342 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The keyword that the metrics in this item describe. |
| `tasks[].result[].items[].keyword_info.monthly_searches[]` | Search volume history as a list of entries. Each entry has `year`, `month` and `search_volume`. |
| `tasks[].result[].items[].keyword_info.cpc` | Cost per click for the keyword. |
| `tasks[].result[].items[].keyword_info.low_top_of_page_bid / high_top_of_page_bid` | Low and high top-of-page bid values for the keyword. |
| `tasks[].result[].items[].keyword_info.competition / competition_level` | Competition as a number from 0 to 1 and as a label such as `HIGH`. |
| `tasks[].result[].items[].keyword_info.categories[]` | Numeric category IDs linked to the keyword. |
| `tasks[].result[].items[].keyword_properties.keyword_difficulty` | Numeric difficulty score for the keyword. |
| `tasks[].result[].items[].keyword_properties.detected_language / is_another_language` | The language detected for the keyword and whether it differs from the requested language. |
| `tasks[].result[].items[].avg_backlinks_info.backlinks / referring_domains / main_domain_rank` | Average backlink counts, referring domain counts and domain rank for pages tied to the keyword. |
| `tasks[].result[].items_count` | Number of keyword items in the result. |

### Notes

- Send several terms in the `keywords` array to get one item per keyword in `tasks[].result[].items[]`.
- `monthly_searches[]` entries use a numeric `month` (for example `9`) and a four-digit `year`.
- Timestamps such as `last_updated_time` use the format `2026-10-18 15:02:03 +00:00`.
- Some blocks, such as `clickstream_keyword_info`, can be `null` in the response.

### Pricing

Billed at the actual cost of each call, about $0.01212 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Google Ads Keyword Search Volume](/apis/dataforseo/v3/keywords_data/google_ads/search_volume/live): Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.
- [DataForSEO Google Trends](/apis/dataforseo/v3/keywords_data/google_trends/explore/live): Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.
- [DataForSEO Website Screenshot](/apis/dataforseo/v3/on_page/page_screenshot): Capture a full-page or viewport screenshot of any URL in desktop, mobile or tablet view.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/historical_search_volume/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/historical_search_volume/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/historical_search_volume/live
