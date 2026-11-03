# Polymarket Closed Positions API: pricing, parameters and code examples

`polymarket/closed-positions` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

A wallet's closed positions with realized PnL, newest first, from the Data API v2.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/closed-positions", "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/closed-positions', {'user': '0xfe787d2da716d60e8acff57fb87eb13cd4d10319'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/closed-positions", {
  "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/closed-positions", sandbase.Params{
	"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
})
```

Same call via the path form: `POST /v1/api/polymarket/closed-positions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end` | integer |  | Inclusive upper bound on `last_event_at`, epoch seconds; omit or `0` for unbounded. A position with no native economics carries no `last_event_at` and is therefore **excluded by any bound**, in either direction; a…  |
| `user` | string | yes | The wallet to anchor on. At least one of `user`/`condition` is required.  |
| `limit` | integer |  | First-page size. Ignored when `cursor` is supplied (the cursor's size wins). range 0–1000 |
| `start` | integer |  | Inclusive lower bound on `last_event_at`, epoch seconds; omit or `0` for unbounded (the `/v2/activity` + `/v2/trades` vocabulary).  |
| `title` | string |  | Case-insensitive market-title substring filter, honoured on every anchor and status. SQL LIKE wildcards (`%`, `_`) keep their usual meaning; empty or whitespace-only is treated as absent; at most 200 characters. NOT…  |
| `cursor` | string |  | Opaque pagination cursor from a prior response's `next_cursor`. It carries the page position, page size, and the status/sort/direction it was minted under.  |
| `sort_by` | string |  | One of `CURRENT_VALUE`, `PRICE`, `TOKENS`, `UNREALIZED_PNL`, `REALIZED_PNL`, `TOTAL_PNL`, or `TIMESTAMP` (the row's `last_event_at`). `PRICE` ranks by the response's effective `current_price` on every supported anchor…  |
| `event_id` | string |  | Event id(s), comma-separated (at most 20 distinct values). User-anchored only.  |
| `condition` | string |  | Condition id(s), comma-separated (at most 20 distinct values). With `user`, narrows that user's positions (all ids honoured). Without `user`, anchors on the market's holders; exactly one id is accepted there, and a…  |
| `filter_type` | string |  | `CASH` or `TOKENS`; defaults to `TOKENS` (the /v2/trades-homogenized filter pair, replacing the former `size_threshold`).  |
| `filter_amount` | number |  | The filter floor. `TOKENS`: minimum CURRENT holding in shares (defaults to the 0.1 dust floor; applies to `OPEN`/`REDEEMABLE`; a user's `CLOSED` set is not narrowed by it, and on a market anchor it moves the…  |
| `sort_direction` | string |  | `ASC` or `DESC`; defaults to `DESC`.  |
| `include_archived` | boolean |  | Also include positions on archived markets; defaults to `false`. `OPEN`/`REDEEMABLE`/`REDEEMABLE_LOST`/`MERGEABLE` only; combining it with `status=CLOSED` is rejected. Inactive markets remain excluded either way.  |

## Details

Returns a wallet's closed Polymarket positions, newest first, with realized PnL, average entry price and market details for each position. It needs a `user` wallet address. You can narrow the list by market, event or title.

### Use cases

- Audit a trader's best and worst settled bets by sorting on `REALIZED_PNL`.
- Build a win/loss history for a wallet over a date window using `start` and `end`.
- Check how a wallet performed in one event, such as a single match, with `event_id` or `condition`.
- Search a wallet's past positions by market title text, such as a team or country name.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/closed-positions" \
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
| `title` | string | No | Case-insensitive market-title substring filter, honoured on every anchor and status. SQL LIKE wildcards (`%`, `_`) keep their usual meaning; empty or whitespace-only is treated as absent; at most 200 characters. NOT carr |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "archived": false,
      "avg_price": 0.5412,
      "condition_id": "0xcd84f901e5b49d769f43d1d78fdf5e913bd736be0dedb7acff688b9655e04ca4",
      "current_price": 1.0,
      "current_size": 0.0,
      "current_value": 0.0,
      "end_date": "2026-07-14",
      "entry_cost_usdc": 0.0,
      "entry_fees_usdc": 5248.774259,
      "event_id": "655090",
      "event_slug": "mlb-atl-pit-2026-07-07",
      "first_entry_at": 1783464052
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 2,
    "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJwb3NpdGlvbnMiLCJwYXJhbXMiOnsibCI6MiwiZCI6MiwiayI6IjM4Njk5…",
    "offset": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].title / data[].slug / data[].event_slug` | Market title and the slugs that identify the market and its event. |
| `data[].condition_id / data[].token_id` | Identifiers for the market condition and the outcome token the wallet held. Use `condition_id` in the `condition` filter. |
| `data[].outcome / data[].opposite_outcome` | The outcome the wallet held and the other side of the same market. |
| `data[].avg_price` | Average entry price of the position, between 0 and 1. |
| `data[].realized_pnl / data[].total_pnl` | Profit or loss locked in on the position. For closed rows both values match and `unrealized_pnl` is `0.0`. |
| `data[].percent_realized_pnl` | Realized profit as a percentage figure, for example `84.6171`. |
| `data[].total_size / data[].total_cost_usdc / data[].entry_fees_usdc` | Total shares bought, total cost in USDC, and fees paid in USDC. |
| `data[].first_entry_at / data[].last_event_at` | Epoch second timestamps of the wallet's first entry and its latest event on the position. `last_event_at` drives the sort order and the `start`/`end` filters. |
| `data[].current_price` | Latest price of the outcome. A value of `1.0` on a closed row means the outcome won. |
| `pagination.has_more / pagination.next_cursor` | Shows whether more rows exist and gives the cursor for the next page. |

### Notes

- Pass `pagination.next_cursor` back as `cursor` to get the next page. The cursor sets the page size, so `limit` is ignored when you send it.
- Re-send filters such as `title` and `condition` on every page of a walk, because the cursor does not carry them.
- `condition_id` values are hex strings. `event_id` is a numeric string. Timestamps are epoch seconds.
- To see a wallet's current holdings instead, call [Polymarket Wallet Positions](/apis/polymarket/positions).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/closed-positions.json`](../../../catalog/models/polymarket/closed-positions.json) · Store page: https://www.sandbase.ai/model/polymarket/closed-positions
