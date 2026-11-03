# Financial Datasets Get Company SEC Filings API: pricing, parameters and code examples

`financial-datasets/filings` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Company SEC Filings from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/filings"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/filings', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/filings", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/filings", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/filings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cik` | string |  | The Central Index Key (CIK) of the company.  |
| `limit` | string |  | The maximum number of filings to return (default: 10). This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. Provider reference (supplier schema):…  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `ticker` | string |  | The ticker symbol.  |
| `filing_type` | array |  | Filter by one or more filing types. Repeat the query parameter to pass multiple values (e.g. filing_type=10-Q&filing_type=10-K).  |

## Details

Returns a list of SEC filings for a US public company, including the filing type, filing date, report date, and a link to the document on sec.gov. Pass a `ticker` or a `cik`, and optionally filter by `filing_type`.

### Use cases

- List a company's annual 10-K filings to build a timeline of yearly reports.
- Find the newest filing link for a ticker so you can fetch and read the full document.
- Track when a company files a given form type by comparing `filing_date` with `report_date`.
- Collect accession numbers to match filings against other SEC data sources.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/filings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL", "filing_type": ["10-K"], "limit": "2"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cik` | string | No | The Central Index Key (CIK) of the company. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or modify  |
| `filing_type` | array | No | Filter by one or more filing types. Repeat the query parameter to pass multiple values (e.g. filing_type=10-Q&filing_type=10-K). |
| `limit` | string | No | The maximum number of filings to return (default: 10). This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. Provider reference (supplier schema): `{"default":1 |
| `ticker` | string | No | The ticker symbol. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "filings": [
    {
      "accession_number": "0000320193-25-000079",
      "cik": "320193",
      "filing_date": "2025-10-31",
      "filing_type": "10-K",
      "report_date": "2025-09-27",
      "ticker": "AAPL",
      "url": "https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `filings[]` | One SEC filing per row. The list holds up to the number of records set by `limit`. |
| `filings[].accession_number` | The SEC accession number that identifies the filing, such as `0000320193-25-000079`. |
| `filings[].filing_type` | The form type of the filing, such as `10-K`. |
| `filings[].filing_date` | The date the filing was submitted, in `YYYY-MM-DD` format. |
| `filings[].report_date` | The period end date the filing covers, in `YYYY-MM-DD` format. |
| `filings[].ticker / filings[].cik` | The ticker symbol and the Central Index Key of the company that filed. |
| `filings[].url` | Link to the filing document on sec.gov. |

### Notes

- Pass `filing_type` as an array. Repeat it to ask for several forms, for example `10-K` and `10-Q`.
- `limit` is the total number of filings across all pages. Each page holds up to 10 records.
- To get the next page, send the `cursor` value from the previous response's `next_page_url`. When you send `cursor`, all other parameters are ignored.
- To read the items inside a filing, call [Financial Datasets Get SEC Filing Items](/apis/financial-datasets/filings-items).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/filings.json`](../../../catalog/models/financial-datasets/filings.json) · Store page: https://www.sandbase.ai/model/financial-datasets/filings
