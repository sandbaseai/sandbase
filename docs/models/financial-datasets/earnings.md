# Financial Datasets Get Earnings Data

`financial-datasets/earnings` · api · Financial Datasets

Get the most recent earnings snapshot for a ticker. Optional change fields are returned only when available.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/earnings", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/earnings', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/earnings", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/earnings", sandbase.Params{
	"ticker": "AAPL",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/earnings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of most-recent report periods worth of filings to return, sorted by `(report_period DESC, filing_date ASC)`. The number of entries returned may exceed `limit` when a recent period has both an 8-K and a 10-Q /… default `1`; range 1–40 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `ticker` | string | yes | The ticker symbol (e.g. `AAPL`).  |

## Details

Get the most recent earnings snapshot for a ticker. Optional change fields are returned only when available.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/earnings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL", "limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original reques |
| `limit` | integer | No | Number of most-recent report periods worth of filings to return, sorted by `(report_period DESC, filing_date ASC)`. The number of entries returned may exceed `l |
| `ticker` | string | Yes | The ticker symbol (e.g. `AAPL`). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/earnings.json`](../../../catalog/models/financial-datasets/earnings.json) · Store page: https://www.sandbase.ai/model/financial-datasets/earnings
