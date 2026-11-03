# Kalshi Get Kalshi Trades API: pricing, parameters and code examples

`kalshi/trades` · data API · Kalshi · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Kalshi Trades from Kalshi. Returns the official Kalshi API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kalshi/trades"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kalshi/trades', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kalshi/trades", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kalshi/trades", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kalshi/trades` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of results per page. Defaults to 100. Maximum value is 1000. default `100`; range 0–1000 |
| `cursor` | string |  | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page.  |
| `max_ts` | integer |  | Filter items before this Unix timestamp  |
| `min_ts` | integer |  | Filter items after this Unix timestamp  |
| `ticker` | string |  | Filter by market ticker  |
| `is_block_trade` | boolean |  | Filter trades by whether they are block trades. Omit to return all trades. Set to `true` to return only block trades. Set to `false` to return only non-block trades.  |

## Details

Returns a list of recent trades on Kalshi prediction markets, newest first in the sample. Each trade has a market ticker, a price, a size, and the taker side. No input is required, and you can filter by `ticker`, time range, or block trade status.

### Use cases

- Pull all trades for one market ticker to build a price history chart.
- Filter with `is_block_trade` set to `true` to track large negotiated trades.
- Use `min_ts` and `max_ts` to collect trades for a fixed time window and compute volume.
- Scan the latest trades across all markets to see which contracts are active right now.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kalshi/trades" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. |
| `is_block_trade` | boolean | No | Filter trades by whether they are block trades. Omit to return all trades. Set to `true` to return only block trades. Set to `false` to return only non-block trades. |
| `limit` | integer | No | Number of results per page. Defaults to 100. Maximum value is 1000. |
| `max_ts` | integer | No | Filter items before this Unix timestamp |
| `min_ts` | integer | No | Filter items after this Unix timestamp |
| `ticker` | string | No | Filter by market ticker |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": "EhIKEAcnIQO2qZAT13CwKNIVuKwaDAjGnabXBhCAupCKAg",
  "trades": [
    {
      "count_fp": "19.41",
      "created_time": "2026-11-03T07:35:35.670231Z",
      "is_block_trade": false,
      "no_price_dollars": "0.2400",
      "taker_book_side": "bid",
      "taker_outcome_side": "yes",
      "taker_side": "yes",
      "ticker": "CONTROLS-2026-D",
      "trade_id": "07271e4e-1e09-b3e8-926e-ee607c9d1a35",
      "yes_price_dollars": "0.7600"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cursor` | Pagination token. Pass it as `cursor` in the next request to get the next page of trades. |
| `trades[].trade_id` | Unique ID of the trade, in UUID format. |
| `trades[].ticker` | Ticker of the market that was traded, for example `KXETH15M-26NOV030245-45`. |
| `trades[].created_time` | Time the trade happened, as an ISO 8601 UTC timestamp with microseconds. |
| `trades[].yes_price_dollars / trades[].no_price_dollars` | Trade price of the `yes` side and the `no` side in dollars, as strings. In the sample the two prices add up to `1.0000`. |
| `trades[].count_fp` | Number of contracts traded, as a decimal string such as `19.41`. |
| `trades[].taker_side` | Side the taker bought, `yes` or `no`. |
| `trades[].taker_outcome_side` | Outcome side of the taker, `yes` or `no`. It matches `taker_side` in the sample. |
| `trades[].taker_book_side` | Order book side of the taker, `bid` or `ask`. |
| `trades[].is_block_trade` | `true` if the trade was a block trade, `false` otherwise. |

### Notes

- Leave `cursor` empty for the first page. For the next page, send the `cursor` value from the previous response.
- `limit` defaults to 100 and accepts up to 1000.
- `min_ts` and `max_ts` are Unix timestamps, while `created_time` in the response is an ISO 8601 string.
- To find a `ticker` first, call [Kalshi Get Kalshi Markets](/apis/kalshi/markets). For current prices of one market, use [Kalshi Get Market Price](/apis/kalshi/markets-by-ticker).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/kalshi/trades.json`](../../../catalog/models/kalshi/trades.json) · Store page: https://www.sandbase.ai/model/kalshi/trades
