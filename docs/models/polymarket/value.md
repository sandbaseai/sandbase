# Polymarket Get total value of a user's positions

`polymarket/value` · api · Polymarket

Get total value of a user's positions from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/value", "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/value', {'user': '0x56687bf447db6ffa42ffe2204a05edaa20f55839'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/value", {
  "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/value", sandbase.Params{
	"user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
})
```

Same call via the path form: `POST /v1/api/polymarket/value` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user` | string | yes | User Profile Address (0x-prefixed, 40 hex chars)  |
| `market` | array |  | market  |

## Details

Get total value of a user's positions from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/value" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `market` | array | No | market |
| `user` | string | Yes | User Profile Address (0x-prefixed, 40 hex chars) |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/value.json`](../../../catalog/models/polymarket/value.json) · Store page: https://www.sandbase.ai/model/polymarket/value
