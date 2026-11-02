# Xianyu Item Details API: pricing, parameters and code examples

`xianyu/item/detail` · data API · Xianyu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get a Xianyu (Goofish) second-hand listing by item ID: title, price, description, images, seller and location.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xianyu/item/detail", "itemId": "1043659406022"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xianyu/item/detail', {'itemId': '1043659406022'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xianyu/item/detail", {
  "itemId": "1043659406022"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xianyu/item/detail", sandbase.Params{
	"itemId": "1043659406022",
})
```

Same call via the path form: `POST /v1/api/xianyu/item/detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | A unique product identifier on Xianyu.  |

## Details

Get a Xianyu (Goofish) second-hand listing by item ID: title, price, description, images, seller and location.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xianyu/item/detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "1043659406022"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | A unique product identifier on Xianyu. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xianyu/item/detail.json`](../../../../catalog/models/xianyu/item/detail.json) · Store page: https://www.sandbase.ai/model/xianyu/item/detail
