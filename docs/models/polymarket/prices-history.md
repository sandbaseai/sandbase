# Polymarket Get prices history

`polymarket/prices-history` · api · Polymarket

Get prices history from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/prices-history", "market": "<market>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/prices-history', {'market': '<market>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/prices-history", {
  "market": "<market>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/prices-history", sandbase.Params{
	"market": "<market>",
})
```

Same call via the path form: `POST /v1/api/polymarket/prices-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `endTs` | number |  | Filter by items before this unix timestamp.  |
| `market` | string | yes | The market (asset id) to query.  |
| `startTs` | number |  | Filter by items after this unix timestamp.  |
| `fidelity` | integer |  | Accuracy of the data expressed in minutes. Default is 1 minute.  |
| `interval` | string |  | Time interval for data aggregation. one of: `max`, `all`, `1m`, `1w`, `1d`, `6h`, `1h` |

## Details

Get prices history from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/prices-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"market": "32338220190071351435772801779725302244575775216413325951443816017994629993401", "interval": "1w", "fidelity": 60}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `endTs` | number | No | Filter by items before this unix timestamp. |
| `fidelity` | integer | No | Accuracy of the data expressed in minutes. Default is 1 minute. |
| `interval` | string | No | Time interval for data aggregation. |
| `market` | string | Yes | The market (asset id) to query. |
| `startTs` | number | No | Filter by items after this unix timestamp. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/prices-history.json`](../../../catalog/models/polymarket/prices-history.json) · Store page: https://www.sandbase.ai/model/polymarket/prices-history
