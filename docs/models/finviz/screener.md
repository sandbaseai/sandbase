# Finviz Stock Screener API: pricing, parameters and code examples

`finviz/screener` · data API · Finviz · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** async

Screen US stocks on Finviz with filter codes for valuation, performance, technicals and fundamentals, returning matching tickers with price, change, market cap and key ratios.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "finviz/screener"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('finviz/screener', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("finviz/screener", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "finviz/screener", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/finviz/screener` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `filters` | string |  | Comma-separated Finviz filter codes (e.g. 'fa_peg_u1' for PEG under 1, 'ta_sma200_pc5' for price within 5% of SMA200). Codes follow the Finviz URL parameter format visible in screener URLs.  |

## Details

Screen US stocks on Finviz with filter codes for valuation, performance, technicals and fundamentals, returning matching tickers with price, change, market cap and key ratios.

---
Machine-readable: [`catalog/models/finviz/screener.json`](../../../catalog/models/finviz/screener.json) · Store page: https://www.sandbase.ai/model/finviz/screener
