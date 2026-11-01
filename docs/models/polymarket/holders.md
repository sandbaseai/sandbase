# Polymarket Get top holders for markets

`polymarket/holders` · api · Polymarket

Get top holders for markets from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/holders", "market": ["0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/holders', {'market': ['0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/holders", {
  "market": [
    "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/holders", sandbase.Params{
	"market": []any{"0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7"},
})
```

Same call via the path form: `POST /v1/api/polymarket/holders` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of holders to return per token. Capped at 20. default `20`; range 0–20 |
| `market` | array | yes | Comma-separated list of condition IDs.  |
| `minBalance` | integer |  | minBalance default `1`; range 0–999999 |

## Details

Get top holders for markets from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/holders" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"market": ["0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7"], "limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of holders to return per token. Capped at 20. |
| `market` | array | Yes | Comma-separated list of condition IDs. |
| `minBalance` | integer | No | minBalance |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/holders.json`](../../../catalog/models/polymarket/holders.json) · Store page: https://www.sandbase.ai/model/polymarket/holders
