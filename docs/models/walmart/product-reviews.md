# Walmart Product Reviews

`walmart/product-reviews` · api · Walmart

Get Walmart product reviews by product ID: overall rating, ratings histogram, top positive and negative reviews, and paginated review text with photos.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "walmart/product-reviews", "product_id": "20349310960"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('walmart/product-reviews', {'product_id': '20349310960'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("walmart/product-reviews", {
  "product_id": "20349310960"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "walmart/product-reviews", sandbase.Params{
	"product_id": "20349310960",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/walmart/product-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string \\| number \\| boolean |  | Value is used to get the reviews on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.).  |
| `sort` | string \\| number \\| boolean |  | Sorting reviews. It can be set to: `relevancy`, `helpful`, `submission-desc`, `submission-asc`, `rating-desc`, `rating-asc`  |
| `rating` |  |  | Filtering reviews by rating. It can be set to: `1`: 1-star, `2`: 2-star, `3`: 3-star, `4`: 4-star, `5`: 5-star.  |
| `product_id` | string \\| number \\| boolean | yes | The unique product identifier to get reviews of a specific product. You need to pass the `us_item_id`. It can be found from either Organic Results API or Product API results.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Walmart product reviews by product ID: overall rating, ratings histogram, top positive and negative reviews, and paginated review text with photos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/walmart/product-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "20349310960"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string/number/boolean | Yes | The unique product identifier to get reviews of a specific product. You need to pass the `us_item_id`. It can be found from either Organic Results API or Product API results. |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `page` | string/number/boolean | No | Value is used to get the reviews on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). |
| `rating` | any | No | Filtering reviews by rating. It can be set to: `1`: 1-star, `2`: 2-star, `3`: 3-star, `4`: 4-star, `5`: 5-star. |
| `sort` | string/number/boolean | No | Sorting reviews. It can be set to: `relevancy`, `helpful`, `submission-desc`, `submission-asc`, `rating-desc`, `rating-asc` |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/walmart/product-reviews.json`](../../../catalog/models/walmart/product-reviews.json) · Store page: https://www.sandbase.ai/model/walmart/product-reviews
