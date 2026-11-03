# Nasdaq Stock Dividend History API: pricing, parameters and code examples

`nasdaq/stock-dividend-history` · data API · Nasdaq · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Dividend history for a stock including ex-dividend date, current yield, annualized dividend, payout ratio, and historical dividend payment records.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/stock-dividend-history", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/stock-dividend-history', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/stock-dividend-history", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/stock-dividend-history", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/stock-dividend-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string | yes | Stock symbol (e.g. AAPL).  |
| `asset_class` | string |  | Asset class: stocks, etf, mutualfunds.  |

## Details

Returns the dividend profile of a stock listed on Nasdaq: the next ex-dividend date, yield, annualized dividend, payout ratio, and a table of past dividend payments. It needs a ticker `symbol` such as `AAPL`.

### Use cases

- Show the next ex-dividend and payment dates for a ticker in a portfolio app.
- Screen holdings by `yield` and `payoutRatio` to find sustainable income stocks.
- Chart the quarterly cash amount a company has paid over time.
- Build a dividend calendar from declaration, record, and payment dates.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/stock-dividend-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Stock symbol (e.g. AAPL). |
| `asset_class` | string | No | Asset class: stocks, etf, mutualfunds. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "data": {
      "annualizedDividend": "1.08",
      "dividendHeaderValues": [
        {
          "label": "Ex-Dividend Date",
          "value": "08/10/2026"
        }
      ],
      "dividendPaymentDate": "08/13/2026",
      "dividends": {
        "asOf": null,
        "headers": {
          "amount": "Cash Amount",
          "declarationDate": "Declaration Date",
          "exOrEffDate": "Ex/EFF Date",
          "paymentDate": "Payment Date",
          "recordDate": "Record Date",
          "type": "Type"
        },
        "rows": [
          {
            "amount": "$0.27",
            "currency": "USD",
            "declarationDate": "07/30/2026",
            "exOrEffDate": "08/10/2026",
            "paymentDate": "08/13/2026",
            "recordDate": "08/10/2026",
            "type": "Cash"
          }
        ]
      },
      "exDividendDate": "08/10/2026",
      "payoutRatio": "38.8",
      "yield": "0.31%"
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
| `data.data.exDividendDate` | Next ex-dividend date, in `MM/DD/YYYY` format. |
| `data.data.dividendPaymentDate` | Payment date for the next dividend. |
| `data.data.yield` | Current dividend yield as a percent string, such as `0.31%`. |
| `data.data.annualizedDividend` | Annualized dividend per share, as a string such as `1.08`. |
| `data.data.payoutRatio` | Payout ratio as a string, such as `38.8`. |
| `data.data.dividendHeaderValues[].label / data.data.dividendHeaderValues[].value` | Display-ready summary items such as Ex-Dividend Date, Dividend Yield, and Annual Dividend. |
| `data.data.dividends.rows[].amount / data.data.dividends.rows[].currency` | Cash amount of one dividend payment, written with a `$` sign, and its currency code. |
| `data.data.dividends.rows[].exOrEffDate` | Ex-dividend or effective date of that payment. |
| `data.data.dividends.rows[].declarationDate / data.data.dividends.rows[].recordDate / data.data.dividends.rows[].paymentDate` | Declaration, record, and payment dates for that dividend. |
| `data.data.dividends.rows[].type` | Type of dividend, such as `Cash`. |

### Notes

- Set `symbol` to the ticker. Use [Nasdaq Search Symbols](/apis/nasdaq/search-symbols) to find a ticker.
- Use `asset_class` (`stocks`, `etf`, or `mutualfunds`) to say what kind of asset the symbol is. It is optional.
- All values are strings, including numbers and dates. Dates use `MM/DD/YYYY`.
- For price data, call [Nasdaq Stock Quote](/apis/nasdaq/stock-quote) next.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/nasdaq/stock-dividend-history.json`](../../../catalog/models/nasdaq/stock-dividend-history.json) · Store page: https://www.sandbase.ai/model/nasdaq/stock-dividend-history
