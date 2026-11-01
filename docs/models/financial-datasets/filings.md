# Financial Datasets Get Company SEC Filings

`financial-datasets/filings` · api · Financial Datasets

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

Get Company SEC Filings from Financial Datasets. Returns the official Financial Datasets API response unchanged.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/filings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL", "filing_type": ["10-K"], "limit": "2"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cik` | string | No | The Central Index Key (CIK) of the company. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original reques |
| `filing_type` | array | No | Filter by one or more filing types. Repeat the query parameter to pass multiple values (e.g. filing_type=10-Q&filing_type=10-K). |
| `limit` | string | No | The maximum number of filings to return (default: 10). This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_pa |
| `ticker` | string | No | The ticker symbol. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/filings.json`](../../../catalog/models/financial-datasets/filings.json) · Store page: https://www.sandbase.ai/model/financial-datasets/filings
