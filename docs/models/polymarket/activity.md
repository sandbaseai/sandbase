# Polymarket Wallet Activity API: pricing, parameters and code examples

`polymarket/activity` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

A wallet's activity feed: trades, splits, merges, redemptions, rewards and conversions, with time-range and type filters.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/activity", "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/activity', {'user': '0xfe787d2da716d60e8acff57fb87eb13cd4d10319'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/activity", {
  "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/activity", sandbase.Params{
	"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
})
```

Same call via the path form: `POST /v1/api/polymarket/activity` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end` | integer |  | Window end, epoch seconds (inclusive); omitted or `0` means now plus one day.  |
| `side` | string |  | BUY or SELL.  |
| `type` | string |  | Activity type(s), comma-separated. Accepted values: `TRADE`, `SPLIT`, `MERGE`, `REDEEM` (automatic redemptions included), `CONVERSION`, `MIGRATION`, `REWARD`, `YIELD`, `MAKER_REBATE`, `TAKER_REBATE`, `REFERRAL_REWARD`,…  |
| `user` | string | yes | Required; the feed is user-anchored.  |
| `limit` | integer |  | Page size; default 100, max 1000, past-cap rejected. range 0–1000 |
| `start` | integer |  | Window start on `block_timestamp`, epoch seconds (inclusive). Omitted or `0` floors to three years back; pass `start=1` for full history.  |
| `cursor` | string |  | Opaque cursor from a prior response's `next_cursor`; binds the sort direction it was minted under.  |
| `sort_by` | string |  | Only `TIMESTAMP` is supported (v2 pages by keyset).  |
| `event_id` | string |  | Gamma event id(s), comma-separated (at most 20 distinct values); resolves to the events' markets. Mutually exclusive with `condition`.  |
| `condition` | string |  | Condition id(s), comma-separated (at most 20 distinct values). `condition_id` / `conditionId` are accepted aliases.  |
| `sort_direction` | string |  | `ASC` or `DESC` (default). The keyset seeks in the chosen direction; the minted cursor binds it, so pass it consistently when paging.  |
| `exclude_deposits_withdrawals` | boolean |  | Defaults to `true`, which drops `DEPOSIT` and `WITHDRAWAL` rows from the page, including when `type` names them. Pass `false` to include them.  |

## Details

A wallet's activity feed: trades, splits, merges, redemptions, rewards and conversions, with time-range and type filters.

Served from the Polymarket Data API v2. The result is returned in `outputs[0].data`: rows are under `data`, and paginated routes add `pagination.next_cursor` (pass it back as `cursor`).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/activity" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319", "limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user` | string | Yes | Required; the feed is user-anchored. |
| `limit` | integer | No | Page size; default 100, max 1000, past-cap rejected. |
| `cursor` | string | No | Opaque cursor from a prior response's `next_cursor`; binds the sort direction it was minted under. |
| `type` | string | No | Activity type(s), comma-separated. Accepted values: `TRADE`, `SPLIT`, `MERGE`, `REDEEM` (automatic redemptions included), `CONVERSION`, `MIGRATION`, `REWARD`, `YIELD`, `MAKER_REBATE`, `TAKER_REBATE`,  |
| `condition` | string | No | Condition id(s), comma-separated (at most 20 distinct values). `condition_id` / `conditionId` are accepted aliases. |
| `event_id` | string | No | Gamma event id(s), comma-separated (at most 20 distinct values); resolves to the events' markets. Mutually exclusive with `condition`. |
| `side` | string | No | BUY or SELL. |
| `start` | integer | No | Window start on `block_timestamp`, epoch seconds (inclusive). Omitted or `0` floors to three years back; pass `start=1` for full history. |
| `end` | integer | No | Window end, epoch seconds (inclusive); omitted or `0` means now plus one day. |
| `sort_by` | string | No | Only `TIMESTAMP` is supported (v2 pages by keyset). |
| `sort_direction` | string | No | `ASC` or `DESC` (default). The keyset seeks in the chosen direction; the minted cursor binds it, so pass it consistently when paging. |
| `exclude_deposits_withdrawals` | boolean | No | Defaults to `true`, which drops `DEPOSIT` and `WITHDRAWAL` rows from the page, including when `type` names them. Pass `false` to include them. |

### Reference

- Official docs: https://docs.polymarket.com/api-reference/data-api/overview

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/activity.json`](../../../catalog/models/polymarket/activity.json) · Store page: https://www.sandbase.ai/model/polymarket/activity
