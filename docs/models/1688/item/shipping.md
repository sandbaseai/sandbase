# 1688 Product Shipping Fee API: pricing, parameters and code examples

`1688/item/shipping` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Estimate domestic shipping for a 1688 product to a Chinese province, by quantity and optional total weight.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/item/shipping", "itemId": "857511694718", "province": "gd"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/item/shipping', {'itemId': '857511694718', 'province': 'gd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/item/shipping", {
  "itemId": "857511694718",
  "province": "gd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/item/shipping", sandbase.Params{
	"itemId": "857511694718",
	"province": "gd",
})
```

Same call via the path form: `POST /v1/api/1688/item/shipping` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | 1688 product ID.  |
| `province` | string | yes | Chinese province name or abbreviation, for example Guangdong or gd.  |
| `totalWeight` | number |  | Total shipment weight in kilograms.  |
| `totalQuantity` | integer |  | Total number of items to ship. default `1` |

## Details

Estimate domestic shipping for a 1688 product to a Chinese province, by quantity and optional total weight.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/item/shipping" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "857511694718", "province": "gd"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | 1688 product ID. |
| `province` | string | Yes | Chinese province name or abbreviation, for example Guangdong or gd. |
| `totalQuantity` | integer | No | Total number of items to ship. |
| `totalWeight` | number | No | Total shipment weight in kilograms. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/1688/item/shipping.json`](../../../../catalog/models/1688/item/shipping.json) · Store page: https://www.sandbase.ai/model/1688/item/shipping
