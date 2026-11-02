# Polymarket Get user activity API: pricing, parameters and code examples

`polymarket/activity` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Get user activity from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/activity", "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/activity', {'user': '0x56687bf447db6ffa42ffe2204a05edaa20f55839'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/activity", {
  "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/activity", sandbase.Params{
	"user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
})
```

Same call via the path form: `POST /v1/api/polymarket/activity` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end` | integer |  | Upper-bound timestamp (epoch seconds) for the activity window. Omit for the default (current time); rows newer than `end` are excluded. range 0– |
| `side` | string |  | side one of: `BUY`, `SELL` |
| `type` | array |  | Comma-separated list of activity types to include. DEPOSIT and WITHDRAWAL records also require `excludeDepositsWithdrawals=false`.  |
| `user` | string | yes | User Profile Address (0x-prefixed, 40 hex chars)  |
| `limit` | integer |  | Page size. Values above the maximum are clamped to 500. default `100`; range 0–500 |
| `start` | integer |  | Lower-bound timestamp (epoch seconds) for the activity window. Omit or pass `0` for the default window (most recent ~3 years); pass a positive epoch (e.g. `1`) to retrieve full history. With `sortDirection=ASC`,… range 0– |
| `market` | array |  | Comma-separated list of condition IDs. Mutually exclusive with eventId.  |
| `offset` | integer |  | Starting index for pagination. Requests past the cap are rejected with a 400 (never silently clamped). To read history deeper than offset 5000, page inside `start`/`end` windows — each window has its own offset budget. default `0`; range 0–5000 |
| `sortBy` | string |  | sortBy one of: `TIMESTAMP`, `TOKENS`, `CASH`; default `"TIMESTAMP"` |
| `eventId` | array |  | Comma-separated list of event IDs. Mutually exclusive with market.  |
| `sortDirection` | string |  | `DESC` (default) returns the newest rows first; `ASC` the oldest first. Both orders are stable — the same query returns the same rows at any `limit`/`offset`, so pages compose without gaps or repeats. one of: `ASC`, `DESC`; default `"DESC"` |
| `excludeDepositsWithdrawals` | boolean |  | Excludes deposit and withdrawal records. The default `true` applies even when `type` requests those records, so to get deposits and withdrawals you must pass `false`. default `true` |

## Details

Get user activity from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

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
| `end` | integer | No | Upper-bound timestamp (epoch seconds) for the activity window. Omit for the default (current time); rows newer than `end` are excluded. |
| `eventId` | array | No | Comma-separated list of event IDs. Mutually exclusive with market. |
| `excludeDepositsWithdrawals` | boolean | No | Excludes deposit and withdrawal records. The default `true` applies even when `type` requests those records, so to get deposits and withdrawals you must pass `f |
| `limit` | integer | No | Page size. Values above the maximum are clamped to 500. |
| `market` | array | No | Comma-separated list of condition IDs. Mutually exclusive with eventId. |
| `offset` | integer | No | Starting index for pagination. Requests past the cap are rejected with a 400 (never silently clamped). To read history deeper than offset 5000, page inside `sta |
| `side` | string | No | side |
| `sortBy` | string | No | sortBy |
| `sortDirection` | string | No | `DESC` (default) returns the newest rows first; `ASC` the oldest first. Both orders are stable — the same query returns the same rows at any `limit`/`offset`, s |
| `start` | integer | No | Lower-bound timestamp (epoch seconds) for the activity window. Omit or pass `0` for the default window (most recent ~3 years); pass a positive epoch (e.g. `1`)  |
| `type` | array | No | Comma-separated list of activity types to include. DEPOSIT and WITHDRAWAL records also require `excludeDepositsWithdrawals=false`. |
| `user` | string | Yes | User Profile Address (0x-prefixed, 40 hex chars) |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/activity.json`](../../../catalog/models/polymarket/activity.json) · Store page: https://www.sandbase.ai/model/polymarket/activity
