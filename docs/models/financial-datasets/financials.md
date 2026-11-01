# Financial Datasets Get Financial Statements

`financial-datasets/financials` · api · Financial Datasets

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

Get Financial Statements from Financial Datasets. Returns the official Financial Datasets API response unchanged.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/financials" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"period": "annual", "limit": 2, "ticker": "AAPL"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cik` | string | No | The Central Index Key (CIK) of the company. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original reques |
| `exchange` | string | No | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class,  |
| `filing_date` | string | No | Filter by exact SEC filing date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_gt` | string | No | Filter by SEC filing date greater than date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_gte` | string | No | Filter by SEC filing date greater than or equal to date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_lt` | string | No | Filter by SEC filing date less than date in YYYY-MM-DD format. Rows without a known filing date are excluded. |
| `filing_date_lte` | string | No | Filter by SEC filing date less than or equal to date in YYYY-MM-DD format. Useful for point-in-time queries: returns only data that was publicly filed by the gi |
| `isin` | string | No | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`. |
| `limit` | integer | No | The maximum number of financial statements to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_pag |
| `period` | string | Yes | The time period of the financial statements. |
| `report_period` | string | No | Filter by exact report period date in YYYY-MM-DD format. |
| `report_period_gt` | string | No | Filter by report period greater than date in YYYY-MM-DD format. |
| `report_period_gte` | string | No | Filter by report period greater than or equal to date in YYYY-MM-DD format. |
| `report_period_lt` | string | No | Filter by report period less than date in YYYY-MM-DD format. |
| `report_period_lte` | string | No | Filter by report period less than or equal to date in YYYY-MM-DD format. |
| `ticker` | string | No | The ticker symbol. Required if cik or isin is not provided. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/financials.json`](../../../catalog/models/financial-datasets/financials.json) · Store page: https://www.sandbase.ai/model/financial-datasets/financials
