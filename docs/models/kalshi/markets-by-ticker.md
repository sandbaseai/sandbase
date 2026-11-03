# Kalshi Get Market Price API: pricing, parameters and code examples

`kalshi/markets-by-ticker` · data API · Kalshi · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Market Price from Kalshi. Returns the official Kalshi API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kalshi/markets-by-ticker", "ticker": "KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N-ROZI3XFZA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kalshi/markets-by-ticker', {'ticker': 'KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N-ROZI3XFZA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kalshi/markets-by-ticker", {
  "ticker": "KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N-ROZI3XFZA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kalshi/markets-by-ticker", sandbase.Params{
	"ticker": "KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N-ROZI3XFZA",
})
```

Same call via the path form: `POST /v1/api/kalshi/markets-by-ticker` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | Market ticker  |

## Details

Returns the full record for one Kalshi market, including its status, prices, timestamps, and settlement result. It needs one input, the market `ticker`.

### Use cases

- Check whether a Kalshi market is still open or has been `finalized`, and read its `result`.
- Read the settlement value and settlement time of a closed market to audit past outcomes.
- Break down a multi-leg combo market into its legs by reading the event, market ticker, and side of each leg.
- Pull the open, close, and expiration times of a market to schedule follow-up checks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kalshi/markets-by-ticker" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N-ROZI3XFZA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | Market ticker |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "market": {
    "can_close_early": true,
    "close_time": "2026-11-02T01:32:48Z",
    "created_time": "2026-10-30T03:15:06.89468Z",
    "custom_strike": {
      "Associated Events": "KXNFLGAME-26NOV01LACLAR,KXNFLGAME-26NOV01TENCIN,KXNFLPASSYDS-26NOV01BALBUF,KXNFL…",
      "Associated Market Sides": "yes,yes,yes,yes,yes,yes,yes,yes,no,yes,yes",
      "Associated Markets": "KXNFLGAME-26NOV01LACLAR-LAR,KXNFLGAME-26NOV01TENCIN-CIN,KXNFLPASSYDS-26NOV01BALB…",
      "Multivariate Event Ticker": "KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N"
    },
    "event_ticker": "KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N",
    "exchange_index": 1,
    "expected_expiration_time": "2026-11-02T03:05:00Z",
    "expiration_time": "2026-11-03T21:05:00Z",
    "expiration_value": "",
    "is_provisional": true,
    "last_price_dollars": "0.0000",
    "latest_expiration_time": "2026-11-03T21:05:00Z"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `market.ticker / market.event_ticker` | The ticker of this market and the ticker of the event it belongs to. |
| `market.status` | Current state of the market. The sample shows `finalized`. |
| `market.result` | Outcome of the market once settled. The sample shows `no`. |
| `market.market_type / market.strike_type` | The market type (`binary` in the sample) and how its strike is defined (`custom` in the sample). |
| `market.yes_bid_dollars / market.no_bid_dollars / market.no_ask_dollars / market.last_price_dollars` | Prices in dollars, given as strings. Only the fields present in the response are returned for a given market. The sample shows `no_bid_dollars` and `no_ask_dollars` at `1.0000` and `last_price_dollars` at `0.0000`. |
| `market.settlement_value_dollars / market.settlement_ts` | The settlement value in dollars and the timestamp when the market settled. |
| `market.open_time / market.close_time / market.expiration_time / market.expected_expiration_time` | Timestamps for when the market opened, closed, and expires, plus the expected expiration time. |
| `market.volume_fp / market.volume_24h_fp / market.open_interest_fp` | Trading volume, 24 hour volume, and open interest, given as decimal strings. |
| `market.mve_selected_legs[].market_ticker / market.mve_selected_legs[].event_ticker / market.mve_selected_legs[].side` | The legs that make up a multivariate combo market. Each leg gives its market ticker, event ticker, and chosen side (`yes` or `no`). |
| `market.price_ranges[].start / market.price_ranges[].end / market.price_ranges[].step` | Price bands and the tick size allowed inside each band. |

### Notes

- Pass the market `ticker` exactly as Kalshi lists it. To find tickers, call [Kalshi Get Kalshi Markets](/apis/kalshi/markets).
- Timestamps use ISO 8601 UTC format, for example `2026-11-02T01:32:48Z`.
- For current bids and asks by price level, call [Kalshi Get Kalshi Market OrderBook](/apis/kalshi/markets-orderbook). For executed trades, call [Kalshi Get Kalshi Trades](/apis/kalshi/trades).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/kalshi/markets-by-ticker.json`](../../../catalog/models/kalshi/markets-by-ticker.json) · Store page: https://www.sandbase.ai/model/kalshi/markets-by-ticker
