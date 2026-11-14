# Vela Breakout Company API: pricing, parameters and code examples

`velabreakout/company` · data API · Vela Breakout · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** async

Get every measured growth signal for one company by name or web domain.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "velabreakout/company", "name_or_domain": "supabase.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('velabreakout/company', {'name_or_domain': 'supabase.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("velabreakout/company", {
  "name_or_domain": "supabase.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "velabreakout/company", sandbase.Params{
	"name_or_domain": "supabase.com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/velabreakout/company` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `name_or_domain` | string | yes | The company's name (e.g. 'Supabase') or web domain (e.g. 'supabase.com'), 2-120 characters. A domain is the surest match.  |

## Details

Get every measured growth signal for one company by name or web domain.

---
Machine-readable: [`catalog/models/velabreakout/company.json`](../../../catalog/models/velabreakout/company.json) · Store page: https://www.sandbase.ai/model/velabreakout/company
