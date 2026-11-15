# H&M Sale Products API: pricing, parameters and code examples

`hm/sale-products` · data API · H&M · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetch sale/discounted products for a category. Returns products with both regular and discounted prices, discount percentages, and pagination. Uses the same listing mechanism as category pages but scoped to sale sections.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hm/sale-products"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hm/sale-products', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hm/sale-products", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hm/sale-products", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/hm/sale-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination (1-based). default `1` |
| `category` | string |  | Sale category path (e.g. 'women/sale/view-all', 'men/sale/view-all'). default `"women/sale/view-all"` |

## Details

Fetch sale/discounted products for a category. Returns products with both regular and discounted prices, discount percentages, and pagination. Uses the same listing mechanism as category pages but scoped to sale sections.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "hm/sale-products", "page": 1, "category": "women/sale/view-all"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Sale category path (e.g. 'women/sale/view-all', 'men/sale/view-all'). |
| `page` | integer | No | Page number for pagination (1-based). |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hm/sale-products.json`](../../../catalog/models/hm/sale-products.json) · Store page: https://www.sandbase.ai/model/hm/sale-products
