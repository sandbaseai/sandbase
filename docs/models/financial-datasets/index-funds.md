# Financial Datasets ETF and Index Fund Holdings API: pricing, parameters and code examples

`financial-datasets/index-funds` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Holdings of an ETF or index fund by ticker, with fund name, asset class, net assets and each holding's weight.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/index-funds", "ticker": "SPY"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/index-funds', {'ticker': 'SPY'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/index-funds", {
  "ticker": "SPY"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/index-funds", sandbase.Params{
	"ticker": "SPY",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/index-funds` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | ETF or index fund ticker, e.g. `SPY`.  |

## Details

Holdings of an ETF or index fund by ticker, with fund name, asset class, net assets and each holding's weight.

The result is returned in `outputs[0].data` as the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/index-funds" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "SPY"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | ETF or index fund ticker, e.g. `SPY`. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/index-funds.json`](../../../catalog/models/financial-datasets/index-funds.json) · Store page: https://www.sandbase.ai/model/financial-datasets/index-funds
