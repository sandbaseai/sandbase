# Channel3 Brands API: pricing, parameters and code examples

`channel3/brands` · data API · Channel3 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0 per run, depending on parameters · **Modes:** async

List top brands, optionally only those selling given categories, with cursor paging.

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
  -d '{"model": "channel3/brands"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('channel3/brands', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("channel3/brands", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "channel3/brands", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/channel3/brands` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Items per page, 1-100. Channel3 default: 20. range 1–100 |
| `cursor` | string |  | next_cursor from the previous page's output; omit for the first page.  |
| `category_ids` | array |  | Only those selling in these categories, by category slug (from category search). Matches within each category's top 1,000.  |

## Details

List top brands, optionally only those selling given categories, with cursor paging.

---
Machine-readable: [`catalog/models/channel3/brands.json`](../../../catalog/models/channel3/brands.json) · Store page: https://www.sandbase.ai/model/channel3/brands
