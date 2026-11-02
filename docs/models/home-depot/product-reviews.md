# Home Depot Product Reviews API: pricing, parameters and code examples

`home-depot/product-reviews` · data API · Home Depot · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Get Home Depot product reviews by product ID: overall rating, ratings histogram, recommendation counts, and reviews with filters and sorting.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "home-depot/product-reviews", "product_id": "310009453"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('home-depot/product-reviews', {'product_id': '310009453'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("home-depot/product-reviews", {
  "product_id": "310009453"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "home-depot/product-reviews", sandbase.Params{
	"product_id": "310009453",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/home-depot/product-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `term` | string \\| number \\| boolean |  | The term you want to search, only reviews with matching term will be returned.  |
| `start` | string \\| number \\| boolean |  | Controls the offset of the reviews. This parameter defaults to `1`. If the `pagesize` is `100`, you have to specify `start` as `101` to get the 2nd page results, and the 3rd page is `201`, and so on.  |
| `rating` | string \\| number \\| boolean |  | To include only results with specified ratings. Example for single rating only: `5` Example for multiple ratings (separated by comma `,`): `5,3,2`  |
| `sort_by` |  |  | Sorting reviews. By default the reviews are sorted by `newest`. Available options: `photoreview` - Photo Reviews `mosthelpfull` - Most Helpful `oldest` - Oldest `newest` - Newest `highestrating` - Highest rating…  |
| `pagesize` | string \\| number \\| boolean |  | Determines the number of items per page. By default, `100` (maximum allowed value) results are returned.  |
| `product_id` | string \\| number \\| boolean | yes | The Home Depot identifier of a product. Only Product IDs gathered from the Home Depot US are supported.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `verified_purchases` | string \\| number \\| boolean |  | Whether to include reviews from verified purchases.  |

## Details

Get Home Depot product reviews by product ID: overall rating, ratings histogram, recommendation counts, and reviews with filters and sorting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/home-depot/product-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "310009453"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string/number/boolean | Yes | The Home Depot identifier of a product. Only Product IDs gathered from the Home Depot US are supported. |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `pagesize` | string/number/boolean | No | Determines the number of items per page. By default, `100` (maximum allowed value) results are returned. |
| `rating` | string/number/boolean | No | To include only results with specified ratings. Example for single rating only: `5` Example for multiple ratings (separated by comma `,`): `5,3,2` |
| `sort_by` | any | No | Sorting reviews. By default the reviews are sorted by `newest`. Available options: `photoreview` - Photo Reviews `mosthelpfull` - Most Helpful `oldest` - Oldest `newest` - Newest `highestrating` - Hig… |
| `start` | string/number/boolean | No | Controls the offset of the reviews. This parameter defaults to `1`. If the `pagesize` is `100`, you have to specify `start` as `101` to get the 2nd page results, and the 3rd page is `201`, and so on. |
| `term` | string/number/boolean | No | The term you want to search, only reviews with matching term will be returned. |
| `verified_purchases` | string/number/boolean | No | Whether to include reviews from verified purchases. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/home-depot/product-reviews.json`](../../../catalog/models/home-depot/product-reviews.json) · Store page: https://www.sandbase.ai/model/home-depot/product-reviews
