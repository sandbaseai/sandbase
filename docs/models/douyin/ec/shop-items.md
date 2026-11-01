# Douyin Shop Items

`douyin/ec/shop-items` · api · Douyin

List the products of a Douyin shop by shop ID, page by page, with price and sales for each item.

## Pricing

- **$0.027778 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/ec/shop-items", "shopId": "42853938"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/ec/shop-items', {'shopId': '42853938'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/ec/shop-items", {
  "shopId": "42853938"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/ec/shop-items", sandbase.Params{
	"shopId": "42853938",
})
```

Same call via the path form: `POST /v1/api/douyin/ec/shop-items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for pagination.  |
| `shopId` | string | yes | The unique ID of the shop on Douyin E-commerce.  |

## Details

List the products of a Douyin shop by shop ID, page by page, with price and sales for each item.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/ec/shop-items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shopId": "42853938"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shopId` | string | Yes | The unique ID of the shop on Douyin E-commerce. |
| `page` | string | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/ec/shop-items.json`](../../../../catalog/models/douyin/ec/shop-items.json) · Store page: https://www.sandbase.ai/model/douyin/ec/shop-items
