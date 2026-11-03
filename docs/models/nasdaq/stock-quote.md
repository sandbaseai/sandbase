# Nasdaq Stock Quote API: pricing, parameters and code examples

`nasdaq/stock-quote` · data API · Nasdaq · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Real-time quote for a single equity including last sale price, net change, percentage change, bid/ask, volume, 52-week range, and market status. Response shape varies by asset class (stocks show keyStats; ETFs and.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/stock-quote", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/stock-quote', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/stock-quote", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/stock-quote", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/stock-quote` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string | yes | Stock symbol (e.g. AAPL).  |
| `asset_class` | string |  | Asset class: stocks, etf, mutualfunds, crypto.  |

## Details

Returns a quote for one Nasdaq-listed symbol, including last sale price, bid and ask, market status, and 52-week range. It needs a `symbol` such as `AAPL`, and optionally an `asset_class`.

### Use cases

- Show the latest sale price and market open or closed state for a ticker in a dashboard.
- Check whether a symbol is listed on Nasdaq or belongs to the Nasdaq-100 before adding it to a watchlist.
- Read the 52-week range to flag stocks trading near their yearly high or low.
- Confirm the company name, exchange, and stock type for a ticker symbol.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/stock-quote" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Stock symbol (e.g. AAPL). |
| `asset_class` | string | No | Asset class: stocks, etf, mutualfunds, crypto. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "data": {
      "assetClass": "STOCKS",
      "companyName": "Apple Inc. Common Stock",
      "exchange": "NASDAQ-GS",
      "isHeld": false,
      "isNasdaq100": true,
      "isNasdaqListed": true,
      "keyStats": {
        "dayrange": {
          "label": "High/Low:",
          "value": "NA"
        },
        "fiftyTwoWeekHighLow": {
          "label": "52 Week Range:",
          "value": "243.42 - 351.73"
        }
      },
      "marketStatus": "Closed",
      "notifications": [
        {
          "eventTypes": [
            {
              "eventName": "High Technical Attribute",
              "id": "tech_attribute",
              "message": "AAPL has a High Technical Rating by Nasdaq Dorsey Wright. Discover why technical…",
              "url": {
                "label": "Discover why technical analysis matters",
                "value": "https://www.nasdaq.com/solutions/nasdaq-dorsey-wright/technical-analysis"
              }
            }
          ],
          "headline": "HIGH TECHNICAL ATTRIBUTE"
        }
      ],
      "primaryData": {
        "askPrice": "N/A",
        "askSize": "N/A",
        "bidPrice": "N/A",
        "bidSize": "N/A",
        "currency": null,
        "deltaIndicator": "down",
        "isRealTime": false,
        "lastSalePrice": "$338.32"
      },
      "secondaryData": null,
      "stockType": "Common Stock"
    },
    "message": null,
    "status": {
      "bCodeMessage": null,
      "developerMessage": null,
      "rCode": 200
    }
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.data.symbol` | Ticker symbol of the quoted security. |
| `data.data.companyName` | Full name of the company and share class. |
| `data.data.primaryData.lastSalePrice` | Last sale price as a string with a currency sign, for example `$338.32`. |
| `data.data.primaryData.deltaIndicator` | Direction of the latest price change, such as `down`. |
| `data.data.primaryData.bidPrice / askPrice / bidSize / askSize` | Current bid and ask price and size. These show `N/A` when no value is available, as when the market is closed. |
| `data.data.primaryData.isRealTime` | Tells you whether the price is real time. It is `false` in this response. |
| `data.data.marketStatus` | Market state at the time of the call, for example `Closed`. |
| `data.data.keyStats.fiftyTwoWeekHighLow.value` | 52-week low and high as one string, for example `243.42 - 351.73`. |
| `data.data.exchange` | Exchange or market tier where the symbol trades, for example `NASDAQ-GS`. |
| `data.data.isNasdaq100 / isNasdaqListed` | Boolean flags for membership in the Nasdaq-100 and for a Nasdaq listing. |

### Notes

- Set `asset_class` to `stocks`, `etf`, `mutualfunds`, or `crypto`. The response shape changes by asset class, so `keyStats` as shown here applies to stocks.
- Price and range values are formatted strings, not numbers. Strip the `$` sign and split the range text before you calculate with them.
- The result sits under `data.data`. The inner `status.rCode` is `200` on success.
- To find a symbol first, use [Nasdaq Search Symbols](/apis/nasdaq/search-symbols). For price history, call [Nasdaq Stock Historical Quotes](/apis/nasdaq/stock-historical-quotes).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/nasdaq/stock-quote.json`](../../../catalog/models/nasdaq/stock-quote.json) · Store page: https://www.sandbase.ai/model/nasdaq/stock-quote
