# DataForSEO Google Keyword Ideas API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/keyword_ideas/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0126 per call · **Modes:** sync

Returns Google keyword suggestions alongside search volume and CPC metrics for SEO analysis. Helps research related search queries and evaluate keyword potential.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0126**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/keyword_ideas/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/keyword_ideas/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/keyword_ideas/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/keyword_ideas/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/keyword_ideas/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `keywords` | array |  | List of keywords (up to 100 per call).  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Keyword ideas related to up to 100 seed keywords, chosen by topic relevance rather than by containing the seed phrase, with search volume, CPC, competition, keyword difficulty and search intent.

### Use cases

- Find adjacent topics and synonyms you do not rank for yet.
- Build topic clusters from a handful of seed keywords.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/keyword_ideas/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "limit": 5, "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No | List of keywords (up to 100 per call). |
| `language_code` | string | No | Language code, e.g. "en". |
| `limit` | integer | No | Maximum number of results (up to 100). |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "tasks": [
    {
      "status_code": 20000,
      "result": [
        {
          "se_type": "google",
          "location_code": 2840,
          "language_code": "en",
          "total_count": 1013880,
          "items_count": 5,
          "items": [
            {
              "keyword": "on running shoes",
              "keyword_info": {
                "search_volume": 201000,
                "cpc": 1.23,
                "competition": 1,
                "competition_level": "HIGH",
                "low_top_of_page_bid": 0.39,
                "high_top_of_page_bid": 1.96
              },
              "keyword_properties": {
                "keyword_difficulty": 27,
                "core_keyword": "running shoes"
              },
              "search_intent_info": {
                "main_intent": "transactional"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[]` | One row per keyword. |
| `keyword` | The keyword. |
| `keyword_info.search_volume` | Average monthly Google searches (last 12 months). |
| `keyword_info.cpc / competition_level` | Average cost per click in USD and Google Ads competition (LOW/MEDIUM/HIGH). |
| `keyword_info.monthly_searches[]` | Searches per month for the last 12 months. |
| `keyword_properties.keyword_difficulty` | Ranking difficulty 0-100 for the top 10 organic results. |
| `search_intent_info.main_intent` | informational, navigational, commercial or transactional. |
| `total_count` | Matching keywords in the database; page with `offset`. |

### Notes

- Ideas can omit the seed phrase. For variants that always contain it, use [Keyword Suggestions](/apis/dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live).
- `keywords` takes up to 100 seeds; `limit` is capped at 100 per call.

### Pricing

Billed at the actual cost of each call, about $0.0126 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/keyword_ideas/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/keyword_ideas/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/keyword_ideas/live
