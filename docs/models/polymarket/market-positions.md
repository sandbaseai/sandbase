# Polymarket Get positions for a market API: pricing, parameters and code examples

`polymarket/market-positions` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns positions for a market, optionally filtered to a single user.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/market-positions", "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/market-positions', {'market': '0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/market-positions", {
  "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/market-positions", sandbase.Params{
	"market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
})
```

Same call via the path form: `POST /v1/api/polymarket/market-positions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user` | string |  | Filter to a single user by proxy wallet address  |
| `limit` | integer |  | Max number of positions to return per outcome token default `50`; range 0–500 |
| `market` | string | yes | The condition ID of the market to query positions for  |
| `offset` | integer |  | Pagination offset per outcome token default `0`; range 0–10000 |
| `sortBy` | string |  | Sort positions by: - `TOKENS` — Position size (number of tokens) - `CASH_PNL` — Unrealized cash PnL - `REALIZED_PNL` — Realized PnL - `TOTAL_PNL` — Total PnL (cash_pnl + realized_pnl) one of: `TOKENS`, `CASH_PNL`, `REALIZED_PNL`, `TOTAL_PNL`; default `"TOTAL_PNL"` |
| `status` | string |  | Filter positions by status. - `OPEN` — Only positions with size > 0.01 - `CLOSED` — Only positions with size <= 0.01 - `ALL` — All positions regardless of size one of: `OPEN`, `CLOSED`, `ALL`; default `"ALL"` |
| `sortDirection` | string |  | sortDirection one of: `ASC`, `DESC`; default `"DESC"` |

## Details

Returns positions for a market, optionally filtered to a single user.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/market-positions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"market": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7", "limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Max number of positions to return per outcome token |
| `market` | string | Yes | The condition ID of the market to query positions for |
| `offset` | integer | No | Pagination offset per outcome token |
| `sortBy` | string | No | Sort positions by: - `TOKENS` — Position size (number of tokens) - `CASH_PNL` — Unrealized cash PnL - `REALIZED_PNL` — Realized PnL - `TOTAL_PNL` — Total PnL (c |
| `sortDirection` | string | No | sortDirection |
| `status` | string | No | Filter positions by status. - `OPEN` — Only positions with size > 0.01 - `CLOSED` — Only positions with size <= 0.01 - `ALL` — All positions regardless of size |
| `user` | string | No | Filter to a single user by proxy wallet address |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/market-positions.json`](../../../catalog/models/polymarket/market-positions.json) · Store page: https://www.sandbase.ai/model/polymarket/market-positions
