# Finviz Market Movers API: pricing, parameters and code examples

`finviz/market-movers` · data API · Finviz · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** async

List today's US stock market movers on Finviz such as top gainers, top losers, new highs and unusual volume, with price, change and volume.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "finviz/market-movers"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('finviz/market-movers', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("finviz/market-movers", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "finviz/market-movers", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/finviz/market-movers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mover_type` | string |  | Type of market mover list to retrieve.  |

## Details

List today's US stock market movers on Finviz such as top gainers, top losers, new highs and unusual volume, with price, change and volume.

---
Machine-readable: [`catalog/models/finviz/market-movers.json`](../../../catalog/models/finviz/market-movers.json) · Store page: https://www.sandbase.ai/model/finviz/market-movers
