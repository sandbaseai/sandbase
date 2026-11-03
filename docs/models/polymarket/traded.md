# Polymarket User Stats API: pricing, parameters and code examples

`polymarket/traded` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

A wallet's profile stats: total trades, biggest win, profile views and join date.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/traded", "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/traded', {'user': '0xfe787d2da716d60e8acff57fb87eb13cd4d10319'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/traded", {
  "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/traded", sandbase.Params{
	"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
})
```

Same call via the path form: `POST /v1/api/polymarket/traded` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user` | string | yes | The wallet whose profile stats to return. Required; `0x` followed by 40 hexadecimal characters.  |

## Details

Returns profile stats for one Polymarket wallet: trade count, biggest win, profile views, join date and an all-time profit and loss breakdown. It needs one input, the wallet address in `user`.

### Use cases

- Check how active and how profitable a wallet is before copying its trades.
- Compare the all-time profit and loss of several wallets side by side.
- Show a trader card with join date, profile views and trade count in a dashboard.
- Spot wallets that earn mostly from fees and rebates rather than from trading.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/traded" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user` | string | Yes | The wallet whose profile stats to return. Required; `0x` followed by 40 hexadecimal characters. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "all_time_pnl": {
      "cashflow_net": null,
      "deposits": null,
      "economic_pnl": 5542941.528962,
      "fees": -4819186.982857,
      "fees_paid": -2146855.218475,
      "fees_refunded": 2672331.764382,
      "maker_rebate": 1555886.072,
      "position_pnl": 2897083.283962,
      "realized_combo_pnl": 0.0,
      "realized_lp_pnl": 0.0,
      "realized_market_pnl": 2899267.130228,
      "realized_pnl": 2899267.130228
    },
    "biggest_win": 412361.928935,
    "join_date": 1774462766,
    "proxy_wallet": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
    "trades": 87633,
    "views": 334708
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.proxy_wallet` | The wallet address the stats belong to. |
| `data.trades` | Number of trades for the wallet shown on its profile. |
| `data.biggest_win` | Largest single win for the wallet. |
| `data.join_date` | When the wallet joined, as a Unix timestamp in seconds. |
| `data.views` | Number of profile views. |
| `data.all_time_pnl.economic_pnl / data.all_time_pnl.settled_pnl` | All-time profit and loss figures for the wallet. They are computed differently, so the two values differ. |
| `data.all_time_pnl.realized_pnl / data.all_time_pnl.unrealized_pnl` | Realized profit and loss from closed results, and unrealized profit and loss on positions still open. Unrealized can be negative. |
| `data.all_time_pnl.trade_count` | Number of trades counted in the all-time profit and loss calculation. |
| `data.all_time_pnl.volume / data.all_time_pnl.volume_usdc` | Total trading volume for the wallet. `volume_usdc` is the volume given in USDC. |
| `data.all_time_pnl.fees_paid / data.all_time_pnl.fees_refunded / data.all_time_pnl.fees` | Fees paid, fees refunded, and the net `fees` figure. Fee values are negative when they cost the wallet money. |
| `data.all_time_pnl.maker_rebate / data.all_time_pnl.taker_rebate / data.all_time_pnl.reward_income` | Income from maker rebates, taker rebates and rewards. |

### Notes

- `user` must be `0x` followed by 40 hexadecimal characters.
- `data.all_time_pnl.trade_count` and `data.trades` are different numbers in the sample response, so do not treat them as the same count.
- `data.all_time_pnl.timestamp` is a Unix timestamp in seconds, and `source_block` is a block number.
- Fields such as `cashflow_net`, `deposits` and `withdrawals` can be `null`.
- For the wallet's current holdings, call [Polymarket Wallet Positions](/apis/polymarket/positions). For its recent trades, call [Polymarket Wallet Activity](/apis/polymarket/activity).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/traded.json`](../../../catalog/models/polymarket/traded.json) · Store page: https://www.sandbase.ai/model/polymarket/traded
