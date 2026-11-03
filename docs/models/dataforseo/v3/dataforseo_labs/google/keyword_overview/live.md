# DataForSEO Google Keyword Overview API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/keyword_overview/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01212 per call · **Modes:** sync

Get search volume, CPC, competition, search intent, monthly trend and SERP info for up to 100 Google keywords by location and language.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01212**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/keyword_overview/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/keyword_overview/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/keyword_overview/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/keyword_overview/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/keyword_overview/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Returns Google keyword metrics for a list of keywords in one location and language. Each keyword comes back with search volume, CPC, competition, keyword difficulty and backlink averages for the pages that rank. You send `keywords`, `location_code` and `language_code`.

### Use cases

- Compare search volume and CPC for a list of candidate keywords before you plan paid or organic campaigns.
- Rank keywords by `keyword_difficulty` to find terms that are easier to target.
- Chart the monthly search trend of a keyword to spot rising or falling demand.
- Estimate the link-building effort for a keyword from the average backlinks and referring domains of ranking pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/keyword_overview/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["openai api"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No |  |
| `language_code` | string | No |  |
| `location_code` | integer | No |  |

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
        "function": "keyword_overview",
        "keywords": [
          "openai api"
        ],
        "language_code": "en",
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030828-2190-0607-0000-86b5b677923c",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "avg_backlinks_info": {
                "backlinks": 209445.7,
                "dofollow": 173685.4,
                "last_updated_time": "2026-07-30 04:48:05 +00:00",
                "main_domain_rank": 586.1,
                "rank": 163.5,
                "referring_domains": 6497.9,
                "referring_main_domains": 5958,
                "referring_pages": 182762.3
              },
              "clickstream_keyword_info": null,
              "keyword": "openai api",
              "keyword_info": {
                "categories": [
                  10019
                ],
                "competition": 0.12,
                "competition_level": "LOW",
                "cpc": 7.57,
                "high_top_of_page_bid": 18.55,
                "last_updated_time": "2026-10-20 05:57:07 +00:00",
                "low_top_of_page_bid": 3.71,
                "monthly_searches": [
                  {
                    "month": 9,
                    "search_volume": 49500,
                    "year": 2026
                  }
                ]
              },
              "keyword_info_normalized_with_bing": null,
              "keyword_info_normalized_with_clickstream": null,
              "keyword_properties": {
                "core_keyword": "api open.ai",
                "detected_language": "en",
                "is_another_language": false,
                "keyword_difficulty": 26,
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
      "time": "0.0263 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0324 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The keyword this row describes. |
| `tasks[].result[].items[].keyword_info.monthly_searches[]` | Search volume per month. Each row has `year`, `month` and `search_volume`. |
| `tasks[].result[].items[].keyword_info.cpc` | Cost per click for the keyword, as a number. |
| `tasks[].result[].items[].keyword_info.low_top_of_page_bid / tasks[].result[].items[].keyword_info.high_top_of_page_bid` | Low and high bid values for top of page ad placement. |
| `tasks[].result[].items[].keyword_info.competition / tasks[].result[].items[].keyword_info.competition_level` | Competition as a number from 0 to 1 and as a label such as `LOW`. |
| `tasks[].result[].items[].keyword_info.categories[]` | Numeric category IDs linked to the keyword. |
| `tasks[].result[].items[].keyword_properties.keyword_difficulty` | Difficulty score for ranking on the keyword. A higher number means harder. |
| `tasks[].result[].items[].keyword_properties.core_keyword` | The main keyword of the synonym group this keyword belongs to. |
| `tasks[].result[].items[].avg_backlinks_info.backlinks / tasks[].result[].items[].avg_backlinks_info.referring_domains` | Average backlink and referring domain counts for pages that rank for the keyword. |
| `tasks[].result[].items_count` | Number of keyword rows in the result. |

### Notes

- Send up to 100 strings in `keywords` per request. Each one returns one entry in `items[]`.
- Set `location_code` and `language_code` together. The example uses `2840` and `en`.
- `clickstream_keyword_info` and the normalized keyword info fields can be `null`, so check for null before you read them.
- Timestamps such as `last_updated_time` use the format `YYYY-MM-DD HH:MM:SS +00:00`.

### Pricing

Billed at the actual cost of each call, about $0.01212 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/keyword_overview/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/keyword_overview/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/keyword_overview/live
