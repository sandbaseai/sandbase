# Financial Datasets Get Financial Metrics Snapshot API: pricing, parameters and code examples

`financial-datasets/financial-metrics-snapshot` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get the real-time financial metrics snapshot for a stock, including valuation ratios, profitability, efficiency, liquidity, leverage, growth, and per share metrics.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/financial-metrics-snapshot"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/financial-metrics-snapshot', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/financial-metrics-snapshot", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/financial-metrics-snapshot", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/financial-metrics-snapshot` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cik` | string |  | The Central Index Key (CIK) of the company. Can be used instead of ticker.  |
| `isin` | string |  | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`.  |
| `market` | string |  | market one of: `UK`, `US` |
| `ticker` | string |  | The ticker symbol of the company.  |
| `exchange` | string |  | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class, returns the company's metrics. Price-based values (market… one of: `LSE` |

## Details

Get the real-time financial metrics snapshot for a stock, including valuation ratios, profitability, efficiency, liquidity, leverage, growth, and per share metrics.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/financial-metrics-snapshot" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cik` | string | No | The Central Index Key (CIK) of the company. Can be used instead of ticker. |
| `exchange` | string | No | The exchange the ticker is listed on. Omit for US listings. Use `LSE` for the London Stock Exchange; any ticker of the company, including a second share class,  |
| `isin` | string | No | The ISIN (International Securities Identification Number) of a non-US listing. An alternative to `ticker` and `exchange`. |
| `market` | string | No | market |
| `ticker` | string | No | The ticker symbol of the company. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/financial-metrics-snapshot.json`](../../../catalog/models/financial-datasets/financial-metrics-snapshot.json) · Store page: https://www.sandbase.ai/model/financial-datasets/financial-metrics-snapshot
