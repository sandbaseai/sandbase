# DataForSEO Google Domain Intersection API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/domain_intersection/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0126 per call · **Modes:** sync

Returns common Google search keywords shared between specified domains. Helps analyze competitive keyword overlap and search ranking intersections.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0126**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/domain_intersection/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/domain_intersection/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/domain_intersection/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/domain_intersection/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/domain_intersection/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `target1` | string |  | First domain.  |
| `target2` | string |  | Second domain.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns Google keywords where both of two domains rank in search results. Each row gives keyword metrics plus the ranking page details for both domains. You send two domains in `target1` and `target2`, plus a `location_code` and `language_code`.

### Use cases

- Find keywords where `nike.com` and `adidas.com` both rank to see where two brands compete head to head.
- Sort shared keywords by search volume to pick high-traffic terms for a content plan.
- Compare backlink counts of each domain's ranking page to see which side has the stronger page for a keyword.
- Filter shared keywords by `keyword_difficulty` and `cpc` to find low-difficulty terms with commercial value.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/domain_intersection/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target1": "nike.com", "target2": "adidas.com", "location_code": 2840, "language_code": "en", "limit": 5}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code, e.g. "en". |
| `limit` | integer | No | Maximum number of results (up to 100). |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |
| `target1` | string | No | First domain. |
| `target2` | string | No | Second domain. |

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
        "function": "domain_intersection",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "se_type": "google",
        "target1": "nike.com",
        "target2": "adidas.com"
      },
      "id": "11030828-2190-0389-0000-00351c77bc44",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "first_domain_serp_element": {
                "about_this_result": null,
                "amp_version": false,
                "backlinks_info": {
                  "backlinks": 8,
                  "dofollow": 8,
                  "referring_domains": 6,
                  "referring_main_domains": 6,
                  "referring_pages": 8,
                  "time_update": "2026-10-11 04:05:17 +00:00"
                },
                "breadcrumb": "https://www.nike.com › ... › Accessories and Equipment",
                "checks": null,
                "clickstream_etv": null,
                "description": "Basketballs ; Nike Elite All-Court · Nike Elite All-Court Basketball ; Nike Elit…",
                "domain": "www.nike.com"
              },
              "keyword_data": {
                "avg_backlinks_info": {
                  "backlinks": 42.29999923706055,
                  "dofollow": 35.20000076293945,
                  "last_updated_time": "2026-08-03 09:35:29 +00:00",
                  "main_domain_rank": 509.5,
                  "rank": 97.5999984741211,
                  "referring_domains": 20.799999237060547,
                  "referring_main_domains": 20.200000762939453,
                  "referring_pages": 38.20000076293945
                },
                "clickstream_keyword_info": null,
                "keyword": "basketballs",
                "keyword_info": {
                  "categories": [
                    10014
                  ],
                  "competition": 0.3199999928474426,
                  "competition_level": "LOW",
                  "cpc": 0.5400000214576721,
                  "high_top_of_page_bid": 2.7699999809265137,
                  "last_updated_time": "2026-10-16 11:26:51 +00:00",
                  "low_top_of_page_bid": 0.2199999988079071,
                  "monthly_searches": [
                    {
                      "month": 9,
                      "search_volume": 1220000,
                      "year": 2026
                    }
                  ]
                },
                "keyword_info_normalized_with_bing": null,
                "keyword_info_normalized_with_clickstream": null,
                "keyword_properties": {
                  "core_keyword": "basketball",
                  "detected_language": "en",
                  "is_another_language": false,
                  "keyword_difficulty": 9,
                  "se_type": "google",
                  "synonym_clustering_algorithm": "text_processing"
                },
                "language_code": "en"
              },
              "se_type": "google",
              "second_domain_serp_element": {
                "about_this_result": null,
                "amp_version": false,
                "backlinks_info": null,
                "breadcrumb": "https://www.adidas.com › Home › Basketball",
                "checks": null,
                "clickstream_etv": null,
                "description": "Get ready to dominate the hardwood or the street court with basketball balls fro…",
                "domain": "www.adidas.com"
              }
            }
          ],
          "items_count": 5,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "target1": "nike.com",
          "target2": "adidas.com",
          "total_count": 114623
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "1.9956 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.0017 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of shared keywords found for the two domains. Only `items_count` of them are returned in this call. |
| `tasks[].result[].items[].keyword_data.keyword` | The shared search keyword. |
| `tasks[].result[].items[].keyword_data.keyword_info.monthly_searches[]` | Search volume per month. Each entry has `year`, `month` and `search_volume`. |
| `tasks[].result[].items[].keyword_data.keyword_info.cpc / competition / competition_level` | Cost per click, a numeric competition score, and a label such as `LOW` or `MEDIUM`. They describe paid search demand for the keyword. |
| `tasks[].result[].items[].keyword_data.keyword_info.low_top_of_page_bid / high_top_of_page_bid` | Low and high top-of-page bid values for the keyword. |
| `tasks[].result[].items[].keyword_data.keyword_properties.keyword_difficulty` | Difficulty score for the keyword. A higher number means a harder keyword to rank for. |
| `tasks[].result[].items[].keyword_data.keyword_properties.core_keyword` | The base keyword that this keyword is grouped under, such as `soccer ball` for `soccer balls`. |
| `tasks[].result[].items[].keyword_data.avg_backlinks_info` | Average backlink metrics, such as `backlinks`, `referring_domains` and `rank`, across pages that rank for the keyword. |
| `tasks[].result[].items[].first_domain_serp_element.domain / second_domain_serp_element.domain` | The ranking hostname for `target1` and for `target2`. |
| `tasks[].result[].items[].first_domain_serp_element.breadcrumb / description` | The breadcrumb path and snippet text shown in Google for the first domain's result. The second domain's element has the same fields. |
| `tasks[].result[].items[].first_domain_serp_element.backlinks_info` | Backlink counts for the first domain's ranking page, such as `backlinks`, `dofollow` and `referring_domains`. It can be `null`, as seen in the second domain's element for the first row. |

### Notes

- Set `limit` to control how many rows come back (up to 100). The example call used `limit` 5 and returned 5 of `total_count` 114623 rows.
- `location_code` 2840 is the United States and `language_code` `en` is English.
- Timestamps such as `time_update` use the format `2026-10-11 04:05:17 +00:00`.
- For link data on the domains themselves, call [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live) or [DataForSEO Backlinks Competitors](/apis/dataforseo/v3/backlinks/competitors/live).

### Pricing

Billed at the actual cost of each call, about $0.0126 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/domain_intersection/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/domain_intersection/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/domain_intersection/live
