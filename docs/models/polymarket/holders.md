# Polymarket Market Holders API: pricing, parameters and code examples

`polymarket/holders` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Top holders of each outcome token in a market by condition ID, with balances and optional PnL.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/holders", "condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/holders', {'condition': '0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/holders", {
  "condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/holders", sandbase.Params{
	"condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b",
})
```

Same call via the path form: `POST /v1/api/polymarket/holders` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Rows per outcome token; defaults to 100, maximum 1000 (100 with `include_pnl=true`). range 0–1000 |
| `cursor` | string |  | Opaque pagination cursor from a prior response's `next_cursor`; carries the per-token `(limit, offset)` window and overrides `limit`. Paging past the first page is cursor-only.  |
| `condition` | string | yes | Comma-separated `condition_id`s (at most 20 distinct values; exactly one with `include_pnl=true`). Required. `condition` is the unified key across v2 (same as the feeds and `/v2/oi`); `condition_id` / `conditionId` are…  |
| `include_pnl` | boolean |  | Opt into per-holder position economics (default `false`; `includePnl` is an accepted alias). Adds `avg_price`, `entry_cost_usdc`, `current_price`, `current_value`, `realized_pnl`, `unrealized_pnl` and `total_pnl` to…  |
| `min_balance` | number |  | Minimum net balance in shares (default 0), applied post-netting. With `include_pnl=true` it applies to the served per-side gross amount instead.  |

## Details

Top holders of each outcome token in a market by condition ID, with balances and optional PnL.

Served from the Polymarket Data API v2. The result is returned in `outputs[0].data`: rows are under `data`, and paginated routes add `pagination.next_cursor` (pass it back as `cursor`).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/holders" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b", "limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `condition` | string | Yes | Comma-separated `condition_id`s (at most 20 distinct values; exactly one with `include_pnl=true`). Required. `condition` is the unified key across v2 (same as the feeds and `/v2/oi`); `condition_id` / |
| `limit` | integer | No | Rows per outcome token; defaults to 100, maximum 1000 (100 with `include_pnl=true`). |
| `cursor` | string | No | Opaque pagination cursor from a prior response's `next_cursor`; carries the per-token `(limit, offset)` window and overrides `limit`. Paging past the first page is cursor-only. |
| `min_balance` | number | No | Minimum net balance in shares (default 0), applied post-netting. With `include_pnl=true` it applies to the served per-side gross amount instead. |
| `include_pnl` | boolean | No | Opt into per-holder position economics (default `false`; `includePnl` is an accepted alias). Adds `avg_price`, `entry_cost_usdc`, `current_price`, `current_value`, `realized_pnl`, `unrealized_pnl` and |

### Reference

- Official docs: https://docs.polymarket.com/api-reference/data-api/overview

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/holders.json`](../../../catalog/models/polymarket/holders.json) · Store page: https://www.sandbase.ai/model/polymarket/holders
