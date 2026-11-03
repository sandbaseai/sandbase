# DataForSEO Google Top Searches API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/top_searches/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

Browse popular Google keywords for a location and language with search volume, CPC and competition, filtered and sorted as needed.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/top_searches/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/top_searches/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/top_searches/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/top_searches/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/top_searches/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Returns a list of popular Google keywords for a location and language. Each keyword comes with search volume, CPC, competition, keyword difficulty and average backlink data. You send `location_code` and `language_code`, and you can set `limit` to control how many rows come back.

### Use cases

- Pull the highest-volume Google keywords in the US to see what people search for most.
- Build a keyword list with CPC and competition values to estimate paid search costs for a market.
- Check the monthly search history of a top keyword to see how its volume changed over recent months.
- Compare `keyword_difficulty` and backlink averages across top keywords to judge how hard they are to rank for.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/top_searches/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_code": 2840, "language_code": "en", "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
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
        "function": "top_searches",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030829-1614-0404-0000-dc861d282e14",
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
                "core_keyword": "youtube",
                "detected_language": "fi",
                "is_another_language": true,
                "keyword_difficulty": 100,
                "se_type": "google",
                "synonym_clustering_algorithm": "keyword_metrics",
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
          "total_count": 1244400009
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "6.4702 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "6.4872 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The popular search term. |
| `tasks[].result[].items[].keyword_info.monthly_searches[]` | Search volume per month. Each row has `year`, `month` and `search_volume`. |
| `tasks[].result[].items[].keyword_info.cpc` | Cost per click for the keyword, as a number. |
| `tasks[].result[].items[].keyword_info.competition / tasks[].result[].items[].keyword_info.competition_level` | Competition as a number and as a label such as `LOW`. |
| `tasks[].result[].items[].keyword_info.low_top_of_page_bid / tasks[].result[].items[].keyword_info.high_top_of_page_bid` | Low and high top-of-page bid values for the keyword. |
| `tasks[].result[].items[].keyword_info.categories[]` | Numeric category IDs assigned to the keyword. |
| `tasks[].result[].items[].keyword_properties.keyword_difficulty` | Difficulty score for ranking on this keyword. The sample shows `100` for the top rows. |
| `tasks[].result[].items[].keyword_properties.detected_language / tasks[].result[].items[].keyword_properties.is_another_language` | The language detected in the keyword text, and whether it differs from the requested language. |
| `tasks[].result[].items[].avg_backlinks_info.backlinks / tasks[].result[].items[].avg_backlinks_info.referring_domains` | Average backlink and referring domain counts for pages that rank for the keyword. |
| `tasks[].result[].total_count` | Total number of keywords available for this location and language. |

### Notes

- Use `location_code` `2840` and `language_code` `en` for the example request. The response echoes both values in `tasks[].result[]`.
- To get the next page, pass the value of `tasks[].result[].offset_token` from the response. The response also reports `offset` and `items_count`.
- `keyword_info.last_updated_time` and `avg_backlinks_info.last_updated_time` use the format `YYYY-MM-DD HH:MM:SS +00:00`.
- Some top keywords are misspellings or other-language terms. Check `keyword_properties.is_another_language` to filter them out.

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/top_searches/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/top_searches/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/top_searches/live
