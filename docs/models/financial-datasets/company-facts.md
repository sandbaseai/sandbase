# Financial Datasets Get Company Facts API: pricing, parameters and code examples

`financial-datasets/company-facts` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Company Facts from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/company-facts"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/company-facts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/company-facts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/company-facts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/company-facts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cik` | string |  | The CIK of the company.  |
| `ticker` | string |  | The ticker symbol.  |

## Details

Returns basic company profile data for a US-listed company, including its name, exchange, sector, industry, and SEC identifiers. Send either a `ticker` such as `AAPL` or a `cik`.

### Use cases

- Resolve a ticker to its SEC CIK before calling filing or financial statement APIs.
- Label a watchlist with each company's exchange, sector, and industry.
- Group companies by SIC code to build peer lists for a sector analysis.
- Link users to a company's SEC EDGAR filing page from an app.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/company-facts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cik` | string | No | The CIK of the company. |
| `ticker` | string | No | The ticker symbol. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "company_facts": {
    "cik": "0000320193",
    "exchange": "NASDAQ",
    "industry": "Technology Hardware, Storage & Peripherals",
    "is_active": true,
    "location": "California; U.S.A",
    "name": "Apple Inc",
    "sec_filings_url": "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320193",
    "sector": "Information Technology",
    "sic_code": "3571",
    "sic_industry": "Electronic Computers",
    "sic_sector": "Manufacturing",
    "ticker": "AAPL"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `company_facts.name` | Company name, for example `Apple Inc`. |
| `company_facts.ticker` | Ticker symbol of the company. |
| `company_facts.cik` | SEC Central Index Key as a zero-padded 10-digit string. |
| `company_facts.exchange` | Exchange where the stock trades, for example `NASDAQ`. |
| `company_facts.sector / company_facts.industry` | Sector and industry classification of the company. In the sample these are `Information Technology` and `Technology Hardware, Storage & Peripherals`. |
| `company_facts.sic_code / company_facts.sic_industry / company_facts.sic_sector` | Standard Industrial Classification code, plus its industry and sector names. In the sample these are `3571`, `Electronic Computers`, and `Manufacturing`. |
| `company_facts.is_active` | Boolean flag. `true` in the sample for Apple. |
| `company_facts.location` | Location text for the company, for example `California; U.S.A`. |
| `company_facts.sec_filings_url` | Link to the company's filing list on the SEC EDGAR website. |

### Notes

- Pass either `ticker` or `cik`. Both are optional in the schema, so send at least one.
- The `cik` value is returned as a 10-digit string with leading zeros, such as `0000320193`.
- Call [Financial Datasets Get Company SEC Filings](/apis/financial-datasets/filings) to list the company's filings, or [Financial Datasets Get Financial Statements](/apis/financial-datasets/financials) for its financials.

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/company-facts.json`](../../../catalog/models/financial-datasets/company-facts.json) · Store page: https://www.sandbase.ai/model/financial-datasets/company-facts
