# Kroger Search API: pricing, parameters and code examples

`kroger/search` · data API · Kroger · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Search Kroger grocery products by keyword with price, size and product URL; pass a store ID for local pricing and stock.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kroger/search", "query": "milk"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kroger/search', {'query': 'milk'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kroger/search", {
  "query": "milk"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kroger/search", sandbase.Params{
	"query": "milk",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/kroger/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Only the first result page is currently supported. range 1–1 |
| `query` | string | yes | Product keywords to search for.  |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |
| `store_id` | string |  | Retailer's store ID. Selects the store catalog, pricing or availability where the retailer exposes it.  |

## Details

Search Kroger grocery products by keyword with price, size and product URL; pass a store ID for local pricing and stock.

---
Machine-readable: [`catalog/models/kroger/search.json`](../../../catalog/models/kroger/search.json) · Store page: https://www.sandbase.ai/model/kroger/search
