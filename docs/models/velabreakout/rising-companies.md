# Vela Breakout Rising Companies API: pricing, parameters and code examples

`velabreakout/rising-companies` · data API · Vela Breakout · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

List companies growing faster than 90% of peers on two or more measures at once.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "velabreakout/rising-companies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('velabreakout/rising-companies', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("velabreakout/rising-companies", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "velabreakout/rising-companies", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/velabreakout/rising-companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | How many rows to return, 1-25. The price is the same for any limit. range 1–25 |

## Details

List companies growing faster than 90% of peers on two or more measures at once.

---
Machine-readable: [`catalog/models/velabreakout/rising-companies.json`](../../../catalog/models/velabreakout/rising-companies.json) · Store page: https://www.sandbase.ai/model/velabreakout/rising-companies
