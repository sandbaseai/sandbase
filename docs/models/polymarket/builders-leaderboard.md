# Polymarket Get aggregated builder leaderboard API: pricing, parameters and code examples

`polymarket/builders-leaderboard` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Get aggregated builder leaderboard from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/builders-leaderboard"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/builders-leaderboard', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/builders-leaderboard", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/builders-leaderboard", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/builders-leaderboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of builders to return default `25`; range 0–50 |
| `offset` | integer |  | Starting index for pagination default `0`; range 0–1000 |
| `timePeriod` | string |  | The time period to aggregate results over. one of: `DAY`, `WEEK`, `MONTH`, `ALL`; default `"DAY"` |

## Details

Get aggregated builder leaderboard from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/builders-leaderboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of builders to return |
| `offset` | integer | No | Starting index for pagination |
| `timePeriod` | string | No | The time period to aggregate results over. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/builders-leaderboard.json`](../../../catalog/models/polymarket/builders-leaderboard.json) · Store page: https://www.sandbase.ai/model/polymarket/builders-leaderboard
