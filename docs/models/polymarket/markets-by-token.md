# Polymarket Get market by token

`polymarket/markets-by-token` · api · Polymarket

Get market by token from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/markets-by-token", "token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/markets-by-token', {'token_id': '32338220190071351435772801779725302244575775216413325951443816017994629993401'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/markets-by-token", {
  "token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/markets-by-token", sandbase.Params{
	"token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401",
})
```

Same call via the path form: `POST /v1/api/polymarket/markets-by-token` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `token_id` | string | yes | The token ID to look up the parent market for  |

## Details

Get market by token from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/markets-by-token" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `token_id` | string | Yes | The token ID to look up the parent market for |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/markets-by-token.json`](../../../catalog/models/polymarket/markets-by-token.json) · Store page: https://www.sandbase.ai/model/polymarket/markets-by-token
