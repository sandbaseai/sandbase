# DataForSEO Google Ads Keywords for Keywords API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/google_ads/keywords_for_keywords/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.09 per call · **Modes:** sync

Returns relevant Google Ads keyword suggestions based on specified seed keywords. Provides search volume metrics and related search queries directly from Google Ads data.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.09**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/google_ads/keywords_for_keywords/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/google_ads/keywords_for_keywords/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/google_ads/keywords_for_keywords/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/google_ads/keywords_for_keywords/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/google_ads/keywords_for_keywords/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | List of keywords (up to 100 per call).  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns Google Ads keyword ideas for a list of seed keywords. Each idea includes competition level, cost per click, top of page bid and brand or topic tags. Send `keywords` (up to 100), `location_code` and `language_code`.

### Use cases

- Expand a short seed list such as `running shoes` into thousands of related keyword ideas for a PPC campaign.
- Compare `cpc` and `high_top_of_page_bid` across ideas to estimate bidding budgets.
- Filter ideas by `competition_index` to find lower competition terms.
- Group ideas by brand tags in `keyword_annotations` to find competitor brand searches.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/google_ads/keywords_for_keywords/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No | List of keywords (up to 100 per call). |
| `language_code` | string | No | Language code, e.g. "en". |
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
        "api": "keywords_data",
        "function": "keywords_for_keywords",
        "keywords": [
          "running shoes"
        ],
        "language_code": "en",
        "location_code": 2840,
        "se": "google_ads"
      },
      "id": "11030829-1614-0368-0000-12dba2f91a04",
      "path": [
        "v3"
      ],
      "result": [
        {
          "competition": "HIGH",
          "competition_index": 100,
          "cpc": 1.09,
          "high_top_of_page_bid": 2.07,
          "keyword": "running shoes",
          "keyword_annotations": {
            "concepts": null
          },
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 2768,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "12.8287 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "12.8613 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].keyword` | The keyword idea suggested for the seed keywords. |
| `tasks[].result[].competition` | Competition level for the keyword as a label, such as `HIGH`. |
| `tasks[].result[].competition_index` | Numeric competition score for the keyword. A value of `100` goes with the `HIGH` label in this response. |
| `tasks[].result[].cpc` | Cost per click value for the keyword. The response shows it as a decimal number, for example `1.09`. |
| `tasks[].result[].high_top_of_page_bid` | Top of page bid value for the keyword. It is higher than `cpc` for each row shown. |
| `tasks[].result[].keyword_annotations.concepts[].name` | Name of a concept detected in the keyword, such as `hoka` or `sneakers`. The value is `null` when no concept is found. |
| `tasks[].result[].keyword_annotations.concepts[].concept_group.name / tasks[].result[].keyword_annotations.concepts[].concept_group.type` | Group label for the concept, such as `Brand` or `Shoe`. `type` is `null` for some groups. |
| `tasks[].result[].language_code / tasks[].result[].location_code` | Language and location the row applies to. They match the request. |
| `tasks[].result_count` | Total number of keyword ideas found for the task, `2768` in this example. |

### Notes

- The `location_code` value `2840` is the United States and `language_code` `en` is English.
- Results sit in `tasks[].result[]`. The call sends one task and returns one item in `tasks`.
- Each task has an `id` in the format `11030829-1614-0368-0000-12dba2f91a04`.
- To get AI-focused search volume for keywords, try [DataForSEO AI Keyword Search Volume](/apis/dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live).

### Pricing

Billed at the actual cost of each call, about $0.09 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/google_ads/keywords_for_keywords/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/google_ads/keywords_for_keywords/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/google_ads/keywords_for_keywords/live
