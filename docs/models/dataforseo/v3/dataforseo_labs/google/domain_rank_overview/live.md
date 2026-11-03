# DataForSEO Google Domain Rank Overview API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/domain_rank_overview/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01212 per call · **Modes:** sync

Returns Google domain ranking overview metrics and search visibility details. It provides high-level ranking metrics to evaluate domain performance across search engine results.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01212**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/domain_rank_overview/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/domain_rank_overview/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/domain_rank_overview/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/domain_rank_overview/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/domain_rank_overview/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | string |  | Target domain or page, e.g. "nike.com".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Organic and paid search overview of a domain in one call: number of ranking keywords, estimated monthly traffic and its value, and how many keywords are in positions 1, 2-3 and 4-10, plus new, rising, falling and lost rankings.

### Use cases

- Compare competitors' organic visibility.
- Track a domain's ranking distribution month over month.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/domain_rank_overview/live" \
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
  "tasks": [
    {
      "result": [
        {
          "target": "nike.com",
          "items": [
            {
              "metrics": {
                "organic": {
                  "count": 665888,
                  "etv": 8815052.876410566,
                  "estimated_paid_traffic_cost": 5818161.501292776,
                  "pos_1": 184525,
                  "pos_2_3": 74630,
                  "pos_4_10": 123907,
                  "is_new": 308184,
                  "is_up": 134495,
                  "is_down": 124703,
                  "is_lost": 386977
                },
                "paid": {
                  "count": 10,
                  "etv": 196.75402009487152,
                  "estimated_paid_traffic_cost": 155.61605195701122,
                  "pos_1": 10,
                  "pos_2_3": 0,
                  "pos_4_10": 0,
                  "is_new": 9,
                  "is_up": 0,
                  "is_down": 1,
                  "is_lost": 17
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
| `metrics.organic.count` | Keywords the domain ranks for in Google organic results. |
| `metrics.organic.etv` | Estimated monthly organic traffic. |
| `metrics.organic.estimated_paid_traffic_cost` | What that traffic would cost in Google Ads, USD. |
| `metrics.organic.pos_1 / pos_2_3 / pos_4_10` | Keywords in those positions. |
| `metrics.organic.is_new / is_up / is_down / is_lost` | Ranking changes since the previous update. |
| `metrics.paid` | The same metrics for Google Ads. |

### Notes

- Figures are estimates from the DataForSEO Labs database for the given location and language.
- For the keyword list behind these numbers use [Ranked Keywords](/apis/dataforseo/v3/dataforseo_labs/google/ranked_keywords/live).

### Pricing

Billed at the actual cost of each call, about $0.01212 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/domain_rank_overview/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/domain_rank_overview/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/domain_rank_overview/live
