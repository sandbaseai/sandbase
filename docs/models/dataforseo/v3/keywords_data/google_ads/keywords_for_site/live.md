# DataForSEO Google Ads Keywords for Site API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/google_ads/keywords_for_site/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.09 per call · **Modes:** sync

Returns Google Ads keyword suggestions tailored to a target website or webpage. Helps discover relevant search terms and search advertising keywords based on site content.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.09**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/google_ads/keywords_for_site/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/google_ads/keywords_for_site/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/google_ads/keywords_for_site/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/google_ads/keywords_for_site/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/google_ads/keywords_for_site/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | string |  | Target domain or page, e.g. "nike.com".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns Google Ads keyword suggestions for a website or page. Send a `target` domain or URL with a `location_code` and `language_code`. Each result has a keyword, its competition level, and bid estimates.

### Use cases

- Build a keyword list for a Google Ads campaign from a competitor's domain.
- Compare `cpc` and `high_top_of_page_bid` across keywords to plan a bidding budget.
- Find brand and country related search terms for a site using the keyword concept labels.
- Filter keywords by `competition_index` to find lower competition terms for a site.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/google_ads/keywords_for_site/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code, e.g. "en". |
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
        "api": "keywords_data",
        "function": "keywords_for_site",
        "language_code": "en",
        "location_code": 2840,
        "se": "google_ads",
        "target": "nike.com"
      },
      "id": "11030829-1614-0369-0000-21a7879d53b0",
      "path": [
        "v3"
      ],
      "result": [
        {
          "competition": "HIGH",
          "competition_index": 95,
          "cpc": 0.77,
          "high_top_of_page_bid": 4.29,
          "keyword": "nike usa",
          "keyword_annotations": {
            "concepts": [
              {
                "concept_group": {
                  "name": "Others",
                  "type": null
                },
                "name": "nike us"
              }
            ]
          },
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1652,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "13.6819 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "13.7044 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].keyword` | The suggested search term related to the target. |
| `tasks[].result[].competition` | Competition level for the keyword as a label, such as `HIGH`. |
| `tasks[].result[].competition_index` | Competition score as a number. The sample values run from 77 to 95 for `HIGH` keywords. |
| `tasks[].result[].cpc` | Cost per click value for the keyword, as a decimal number. |
| `tasks[].result[].high_top_of_page_bid` | Bid value for a top of page ad position. It is higher than `cpc` in every sample row. |
| `tasks[].result[].keyword_annotations.concepts[].name` | A concept label detected in the keyword, such as `usa`. The value is `null` when no concept applies. |
| `tasks[].result[].keyword_annotations.concepts[].concept_group.name` | The group the concept belongs to, such as `Country` or `Other Brands`. |
| `tasks[].result[].location_code / tasks[].result[].language_code` | The location and language the keyword data applies to. They match the request values. |
| `tasks[].result_count` | Total number of keyword results for the task. |

### Notes

- Use `location_code` `2840` for the United States and `language_code` `en` for English, as in the example request.
- The `target` can be a bare domain such as `nike.com` or a page.
- Results sit under `tasks[].result[]`. Check `tasks[].status_code` (`20000` means success) before reading them.
- Use [DataForSEO AI Keyword Search Volume](/apis/dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live) to look up AI search volume for keywords you pick from this list.

### Pricing

Billed at the actual cost of each call, about $0.09 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/google_ads/keywords_for_site/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/google_ads/keywords_for_site/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/google_ads/keywords_for_site/live
