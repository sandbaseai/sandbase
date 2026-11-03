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

Returns a Polymarket wallet's activity feed, newest first by default. Each row is one event such as a trade, split, merge, redemption or reward. The only required input is the wallet address in `user`.

### Use cases

- Track every trade a wallet makes on a given market by filtering on `condition` and `type=TRADE`.
- Build a timeline of a wallet's buys and sells for a chosen date range using `start` and `end`.
- Audit a wallet's redemptions, rewards and rebates by passing those values in `type`.
- Copy-trade or monitor a large trader by polling the feed and reading new rows as they appear.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/activity" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319", "limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user` | string | Yes | Required; the feed is user-anchored. |
| `condition` | string | No | Condition id(s), comma-separated (at most 20 distinct values). `condition_id` / `conditionId` are accepted aliases. |
| `cursor` | string | No | Opaque cursor from a prior response's `next_cursor`; binds the sort direction it was minted under. |
| `end` | integer | No | Window end, epoch seconds (inclusive); omitted or `0` means now plus one day. |
| `event_id` | string | No | Gamma event id(s), comma-separated (at most 20 distinct values); resolves to the events' markets. Mutually exclusive with `condition`. |
| `exclude_deposits_withdrawals` | boolean | No | Defaults to `true`, which drops `DEPOSIT` and `WITHDRAWAL` rows from the page, including when `type` names them. Pass `false` to include them. |
| `limit` | integer | No | Page size; default 100, max 1000, past-cap rejected. |
| `side` | string | No | BUY or SELL. |
| `sort_by` | string | No | Only `TIMESTAMP` is supported (v2 pages by keyset). |
| `sort_direction` | string | No | `ASC` or `DESC` (default). The keyset seeks in the chosen direction; the minted cursor binds it, so pass it consistently when paging. |
| `start` | integer | No | Window start on `block_timestamp`, epoch seconds (inclusive). Omitted or `0` floors to three years back; pass `start=1` for full history. |
| `type` | string | No | Activity type(s), comma-separated. Accepted values: `TRADE`, `SPLIT`, `MERGE`, `REDEEM` (automatic redemptions included), `CONVERSION`, `MIGRATION`, `REWARD`, `YIELD`, `MAKER_REBATE`, `TAKER_REBATE`, `REFERRAL_REWARD`, ` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "bio": "",
      "condition_id": "0xdbcc54e623b74b67ea5a8733639a9f5e43ea16bd9b264ddf8772c615a7790d62",
      "event_slug": "wta-yastrem-sonmez-2026-11-01",
      "icon": "https://polymarket-upload.s3.us-east-2.amazonaws.com/wta-logo-41f331bdf1.png",
      "name": "ferrariChampions2026",
      "outcome": "Zeynep Sonmez",
      "outcome_index": 1,
      "price": 0.9,
      "profile_image": "",
      "profile_image_optimized": "",
      "proxy_wallet": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
      "pseudonym": "Glaring-Salt"
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 2,
    "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJhY3Rpdml0eSIsInBhcmFtcyI6eyJsIjoyLCJ0cyI6MTc5MzY5MTYxMywi…",
    "offset": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].type` | Kind of activity for the row, such as `TRADE`. |
| `data[].side` | Direction of the trade, `BUY` or `SELL`. |
| `data[].timestamp` | Time of the activity as epoch seconds. |
| `data[].price` | Price per share for the row. In the sample it is `0.9`. |
| `data[].size / data[].usdc_size` | `size` is the share quantity. `usdc_size` is the USDC value of the row. |
| `data[].title / data[].event_slug / data[].slug` | Market title and the slugs that identify the market and its event. |
| `data[].condition_id / data[].token_id` | Identify the market condition and the outcome token that was traded. |
| `data[].outcome / data[].outcome_index` | Name of the outcome and its index within the market. |
| `data[].transaction_hash` | Hash of the on-chain transaction for the row. |
| `data[].proxy_wallet / data[].pseudonym / data[].name` | The wallet address and the profile names tied to it. |

### Notes

- Pass `pagination.next_cursor` back as `cursor` to get the next page. Keep `sort_direction` the same on every page, since the cursor binds it.
- `pagination.has_more` shows whether more rows exist. `limit` accepts up to 1000.
- `DEPOSIT` and `WITHDRAWAL` rows are dropped by default. Set `exclude_deposits_withdrawals` to `false` to include them.
- To see what a wallet currently holds, call [Polymarket Wallet Positions](/apis/polymarket/positions). For settled markets, call [Polymarket Closed Positions](/apis/polymarket/closed-positions).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/activity.json`](../../../catalog/models/polymarket/activity.json) · Store page: https://www.sandbase.ai/model/polymarket/activity
