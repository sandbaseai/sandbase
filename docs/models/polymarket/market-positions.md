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

Positions held in one market by condition ID, with each holder wallet, size, value and PnL.

Served from the Polymarket Data API v2. The result is returned in `outputs[0].data`: rows are under `data`, and paginated routes add `pagination.next_cursor` (pass it back as `cursor`).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/market-positions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b", "limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user` | string | No | The wallet to anchor on. At least one of `user`/`condition` is required. |
| `condition` | string | Yes | Condition id(s), comma-separated (at most 20 distinct values). With `user`, narrows that user's positions (all ids honoured). Without `user`, anchors on the market's holders; exactly one id is accepte |
| `limit` | integer | No | First-page size. Ignored when `cursor` is supplied (the cursor's size wins). |
| `cursor` | string | No | Opaque pagination cursor from a prior response's `next_cursor`. It carries the page position, page size, and the status/sort/direction it was minted under. |
| `status` | string | No | One of `OPEN`, `REDEEMABLE`, `REDEEMABLE_LOST`, `MERGEABLE`, or `CLOSED`; defaults to `OPEN`. `REDEEMABLE_LOST` requires `user`, supports all six sorts, and defaults to `CURRENT_VALUE`; it preserves r |
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
Machine-readable: [`catalog/models/polymarket/market-positions.json`](../../../catalog/models/polymarket/market-positions.json) · Store page: https://www.sandbase.ai/model/polymarket/market-positions
