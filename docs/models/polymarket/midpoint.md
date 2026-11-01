# Polymarket Get midpoint price

`polymarket/midpoint` · api · Polymarket

Retrieves the midpoint price for a specific token ID. The midpoint is calculated as the average of the best bid and best ask prices.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/midpoint", "token_id": "0xabc123def456..."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/midpoint', {'token_id': '0xabc123def456...'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/midpoint", {
  "token_id": "0xabc123def456..."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/midpoint", sandbase.Params{
	"token_id": "0xabc123def456...",
})
```

Same call via the path form: `POST /v1/api/polymarket/midpoint` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `token_id` | string | yes | Token ID (asset ID)  |

## Details

Retrieves the midpoint price for a specific token ID. The midpoint is calculated as the average of the best bid and best ask prices.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/midpoint" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `token_id` | string | Yes | Token ID (asset ID) |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/midpoint.json`](../../../catalog/models/polymarket/midpoint.json) · Store page: https://www.sandbase.ai/model/polymarket/midpoint
