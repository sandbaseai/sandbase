# Taobao Shop Detail API: pricing, parameters and code examples

`taobao/shop/detail` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get a Taobao or Tmall shop's homepage info, shop categories and default product listing by seller ID and shop ID. Use the category IDs to filter Taobao Shop Items.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/shop/detail", "sellerId": "1659916565", "shopId": "103710607"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/shop/detail', {'sellerId': '1659916565', 'shopId': '103710607'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/shop/detail", {
  "sellerId": "1659916565",
  "shopId": "103710607"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/shop/detail", sandbase.Params{
	"sellerId": "1659916565",
	"shopId": "103710607",
})
```

Same call via the path form: `POST /v1/api/taobao/shop/detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shopId` | string | yes | Taobao shop ID associated with the seller.  |
| `sellerId` | string | yes | Taobao seller user ID associated with the shop.  |

## Details

Get a Taobao or Tmall shop's homepage info, shop categories and default product listing by seller ID and shop ID. Use the category IDs to filter Taobao Shop Items.

The result is returned in `outputs[0].data` in the platform's original structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/shop/detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sellerId": "1659916565", "shopId": "103710607"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sellerId` | string | Yes | Taobao seller user ID associated with the shop. |
| `shopId` | string | Yes | Taobao shop ID associated with the seller. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/taobao/shop/detail.json`](../../../../catalog/models/taobao/shop/detail.json) · Store page: https://www.sandbase.ai/model/taobao/shop/detail
