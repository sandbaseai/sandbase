# Financial Datasets Get Income Statements API: pricing, parameters and code examples

`financial-datasets/financials-income-statements` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Income Statements from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/financials-income-statements"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/financials-income-statements', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/financials-income-statements", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/financials-income-statements", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/financials-income-statements` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cik` | string |  | The Central Index Key (CIK) of the company.  |
| `isin` | string |  | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`.  |
| `limit` | string |  | The maximum number of income statements to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. Provider reference (supplier schema):…  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `market` | string |  | market one of: `UK`, `US` |
| `period` | string |  | The time period of the income statements. Provider reference (supplier schema): `{"enum":["annual","quarterly","ttm"],"type":"string"}`.  |
| `ticker` | string |  | The ticker symbol. Required if cik or isin is not provided.  |
| `exchange` | string |  | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class, returns the company's statements. one of: `LSE` |
| `filing_date` | string |  | Filter by exact SEC filing date in YYYY-MM-DD format. Rows without a known filing date are excluded. Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `report_period` | string |  | Filter by exact report period date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_gt` | string |  | Filter by SEC filing date greater than date in YYYY-MM-DD format. Rows without a known filing date are excluded. Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_lt` | string |  | Filter by SEC filing date less than date in YYYY-MM-DD format. Rows without a known filing date are excluded. Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_gte` | string |  | Filter by SEC filing date greater than or equal to date in YYYY-MM-DD format. Rows without a known filing date are excluded. Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_lte` | string |  | Filter by SEC filing date less than or equal to date in YYYY-MM-DD format. Useful for point-in-time queries: returns only data that was publicly filed by the given date. Rows without a known filing date are excluded.…  |
| `report_period_gt` | string |  | Filter by report period greater than date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `report_period_lt` | string |  | Filter by report period less than date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `report_period_gte` | string |  | Filter by report period greater than or equal to date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `report_period_lte` | string |  | Filter by report period less than or equal to date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |

## Details

Returns income statements for a public company, one record per reporting period. You pass a `ticker`, `cik`, or `isin`, and you can filter by `period` (`annual`, `quarterly`, or `ttm`), report period dates, and SEC filing dates.

### Use cases

- Build a multi-year revenue and net income trend for a company from its annual filings.
- Compare gross profit, operating income, and R&D spend across fiscal years.
- Run point-in-time backtests by limiting rows to statements filed on or before a date with `filing_date_lte`.
- Link each figure back to its SEC filing page using `filing_url` for audit checks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/financials-income-statements" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": "2", "period": "annual", "ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cik` | string | No | The Central Index Key (CIK) of the company. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or modify  |
| `exchange` | string | No | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class, returns the company's statements. |
| `filing_date` | string | No | Filter by exact SEC filing date in YYYY-MM-DD format. Rows without a known filing date are excluded. Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_gt` | string | No | Filter by SEC filing date greater than date in YYYY-MM-DD format. Rows without a known filing date are excluded. Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_gte` | string | No | Filter by SEC filing date greater than or equal to date in YYYY-MM-DD format. Rows without a known filing date are excluded. Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_lt` | string | No | Filter by SEC filing date less than date in YYYY-MM-DD format. Rows without a known filing date are excluded. Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_lte` | string | No | Filter by SEC filing date less than or equal to date in YYYY-MM-DD format. Useful for point-in-time queries: returns only data that was publicly filed by the given date. Rows without a known filing date are excluded. Pro |
| `isin` | string | No | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`. |
| `limit` | string | No | The maximum number of income statements to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. Provider reference (supplier schema): `{"format":"int32 |
| `market` | string | No | market |
| `period` | string | No | The time period of the income statements. Provider reference (supplier schema): `{"enum":["annual","quarterly","ttm"],"type":"string"}`. |
| `report_period` | string | No | Filter by exact report period date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `report_period_gt` | string | No | Filter by report period greater than date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `report_period_gte` | string | No | Filter by report period greater than or equal to date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `report_period_lt` | string | No | Filter by report period less than date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `report_period_lte` | string | No | Filter by report period less than or equal to date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `ticker` | string | No | The ticker symbol. Required if cik or isin is not provided. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
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
```

### Response fields

| Field | Meaning |
|---|---|
| `income_statements[]` | One income statement per reporting period. Newest period comes first in the sample. |
| `income_statements[].revenue / cost_of_revenue / gross_profit` | Top line sales, the cost tied to that revenue, and the gross profit. Values are plain numbers in the statement `currency`. |
| `income_statements[].operating_expense / operating_income / ebit` | Total operating costs, income from operations, and EBIT for the period. |
| `income_statements[].research_and_development / selling_general_and_administrative_expenses` | Spending on research and development, and on selling, general and administrative costs. |
| `income_statements[].net_income / consolidated_income` | Net income for the period and consolidated income. |
| `income_statements[].earnings_per_share / earnings_per_share_diluted` | Basic and diluted earnings per share. |
| `income_statements[].weighted_average_shares / weighted_average_shares_diluted` | Weighted average share counts used for basic and diluted per share figures. |
| `income_statements[].report_period / fiscal_period / period` | The period end date (`YYYY-MM-DD`), a fiscal label such as `FY2025`, and the period type such as `annual`. |
| `income_statements[].filing_date / filing_datetime / form_type` | When the statement was filed with the SEC and the form type, for example `10-K`. |
| `income_statements[].accession_number / filing_url` | The SEC accession number and a link to the filing index page. |

### Notes

- `limit` is the total number of records across all pages. Each page holds up to 10 records, and `next_page_url` links to the next page.
- To fetch the next page, pass the opaque `cursor` from a previous response. Other parameters are ignored when you send `cursor`.
- Fields such as `interest_expense` and `net_income_discontinued_operations` can be `null` when the filing has no value.
- For non-US listings, use `isin`, or set `exchange` to `LSE`. For balance sheet or cash flow data, call [Financial Datasets Get Balance Sheets](/apis/financial-datasets/financials-balance-sheets) or [Financial Datasets Get Cash Flow Statements](/apis/financial-datasets/financials-cash-flow-statements).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/financials-income-statements.json`](../../../catalog/models/financial-datasets/financials-income-statements.json) · Store page: https://www.sandbase.ai/model/financial-datasets/financials-income-statements
