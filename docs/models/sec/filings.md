# SEC EDGAR Filings API: pricing, parameters and code examples

`sec/filings` · data API · SEC EDGAR · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00132 per call · **Modes:** sync

List a public company's SEC EDGAR filings - form type, filing date, accession number, and document links - by ticker, company name, or CIK, with optional form-type and date filters.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sec/filings"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sec/filings', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sec/filings", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sec/filings", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/sec/filings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `form` | string |  | Filter filings by SEC form type (e.g. 10-K, 10-Q, 8-K, 4, DEF 14A, S-1, 13F-HR); omit for all forms.  |
| `limit` | integer |  | Maximum number of filings to return (1-25, default 25). You are billed per result returned, so a lower limit costs less. range 1–25 |
| `dateTo` | string |  | Only return filings filed on or before this date, in YYYY-MM-DD format (e.g. 2026-06-01).  |
| `ticker` | string |  | Company stock ticker symbol, e.g. AAPL, MSFT, or TSLA. Provide either ticker or companyName; ticker is the more precise lookup.  |
| `dateFrom` | string |  | Only return filings filed on or after this date, in YYYY-MM-DD format (e.g. 2025-01-01).  |
| `companyName` | string |  | Company name to search for (partial match supported, e.g. 'Tesla' or 'Berkshire'). Use this when you do not have the ticker symbol. If both ticker and companyName are given, ticker takes precedence.  |

## Details

List a public company's SEC EDGAR filings - form type, filing date, accession number, and document links - by ticker, company name, or CIK, with optional form-type and date filters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "sec/filings", "limit": 3, "ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `companyName` | string | No | Company name to search for (partial match supported, e.g. 'Tesla' or 'Berkshire'). Use this when you do not have the ticker symbol. If both ticker and companyName are given, ticker takes precedence. |
| `dateFrom` | string | No | Only return filings filed on or after this date, in YYYY-MM-DD format (e.g. 2025-01-01). |
| `dateTo` | string | No | Only return filings filed on or before this date, in YYYY-MM-DD format (e.g. 2026-06-01). |
| `form` | string | No | Filter filings by SEC form type (e.g. 10-K, 10-Q, 8-K, 4, DEF 14A, S-1, 13F-HR); omit for all forms. |
| `limit` | integer | No | Maximum number of filings to return (1-25, default 25). You are billed per result returned, so a lower limit costs less. |
| `ticker` | string | No | Company stock ticker symbol, e.g. AAPL, MSFT, or TSLA. Provide either ticker or companyName; ticker is the more precise lookup. |

### Pricing

Billed at the actual cost of each call: about $0.00044 per result returned, up to $0.0132 per request (about $0.00132 for the request above). A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/sec/filings.json`](../../../catalog/models/sec/filings.json) · Store page: https://www.sandbase.ai/model/sec/filings
