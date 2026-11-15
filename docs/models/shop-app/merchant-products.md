# Shop Merchant Products API: pricing, parameters and code examples

`shop-app/merchant-products` · data API · Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieves one page of a merchant's in-stock product listing, sorted by the site's most-sales order, in a single upstream request.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shop-app/merchant-products", "broker_id": "9658745"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shop-app/merchant-products', {'broker_id': '9658745'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shop-app/merchant-products", {
  "broker_id": "9658745"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shop-app/merchant-products", sandbase.Params{
	"broker_id": "9658745",
})
```

Same call via the path form: `POST /v1/api/shop-app/merchant-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `after` | string |  | Pagination cursor taken unchanged from a previous response's endCursor field. Omit or leave empty for the first page.  |
| `first` | integer |  | Number of products to retrieve per page; must be an integer from 1 to 100, other values are rejected before any request. default `30` |
| `broker_id` | string | yes | Merchant numeric ID from get_merchant_info or get_search_autocomplete results.  |

## Details

Retrieves one page of a merchant's in-stock product listing, sorted by the site's most-sales order, in a single upstream request.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "shop-app/merchant-products", "broker_id": "9658745"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `broker_id` | string | Yes | Merchant numeric ID from get_merchant_info or get_search_autocomplete results. |
| `after` | string | No | Pagination cursor taken unchanged from a previous response's endCursor field. Omit or leave empty for the first page. |
| `first` | integer | No | Number of products to retrieve per page; must be an integer from 1 to 100, other values are rejected before any request. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/shop-app/merchant-products.json`](../../../catalog/models/shop-app/merchant-products.json) · Store page: https://www.sandbase.ai/model/shop-app/merchant-products
