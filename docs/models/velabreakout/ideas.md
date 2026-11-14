# Vela Breakout Ideas API: pricing, parameters and code examples

`velabreakout/ideas` · data API · Vela Breakout · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

List AI research ideas gaining or losing share of new papers, with who publishes on each.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "velabreakout/ideas", "direction": "rising"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('velabreakout/ideas', {'direction': 'rising'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("velabreakout/ideas", {
  "direction": "rising"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "velabreakout/ideas", sandbase.Params{
	"direction": "rising",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/velabreakout/ideas` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | How many rows to return, 1-25. The price is the same for any limit. range 1–25 |
| `direction` | string | yes | 'rising' for ideas gaining share of new AI research papers, 'fading' for ideas losing it. one of: `rising`, `fading` |

## Details

List AI research ideas gaining or losing share of new papers, with who publishes on each.

---
Machine-readable: [`catalog/models/velabreakout/ideas.json`](../../../catalog/models/velabreakout/ideas.json) · Store page: https://www.sandbase.ai/model/velabreakout/ideas
