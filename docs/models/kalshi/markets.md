# Kalshi Get Kalshi Markets API: pricing, parameters and code examples

`kalshi/markets` · data API · Kalshi · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Kalshi Markets from Kalshi. Returns the official Kalshi API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kalshi/markets"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kalshi/markets', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kalshi/markets", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kalshi/markets", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kalshi/markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of results per page. Defaults to 100. Maximum value is 1000. default `100`; range 0–1000 |
| `cursor` | string |  | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page.  |
| `status` | string |  | Filter by market status. Leave empty to return markets with any status. one of: `unopened`, `open`, `paused`, `closed`, `settled` |
| `tickers` | string |  | Filter by specific market tickers. Comma-separated list of market tickers to retrieve.  |
| `mve_filter` | string |  | Filter by multivariate events (combos). 'only' returns only multivariate events, 'exclude' excludes multivariate events. one of: `only`, `exclude` |
| `event_ticker` | string |  | Event ticker to filter by. Only a single event ticker is supported.  |
| `max_close_ts` | integer |  | Filter items that close before this Unix timestamp  |
| `min_close_ts` | integer |  | Filter items that close after this Unix timestamp  |
| `series_ticker` | string |  | Filter by series ticker  |
| `max_created_ts` | integer |  | Filter items that created before this Unix timestamp  |
| `max_settled_ts` | integer |  | Filter items that settled before this Unix timestamp  |
| `max_updated_ts` | integer |  | Return markets with metadata updated at or before this Unix timestamp (in seconds). Tracks non-trading changes only. May be combined with min_updated_ts and mve_filter=exclude. May also be combined with series_ticker,…  |
| `min_created_ts` | integer |  | Filter items that created after this Unix timestamp  |
| `min_settled_ts` | integer |  | Filter items that settled after this Unix timestamp  |
| `min_updated_ts` | integer |  | Return markets with metadata updated later than this Unix timestamp (in seconds). Tracks non-trading changes only. May be combined with max_updated_ts and mve_filter=exclude. May also be combined with series_ticker,…  |

## Details

Returns a page of Kalshi prediction markets with their ticker, title, status, open and close times, and current bid, ask and last prices in dollars. All parameters are optional. With no input it returns the first page of markets of any status.

### Use cases

