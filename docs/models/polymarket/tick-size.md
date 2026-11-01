# Polymarket Get tick size

`polymarket/tick-size` · api · Polymarket

Retrieves the minimum tick size (price increment) for a specific token ID. The tick size can be provided either as a query parameter or as a path parameter.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tick-size"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tick-size', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tick-size", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tick-size", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/tick-size` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `token_id` | string |  | Token ID (asset ID)  |

## Details

Retrieves the minimum tick size (price increment) for a specific token ID. The tick size can be provided either as a query parameter or as a path parameter.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tick-size" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `token_id` | string | No | Token ID (asset ID) |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/tick-size.json`](../../../catalog/models/polymarket/tick-size.json) · Store page: https://www.sandbase.ai/model/polymarket/tick-size
