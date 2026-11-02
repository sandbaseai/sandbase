# Taobao Shop Product List API: pricing, parameters and code examples

`taobao/shop-item-list` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.027778 per call · **Modes:** sync

Get products from a Taobao or Tmall shop using both seller or user ID and shop ID, with page-based pagination and sorting by sales, new arrivals, credit, or price. Use it to browse a known shop catalog.

## Pricing

- **$0.027778 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/shop-item-list", "userId": "1659916565", "shopId": "103710607"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/shop-item-list', {'userId': '1659916565', 'shopId': '103710607'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/shop-item-list", {
  "userId": "1659916565",
  "shopId": "103710607"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/shop-item-list", sandbase.Params{
	"userId": "1659916565",
	"shopId": "103710607",
})
```

Same call via the path form: `POST /v1/api/taobao/shop-item-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `sort` | string |  | Sort order for the result set. one of: `sales-des`, `new-des`, `credit-des`, `price-asc`, `price-des`; default `"sales-des"` |
| `shopId` | string | yes | Unique shop identifier on Taobao/Tmall (shop ID).  |
| `userId` | string | yes | Shop identifier. Also known as Seller ID or User ID (they refer to the same value).  |

## Details

Get products from a Taobao or Tmall shop using both seller or user ID and shop ID, with page-based pagination and sorting by sales, new arrivals, credit, or price. Use it to browse a known shop catalog.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/shop-item-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "1659916565", "shopId": "103710607"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | Shop identifier. Also known as Seller ID or User ID (they refer to the same value). |
| `shopId` | string | Yes | Unique shop identifier on Taobao/Tmall (shop ID). |
| `sort` | string | No | Sort order for the result set. |
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/taobao/shop-item-list.json`](../../../catalog/models/taobao/shop-item-list.json) · Store page: https://www.sandbase.ai/model/taobao/shop-item-list
