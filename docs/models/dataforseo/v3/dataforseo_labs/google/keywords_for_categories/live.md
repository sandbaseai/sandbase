# DataForSEO Google Keywords for Categories API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/keywords_for_categories/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

Get Google keywords that belong to the product and service categories you pass, with search volume, CPC and competition.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/keywords_for_categories/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/keywords_for_categories/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/keywords_for_categories/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/keywords_for_categories/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/keywords_for_categories/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |
| `category_codes` | array |  |   |

## Details

Returns Google keywords that belong to one or more product and service category codes. Each keyword comes with search volume, CPC, competition, keyword difficulty and average backlink data. You pass `category_codes`, `location_code` and `language_code`.

### Use cases

- Build a keyword list for a product niche by pulling every keyword tied to one Google category code.
- Compare CPC and competition across keywords in a category to plan a paid search budget.
- Spot high-volume keywords in a category and filter out ones in another language using `keyword_properties.is_another_language`.
- Estimate how hard it is to rank in a category by checking keyword difficulty and backlink averages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/keywords_for_categories/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_codes": [13418], "location_code": 2840, "language_code": "en", "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_codes` | array | No |  |
| `language_code` | string | No |  |
| `limit` | integer | No |  |
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
        "category_codes": [
          13418
        ],
        "function": "keywords_for_categories",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030828-2190-0407-0000-f445e4eb9b5f",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "avg_backlinks_info": {
                "backlinks": 323337.2,
                "dofollow": 183183,
                "last_updated_time": "2023-10-12 06:04:23 +00:00",
                "main_domain_rank": 846.3,
                "rank": 268.1,
                "referring_domains": 1969.1,
                "referring_main_domains": 3611.4,
                "referring_pages": 228521.2
              },
              "clickstream_keyword_info": null,
              "keyword": "yout7be",
              "keyword_info": {
                "categories": [
                  10007
                ],
                "competition": 0.01,
                "competition_level": "LOW",
                "cpc": 0.03,
                "high_top_of_page_bid": 0.02,
                "last_updated_time": "2026-10-16 04:37:35 +00:00",
                "low_top_of_page_bid": 0.01,
                "monthly_searches": [
                  {
                    "month": 9,
                    "search_volume": 226000000,
                    "year": 2026
                  }
                ]
              },
              "keyword_info_normalized_with_bing": null,
              "keyword_info_normalized_with_clickstream": null,
              "keyword_properties": {
                "core_keyword": null,
                "detected_language": "fi",
                "is_another_language": true,
                "keyword_difficulty": 100,
                "se_type": "google",
                "synonym_clustering_algorithm": null,
                "words_count": 1
              },
              "language_code": "en"
            }
          ],
          "items_count": 10,
          "language_code": "en",
          "location_code": 2840,
          "offset": 0,
          "offset_token": "eyJDdXJy…",
          "se_type": "google",
          "seed_categories": [
            13418
          ]
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.7144 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.7219 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The keyword text that belongs to the requested category. |
| `tasks[].result[].items[].keyword_info.categories` | List of category codes the keyword is tied to. Codes can repeat in the list. |
| `tasks[].result[].items[].keyword_info.monthly_searches[]` | Search volume per month. Each row has `year`, `month` and `search_volume`. |
| `tasks[].result[].items[].keyword_info.cpc` | Cost per click value for the keyword. |
| `tasks[].result[].items[].keyword_info.competition / tasks[].result[].items[].keyword_info.competition_level` | Competition score as a number and as a label such as `LOW`. |
| `tasks[].result[].items[].keyword_info.low_top_of_page_bid / tasks[].result[].items[].keyword_info.high_top_of_page_bid` | Low and high bid values for a top of page ad placement. |
| `tasks[].result[].items[].keyword_properties.keyword_difficulty` | Difficulty score for ranking on this keyword. The sample returns `100` for every item. |
| `tasks[].result[].items[].keyword_properties.detected_language / tasks[].result[].items[].keyword_properties.is_another_language` | Language detected for the keyword text and a flag showing whether it differs from the requested language. |
| `tasks[].result[].items[].avg_backlinks_info.backlinks / tasks[].result[].items[].avg_backlinks_info.referring_domains` | Average backlink and referring domain counts for pages that rank for the keyword. |
| `tasks[].result[].offset_token` | Token that marks where the next page of results starts. |

### Notes

- Use `limit` to set how many keywords come back. The response shows `items_count` and `offset` for the current page.
- Pass `offset_token` from a previous response to fetch the next page.
- `monthly_searches` rows use a numeric `month` and a four digit `year`. Timestamps such as `last_updated_time` use the format `2026-10-16 04:37:35 +00:00`.
- Fields such as `clickstream_keyword_info` can be `null` when no data exists for that keyword.

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/keywords_for_categories/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/keywords_for_categories/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/keywords_for_categories/live
