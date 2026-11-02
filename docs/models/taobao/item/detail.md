# Taobao Product Details API: pricing, parameters and code examples

`taobao/item/detail` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020834 per call · **Modes:** sync

Get a Taobao or Tmall product by item ID: title, images, price, SKU options, delivery and seller details.

## Pricing

- **$0.020834 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/item/detail", "itemId": "920640959876"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/item/detail', {'itemId': '920640959876'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/item/detail", {
  "itemId": "920640959876"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/item/detail", sandbase.Params{
	"itemId": "920640959876",
})
```

Same call via the path form: `POST /v1/api/taobao/item/detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | Unique product identifier on Taobao/Tmall (item ID).  |

## Details

Get a Taobao or Tmall product by item ID: title, images, price, SKU options, delivery and seller details.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/item/detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "920640959876"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Unique product identifier on Taobao/Tmall (item ID). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/taobao/item/detail.json`](../../../../catalog/models/taobao/item/detail.json) · Store page: https://www.sandbase.ai/model/taobao/item/detail
