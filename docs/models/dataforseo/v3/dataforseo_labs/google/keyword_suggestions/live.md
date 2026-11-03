# DataForSEO Labs Google Keyword Suggestions API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0126 per call · **Modes:** sync

Returns Google keyword suggestions alongside relevant search metrics from DataForSEO Labs. Enables discovery of related search terms and query opportunities.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0126**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Long-tail keyword suggestions that contain your seed keyword, each with search volume, CPC, competition, keyword difficulty and search intent, from the DataForSEO Labs database.

### Use cases

- Expand one seed keyword into long-tail variants for content planning.
- Filter suggestions by volume or difficulty to find easy wins.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live" \
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
  "tasks": [
    {
      "status_code": 20000,
      "result": [
        {
          "se_type": "google",
          "location_code": 2840,
          "language_code": "en",
          "total_count": 87287,
          "items_count": 5,
          "items": [
            {
              "keyword": "sneaker running shoes",
              "keyword_info": {
                "search_volume": 301000,
                "cpc": 1.09,
                "competition": 1,
                "competition_level": "HIGH",
                "low_top_of_page_bid": 0.47,
                "high_top_of_page_bid": 2.17
              },
              "keyword_properties": {
                "keyword_difficulty": 43,
                "core_keyword": "sneakers shoes running"
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

- Suggestions always contain the seed phrase. For related ideas that do not, use [Keyword Ideas](/apis/dataforseo/v3/dataforseo_labs/google/keyword_ideas/live).
- `limit` is capped at 100 per call; page with `offset`.

### Pricing

Billed at the actual cost of each call, about $0.0126 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live
