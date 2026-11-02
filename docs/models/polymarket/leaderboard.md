# Polymarket Trader Leaderboard API: pricing, parameters and code examples

`polymarket/leaderboard` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Polymarket trader leaderboard by PnL or volume, for a time period and category.

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
| `user` | string |  | Look up one wallet's standing instead of reading the board. Returns a single object carrying both ranks, not a page.  |
| `limit` | integer |  | First-page size. Ignored when `cursor` is supplied. range 0–1000 |
| `cursor` | string |  | Opaque pagination cursor from a prior response's `next_cursor`.  |
| `sort_by` | string |  | Which board: `PNL` (default) or `VOLUME`.  |
| `category` | string |  | `overall` (default), a Gamma market category (e.g. `sports`), or a synthetic category: `combos` (combinatorial positions; PNL boards only; the volume board has no combos rows) or `esports` (promoted subcategory).  |
| `time_period` | string |  | Window: `day` \| `week` \| `month` \| `all`. Defaults to `day`.  |

## Details

Polymarket trader leaderboard by PnL or volume, for a time period and category.

Served from the Polymarket Data API v2. The result is returned in `outputs[0].data`: rows are under `data`, and paginated routes add `pagination.next_cursor` (pass it back as `cursor`).

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
| `time_period` | string | No | Window: `day` / `week` / `month` / `all`. Defaults to `day`. |
| `category` | string | No | `overall` (default), a Gamma market category (e.g. `sports`), or a synthetic category: `combos` (combinatorial positions; PNL boards only; the volume board has no combos rows) or `esports` (promoted s |
| `sort_by` | string | No | Which board: `PNL` (default) or `VOLUME`. |
| `user` | string | No | Look up one wallet's standing instead of reading the board. Returns a single object carrying both ranks, not a page. |
| `limit` | integer | No | First-page size. Ignored when `cursor` is supplied. |
| `cursor` | string | No | Opaque pagination cursor from a prior response's `next_cursor`. |

### Reference

- Official docs: https://docs.polymarket.com/api-reference/data-api/overview

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/leaderboard.json`](../../../catalog/models/polymarket/leaderboard.json) · Store page: https://www.sandbase.ai/model/polymarket/leaderboard
