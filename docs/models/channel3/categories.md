# Channel3 Categories API: pricing, parameters and code examples

`channel3/categories` · data API · Channel3 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0 per run, depending on parameters · **Modes:** async

List product categories page by page, optionally only the top-level ones.

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
  -d '{"model": "channel3/categories"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('channel3/categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("channel3/categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "channel3/categories", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/channel3/categories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-indexed page number. Channel3 default: 1. range 1–9007199254740991 |
| `page_size` | integer |  | Items per page, 1-100. Channel3 default: 20. range 1–100 |
| `roots_only` | boolean |  | true = only top-level categories. Channel3 default: false.  |

## Details

List product categories page by page, optionally only the top-level ones.

---
Machine-readable: [`catalog/models/channel3/categories.json`](../../../catalog/models/channel3/categories.json) · Store page: https://www.sandbase.ai/model/channel3/categories