- List all `open` markets for one `event_ticker` to see every contract in that event.
- Pull markets that close between `min_close_ts` and `max_close_ts` to build a calendar of upcoming resolutions.
- Use `mve_filter` set to `exclude` to skip combo markets and keep only single-outcome markets.
- Look up several known markets at once by passing a comma-separated `tickers` list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kalshi/markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. |
| `event_ticker` | string | No | Event ticker to filter by. Only a single event ticker is supported. |
| `limit` | integer | No | Number of results per page. Defaults to 100. Maximum value is 1000. |
| `max_close_ts` | integer | No | Filter items that close before this Unix timestamp |
| `max_created_ts` | integer | No | Filter items that created before this Unix timestamp |
| `max_settled_ts` | integer | No | Filter items that settled before this Unix timestamp |
| `max_updated_ts` | integer | No | Return markets with metadata updated at or before this Unix timestamp (in seconds). Tracks non-trading changes only. May be combined with min_updated_ts and mve_filter=exclude. May also be combined with series_ticker, wh |
| `min_close_ts` | integer | No | Filter items that close after this Unix timestamp |
| `min_created_ts` | integer | No | Filter items that created after this Unix timestamp |
| `min_settled_ts` | integer | No | Filter items that settled after this Unix timestamp |
| `min_updated_ts` | integer | No | Return markets with metadata updated later than this Unix timestamp (in seconds). Tracks non-trading changes only. May be combined with max_updated_ts and mve_filter=exclude. May also be combined with series_ticker, whic |
| `mve_filter` | string | No | Filter by multivariate events (combos). 'only' returns only multivariate events, 'exclude' excludes multivariate events. |
| `series_ticker` | string | No | Filter by series ticker |
| `status` | string | No | Filter by market status. Leave empty to return markets with any status. |
| `tickers` | string | No | Filter by specific market tickers. Comma-separated list of market tickers to retrieve. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": "CgwIwJ2m1wYQwJOY2wESMktYTVZFQ1JPU1NDQVRFR09SWS1TMjAyNkNUMkxZV0xYVVhIQVJBT0YtS0RG…",
  "markets": [
    {
      "can_close_early": true,
      "close_time": "2026-11-10T20:00:00Z",
      "created_time": "2026-11-03T07:35:29.872509Z",
      "custom_strike": {
        "Associated Events": "KXALLSVENSKANGAME-26NOV03SIRHAL,KXBUNDESLIGAGAME-26NOV07BVBSVE,KXBUNDESLIGAGAME-…",
        "Associated Market Sides": "yes,yes,yes,yes,yes,yes,yes,yes,yes,yes,yes,yes,yes,yes,yes,yes,yes,yes,yes,yes,…",
        "Associated Markets": "KXALLSVENSKANGAME-26NOV03SIRHAL-SIR,KXBUNDESLIGAGAME-26NOV07BVBSVE-BVB,KXBUNDESL…",
        "Multivariate Event Ticker": "KXMVECROSSCATEGORY-S2026JL77JHDP6ANNFK7D"
      },
      "event_ticker": "KXMVECROSSCATEGORY-S2026JL77JHDP6ANNFK7D",
      "exchange_index": 1,
      "expected_expiration_time": "2026-11-09T02:00:00Z",
      "expiration_time": "2026-11-10T20:00:00Z",
      "expiration_value": "",
      "is_provisional": true,
      "last_price_dollars": "0.0000",
      "latest_expiration_time": "2026-11-10T20:00:00Z"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cursor` | Pagination token for the next page of markets. Send it back as `cursor` in the next request. |
| `markets[].ticker` | Unique ticker of the market. Use it to look up a single market, its order book, or its trades. |
| `markets[].event_ticker` | Ticker of the event the market belongs to. Use it as the `event_ticker` filter. |
| `markets[].title / markets[].no_sub_title` | Text describing the market and its outcome. For combo markets these list each leg, such as `yes Sirius,yes Dortmund`. |
| `markets[].status` | Current state of the market, for example `active`. |
| `markets[].market_type` | Kind of market. The sample shows `binary`. |
| `markets[].open_time / markets[].close_time / markets[].expiration_time` | ISO 8601 UTC timestamps for when trading opens, when it closes, and when the market expires. |
| `markets[].yes_ask_dollars / markets[].no_ask_dollars / markets[].no_bid_dollars / markets[].last_price_dollars` | Prices in dollars, given as strings with four decimals. They cover the yes ask, no ask, no bid, and the last traded price. |
| `markets[].volume_fp / markets[].volume_24h_fp / markets[].open_interest_fp` | Trading volume, 24-hour volume, and open interest, given as decimal strings. |
| `markets[].mve_selected_legs[]` | For combo markets, the legs that make up the market. Each leg has `event_ticker`, `market_ticker` and `side`. |
| `markets[].result` | Settlement result of the market. It is an empty string in the sample, where the markets have not settled. |

### Notes

- Page through results by sending the returned `cursor` value as `cursor`. Set `limit` up to 1000 (default 100).
- The `*_ts` filters take Unix timestamps in seconds. Response times are ISO 8601 strings.
- `min_updated_ts` and `max_updated_ts` cannot be combined with most other filters. See the parameter descriptions for the allowed combinations.
- To see live bids and asks for one market, call [Kalshi Get Kalshi Market OrderBook](/apis/kalshi/markets-orderbook). To see executed trades, call [Kalshi Get Kalshi Trades](/apis/kalshi/trades).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/kalshi/markets.json`](../../../catalog/models/kalshi/markets.json) · Store page: https://www.sandbase.ai/model/kalshi/markets
