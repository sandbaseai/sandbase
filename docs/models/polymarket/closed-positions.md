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

A wallet's closed positions with realized PnL, newest first, from the Data API v2.

Served from the Polymarket Data API v2. The result is returned in `outputs[0].data`: rows are under `data`, and paginated routes add `pagination.next_cursor` (pass it back as `cursor`).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/closed-positions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319", "limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user` | string | Yes | The wallet to anchor on. At least one of `user`/`condition` is required. |
| `condition` | string | No | Condition id(s), comma-separated (at most 20 distinct values). With `user`, narrows that user's positions (all ids honoured). Without `user`, anchors on the market's holders; exactly one id is accepte |
| `limit` | integer | No | First-page size. Ignored when `cursor` is supplied (the cursor's size wins). |
| `cursor` | string | No | Opaque pagination cursor from a prior response's `next_cursor`. It carries the page position, page size, and the status/sort/direction it was minted under. |
| `event_id` | string | No | Event id(s), comma-separated (at most 20 distinct values). User-anchored only. |
| `title` | string | No | Case-insensitive market-title substring filter, honoured on every anchor and status. SQL LIKE wildcards (`%`, `_`) keep their usual meaning; empty or whitespace-only is treated as absent; at most 200  |
| `filter_type` | string | No | `CASH` or `TOKENS`; defaults to `TOKENS` (the /v2/trades-homogenized filter pair, replacing the former `size_threshold`). |
| `filter_amount` | number | No | The filter floor. `TOKENS`: minimum CURRENT holding in shares (defaults to the 0.1 dust floor; applies to `OPEN`/`REDEEMABLE`; a user's `CLOSED` set is not narrowed by it, and on a market anchor it mo |
| `include_archived` | boolean | No | Also include positions on archived markets; defaults to `false`. `OPEN`/`REDEEMABLE`/`REDEEMABLE_LOST`/`MERGEABLE` only; combining it with `status=CLOSED` is rejected. Inactive markets remain excluded |
| `sort_by` | string | No | One of `CURRENT_VALUE`, `PRICE`, `TOKENS`, `UNREALIZED_PNL`, `REALIZED_PNL`, `TOTAL_PNL`, or `TIMESTAMP` (the row's `last_event_at`). `PRICE` ranks by the response's effective `current_price` on every |
| `start` | integer | No | Inclusive lower bound on `last_event_at`, epoch seconds; omit or `0` for unbounded (the `/v2/activity` + `/v2/trades` vocabulary). |
| `end` | integer | No | Inclusive upper bound on `last_event_at`, epoch seconds; omit or `0` for unbounded. A position with no native economics carries no `last_event_at` and is therefore **excluded by any bound**, in either |
| `sort_direction` | string | No | `ASC` or `DESC`; defaults to `DESC`. |

### Reference

- Official docs: https://docs.polymarket.com/api-reference/data-api/overview

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/closed-positions.json`](../../../catalog/models/polymarket/closed-positions.json) · Store page: https://www.sandbase.ai/model/polymarket/closed-positions
