# DataForSEO Google Ranked Keywords API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/ranked_keywords/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0126 per call · **Modes:** sync

Returns all Google search keywords for which a specified domain currently ranks. Provides ranking keyword metrics and organic search performance data.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0126**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/ranked_keywords/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/ranked_keywords/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/ranked_keywords/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/ranked_keywords/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/ranked_keywords/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `target` | string |  | Target domain or page, e.g. "nike.com".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

List the Google keywords a domain or URL ranks for, with each keyword's position, ranking URL, search volume, CPC and estimated traffic. Data comes from the DataForSEO Labs database, which is updated regularly, so a call returns in seconds without running live searches.

### Use cases

- See which keywords bring a competitor its organic traffic.
- Find pages on your site that rank on page two and are worth improving.
- Estimate a domain's organic visibility by summing `etv`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/ranked_keywords/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "limit": 5, "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0].data`.

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
  "tasks": [
    {
      "result": [
        {
          "target": "nike.com",
          "total_count": 665898,
          "items_count": 5,
          "items": [
            {
              "keyword_data": {
                "keyword": "0 3 month nike shoes",
                "keyword_info": {
                  "search_volume": 40,
                  "cpc": 0.3400000035762787,
                  "competition": 1,
                  "competition_level": "HIGH",
                  "low_top_of_page_bid": 0.15000000596046448,
                  "high_top_of_page_bid": 0.49000000953674316
                }
              },
              "ranked_serp_element": {
                "serp_item": {
                  "type": "organic",
                  "rank_group": 1,
                  "rank_absolute": 2,
                  "url": "https://www.nike.com/w/baby-toddler-kids-shoes-2j488zv4dhzy7ok",
                  "title": "Babies & Toddlers (0-3 yrs) Kids Shoes",
                  "etv": 0.71678626537323
                }
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
| `items[].keyword_data.keyword` | The ranking keyword. |
| `items[].keyword_data.keyword_info` | Search volume, CPC, competition and monthly searches for the keyword. |
| `items[].ranked_serp_element.serp_item.rank_group / rank_absolute` | Position among organic results / among all SERP elements. |
| `items[].ranked_serp_element.serp_item.url` | The page of the target that ranks. |
| `items[].ranked_serp_element.serp_item.etv` | Estimated monthly traffic from this keyword. |
| `total_count` | Total ranking keywords; page with `offset` and `limit` (max 100). |

### Notes

- Use `filters` and `order_by` from the official schema, e.g. `["ranked_serp_element.serp_item.rank_group", "<=", 10]` for top-10 rankings only.
- Positions come from the latest database update, not a live search. For live positions use [Google Organic SERP](/apis/dataforseo/v3/serp/google/organic/live/advanced).

### Pricing

Billed at the actual cost of each call, about $0.0126 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/ranked_keywords/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/ranked_keywords/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/ranked_keywords/live
