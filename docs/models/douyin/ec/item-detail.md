# Douyin Shop Item Details API: pricing, parameters and code examples

`douyin/ec/item-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.025 per call · **Modes:** sync

Get a Douyin shop product by item ID: title, price, sales, images, specs and shop information.

## Pricing

- **$0.025 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/ec/item-detail", "itemId": "3734619545235751048"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/ec/item-detail', {'itemId': '3734619545235751048'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/ec/item-detail", {
  "itemId": "3734619545235751048"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/ec/item-detail", sandbase.Params{
	"itemId": "3734619545235751048",
})
```

Same call via the path form: `POST /v1/api/douyin/ec/item-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | The unique ID of the item on Douyin E-commerce.  |

## Details

Get a Douyin shop product by item ID: title, price, sales, images, specs and shop information.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/ec/item-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "3734619545235751048"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | The unique ID of the item on Douyin E-commerce. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/ec/item-detail.json`](../../../../catalog/models/douyin/ec/item-detail.json) · Store page: https://www.sandbase.ai/model/douyin/ec/item-detail
