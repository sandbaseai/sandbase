# Polymarket Get public profile by wallet address

`polymarket/public-profile` · api · Polymarket

Get public profile by wallet address from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/public-profile", "address": "<address>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/public-profile', {'address': '<address>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/public-profile", {
  "address": "<address>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/public-profile", sandbase.Params{
	"address": "<address>",
})
```

Same call via the path form: `POST /v1/api/polymarket/public-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `address` | string | yes | The wallet address (proxy wallet or user address)  |

## Details

Get public profile by wallet address from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/public-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"address": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `address` | string | Yes | The wallet address (proxy wallet or user address) |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/public-profile.json`](../../../catalog/models/polymarket/public-profile.json) · Store page: https://www.sandbase.ai/model/polymarket/public-profile
