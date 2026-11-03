# Polymarket Wallet Positions API: pricing, parameters and code examples

`polymarket/positions` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

A wallet's positions across their lifecycle (open, redeemable, mergeable, closed), with size, average price, current value and PnL.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/positions", "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/positions', {'user': '0xfe787d2da716d60e8acff57fb87eb13cd4d10319'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/positions", {
  "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/positions", sandbase.Params{
	"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
})
```

Same call via the path form: `POST /v1/api/polymarket/positions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end` | integer |  | Inclusive upper bound on `last_event_at`, epoch seconds; omit or `0` for unbounded. A position with no native economics carries no `last_event_at` and is therefore **excluded by any bound**, in either direction; a…  |
| `user` | string | yes | The wallet to anchor on. At least one of `user`/`condition` is required.  |
| `limit` | integer |  | First-page size. Ignored when `cursor` is supplied (the cursor's size wins). range 0–1000 |
| `start` | integer |  | Inclusive lower bound on `last_event_at`, epoch seconds; omit or `0` for unbounded (the `/v2/activity` + `/v2/trades` vocabulary).  |
| `title` | string |  | Case-insensitive market-title substring filter, honoured on every anchor and status. SQL LIKE wildcards (`%`, `_`) keep their usual meaning; empty or whitespace-only is treated as absent; at most 200 characters. NOT…  |
| `cursor` | string |  | Opaque pagination cursor from a prior response's `next_cursor`. It carries the page position, page size, and the status/sort/direction it was minted under.  |
| `status` | string |  | One of `OPEN`, `REDEEMABLE`, `REDEEMABLE_LOST`, `MERGEABLE`, or `CLOSED`; defaults to `OPEN`. `REDEEMABLE_LOST` requires `user`, supports all six sorts, and defaults to `CURRENT_VALUE`; it preserves row status…  |
| `sort_by` | string |  | One of `CURRENT_VALUE`, `PRICE`, `TOKENS`, `UNREALIZED_PNL`, `REALIZED_PNL`, `TOTAL_PNL`, or `TIMESTAMP` (the row's `last_event_at`). `PRICE` ranks by the response's effective `current_price` on every supported anchor…  |
| `event_id` | string |  | Event id(s), comma-separated (at most 20 distinct values). User-anchored only.  |
| `condition` | string |  | Condition id(s), comma-separated (at most 20 distinct values). With `user`, narrows that user's positions (all ids honoured). Without `user`, anchors on the market's holders; exactly one id is accepted there, and a…  |
| `filter_type` | string |  | `CASH` or `TOKENS`; defaults to `TOKENS` (the /v2/trades-homogenized filter pair, replacing the former `size_threshold`).  |
| `filter_amount` | number |  | The filter floor. `TOKENS`: minimum CURRENT holding in shares (defaults to the 0.1 dust floor; applies to `OPEN`/`REDEEMABLE`; a user's `CLOSED` set is not narrowed by it, and on a market anchor it moves the…  |
| `sort_direction` | string |  | `ASC` or `DESC`; defaults to `DESC`.  |
| `include_archived` | boolean |  | Also include positions on archived markets; defaults to `false`. `OPEN`/`REDEEMABLE`/`REDEEMABLE_LOST`/`MERGEABLE` only; combining it with `status=CLOSED` is rejected. Inactive markets remain excluded either way.  |

## Details

Returns a list of Polymarket positions for one wallet. Each row shows share size, average entry price, current price, current value and PnL. It needs a wallet address in `user` and filters by `status`, which defaults to `OPEN`.

### Use cases

- Track what a specific wallet holds right now and how much each position is worth.
- Rank a wallet's positions by `unrealized_pnl` or `total_pnl` to find its best and worst bets.
- Find positions that are `REDEEMABLE` so a wallet owner knows which markets to claim.
- Filter a wallet's positions by market title, such as a tennis tournament, to see its exposure to one topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/positions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319", "limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user` | string | Yes | The wallet to anchor on. At least one of `user`/`condition` is required. |
| `condition` | string | No | Condition id(s), comma-separated (at most 20 distinct values). With `user`, narrows that user's positions (all ids honoured). Without `user`, anchors on the market's holders; exactly one id is accepted there, and a multi |
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

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "archived": false,
      "avg_price": 0.8959,
      "condition_id": "0xdbcc54e623b74b67ea5a8733639a9f5e43ea16bd9b264ddf8772c615a7790d62",
      "current_price": 0.935,
      "current_size": 47155.6168,
      "current_value": 44090.5017,
      "end_date": "2026-11-09",
      "entry_cost_usdc": 42248.4147,
      "entry_fees_usdc": 0.0,
      "event_id": "1289266",
      "event_slug": "wta-yastrem-sonmez-2026-11-01",
      "first_entry_at": 1793687014
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 2,
    "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJwb3NpdGlvbnMiLCJwYXJhbXMiOnsibCI6MiwiZCI6MiwiayI6IjMxODQw…",
    "offset": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].title / data[].outcome` | The market question and the outcome this position holds. `opposite_outcome` names the other side of the market. |
| `data[].condition_id / data[].token_id` | IDs for the market condition and for the outcome token held. `opposite_token_id` is the token for the other outcome. |
| `data[].current_size / data[].total_size` | `current_size` is the number of shares held now. `total_size` is the total share amount shown for the position, which is larger when shares were sold or closed. |
| `data[].avg_price / data[].current_price` | The average entry price and the current price per share. Prices in this response fall between 0 and 1. |
| `data[].current_value` | Mark-to-market value of the position in USDC, based on `current_size` and `current_price`. |
| `data[].entry_cost_usdc / data[].total_cost_usdc / data[].entry_fees_usdc` | USDC cost paid to enter the position, the total cost, and the fees paid on entry. |
| `data[].unrealized_pnl / data[].realized_pnl / data[].total_pnl` | PnL on shares still held, PnL from shares already sold, and the combined figure. |
| `data[].percent_pnl / data[].percent_realized_pnl` | PnL shown as percentages. `percent_realized_pnl` covers the realized part. |
| `data[].first_entry_at / data[].last_event_at` | Epoch-second timestamps of the first entry and the most recent event on the position. |
| `data[].status / data[].redeemable / data[].mergeable` | Lifecycle state of the row, such as `OPEN`, and flags for whether it can be redeemed or merged. |

### Notes

- Use `pagination.next_cursor` as `cursor` to get the next page. `pagination.has_more` tells you if another page exists.
- Re-send `title`, `condition` and other filters on each page of a walk. The cursor only carries the page position, size, status and sort.
- Use `status` set to `CLOSED` for ended positions. [Polymarket Closed Positions](/apis/polymarket/closed-positions) is a related API for that.
- To see who holds a market, call [Polymarket Market Holders](/apis/polymarket/holders) with a condition id.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/positions.json`](../../../catalog/models/polymarket/positions.json) · Store page: https://www.sandbase.ai/model/polymarket/positions
