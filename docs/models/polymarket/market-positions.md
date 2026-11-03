# Polymarket Market Positions API: pricing, parameters and code examples

`polymarket/market-positions` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Positions held in one market by condition ID, with each holder wallet, size, value and PnL.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/market-positions", "condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/market-positions', {'condition': '0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/market-positions", {
  "condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/market-positions", sandbase.Params{
	"condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b",
})
```

Same call via the path form: `POST /v1/api/polymarket/market-positions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end` | integer |  | Inclusive upper bound on `last_event_at`, epoch seconds; omit or `0` for unbounded. A position with no native economics carries no `last_event_at` and is therefore **excluded by any bound**, in either direction; a…  |
| `user` | string |  | The wallet to anchor on. At least one of `user`/`condition` is required.  |
| `limit` | integer |  | First-page size. Ignored when `cursor` is supplied (the cursor's size wins). range 0–1000 |
| `start` | integer |  | Inclusive lower bound on `last_event_at`, epoch seconds; omit or `0` for unbounded (the `/v2/activity` + `/v2/trades` vocabulary).  |
| `title` | string |  | Case-insensitive market-title substring filter, honoured on every anchor and status. SQL LIKE wildcards (`%`, `_`) keep their usual meaning; empty or whitespace-only is treated as absent; at most 200 characters. NOT…  |
| `cursor` | string |  | Opaque pagination cursor from a prior response's `next_cursor`. It carries the page position, page size, and the status/sort/direction it was minted under.  |
| `status` | string |  | One of `OPEN`, `REDEEMABLE`, `REDEEMABLE_LOST`, `MERGEABLE`, or `CLOSED`; defaults to `OPEN`. `REDEEMABLE_LOST` requires `user`, supports all six sorts, and defaults to `CURRENT_VALUE`; it preserves row status…  |
| `sort_by` | string |  | One of `CURRENT_VALUE`, `PRICE`, `TOKENS`, `UNREALIZED_PNL`, `REALIZED_PNL`, `TOTAL_PNL`, or `TIMESTAMP` (the row's `last_event_at`). `PRICE` ranks by the response's effective `current_price` on every supported anchor…  |
| `event_id` | string |  | Event id(s), comma-separated (at most 20 distinct values). User-anchored only.  |
| `condition` | string | yes | Condition id(s), comma-separated (at most 20 distinct values). With `user`, narrows that user's positions (all ids honoured). Without `user`, anchors on the market's holders; exactly one id is accepted there, and a…  |
| `filter_type` | string |  | `CASH` or `TOKENS`; defaults to `TOKENS` (the /v2/trades-homogenized filter pair, replacing the former `size_threshold`).  |
| `filter_amount` | number |  | The filter floor. `TOKENS`: minimum CURRENT holding in shares (defaults to the 0.1 dust floor; applies to `OPEN`/`REDEEMABLE`; a user's `CLOSED` set is not narrowed by it, and on a market anchor it moves the…  |
| `sort_direction` | string |  | `ASC` or `DESC`; defaults to `DESC`.  |
| `include_archived` | boolean |  | Also include positions on archived markets; defaults to `false`. `OPEN`/`REDEEMABLE`/`REDEEMABLE_LOST`/`MERGEABLE` only; combining it with `status=CLOSED` is rejected. Inactive markets remain excluded either way.  |

## Details

Returns the positions holders have in one Polymarket market, with each holder's wallet, share count, current value and PnL. The `condition` parameter takes the market's condition ID. You can also pass `user` to look at one wallet.

### Use cases

- List the largest holders of one outcome in a market, sorted by `current_value`.
- Check how much a large wallet has made or lost on a market through `realized_pnl`, `unrealized_pnl` and `total_pnl`.
- Find the wallets that hold both sides of a market by comparing `outcome` across rows.
- Track when large positions last changed by reading `last_event_at` and filtering with `start` and `end`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/market-positions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b", "limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `condition` | string | Yes | Condition id(s), comma-separated (at most 20 distinct values). With `user`, narrows that user's positions (all ids honoured). Without `user`, anchors on the market's holders; exactly one id is accepted there, and a multi |
| `cursor` | string | No | Opaque pagination cursor from a prior response's `next_cursor`. It carries the page position, page size, and the status/sort/direction it was minted under. |
| `end` | integer | No | Inclusive upper bound on `last_event_at`, epoch seconds; omit or `0` for unbounded. A position with no native economics carries no `last_event_at` and is therefore **excluded by any bound**, in either direction; a window |
| `event_id` | string | No | Event id(s), comma-separated (at most 20 distinct values). User-anchored only. |
| `filter_amount` | number | No | The filter floor. `TOKENS`: minimum CURRENT holding in shares (defaults to the 0.1 dust floor; applies to `OPEN`/`REDEEMABLE`; a user's `CLOSED` set is not narrowed by it, and on a market anchor it moves the OPEN/CLOSED  |
| `filter_type` | string | No | `CASH` or `TOKENS`; defaults to `TOKENS` (the /v2/trades-homogenized filter pair, replacing the former `size_threshold`). |
| `include_archived` | boolean | No | Also include positions on archived markets; defaults to `false`. `OPEN`/`REDEEMABLE`/`REDEEMABLE_LOST`/`MERGEABLE` only; combining it with `status=CLOSED` is rejected. Inactive markets remain excluded either way. |
| `limit` | integer | No | First-page size. Ignored when `cursor` is supplied (the cursor's size wins). |
| `sort_by` | string | No | One of `CURRENT_VALUE`, `PRICE`, `TOKENS`, `UNREALIZED_PNL`, `REALIZED_PNL`, `TOTAL_PNL`, or `TIMESTAMP` (the row's `last_event_at`). `PRICE` ranks by the response's effective `current_price` on every supported anchor an |
| `sort_direction` | string | No | `ASC` or `DESC`; defaults to `DESC`. |
| `start` | integer | No | Inclusive lower bound on `last_event_at`, epoch seconds; omit or `0` for unbounded (the `/v2/activity` + `/v2/trades` vocabulary). |
| `status` | string | No | One of `OPEN`, `REDEEMABLE`, `REDEEMABLE_LOST`, `MERGEABLE`, or `CLOSED`; defaults to `OPEN`. `REDEEMABLE_LOST` requires `user`, supports all six sorts, and defaults to `CURRENT_VALUE`; it preserves row status `REDEEMABL |
| `title` | string | No | Case-insensitive market-title substring filter, honoured on every anchor and status. SQL LIKE wildcards (`%`, `_`) keep their usual meaning; empty or whitespace-only is treated as absent; at most 200 characters. NOT carr |
| `user` | string | No | The wallet to anchor on. At least one of `user`/`condition` is required. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "archived": false,
      "avg_price": 0.0,
      "condition_id": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b",
      "current_price": 0.945,
      "current_size": 6736573.9941,
      "current_value": 6366062.4244,
      "end_date": "2026-11-04",
      "entry_cost_usdc": 0.0,
      "entry_fees_usdc": 0.0,
      "event_id": "32228",
      "event_slug": "balance-of-power-2026-midterms",
      "first_entry_at": 0
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 2,
    "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJwb3NpdGlvbnMiLCJwYXJhbXMiOnsibCI6MiwiZCI6MiwiayI6IjE0MjYz…",
    "offset": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].proxy_wallet` | Wallet address of the position holder. |
| `data[].name` | Display name of the holder. It can be an empty string when the holder has no name. |
| `data[].outcome / data[].outcome_index / data[].opposite_outcome` | The outcome this position holds (for example `No`), its index, and the name of the other side of the market. |
| `data[].current_size / data[].total_size` | `current_size` is the number of shares held now. `total_size` is the total shares the holder has bought into this position, and it can be `0.0` when no entry data exists. |
| `data[].current_price / data[].avg_price` | The current price of the outcome token and the holder's average entry price. Both are on a 0 to 1 scale. |
| `data[].current_value` | Mark-to-market value of the position in USDC, based on `current_size` and `current_price`. |
| `data[].total_cost_usdc / data[].entry_cost_usdc / data[].entry_fees_usdc` | Cost and fees the holder paid to enter the position, in USDC. |
| `data[].realized_pnl / data[].unrealized_pnl / data[].total_pnl` | Profit and loss for the holder on this position. `total_pnl` is the sum of the realized and unrealized parts. |
| `data[].percent_pnl / data[].percent_realized_pnl` | Profit and loss as a ratio of cost. |
| `data[].first_entry_at / data[].last_event_at` | Epoch seconds of the holder's first entry and latest event. Both are `0` when the row has no entry data. |

### Notes

- Get the condition ID from the `condition_id` field of a market. Without `user`, `condition` accepts exactly one ID.
- Paginate by passing `pagination.next_cursor` back as `cursor` while `pagination.has_more` is `true`. Re-send `condition` and `title` on every page.
- `status` defaults to `OPEN`. Use `sort_by` and `sort_direction` to change the order.
- To see all markets for one wallet, call [Polymarket Wallet Positions](/apis/polymarket/positions). For a list of holders per outcome token, use [Polymarket Market Holders](/apis/polymarket/holders).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/market-positions.json`](../../../catalog/models/polymarket/market-positions.json) · Store page: https://www.sandbase.ai/model/polymarket/market-positions
