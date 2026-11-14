# Channel3 Categories Search API: pricing, parameters and code examples

`channel3/categories-search` · data API · Channel3 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0 per run, depending on parameters · **Modes:** async

Find product categories by keyword or meaning, to filter product searches by slug.

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
  -d '{"model": "channel3/categories-search", "query": "yoga mats"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('channel3/categories-search', {'query': 'yoga mats'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("channel3/categories-search", {
  "query": "yoga mats"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "channel3/categories-search", sandbase.Params{
	"query": "yoga mats",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/channel3/categories-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Results to return, 1-20. Channel3 default: 5. range 1–20 |
| `query` | string | yes | Product type or free text, e.g. 'sofas', 'yoga mats'.  |

## Details

Find product categories by keyword or meaning, to filter product searches by slug.

---
Machine-readable: [`catalog/models/channel3/categories-search.json`](../../../catalog/models/channel3/categories-search.json) · Store page: https://www.sandbase.ai/model/channel3/categories-search
