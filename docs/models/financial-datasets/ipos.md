# Financial Datasets IPO Filings API: pricing, parameters and code examples

`financial-datasets/ipos` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.16 per call · **Modes:** sync

Recent US IPO and registration filings (S-1, F-1 and amendments) with company, form type and filing links.

## Pricing

- **$0.16 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/ipos"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/ipos', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/ipos", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/ipos", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/ipos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of filings to return.  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url.  |

## Details

Returns recent US IPO and registration filings (S-1, F-1 and amendments) from SEC EDGAR. Each row has the company name, form type, filing link and an IPO classification. The only inputs are an optional `limit` and an optional `cursor`.

### Use cases

- Track new S-1 and S-1/A filings to see which companies are preparing to go public.
- Filter for rows where `is_ipo_grade` is `true` to build a watchlist of likely IPOs.
- Collect `filing_url` links to read the full registration documents on SEC EDGAR.
- Match `cik` and `ticker` values against other company data to follow a filer over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/ipos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. |
| `limit` | integer | No | Maximum number of filings to return. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ipos": [
    {
      "accepted_datetime": "2026-07-14T01:18:24Z",
      "accession_number": "0001193125-26-302144",
      "cik": "0001718728",
      "classification": "ipo",
      "company_name": "Syntiant Corp.",
      "exchange": null,
      "expected_offering_price": null,
      "filing_date": null,
      "filing_url": "https://www.sec.gov/Archives/edgar/data/1718728/0001193125-26-302144-index.html",
      "financials": null,
      "form_type": "S-1/A",
      "has_financial_statements": true
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `ipos[].company_name` | Name of the company that filed. |
| `ipos[].form_type` | SEC form type of the filing, such as `S-1/A`. |
| `ipos[].classification` | Label for the filing, such as `ipo` or `other`. |
| `ipos[].is_ipo_grade` | Boolean flag. It is `true` for filings marked as IPO-grade and `false` for others, such as the ETF filing in the sample. |
| `ipos[].ticker / ipos[].exchange` | Proposed ticker symbol and exchange for the listing. Both can be `null` when the filing does not give them. |
| `ipos[].filing_url` | Link to the filing index page on sec.gov. |
| `ipos[].accepted_datetime / ipos[].filing_date` | Time the SEC accepted the filing (UTC timestamp) and the filing date. `filing_date` can be `null`. |
| `ipos[].cik / ipos[].accession_number` | SEC company identifier and SEC filing identifier. |
| `ipos[].price_range_low / ipos[].price_range_high / ipos[].expected_offering_price` | Price range and expected offering price. These are `null` in the sample, so expect them to be empty when the filing shows no price. |
| `ipos[].has_financial_statements / ipos[].has_price_on_cover` | Booleans that show whether the filing includes financial statements and whether a price appears on the cover. |

### Notes

- Use `limit` to set how many filings to return. For the next page, pass the cursor from the response's `next_page_url` as `cursor`.
- `cik` is a 10-digit string with leading zeros. `accession_number` follows the pattern `0001193125-26-302144`.
- Several fields, including `financials` and `status`, were `null` or `SKIPPED` in the sample, so check for `null` before using a value.
- To read the filing contents after finding a company, call [Financial Datasets Get Company SEC Filings](/apis/financial-datasets/filings) or [Financial Datasets Get Company Facts](/apis/financial-datasets/company-facts).

### Pricing

$0.16 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/ipos.json`](../../../catalog/models/financial-datasets/ipos.json) · Store page: https://www.sandbase.ai/model/financial-datasets/ipos
