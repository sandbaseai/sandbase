# US Census Explore Variables API: pricing, parameters and code examples

`censusdata-xyz/explore-variables` · data API · US Census · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0 per run, depending on parameters · **Modes:** async

Discover which US Census variables exist for a topic keyword.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0 |

Formula: `0`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "censusdata-xyz/explore-variables", "keyword": "income"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('censusdata-xyz/explore-variables', {'keyword': 'income'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("censusdata-xyz/explore-variables", {
  "keyword": "income"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "censusdata-xyz/explore-variables", sandbase.Params{
	"keyword": "income",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/censusdata-xyz/explore-variables` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | A topic keyword to search the Census variable catalog for (e.g. 'veterans', 'income', 'commute', 'broadband'). Returns matching variables, descriptions, and suggested natural-language queries.  |

## Details

Discover which US Census variables exist for a topic keyword.

---
Machine-readable: [`catalog/models/censusdata-xyz/explore-variables.json`](../../../catalog/models/censusdata-xyz/explore-variables.json) · Store page: https://www.sandbase.ai/model/censusdata-xyz/explore-variables
