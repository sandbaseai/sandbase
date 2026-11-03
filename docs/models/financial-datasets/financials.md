# Financial Datasets Get Financial Statements API: pricing, parameters and code examples

`financial-datasets/financials` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Financial Statements from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/financials", "period": "annual"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/financials', {'period': 'annual'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/financials", {
  "period": "annual"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/financials", sandbase.Params{
	"period": "annual",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/financials` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cik` | string |  | The Central Index Key (CIK) of the company.  |
| `isin` | string |  | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`.  |
| `limit` | integer |  | The maximum number of financial statements to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`.  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `period` | string | yes | The time period of the financial statements. one of: `annual`, `quarterly`, `ttm` |
| `ticker` | string |  | The ticker symbol. Required if cik or isin is not provided.  |
| `exchange` | string |  | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class, returns the company's statements. one of: `LSE` |
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

Returns balance sheets, cash flow statements and income statements for one company in a single response. Each statement list holds one record per reporting period. The call needs `period` and one company identifier: `ticker`, `cik` or `isin`.

### Use cases

- Build a multi-year view of revenue, net income and EPS for a company from its annual income statements.
- Track free cash flow and capital spending over time to compare cash generation across years.
- Check debt, cash and equity on the balance sheet to compute debt-to-equity and other balance sheet ratios.
- Run point-in-time backtests by filtering on `filing_date_lte` so only data already filed is used.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/financials" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"period": "annual", "limit": 2, "ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `period` | string | Yes | The time period of the financial statements. |
| `cik` | string | No | The Central Index Key (CIK) of the company. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or modify  |
| `exchange` | string | No | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class, returns the company's statements. |
| `filing_date` | string | No | Filter by exact SEC filing date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_gt` | string | No | Filter by SEC filing date greater than date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_gte` | string | No | Filter by SEC filing date greater than or equal to date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_lt` | string | No | Filter by SEC filing date less than date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_lte` | string | No | Filter by SEC filing date less than or equal to date in YYYY-MM-DD format. Useful for point-in-time queries: returns only data that was publicly filed by the given date. Rows without a known filing date are excluded. |
| `isin` | string | No | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`. |
| `limit` | integer | No | The maximum number of financial statements to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. |
| `report_period` | string | No | Filter by exact report period date in YYYY-MM-DD format. |
| `report_period_gt` | string | No | Filter by report period greater than date in YYYY-MM-DD format. |
| `report_period_gte` | string | No | Filter by report period greater than or equal to date in YYYY-MM-DD format. |
| `report_period_lt` | string | No | Filter by report period less than date in YYYY-MM-DD format. |
| `report_period_lte` | string | No | Filter by report period less than or equal to date in YYYY-MM-DD format. |
| `ticker` | string | No | The ticker symbol. Required if cik or isin is not provided. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "financials": {
    "balance_sheets": [
      {
        "accession_number": "0000320193-25-000079",
        "accumulated_other_comprehensive_income": -5571000000.0,
        "cash_and_equivalents": 35934000000.0,
        "currency": "USD",
        "current_assets": 147957000000.0,
        "current_debt": 20867000000.0,
        "current_investments": 18763000000.0,
        "current_liabilities": 165631000000.0,
        "deferred_revenue": 9055000000.0,
        "deposit_liabilities": 13700000000.0,
        "filing_date": "2025-10-31",
        "filing_datetime": "2025-10-31T06:01:26-04:00"
      }
    ],
    "cash_flow_statements": [
      {
        "accession_number": "0000320193-25-000079",
        "business_acquisitions_and_disposals": null,
        "capital_expenditure": 12715000000.0,
        "change_in_cash_and_equivalents": 5991000000.0,
        "currency": "USD",
        "depreciation_and_amortization": 11698000000.0,
        "dividends_and_other_cash_distributions": 15421000000.0,
        "effect_of_exchange_rate_changes": null,
        "ending_cash_balance": 35934000000.0,
        "filing_date": "2025-10-31",
        "filing_datetime": "2025-10-31T06:01:26-04:00",
        "filing_url": "https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/0000320193-25-…"
      }
    ],
    "income_statements": [
      {
        "accession_number": "0000320193-25-000079",
        "consolidated_income": 112010000000.0,
        "cost_of_revenue": 220960000000.0,
        "currency": "USD",
        "dividends_per_common_share": 1.02,
        "earnings_per_share": 7.49,
        "earnings_per_share_diluted": 7.46,
        "ebit": 133050000000.0,
        "filing_date": "2025-10-31",
        "filing_datetime": "2025-10-31T06:01:26-04:00",
        "filing_url": "https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/0000320193-25-…",
        "fiscal_period": "FY2025"
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `financials.income_statements[].revenue / cost_of_revenue / gross_profit` | Total revenue, cost of revenue and gross profit for the period, in the statement `currency`. |
| `financials.income_statements[].operating_income / net_income` | Operating income and net income for the period. |
| `financials.income_statements[].earnings_per_share / earnings_per_share_diluted` | Basic and diluted earnings per share. |
| `financials.balance_sheets[].total_assets / total_liabilities / shareholders_equity` | Main balance sheet totals at the end of the report period. |
| `financials.balance_sheets[].cash_and_equivalents / total_debt` | Cash and cash equivalents, and total debt, at the end of the report period. |
| `financials.cash_flow_statements[].net_cash_flow_from_operations / net_cash_flow_from_investing / net_cash_flow_from_financing` | Net cash flow from operating, investing and financing activities. Negative values are cash outflows. |
| `financials.cash_flow_statements[].free_cash_flow / capital_expenditure` | Free cash flow and capital expenditure for the period. |
| `financials.income_statements[].report_period / fiscal_period` | Period end date in `YYYY-MM-DD` format and the fiscal period label, such as `FY2025`. The same fields appear in all three statement lists. |
| `financials.income_statements[].filing_date / filing_url / form_type` | Date the report was filed, a link to the SEC filing index, and the form type, such as `10-K`. |

### Notes

- Pass `period` as `annual`, `quarterly` or `ttm`. Use `report_period_*` to filter by period end date and `filing_date_*` to filter by filing date.
- `limit` is the total number of records across all pages. Each page holds up to 10 records. Pass the cursor from `next_page_url` as `cursor` to get the next page, and do not change it.
- For non-US listings, use `isin`, or use `ticker` with `exchange` set to `LSE`.
- To fetch only one statement, use [Financial Datasets Get Balance Sheets](/apis/financial-datasets/financials-balance-sheets), [Financial Datasets Get Cash Flow Statements](/apis/financial-datasets/financials-cash-flow-statements) or [Financial Datasets Get Income Statements](/apis/financial-datasets/financials-income-statements).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/financials.json`](../../../catalog/models/financial-datasets/financials.json) · Store page: https://www.sandbase.ai/model/financial-datasets/financials
