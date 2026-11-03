# DataForSEO Amazon Product Rank Overview API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/amazon/product_rank_overview/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01212 per call · **Modes:** sync

Get Amazon organic and paid ranking metrics for up to 100 ASINs: keyword counts, position distribution and estimated visibility.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01212**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/amazon/product_rank_overview/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/amazon/product_rank_overview/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/amazon/product_rank_overview/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/amazon/product_rank_overview/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/amazon/product_rank_overview/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asins` | array |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Returns Amazon ranking metrics for each ASIN you send: how many keywords the product ranks for, how those rankings split across position bands, and the combined search volume of those keywords. Organic and paid results are reported separately. It needs a list of `asins`, a `location_code` and a `language_code`.

### Use cases

- Compare how many Amazon keywords your product and a competitor's product rank for.
- Check how many of a listing's keywords sit in the top 3 versus on page 2 and below.
- Find out whether a product gets any paid placements in a given market.
- Track a batch of ASINs over time by saving the keyword counts from each call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/amazon/product_rank_overview/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asins": ["B0D1XD1ZV3"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `asins` | array | No |  |
| `language_code` | string | No |  |
| `location_code` | integer | No |  |

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
        "asins": [
          "B0D1XD1ZV3"
        ],
        "function": "product_rank_overview",
        "language_code": "en",
        "location_code": 2840,
        "se_type": "amazon"
      },
      "id": "11030828-2190-0378-0000-5c333a1ed051",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "asin": "B0D1XD1ZV3",
              "metrics": {
                "amazon_paid": {
                  "count": 0,
                  "pos_1": 0,
                  "pos_11_100": 0,
                  "pos_2_3": 0,
                  "pos_4_10": 0,
                  "search_volume": 0
                },
                "amazon_serp": {
                  "count": 248,
                  "pos_1": 4,
                  "pos_11_100": 108,
                  "pos_2_3": 28,
                  "pos_4_10": 108,
                  "search_volume": 13720
                }
              },
              "se_type": "amazon"
            }
          ],
          "items_count": 1,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "amazon",
          "total_count": 1
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.1518 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1581 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].asin` | The ASIN these metrics belong to. Match it to the ASIN in your request. |
| `tasks[].result[].items[].metrics.amazon_serp.count` | Number of keywords the product ranks for in organic Amazon search results. |
| `tasks[].result[].items[].metrics.amazon_serp.pos_1 / pos_2_3 / pos_4_10 / pos_11_100` | Number of organic keywords where the product ranks at position 1, positions 2 to 3, positions 4 to 10, and positions 11 to 100. |
| `tasks[].result[].items[].metrics.amazon_serp.search_volume` | Search volume figure attached to the organic keywords of this product. |
| `tasks[].result[].items[].metrics.amazon_paid.count` | Number of keywords where the product appears in paid Amazon results. It is `0` when the product has no paid placements. |
| `tasks[].result[].items[].metrics.amazon_paid.pos_1 / pos_2_3 / pos_4_10 / pos_11_100` | Paid keyword counts in the same position bands as the organic metrics. |
| `tasks[].result[].items[].metrics.amazon_paid.search_volume` | Search volume figure attached to the paid keywords of this product. |
| `tasks[].result[].items_count / total_count` | Number of items returned and total number of items for the request. |

### Notes

- Send up to 100 ASINs in `asins` in one call. Each ASIN returns one object in `items`.
- `location_code` and `language_code` set the Amazon market. The example uses `2840` and `en`.
- The position bands are separate, so `pos_1`, `pos_2_3`, `pos_4_10` and `pos_11_100` add up to `count` in the example response.

### Pricing

Billed at the actual cost of each call, about $0.01212 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/amazon/product_rank_overview/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/amazon/product_rank_overview/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/amazon/product_rank_overview/live
