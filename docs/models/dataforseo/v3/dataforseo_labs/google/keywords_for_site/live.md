# DataForSEO Google Keywords for Site API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/keywords_for_site/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0126 per call · **Modes:** sync

DataForSEO Google Keywords for Site returns Google search keywords that a specified domain ranks for, sourced from the DataForSEO Labs database.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0126**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/keywords_for_site/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/keywords_for_site/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/keywords_for_site/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/keywords_for_site/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/keywords_for_site/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `target` | string |  | Target domain or page, e.g. "nike.com".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

This API returns Google keywords that a domain or page ranks for, with search volume, cost per click, competition and backlink averages for each keyword. It needs a `target` domain or page, plus optional `location_code`, `language_code` and `limit` values.

### Use cases

- Review which Google keywords a competitor domain ranks for in a given country.
- Find high-volume keywords with a low `keyword_difficulty` that a site already ranks for.
- Estimate paid search value of a domain's keywords using `cpc` and top of page bid ranges.
- Track seasonal demand for a site's keywords using the monthly search volume history.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/keywords_for_site/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "limit": 5, "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code, e.g. "en". |
| `limit` | integer | No | Maximum number of results (up to 100). |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |
| `target` | string | No | Target domain or page, e.g. "nike.com". |

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
        "function": "keywords_for_site",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "se_type": "google",
        "target": "nike.com"
      },
      "id": "11030829-1614-0398-0000-208d671a5061",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "avg_backlinks_info": {
                "backlinks": 9.2,
                "dofollow": 6,
                "last_updated_time": "2026-08-01 21:21:04 +00:00",
                "main_domain_rank": 683.2,
                "rank": 30.9,
                "referring_domains": 3.5,
                "referring_main_domains": 3.5,
                "referring_pages": 6.9
              },
              "clickstream_keyword_info": null,
              "keyword": "nike acg fleece",
              "keyword_info": {
                "categories": [
                  10014
                ],
                "competition": 1,
                "competition_level": "HIGH",
                "cpc": 0.51,
                "high_top_of_page_bid": 0.86,
                "last_updated_time": "2026-10-20 00:16:59 +00:00",
                "low_top_of_page_bid": 0.26,
                "monthly_searches": [
                  {
                    "month": 9,
                    "search_volume": 590,
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
                "keyword_difficulty": 0,
                "se_type": "google",
                "synonym_clustering_algorithm": "text_processing",
                "words_count": 3
              },
              "language_code": "en"
            }
          ],
          "items_count": 5,
          "language_code": "en",
          "location_code": 2840,
          "offset": 0,
          "offset_token": "eyJDdXJy…",
          "se_type": "google",
          "target": "nike.com"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "12.8162 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "12.8673 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The Google search keyword that the target ranks for. |
| `tasks[].result[].items[].keyword_info.monthly_searches[]` | Search volume per `month` and `year`. Use it to see recent trends for the keyword. |
| `tasks[].result[].items[].keyword_info.cpc` | Cost per click for the keyword, as a number. |
| `tasks[].result[].items[].keyword_info.competition / tasks[].result[].items[].keyword_info.competition_level` | Competition score for the keyword (`competition`) and its label such as `HIGH` (`competition_level`). |
| `tasks[].result[].items[].keyword_info.low_top_of_page_bid / tasks[].result[].items[].keyword_info.high_top_of_page_bid` | Low and high top of page bid values for the keyword. They can be `null`. |
| `tasks[].result[].items[].keyword_properties.keyword_difficulty` | Difficulty score for ranking on the keyword. Lower values mean easier. |
| `tasks[].result[].items[].keyword_properties.words_count` | Number of words in the keyword. |
| `tasks[].result[].items[].avg_backlinks_info.backlinks / tasks[].result[].items[].avg_backlinks_info.referring_domains` | Average backlink and referring domain counts for pages ranking for this keyword. |
| `tasks[].result[].items[].avg_backlinks_info.rank / tasks[].result[].items[].avg_backlinks_info.main_domain_rank` | Average rank values for the ranking pages and their main domains. |
| `tasks[].result[].items_count` | Number of keyword items returned in this response. |

### Notes

- Use `location_code` such as `2840` (United States) together with `language_code` such as `en` to pick the market.
- `limit` sets the maximum number of items, up to 100.
- For the next page, the response gives `offset` and `offset_token` in `tasks[].result[]`.
- Timestamps such as `last_updated_time` use the format `2026-10-20 00:16:59 +00:00`.

### Pricing

Billed at the actual cost of each call, about $0.0126 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/keywords_for_site/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/keywords_for_site/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/keywords_for_site/live
