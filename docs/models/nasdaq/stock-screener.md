# Nasdaq Stock Screener API: pricing, parameters and code examples

`nasdaq/stock-screener` · data API · Nasdaq · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Screen stocks by exchange and market capitalization. Returns paginated results with symbol, name, last sale, change, and market cap.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/stock-screener"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/stock-screener', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/stock-screener", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/stock-screener", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/stock-screener` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Max results to return. range -9007199254740991–9007199254740991 |
| `offset` | integer |  | Offset for pagination. range -9007199254740991–9007199254740991 |
| `exchange` | string |  | Exchange filter: NASDAQ, NYSE, AMEX.  |
| `market_cap` | string |  | Market cap filter: mega, large, mid, small, micro, nano.  |

## Details

Returns a paginated list of stocks from Nasdaq, with symbol, name, last sale, net change, percent change, and market cap for each row. All inputs are optional. You can filter by `exchange` and `market_cap`, and page with `limit` and `offset`.

### Use cases

- Build a list of the largest US stocks by filtering `market_cap` to `mega`.
- List every stock on one exchange, such as `NYSE` or `AMEX`, to seed a watchlist.
- Page through all rows with `limit` and `offset` to load a local copy of the stock universe.
- Find the biggest daily gainers or losers in a market cap band by sorting the rows on `pctchange`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/stock-screener" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `exchange` | string | No | Exchange filter: NASDAQ, NYSE, AMEX. |
| `limit` | integer | No | Max results to return. |
| `market_cap` | string | No | Market cap filter: mega, large, mid, small, micro, nano. |
| `offset` | integer | No | Offset for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "data": {
      "asof": "Last price as of Oct 30, 2026",
      "filters": {
        "country": [
          {
            "name": "United States",
            "value": "united_states"
          }
        ],
        "exchange": [
          {
            "name": "NASDAQ",
            "value": "NASDAQ"
          }
        ],
        "exsubcategory": [
          {
            "name": "Global Select",
            "value": "NGS"
          }
        ],
        "marketcap": [
          {
            "name": "Mega (>$200B)",
            "value": "mega"
          }
        ],
        "recommendation": [
          {
            "name": "Strong Buy",
            "value": "strong_buy"
          }
        ],
        "region": [
          {
            "name": "Africa",
            "value": "africa"
          }
        ],
        "sector": [
          {
            "name": "Technology",
            "value": "technology"
          }
        ]
      },
      "table": {
        "asOf": null,
        "headers": {
          "lastsale": "Last Sale",
          "marketCap": "Market Cap",
          "name": "Name",
          "netchange": "Net Change",
          "pctchange": "% Change",
          "symbol": "Symbol"
        },
        "rows": [
          {
            "lastsale": "$344.63",
            "marketCap": "5,029,592,253,400",
            "name": "Apple Inc. Common Stock",
            "netchange": "-4.28",
            "pctchange": "-1.227%",
            "symbol": "AAPL",
            "url": "/market-activity/stocks/aapl"
          }
        ]
      },
      "totalrecords": 6974
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
| `data.data.table.rows[].symbol` | Ticker symbol of the stock, such as `AAPL`. |
| `data.data.table.rows[].name` | Company name with the share class, such as `Apple Inc. Common Stock`. |
| `data.data.table.rows[].lastsale` | Last sale price as a string with a dollar sign, such as `$344.63`. |
| `data.data.table.rows[].netchange / data.data.table.rows[].pctchange` | Price change and percent change. Both are strings, and the percent value ends with `%`. |
| `data.data.table.rows[].marketCap` | Market capitalization as a string with comma separators, such as `5,029,592,253,400`. |
| `data.data.table.rows[].url` | Relative Nasdaq page path for the stock. |
| `data.data.totalrecords` | Total number of rows that match the filters, across all pages. |
| `data.data.asof` | Text that states the date of the last price, such as `Last price as of Oct 30, 2026`. |
| `data.data.filters.marketcap[]` | Market cap bands with a display `name` and the `value` to send, such as `mega` for more than $200B. |
| `data.data.filters.exchange[]` | Exchange options with `name` and `value`. Values are `NASDAQ`, `NYSE`, and `AMEX`. |

### Notes

- Prices, changes, and market cap come back as formatted strings. Remove `$`, `,` and `%` before you do math.
- Use `totalrecords` with `limit` and `offset` to work out how many pages exist.
- The `filters` object also lists `country`, `sector`, `region`, `recommendation`, and `exsubcategory` options. The request parameters for this API only accept `exchange`, `market_cap`, `limit`, and `offset`.
- Pass a `symbol` from the rows to [Nasdaq Stock Quote](/apis/nasdaq/stock-quote) for a detailed quote, or to [Nasdaq Stock Financials](/apis/nasdaq/stock-financials) for company financials.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/nasdaq/stock-screener.json`](../../../catalog/models/nasdaq/stock-screener.json) · Store page: https://www.sandbase.ai/model/nasdaq/stock-screener
