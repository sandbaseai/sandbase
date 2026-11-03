# Financial Datasets Get Financial Metrics Snapshot API: pricing, parameters and code examples

`financial-datasets/financial-metrics-snapshot` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get the real-time financial metrics snapshot for a stock, including valuation ratios, profitability, efficiency, liquidity, leverage, growth, and per share metrics.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/financial-metrics-snapshot"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/financial-metrics-snapshot', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/financial-metrics-snapshot", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/financial-metrics-snapshot", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/financial-metrics-snapshot` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cik` | string |  | The Central Index Key (CIK) of the company. Can be used instead of ticker.  |
| `isin` | string |  | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`.  |
| `market` | string |  | market one of: `UK`, `US` |
| `ticker` | string |  | The ticker symbol of the company.  |
| `exchange` | string |  | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class, returns the company's metrics. Price-based values (market… one of: `LSE` |

## Details

Returns one snapshot of financial metrics for a public company: valuation ratios, margins, returns, liquidity, debt ratios, growth rates and per share values. Pass a `ticker`, or use `cik` or `isin` instead.

### Use cases

- Pull the current P/E, price to book and enterprise value multiples for a stock in a valuation screen.
- Compare margins and return on equity across several companies.
- Check liquidity and debt ratios such as `current_ratio` and `debt_to_equity` before a credit or risk review.
- Feed growth rates for revenue, earnings and free cash flow into a stock research dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/financial-metrics-snapshot" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cik` | string | No | The Central Index Key (CIK) of the company. Can be used instead of ticker. |
| `exchange` | string | No | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class, returns the company's metrics. Price-based values (market ca |
| `isin` | string | No | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`. |
| `market` | string | No | market |
| `ticker` | string | No | The ticker symbol of the company. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "snapshot": {
    "asset_turnover": 1.2376860547121489,
    "book_value_growth": 0.6332978885006836,
    "book_value_per_share": 7.30699065341296,
    "cash_ratio": 0.2648165758139909,
    "currency": "USD",
    "current_ratio": 1.0032948046555858,
    "days_sales_outstanding": 24.135491396096594,
    "debt_to_assets": 0.2486628085976841,
    "debt_to_equity": 0.8863839285714286,
    "earnings_growth": 0.29865028203062044,
    "earnings_per_share": 8.762000604022814,
    "earnings_per_share_growth": 0.3192581932618972
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `snapshot.ticker / snapshot.currency` | The ticker symbol and the currency of the money values in the snapshot, for example `USD`. |
| `snapshot.market_cap / snapshot.enterprise_value` | Market capitalization and enterprise value as plain numbers in the snapshot currency. |
| `snapshot.price_to_earnings_ratio / snapshot.price_to_book_ratio / snapshot.price_to_sales_ratio / snapshot.peg_ratio` | Valuation ratios based on the current price. |
| `snapshot.enterprise_value_to_ebitda_ratio / snapshot.enterprise_value_to_revenue_ratio` | Enterprise value divided by EBITDA and by revenue. |
| `snapshot.gross_margin / snapshot.operating_margin / snapshot.net_margin` | Profit margins as decimal fractions. A value of `0.4865` means 48.65%. |
| `snapshot.return_on_equity / snapshot.return_on_assets / snapshot.return_on_invested_capital` | Return ratios as decimal fractions. |
| `snapshot.current_ratio / snapshot.quick_ratio / snapshot.cash_ratio / snapshot.debt_to_equity / snapshot.debt_to_assets` | Liquidity and debt ratios. |
| `snapshot.revenue_growth / snapshot.earnings_growth / snapshot.earnings_per_share_growth / snapshot.free_cash_flow_growth` | Growth rates for revenue, earnings, EPS and free cash flow, as decimal fractions. |
| `snapshot.earnings_per_share / snapshot.book_value_per_share / snapshot.free_cash_flow_per_share` | Per share values for earnings, book value and free cash flow. |
| `snapshot.free_cash_flow_yield / snapshot.payout_ratio` | Free cash flow yield and the share of earnings paid out, as decimal fractions. |

### Notes

- Some fields can be `null`. In this response `interest_coverage` is `null`.
- Set `exchange` to `LSE` for London listings, or use `isin` for a non-US listing. `market` accepts `UK` or `US`.
- For metrics over several periods, call [Financial Datasets Get Financial Metrics](/apis/financial-datasets/financial-metrics).
- For the current share price, call [Financial Datasets Get Stock Price Snapshot](/apis/financial-datasets/prices-snapshot).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/financial-metrics-snapshot.json`](../../../catalog/models/financial-datasets/financial-metrics-snapshot.json) · Store page: https://www.sandbase.ai/model/financial-datasets/financial-metrics-snapshot
