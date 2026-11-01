# Polymarket Get trader leaderboard rankings

`polymarket/leaderboard` · api · Polymarket

Returns trader leaderboard rankings for a selected category and time period.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/leaderboard"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/leaderboard', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/leaderboard", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/leaderboard", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/leaderboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user` | string |  | Limit leaderboard to a single user by address  |
| `limit` | integer |  | Max number of leaderboard traders to return default `25`; range 1–50 |
| `offset` | integer |  | Starting index for pagination default `0`; range 0–1000 |
| `orderBy` | string |  | Leaderboard ordering criteria one of: `PNL`, `VOL`; default `"PNL"` |
| `category` | string |  | Market category for the leaderboard one of: `OVERALL`, `POLITICS`, `SPORTS`, `ESPORTS`, `CRYPTO`, `CULTURE`, `MENTIONS`, `WEATHER`, `ECONOMICS`, `TECH`, `FINANCE`; default `"OVERALL"` |
| `userName` | string |  | Limit leaderboard to a single username  |
| `timePeriod` | string |  | Time period for leaderboard results one of: `DAY`, `WEEK`, `MONTH`, `ALL`; default `"DAY"` |

## Details

Returns trader leaderboard rankings for a selected category and time period.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/leaderboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Market category for the leaderboard |
| `limit` | integer | No | Max number of leaderboard traders to return |
| `offset` | integer | No | Starting index for pagination |
| `orderBy` | string | No | Leaderboard ordering criteria |
| `timePeriod` | string | No | Time period for leaderboard results |
| `user` | string | No | Limit leaderboard to a single user by address |
| `userName` | string | No | Limit leaderboard to a single username |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/leaderboard.json`](../../../catalog/models/polymarket/leaderboard.json) · Store page: https://www.sandbase.ai/model/polymarket/leaderboard
