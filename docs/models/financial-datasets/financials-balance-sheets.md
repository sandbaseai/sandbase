# Financial Datasets Get Balance Sheets API: pricing, parameters and code examples

`financial-datasets/financials-balance-sheets` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Balance Sheets from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/financials-balance-sheets"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/financials-balance-sheets', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/financials-balance-sheets", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/financials-balance-sheets", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/financials-balance-sheets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cik` | string |  | The Central Index Key (CIK) of the company.  |
| `isin` | string |  | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`.  |
| `limit` | string |  | The maximum number of balance sheets to return This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. Provider reference (supplier schema):…  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `market` | string |  | market one of: `UK`, `US` |
| `period` | string |  | The time period of the balance sheets. Provider reference (supplier schema): `{"enum":["annual","quarterly","ttm"],"type":"string"}`.  |
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

Returns balance sheet records for a public company, one record per reporting period. Each record has assets, liabilities, debt, equity and SEC filing details. You pass a `ticker`, `cik` or `isin`, and you can narrow results by `period`, `report_period` and `filing_date` filters.

### Use cases

- Compare `total_assets`, `total_liabilities` and `shareholders_equity` for a company across several fiscal years.
- Compute debt ratios from `total_debt`, `current_debt` and `non_current_debt`.
- Build point-in-time datasets by filtering on `filing_date_lte` so you only see data filed by a given date.
- Link each figure to its SEC filing through `filing_url` and `accession_number` for audit checks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/financials-balance-sheets" \
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
| `limit` | string | No | The maximum number of balance sheets to return This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. Provider reference (supplier schema): `{"format":"int32","t |
| `market` | string | No | market |
| `period` | string | No | The time period of the balance sheets. Provider reference (supplier schema): `{"enum":["annual","quarterly","ttm"],"type":"string"}`. |
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
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `balance_sheets[]` | One balance sheet per reporting period. The newest period comes first in the sample. |
| `ticker / period / fiscal_period / report_period` | The company ticker, the period type (such as `annual`), the fiscal label (such as `FY2025`) and the balance sheet date in YYYY-MM-DD format. |
| `total_assets / current_assets / non_current_assets` | Total assets and their split between current and non-current assets. The currency is in `balance_sheets[].currency`. |
| `total_liabilities / current_liabilities / non_current_liabilities` | Total liabilities and their split between current and non-current liabilities. |
| `total_debt / current_debt / non_current_debt` | Total debt and its short-term and long-term parts. |
| `shareholders_equity / retained_earnings / accumulated_other_comprehensive_income` | Equity figures. `retained_earnings` can be negative. |
| `cash_and_equivalents / current_investments / non_current_investments / investments` | Cash and investment balances. |
| `outstanding_shares` | Number of shares outstanding for that period. |
| `filing_date / filing_datetime / form_type / accession_number / filing_url` | Details of the SEC filing the data came from. `filing_url` links to the filing index page. |

### Notes

- Provide one of `ticker`, `cik` or `isin`. Use `exchange` set to `LSE` for London listings.
- `limit` is the total number of records across all pages. Each page holds up to 10 records, and `next_page_url` links to the next page. Pass the `cursor` value from it to continue, and do not change it.
- Some fields, such as `goodwill_and_intangible_assets` and `tax_liabilities`, can be `null`.
- For the other statements, call [Financial Datasets Get Income Statements](/apis/financial-datasets/financials-income-statements) or [Financial Datasets Get Cash Flow Statements](/apis/financial-datasets/financials-cash-flow-statements). To get all three together, use [Financial Datasets Get Financial Statements](/apis/financial-datasets/financials).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/financials-balance-sheets.json`](../../../catalog/models/financial-datasets/financials-balance-sheets.json) · Store page: https://www.sandbase.ai/model/financial-datasets/financials-balance-sheets
