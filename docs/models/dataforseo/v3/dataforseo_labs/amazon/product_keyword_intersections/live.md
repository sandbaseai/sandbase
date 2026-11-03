# DataForSEO Amazon Product Keyword Intersections API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.012 per call · **Modes:** sync

List keywords several ASINs rank for together, with positions.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asins` | object |  | Amazon ASINs, keyed "1", "2", ...  |
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

This API returns Amazon keywords that two or more ASINs rank for together, with their positions. It needs a set of ASINs (keyed `"1"`, `"2"`, and so on), a `location_code` and a `language_code`.

### Use cases

- Find shared search terms between your product and a competitor's listing on Amazon.
- Spot keyword gaps by comparing the keywords several rival ASINs rank for.
- Build a keyword list for Amazon listing copy or ad campaigns from products that sell in the same niche.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asins": {"1": "B0CP9YB3Q4", "2": "B0D1XD1ZV3"}, "limit": 5, "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `asins` | object | No | Amazon ASINs, keyed "1", "2", ... |
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
        "asins": {
          "1": "B0CP9YB3Q4",
          "2": "B0D1XD1ZV3"
        },
        "function": "product_keyword_intersections",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "se_type": "amazon"
      },
      "id": "11030828-2190-0376-0000-f07f8eaf4f8b",
      "path": [
        "v3"
      ],
      "result": [
        {
          "asins": {
            "1": "B0CP9YB3Q4",
            "2": "B0D1XD1ZV3"
          },
          "items": null,
          "items_count": 0,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "amazon",
          "total_count": null
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.6807 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.6869 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items` | List of keywords the ASINs rank for together. It is `null` when no shared keywords are found, as in this sample. |
| `tasks[].result[].items_count` | Number of items returned in this response. It is `0` when `items` is `null`. |
| `tasks[].result[].total_count` | Total number of matching keywords. It is `null` when there are no results. |
| `tasks[].result[].asins` | The ASINs used in the request, keyed `"1"`, `"2"`, and so on. |
| `tasks[].result[].location_code / tasks[].result[].language_code` | The location and language the request used. The sample shows `2840` and `en`. |
| `tasks[].result[].se_type` | The search engine type. The value is `amazon`. |
| `tasks[].id` | Unique ID of the task, in a UUID-like format. |
| `tasks[].status_code / tasks[].status_message` | Status of the task. `20000` with `Ok.` means the task ran without error. |

### Notes

- Check `items_count` before reading `items`. A call can succeed with status `20000` and still return `items` as `null`.
- Send at least two ASINs in `asins`, keyed as strings (`"1"`, `"2"`). Each ASIN is an Amazon product ID, such as `B0CP9YB3Q4`.
- `limit` sets the maximum number of results and accepts up to 100.
- Results sit in `tasks[].result`. Check `tasks_error` at the top level for failed tasks.

### Pricing

Billed at the actual cost of each call, about $0.012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live
