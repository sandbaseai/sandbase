# Finviz Insider Trading API: pricing, parameters and code examples

`finviz/insider-trading` · data API · Finviz · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** async

List recent insider transactions in US stocks from Finviz with insider, relationship, transaction type, shares, price and value, filtered by minimum value.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "finviz/insider-trading"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('finviz/insider-trading', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("finviz/insider-trading", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "finviz/insider-trading", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/finviz/insider-trading` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `min_value` | integer |  | Minimum transaction value in USD. Transactions with Value ($) below this threshold are excluded from results. range -9007199254740991–9007199254740991 |

## Details

List recent insider transactions in US stocks from Finviz with insider, relationship, transaction type, shares, price and value, filtered by minimum value.

---
Machine-readable: [`catalog/models/finviz/insider-trading.json`](../../../catalog/models/finviz/insider-trading.json) · Store page: https://www.sandbase.ai/model/finviz/insider-trading
