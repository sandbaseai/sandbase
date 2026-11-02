# Financial Datasets Get SEC Filing Items API: pricing, parameters and code examples

`financial-datasets/filings-items` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get SEC Filing Items from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/filings-items", "filing_type": "10-K", "ticker": "AAPL", "year": 2024}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/filings-items', {'filing_type': '10-K', 'ticker': 'AAPL', 'year': 2024})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/filings-items", {
  "filing_type": "10-K",
  "ticker": "AAPL",
  "year": 2024
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/filings-items", sandbase.Params{
	"filing_type": "10-K",
	"ticker": "AAPL",
	"year": 2024,
})
```

Same call via the path form: `POST /v1/api/financial-datasets/filings-items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item` | string |  | The item to get. one of: `Item-1`, `Item-1A`, `Item-1B`, `Item-2`, `Item-3`, `Item-4`, `Item-5`, `Item-6`, `Item-7`, `Item-7A`, `Item-8`, `Item-9` … |
| `year` | integer | yes | The year of the filing.  |
| `ticker` | string | yes | The ticker symbol.  |
| `quarter` | integer |  | The quarter of the filing if 10-Q.  |
| `filing_type` | string | yes | The type of filing. one of: `10-K`, `10-Q`, `8-K` |
| `accession_number` | string |  | The accession number of the filing if 8-K.  |
| `include_exhibits` | boolean |  | Whether to include the raw text from linked exhibits. Only applicable for 8-K filings. When true, exhibit objects will include the 'text' field containing the full exhibit content. default `false` |

## Details

Get SEC Filing Items from Financial Datasets. Returns the official Financial Datasets API response unchanged.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/filings-items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"filing_type": "10-K", "ticker": "AAPL", "year": 2024}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `accession_number` | string | No | The accession number of the filing if 8-K. |
| `filing_type` | string | Yes | The type of filing. |
| `include_exhibits` | boolean | No | Whether to include the raw text from linked exhibits. Only applicable for 8-K filings. When true, exhibit objects will include the 'text' field containing the f |
| `item` | string | No | The item to get. |
| `quarter` | integer | No | The quarter of the filing if 10-Q. |
| `ticker` | string | Yes | The ticker symbol. |
| `year` | integer | Yes | The year of the filing. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/filings-items.json`](../../../catalog/models/financial-datasets/filings-items.json) · Store page: https://www.sandbase.ai/model/financial-datasets/filings-items
