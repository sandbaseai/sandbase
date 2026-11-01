# 1688 Shop Info

`1688/shop/info` · api · 1688

Get 1688 shop information by shop URL or seller member ID: company, location, ratings and business type.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/shop/info"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/shop/info', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/shop/info", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/shop/info", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/1688/shop/info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shopUrl` | string |  | 1688 shop homepage URL. Supply shopUrl or memberId.  |
| `memberId` | string |  | Seller member ID. Supply memberId or shopUrl.  |

## Details

Get 1688 shop information by shop URL or seller member ID: company, location, ratings and business type.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/shop/info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"memberId": "b2b-3945631662b7581"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shopUrl` | string | No | 1688 shop homepage URL. Supply shopUrl or memberId. |
| `memberId` | string | No | Seller member ID. Supply memberId or shopUrl. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/1688/shop/info.json`](../../../../catalog/models/1688/shop/info.json) · Store page: https://www.sandbase.ai/model/1688/shop/info
