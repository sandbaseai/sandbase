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

Returns the Polymarket trader leaderboard, ranked by profit and loss (`PNL`) or trading `VOLUME`. You can filter by `time_period` and `category`, or pass a wallet in `user` to get that wallet's standing. No input is required.

### Use cases

- Build a ranked list of the most profitable Polymarket traders for the past day, week, or month.
- Compare top traders by `VOLUME` against top traders by `PNL` in a category such as `sports`.
- Look up one wallet's ranks on both boards to check how a trader performs.
- Collect wallet addresses of top traders so you can study their positions and activity.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/leaderboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | `overall` (default), a Gamma market category (e.g. `sports`), or a synthetic category: `combos` (combinatorial positions; PNL boards only; the volume board has no combos rows) or `esports` (promoted subcategory). |
| `cursor` | string | No | Opaque pagination cursor from a prior response's `next_cursor`. |
| `limit` | integer | No | First-page size. Ignored when `cursor` is supplied. |
| `sort_by` | string | No | Which board: `PNL` (default) or `VOLUME`. |
| `time_period` | string | No | Window: `day` / `week` / `month` / `all`. Defaults to `day`. |
| `user` | string | No | Look up one wallet's standing instead of reading the board. Returns a single object carrying both ranks, not a page. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "pnl": 454238.2733963345,
      "profile_image": "",
      "rank": 1,
      "user_id": "0x2c335066fe58fe9237c3d3dc7b275c2a034a0563",
      "user_name": "0x2c335066FE58fe9237c3d3Dc7b275C2a034a0563-1759935795465",
      "verified": false,
      "volume": 5394555.845070001,
      "x_username": ""
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 2,
    "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJsZWFkZXJib2FyZCIsInBhcmFtcyI6eyJsIjoyLCJvIjoyLCJzIjoiUE5M…",
    "offset": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].rank` | Position of the trader on the selected board. |
| `data[].user_id` | The trader's wallet address, as a `0x` hex string. |
| `data[].user_name` | Display name of the trader. Some names are the wallet address followed by a number. |
| `data[].pnl` | Profit and loss for the chosen time period and category. |
| `data[].volume` | Trading volume for the chosen time period and category. |
| `data[].verified` | Boolean flag for whether the profile is marked verified. |
| `data[].x_username / data[].profile_image` | The trader's X username and profile image URL. Both can be empty strings. |
| `pagination.has_more` | `true` when more rows are available after this page. |
| `pagination.next_cursor` | Opaque cursor string. Send it back as `cursor` to get the next page. |

### Notes

- Set `sort_by` to `PNL` (default) or `VOLUME` to choose the board. `time_period` defaults to `day` and `category` defaults to `overall`.
- `limit` sets the first-page size, up to 1000. It is ignored when you send `cursor`.
- With `user` set, the call returns a single object with both ranks instead of a page.
- To see what a ranked wallet holds, pass its `user_id` to [Polymarket Wallet Positions](/apis/polymarket/positions) or [Polymarket Wallet Activity](/apis/polymarket/activity).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/leaderboard.json`](../../../catalog/models/polymarket/leaderboard.json) · Store page: https://www.sandbase.ai/model/polymarket/leaderboard
