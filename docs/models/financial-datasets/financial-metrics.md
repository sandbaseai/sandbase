# Financial Datasets Get Financial Metrics API: pricing, parameters and code examples

`financial-datasets/financial-metrics` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get financial metrics for a ticker, including valuation, profitability, efficiency, liquidity, leverage, growth, and per share metrics.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/financial-metrics", "period": "annual"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/financial-metrics', {'period': 'annual'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/financial-metrics", {
  "period": "annual"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/financial-metrics", sandbase.Params{
	"period": "annual",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/financial-metrics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cik` | string |  | The Central Index Key (CIK) of the company. Can be used instead of ticker.  |
| `isin` | string |  | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`.  |
| `limit` | integer |  | The maximum number of results to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`.  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `period` | string | yes | The time period for the financial data. one of: `annual`, `quarterly`, `ttm` |
| `ticker` | string |  | The ticker symbol of the company. Required if cik is not provided.  |
| `exchange` | string |  | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class, returns the company's metrics. Price-based values (market… one of: `LSE` |
| `filing_date` | string |  | Filter by exact SEC filing date in YYYY-MM-DD format. Rows without a known filing date are excluded.  |
| `report_period` | string |  | Filter by exact report period date in YYYY-MM-DD format.  |
| `filing_date_gt` | string |  | Filter by SEC filing date greater than date in YYYY-MM-DD format. Rows without a known filing date are excluded.  |
| `filing_date_lt` | string |  | Filter by SEC filing date less than date in YYYY-MM-DD format. Rows without a known filing date are excluded.  |
| `filing_date_gte` | string |  | Filter by SEC filing date greater than or equal to date in YYYY-MM-DD format. Rows without a known filing date are excluded.  |
| `filing_date_lte` | string |  | Filter by SEC filing date less than or equal to date in YYYY-MM-DD format. Useful for point-in-time queries: returns only data that was publicly filed by the given date. Rows without a known filing date are excluded.  |
| `report_period_gt` | string |  | Filter by report period greater than date in YYYY-MM-DD format.  |
| `report_period_lt` | string |  | Filter by report period less than date in YYYY-MM-DD format.  |
| `report_period_gte` | string |  | Filter by report period greater than or equal to date in YYYY-MM-DD format.  |
| `report_period_lte` | string |  | Filter by report period less than or equal to date in YYYY-MM-DD format.  |

## Details

Returns historical financial metrics for a company, one record per reporting period. Each record covers valuation, profitability, liquidity, debt, growth, and per share figures. You pass a `ticker` (or `cik`, or `isin`) and a required `period` of `annual`, `quarterly`, or `ttm`.

### Use cases

- Chart `price_to_earnings_ratio` and `enterprise_value_to_ebitda_ratio` over several years to see how a stock's valuation has changed.
- Compare `gross_margin`, `operating_margin`, and `net_margin` across fiscal years to track profitability trends.
- Screen balance sheet health by reading `current_ratio`, `debt_to_equity`, and `debt_to_assets` for each filing.
- Run point-in-time backtests by filtering on `filing_date_lte` so only data already filed is used.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/financial-metrics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"period": "annual", "limit": 2, "ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `period` | string | Yes | The time period for the financial data. |
| `cik` | string | No | The Central Index Key (CIK) of the company. Can be used instead of ticker. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or modify  |
| `exchange` | string | No | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class, returns the company's metrics. Price-based values (market ca |
| `filing_date` | string | No | Filter by exact SEC filing date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_gt` | string | No | Filter by SEC filing date greater than date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_gte` | string | No | Filter by SEC filing date greater than or equal to date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_lt` | string | No | Filter by SEC filing date less than date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_lte` | string | No | Filter by SEC filing date less than or equal to date in YYYY-MM-DD format. Useful for point-in-time queries: returns only data that was publicly filed by the given date. Rows without a known filing date are excluded. |
| `isin` | string | No | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`. |
| `limit` | integer | No | The maximum number of results to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. |
| `report_period` | string | No | Filter by exact report period date in YYYY-MM-DD format. |
| `report_period_gt` | string | No | Filter by report period greater than date in YYYY-MM-DD format. |
| `report_period_gte` | string | No | Filter by report period greater than or equal to date in YYYY-MM-DD format. |
| `report_period_lt` | string | No | Filter by report period less than date in YYYY-MM-DD format. |
| `report_period_lte` | string | No | Filter by report period less than or equal to date in YYYY-MM-DD format. |
| `ticker` | string | No | The ticker symbol of the company. Required if cik is not provided. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "financial_metrics": [
    {
      "accession_number": "0000320193-25-000079",
      "asset_turnover": 1.1584451663368045,
      "book_value_growth": 0.2946971027216857,
      "book_value_per_share": 4.989932224818939,
      "cash_ratio": 0.21695214060169896,
      "currency": "USD",
      "current_ratio": 0.8932929222186667,
      "days_sales_outstanding": 32.09485631762708,
      "debt_to_assets": 0.31050186365142063,
      "debt_to_equity": 1.5128232948611884,
      "earnings_growth": 0.19495177946573355,
      "earnings_per_share": 7.5803549089548685
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `financial_metrics[]` | One record per reporting period, newest first in this response. |
| `financial_metrics[].fiscal_period / period / form_type` | The fiscal label (such as `FY2025`), the period type you requested, and the SEC form the data came from (such as `10-K`). |
| `financial_metrics[].filing_date / filing_datetime / filing_url / accession_number` | When the report was filed with the SEC, a link to the filing index page, and the filing's accession number. |
| `financial_metrics[].market_cap / enterprise_value` | Company market capitalization and enterprise value, in the currency given in `currency`. |
| `financial_metrics[].price_to_earnings_ratio / price_to_book_ratio / price_to_sales_ratio / peg_ratio` | Valuation ratios for the period. |
| `financial_metrics[].gross_margin / operating_margin / net_margin` | Profitability margins as decimal ratios. A value of `0.27` reads as 27%. |
| `financial_metrics[].current_ratio / cash_ratio / debt_to_equity / debt_to_assets / interest_coverage` | Liquidity and debt measures. `interest_coverage` is `null` for Apple in this response. |
| `financial_metrics[].earnings_growth / earnings_per_share_growth / ebitda_growth / operating_income_growth / free_cash_flow_growth / book_value_growth` | Growth rates compared with the prior period, as decimals. Negative values mean a decline. |
| `financial_metrics[].earnings_per_share / book_value_per_share / free_cash_flow_per_share` | Per share figures for the period. |
| `financial_metrics[].asset_turnover / inventory_turnover / days_sales_outstanding / operating_cycle` | Efficiency measures for how the company uses assets, inventory, and receivables. |

### Notes

- `limit` is the total number of records across all pages. Each page holds up to 10 records, linked by `next_page_url`. Pass the `cursor` value from that URL to get the next page, and send no other filters with it.
- Use `report_period` filters to select by period end date and `filing_date` filters to select by SEC filing date. Both use `YYYY-MM-DD`.
- Set `exchange` to `LSE` for London listings. Price-based values are not yet available for those.
- For the latest values only, call [Financial Datasets Get Financial Metrics Snapshot](/apis/financial-datasets/financial-metrics-snapshot). For the underlying statements, call [Financial Datasets Get Financial Statements](/apis/financial-datasets/financials).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/financial-metrics.json`](../../../catalog/models/financial-datasets/financial-metrics.json) · Store page: https://www.sandbase.ai/model/financial-datasets/financial-metrics
