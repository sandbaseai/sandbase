# 1688 Product Details

`1688/item/detail` · api · 1688

Get a 1688 wholesale product by item ID: images, video, SKU options and prices, tiered pricing, minimum order, seller and shop details.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/item/detail", "itemId": "1046925823679"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/item/detail', {'itemId': '1046925823679'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/item/detail", {
  "itemId": "1046925823679"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/item/detail", sandbase.Params{
	"itemId": "1046925823679",
})
```

Same call via the path form: `POST /v1/api/1688/item/detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | A unique product identifier on 1688.  |

## Details

Get a 1688 wholesale product by item ID: images, video, SKU options and prices, tiered pricing, minimum order, seller and shop details.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/item/detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "1046925823679"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | A unique product identifier on 1688. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/1688/item/detail.json`](../../../../catalog/models/1688/item/detail.json) · Store page: https://www.sandbase.ai/model/1688/item/detail
