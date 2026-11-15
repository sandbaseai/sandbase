# H&M New Arrivals API: pricing, parameters and code examples

`hm/new-arrivals` · data API · H&M · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetch new arrivals for a category. Returns recently added products with pricing and availability. Uses the same listing mechanism as category pages but scoped to new arrivals sections.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hm/new-arrivals"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hm/new-arrivals', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hm/new-arrivals", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hm/new-arrivals", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/hm/new-arrivals` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination (1-based). default `1` |
| `category` | string |  | New arrivals category path (e.g. 'women/new-arrivals/view-all', 'men/new-arrivals/view-all'). default `"men/new-arrivals/view-all"` |

## Details

Fetch new arrivals for a category. Returns recently added products with pricing and availability. Uses the same listing mechanism as category pages but scoped to new arrivals sections.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "hm/new-arrivals", "page": 1, "category": "men/new-arrivals/view-all"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | New arrivals category path (e.g. 'women/new-arrivals/view-all', 'men/new-arrivals/view-all'). |
| `page` | integer | No | Page number for pagination (1-based). |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hm/new-arrivals.json`](../../../catalog/models/hm/new-arrivals.json) · Store page: https://www.sandbase.ai/model/hm/new-arrivals
