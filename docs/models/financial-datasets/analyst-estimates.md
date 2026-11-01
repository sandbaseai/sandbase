# Financial Datasets Get Analyst Estimates

`financial-datasets/analyst-estimates` · api · Financial Datasets

Get Analyst Estimates from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/analyst-estimates"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/analyst-estimates', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/analyst-estimates", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/analyst-estimates", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/analyst-estimates` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | limit  |
| `period` | string |  | period  |
| `ticker` | string |  | ticker  |

## Details

Get Analyst Estimates from Financial Datasets. Returns the official Financial Datasets API response unchanged.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/analyst-estimates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": "2", "period": "annual", "ticker": "AAPL"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | string | No | limit |
| `period` | string | No | period |
| `ticker` | string | No | ticker |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/analyst-estimates.json`](../../../catalog/models/financial-datasets/analyst-estimates.json) · Store page: https://www.sandbase.ai/model/financial-datasets/analyst-estimates
