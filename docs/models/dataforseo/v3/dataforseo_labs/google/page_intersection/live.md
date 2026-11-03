# DataForSEO Google Page Intersection API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/page_intersection/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0126 per call · **Modes:** sync

Returns search keywords shared between multiple specified Google pages. Helps analyze overlapping search terms to evaluate organic search visibility and competitor overlap.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0126**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/page_intersection/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/page_intersection/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/page_intersection/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/page_intersection/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/page_intersection/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `pages` | object |  | Pages to compare, keyed "1", "2", ...  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns Google keywords that two or more pages all rank for, with search volume, bid, and difficulty data for each keyword. It needs a `pages` object of URLs, plus `location_code` and `language_code`.

### Use cases

- Find the search terms that both `https://www.nike.com/` and `https://www.adidas.com/us` rank for.
- Compare backlink counts of competing pages for the same shared keyword.
- Pick shared keywords with high search volume and low `keyword_difficulty` as content targets.
- Spot shared keywords in other languages by checking `is_another_language`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/page_intersection/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"pages": {"1": "https://www.nike.com/", "2": "https://www.adidas.com/us"}, "limit": 5, "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code, e.g. "en". |
| `limit` | integer | No | Maximum number of results (up to 100). |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |
| `pages` | object | No | Pages to compare, keyed "1", "2", ... |

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
        "function": "page_intersection",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "pages": {
          "1": "https://www.nike.com/",
          "2": "https://www.adidas.com/us"
        },
        "se_type": "google"
      },
      "id": "11030829-1614-0390-0000-ed81aab22af1",
      "path": [
        "v3"
      ],
      "result": [
        {
          "exclude_pages": null,
          "items": [
            {
              "intersection_result": {
                "1": {
                  "about_this_result": null,
                  "amp_version": false,
                  "backlinks_info": {
                    "backlinks": 1667683,
                    "dofollow": 1544885,
                    "referring_domains": 28821,
                    "referring_main_domains": 27025,
                    "referring_pages": 1597382,
                    "time_update": "2026-08-02 05:31:42 +00:00"
                  },
                  "breadcrumb": "https://www.nike.com",
                  "checks": null,
                  "clickstream_etv": null,
                  "description": "From class to sport, find back-to-school essentials for day one and beyond. Shop…",
                  "domain": "www.nike.com"
                },
                "2": {
                  "about_this_result": null,
                  "amp_version": false,
                  "backlinks_info": {
                    "backlinks": 571654,
                    "dofollow": 553535,
                    "referring_domains": 5818,
                    "referring_main_domains": 5352,
                    "referring_pages": 558236,
                    "time_update": "2026-08-02 05:06:18 +00:00"
                  },
                  "breadcrumb": "https://www.adidas.com › ...",
                  "checks": null,
                  "clickstream_etv": null,
                  "description": "SHOP THE LATEST DROPS · Three young people in athletic wear stand in front of a …",
                  "domain": "www.adidas.com"
                }
              },
              "keyword_data": {
                "avg_backlinks_info": {
                  "backlinks": 30383.900390625,
                  "dofollow": 11344.599609375,
                  "last_updated_time": "2026-08-02 12:25:01 +00:00",
                  "main_domain_rank": 626.2000122070312,
                  "rank": 404.29998779296875,
                  "referring_domains": 1204.199951171875,
                  "referring_main_domains": 1139.800048828125,
                  "referring_pages": 22147.599609375
                },
                "clickstream_keyword_info": null,
                "keyword": "available on store",
                "keyword_info": {
                  "categories": [
                    13575
                  ],
                  "competition": 0,
                  "competition_level": "LOW",
                  "cpc": null,
                  "high_top_of_page_bid": null,
                  "last_updated_time": "2026-09-16 20:30:58 +00:00",
                  "low_top_of_page_bid": null,
                  "monthly_searches": [
                    {
                      "month": 8,
                      "search_volume": 4400,
                      "year": 2026
                    }
                  ]
                },
                "keyword_info_normalized_with_bing": null,
                "keyword_info_normalized_with_clickstream": null,
                "keyword_properties": {
                  "core_keyword": "available in-store",
                  "detected_language": "en",
                  "is_another_language": false,
                  "keyword_difficulty": 92,
                  "se_type": "google",
                  "synonym_clustering_algorithm": "text_processing"
                },
                "language_code": "en"
              },
              "se_type": "google"
            }
          ],
          "items_count": 5,
          "language_code": "en",
          "location_code": 2840,
          "pages": {
            "1": "https://www.nike.com/",
            "2": "https://www.adidas.com/us"
          },
          "se_type": "google",
          "total_count": 23
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.7949 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.8192 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of shared keywords found for the pages. `items_count` shows how many came back in this response. |
| `tasks[].result[].items[].keyword_data.keyword` | The shared search keyword. |
| `tasks[].result[].items[].keyword_data.keyword_info.monthly_searches[]` | Search volume per month. Each row has `year`, `month` and `search_volume`. |
| `tasks[].result[].items[].keyword_data.keyword_info.cpc / competition / competition_level` | Cost per click, a numeric competition value, and a `LOW`, `MEDIUM` or similar label for the keyword. Some values are `null` when no ad data exists. |
| `tasks[].result[].items[].keyword_data.keyword_info.low_top_of_page_bid / high_top_of_page_bid` | Low and high top-of-page bid values for the keyword. These can be `null`. |
| `tasks[].result[].items[].keyword_data.keyword_properties.keyword_difficulty` | Difficulty score for ranking on the keyword. Higher values mean harder. |
| `tasks[].result[].items[].keyword_data.keyword_properties.detected_language / is_another_language` | Language detected for the keyword text, and whether it differs from the requested `language_code`. |
| `tasks[].result[].items[].keyword_data.avg_backlinks_info` | Average backlink metrics, such as `backlinks`, `referring_domains` and `rank`, for pages ranking on this keyword. |
| `tasks[].result[].items[].intersection_result.1 / intersection_result.2` | Result details for each input page, keyed by the same numbers used in `pages`. Includes `domain`, `description` and `breadcrumb`. |
| `tasks[].result[].items[].intersection_result.1.backlinks_info` | Backlink totals for the ranking page, including `backlinks`, `dofollow`, `referring_domains` and `referring_pages`. The same block exists under key `2`. |

### Notes

- Send each page URL in `pages` under a numbered key: `"1"`, `"2"`, and so on.
- Set `limit` to control how many keywords return, up to 100. The sample call used `limit` 5.
- Compare `items_count` with `total_count` to see whether more shared keywords exist than the response holds.
- To study backlinks in depth for a page, call [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live) or [DataForSEO Backlinks Page Intersection](/apis/dataforseo/v3/backlinks/page_intersection/live).

### Pricing

Billed at the actual cost of each call, about $0.0126 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/page_intersection/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/page_intersection/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/page_intersection/live
