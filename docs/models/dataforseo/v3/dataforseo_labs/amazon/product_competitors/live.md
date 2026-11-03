# DataForSEO Amazon Product Competitors API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/amazon/product_competitors/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0126 per call · **Modes:** sync

Find ASINs competing with a product on shared keywords.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0126**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/amazon/product_competitors/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/amazon/product_competitors/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/amazon/product_competitors/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/amazon/product_competitors/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/amazon/product_competitors/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asin` | string |  | Amazon product ASIN.  |
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns Amazon ASINs that rank for the same keywords as a given product. It needs an Amazon `asin`, plus an optional `location_code`, `language_code` and `limit`. Each competitor comes with keyword overlap counts and ranking position buckets.

### Use cases

- Find the products that compete most directly with your own listing on Amazon search.
- Rank competitors by shared keyword count to pick which listings to study first.
- Compare how often a rival ranks in the top positions against your own product.
- Estimate how much of a competitor's search volume comes from paid placements versus organic results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/amazon/product_competitors/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B0CP9YB3Q4", "limit": 5, "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `asin` | string | No | Amazon product ASIN. |
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
        "asin": "B0CP9YB3Q4",
        "function": "product_competitors",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "se_type": "amazon"
      },
      "id": "11030828-2190-0375-0000-5363d80035e7",
      "path": [
        "v3"
      ],
      "result": [
        {
          "asin": "B0CP9YB3Q4",
          "items": [
            {
              "asin": "B0CP9YB3Q4",
              "avg_position": 16.424508320726172,
              "competitor_metrics": {
                "amazon_paid": {
                  "count": 7,
                  "pos_1": 0,
                  "pos_11_100": 2,
                  "pos_2_3": 0,
                  "pos_4_10": 5,
                  "search_volume": 111
                },
                "amazon_serp": {
                  "count": 3298,
                  "pos_1": 368,
                  "pos_11_100": 1835,
                  "pos_2_3": 446,
                  "pos_4_10": 649,
                  "search_volume": 1979884
                }
              },
              "full_metrics": {
                "amazon_paid": {
                  "count": 7,
                  "pos_1": 0,
                  "pos_11_100": 2,
                  "pos_2_3": 0,
                  "pos_4_10": 5,
                  "search_volume": 111
                },
                "amazon_serp": {
                  "count": 3298,
                  "pos_1": 368,
                  "pos_11_100": 1835,
                  "pos_2_3": 446,
                  "pos_4_10": 649,
                  "search_volume": 1979884
                }
              },
              "intersections": 3305,
              "se_type": "amazon",
              "sum_position": 54283
            }
          ],
          "items_count": 5,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "amazon",
          "total_count": 19923
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "8.4149 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "8.4549 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].asin` | ASIN of a competing product. The first item can be the input ASIN itself, which gives you a baseline for comparison. |
| `tasks[].result[].items[].intersections` | Number of keywords where this ASIN and the input ASIN both appear. |
| `tasks[].result[].items[].avg_position / sum_position` | `avg_position` is the average rank of this ASIN across the shared keywords. `sum_position` is the total of those ranks. |
| `tasks[].result[].items[].competitor_metrics.amazon_serp.count` | Number of shared keywords where the competitor appears in Amazon search results. |
| `tasks[].result[].items[].competitor_metrics.amazon_serp.search_volume` | Total search volume of those shared keywords. |
| `tasks[].result[].items[].competitor_metrics.amazon_serp.pos_1 / pos_2_3 / pos_4_10 / pos_11_100` | Number of keywords where the competitor ranks at position 1, 2 to 3, 4 to 10, or 11 to 100. |
| `tasks[].result[].items[].competitor_metrics.amazon_paid` | Same counts and `search_volume` for paid placements, limited to the shared keywords. |
| `tasks[].result[].items[].full_metrics` | Same structure as `competitor_metrics`, but covers all keywords the ASIN ranks for, not just the shared ones. |
| `tasks[].result[].total_count` | Total number of competing ASINs found for the input product. |
| `tasks[].result[].items_count` | Number of competitors returned in this response. |

### Notes

- Set `limit` to control how many competitors come back, up to 100.
- Use the 10-character Amazon product ASIN as `asin`, for example `B0CP9YB3Q4`.
- Use `location_code` `2840` for the United States and `language_code` `en` for English.
- Results sit under `tasks[].result[]`, and each task has an `id` you can log.

### Pricing

Billed at the actual cost of each call, about $0.0126 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/amazon/product_competitors/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/amazon/product_competitors/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/amazon/product_competitors/live
