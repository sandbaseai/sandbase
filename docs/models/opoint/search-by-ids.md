# Opoint Search By Ids API: pricing, parameters and code examples

`opoint/search-by-ids` · data API · Opoint · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.06 per call · **Modes:** async

Fetch specific articles by their site and article id pairs.

## Pricing

- **$0.06 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "opoint/search-by-ids", "params": "<params>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('opoint/search-by-ids', {'params': '<params>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("opoint/search-by-ids", {
  "params": "<params>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "opoint/search-by-ids", sandbase.Params{
	"params": "<params>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/opoint/search-by-ids` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `params` | object | yes |   |

## Details

Fetch specific articles by their site and article id pairs.

---
Machine-readable: [`catalog/models/opoint/search-by-ids.json`](../../../catalog/models/opoint/search-by-ids.json) · Store page: https://www.sandbase.ai/model/opoint/search-by-ids
