# Financial Datasets Get Insider Trades API: pricing, parameters and code examples

`financial-datasets/insider-trades` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get insider trades like buys and sells for a ticker by a company insider.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/insider-trades"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/insider-trades', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/insider-trades", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/insider-trades", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/insider-trades` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `name` | string |  | Filter by insider name (e.g., 'Jen Hsun Huang'). Use the /insider-trades/names endpoint to get available names for a ticker.  |
| `limit` | string |  | The maximum number of transactions to return (default: 10). This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. Provider reference (supplier schema):…  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `ticker` | string |  | The ticker symbol of the company.  |
| `form_type` | string |  | Filter by SEC form type: 4 for trades, 5 for annual statements (or their amendments 4/A, 5/A). one of: `4`, `4/A`, `5`, `5/A` |
| `filing_date` | string |  | Filter by exact filing date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_gt` | string |  | Filter by filing date greater than this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_lt` | string |  | Filter by filing date less than this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_gte` | string |  | Filter by filing date greater than or equal to this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_lte` | string |  | Filter by filing date less than or equal to this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `transaction_type` | string |  | Filter by transaction type (e.g., 'Open market sale', 'Gift'). Use the /insider-trades/transaction-types endpoint to get available types.  |

## Details

Get insider trades like buys and sells for a ticker by a company insider.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/insider-trades" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": "2", "ticker": "AAPL"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original reques |
| `filing_date` | string | No | Filter by exact filing date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_gt` | string | No | Filter by filing date greater than this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_gte` | string | No | Filter by filing date greater than or equal to this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_lt` | string | No | Filter by filing date less than this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_lte` | string | No | Filter by filing date less than or equal to this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `form_type` | string | No | Filter by SEC form type: 4 for trades, 5 for annual statements (or their amendments 4/A, 5/A). |
| `limit` | string | No | The maximum number of transactions to return (default: 10). This is the total across all pages, not a page size: each page holds up to 10 records, linked by `ne |
| `name` | string | No | Filter by insider name (e.g., 'Jen Hsun Huang'). Use the /insider-trades/names endpoint to get available names for a ticker. |
| `ticker` | string | No | The ticker symbol of the company. |
| `transaction_type` | string | No | Filter by transaction type (e.g., 'Open market sale', 'Gift'). Use the /insider-trades/transaction-types endpoint to get available types. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/insider-trades.json`](../../../catalog/models/financial-datasets/insider-trades.json) · Store page: https://www.sandbase.ai/model/financial-datasets/insider-trades
