# DataForSEO Google Related Keywords API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/related_keywords/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0126 per call · **Modes:** sync

Returns related search terms that share Google SERP rankings with specified keywords. Helps identify semantically connected queries and search patterns.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0126**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/related_keywords/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/related_keywords/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/related_keywords/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/related_keywords/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/related_keywords/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns keywords related to a seed keyword on Google, with search volume, CPC, competition and keyword difficulty for each one. It needs a `keyword`, and you can set `location_code`, `language_code` and `limit`.

### Use cases

- Build a keyword list around a seed term such as `running shoes`, with search volume and CPC for each row.
- Rank related terms by `keyword_difficulty` to find easier targets.
- Estimate ad costs for related terms from the CPC and top-of-page bid range.
- Chart seasonality of related terms from their monthly search volumes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/related_keywords/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "running shoes", "limit": 5, "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
| `language_code` | string | No | Language code, e.g. "en". |
| `limit` | integer | No | Maximum number of results (up to 100). |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

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
        "function": "related_keywords",
        "keyword": "running shoes",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030828-2190-0387-0000-481d8d79144d",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "depth": 0,
              "keyword_data": {
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
              },
              "related_keywords": [
                "running shoes nike"
              ],
              "se_type": "google"
            }
          ],
          "items_count": 5,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "seed_keyword": "running shoes",
          "seed_keyword_data": null,
          "total_count": 9
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0455 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0529 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].seed_keyword` | The keyword you sent in the request. |
| `tasks[].result[].total_count / items_count` | `total_count` is the number of related keywords found. `items_count` is the number returned in this response. |
| `tasks[].result[].items[].keyword_data.keyword` | A related keyword. |
| `tasks[].result[].items[].depth` | Distance from the seed keyword in the related keyword tree. The seed itself is `0` and its direct related terms are `1`. |
| `tasks[].result[].items[].related_keywords[]` | Further related keywords listed under this item. |
| `tasks[].result[].items[].keyword_data.keyword_info.monthly_searches[]` | Search volume per month. Each row has `year`, `month` and `search_volume`. |
| `tasks[].result[].items[].keyword_data.keyword_info.cpc / low_top_of_page_bid / high_top_of_page_bid` | Cost per click and the low and high top-of-page bid for the keyword. These are price values. |
| `tasks[].result[].items[].keyword_data.keyword_info.competition / competition_level` | Competition score and its label, such as `HIGH`. |
| `tasks[].result[].items[].keyword_data.keyword_properties.keyword_difficulty` | Difficulty score for ranking on this keyword. Higher values mean harder. |
| `tasks[].result[].items[].keyword_data.avg_backlinks_info.backlinks / referring_domains` | Average backlink and referring domain counts for pages that rank for this keyword. |

### Notes

- Pass `location_code` such as `2840` (United States) and `language_code` such as `en` to set the market.
- `limit` caps the number of items returned, up to 100. In the sample, `limit` 5 gave a `total_count` of 9.
- Read results from `tasks[0].result[0].items`. Check `status_code` `20000` for success.
- To check backlink strength for pages that rank for these terms, try [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live).

### Pricing

Billed at the actual cost of each call, about $0.0126 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/related_keywords/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/related_keywords/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/related_keywords/live
