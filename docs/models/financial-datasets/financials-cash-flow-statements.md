# Financial Datasets Get Cash Flow Statements API: pricing, parameters and code examples

`financial-datasets/financials-cash-flow-statements` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Cash Flow Statements from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/financials-cash-flow-statements", "period": "annual"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/financials-cash-flow-statements', {'period': 'annual'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/financials-cash-flow-statements", {
  "period": "annual"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/financials-cash-flow-statements", sandbase.Params{
	"period": "annual",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/financials-cash-flow-statements` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cik` | string |  | The Central Index Key (CIK) of the company.  |
| `isin` | string |  | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`.  |
| `limit` | integer |  | The maximum number of cash flow statements to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`.  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `period` | string | yes | The time period of the cash flow statements. one of: `annual`, `quarterly`, `ttm` |
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

Returns cash flow statements for a public company, one record per reporting period. You choose the `period` (`annual`, `quarterly` or `ttm`) and identify the company with `ticker`, `cik` or `isin`.

### Use cases

- Track operating cash flow and free cash flow for a company across several fiscal years.
- Compare share buybacks and dividends against `net_cash_flow_from_operations` to see how a company returns cash.
- Pull statements filed on or before a past date to build point-in-time backtests.
- Link each statement to its SEC filing page to check the source document.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/financials-cash-flow-statements" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"period": "annual", "limit": 2, "ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `period` | string | Yes | The time period of the cash flow statements. |
| `cik` | string | No | The Central Index Key (CIK) of the company. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or modify  |
| `exchange` | string | No | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class, returns the company's statements. |
| `filing_date` | string | No | Filter by exact SEC filing date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_gt` | string | No | Filter by SEC filing date greater than date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_gte` | string | No | Filter by SEC filing date greater than or equal to date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_lt` | string | No | Filter by SEC filing date less than date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_lte` | string | No | Filter by SEC filing date less than or equal to date in YYYY-MM-DD format. Useful for point-in-time queries: returns only data that was publicly filed by the given date. Rows without a known filing date are excluded. |
| `isin` | string | No | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`. |
| `limit` | integer | No | The maximum number of cash flow statements to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. |
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
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cash_flow_statements[]` | One cash flow statement per reporting period, newest first in this sample. |
| `ticker / period / fiscal_period / report_period` | Identify the statement: the company ticker, the period type, the fiscal label such as `FY2025`, and the period end date in YYYY-MM-DD. |
| `net_cash_flow_from_operations / net_cash_flow_from_investing / net_cash_flow_from_financing` | Net cash from operating, investing and financing activities. Negative values mean cash went out. |
| `free_cash_flow` | Free cash flow for the period as reported in the record. |
| `net_income / depreciation_and_amortization / share_based_compensation` | Net income and two common non-cash items used to move from earnings to operating cash flow. |
| `capital_expenditure / property_plant_and_equipment` | Spending on capital assets. `property_plant_and_equipment` can be negative. |
| `dividends_and_other_cash_distributions / issuance_or_purchase_of_equity_shares / issuance_or_repayment_of_debt_securities` | Cash paid out as dividends, net equity issuance or repurchase, and net debt issuance or repayment. |
| `change_in_cash_and_equivalents / ending_cash_balance` | The change in cash over the period and the cash balance at the end of it. |
| `filing_date / filing_datetime / form_type / accession_number / filing_url` | Details of the SEC filing the data came from: date, timestamp with offset, form such as `10-K`, accession number and a link to the filing index. |
| `currency` | Currency of the amounts, such as `USD`. |

### Notes

- Some fields, such as `business_acquisitions_and_disposals` and `effect_of_exchange_rate_changes`, can be `null` when no value is reported.
- `limit` is the total number of records across all pages. Each page holds up to 10 records. Pass the cursor from `next_page_url` as `cursor` to get the next page; other filters are then ignored.
- Use `filing_date_lte` for point-in-time queries and the `report_period` filters to select fiscal periods.
- For the other statements, call [Financial Datasets Get Balance Sheets](/apis/financial-datasets/financials-balance-sheets) or [Financial Datasets Get Income Statements](/apis/financial-datasets/financials-income-statements).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/financials-cash-flow-statements.json`](../../../catalog/models/financial-datasets/financials-cash-flow-statements.json) · Store page: https://www.sandbase.ai/model/financial-datasets/financials-cash-flow-statements
