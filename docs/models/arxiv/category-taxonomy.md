# arXiv Category Taxonomy API: pricing, parameters and code examples

`arxiv/category-taxonomy` · data API · arXiv · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Browse the full arXiv category taxonomy organized by discipline groups. Each group contains categories with their ID, name, and description. Optionally filter to a single group by name. Returns all groups when no filter is specified.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "arxiv/category-taxonomy"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('arxiv/category-taxonomy', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("arxiv/category-taxonomy", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "arxiv/category-taxonomy", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/arxiv/category-taxonomy` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `group` | string |  | Filter by group name (e.g., Computer Science, Physics, Mathematics, Quantitative Biology, Quantitative Finance, Statistics, Electrical Engineering and Systems Science, Economics). Returns all groups if not specified.  |

## Details

Browse the full arXiv category taxonomy organized by discipline groups. Each group contains categories with their ID, name, and description. Optionally filter to a single group by name. Returns all groups when no filter is specified.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "arxiv/category-taxonomy", "group": "Computer Science"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `group` | string | No | Filter by group name (e.g., Computer Science, Physics, Mathematics, Quantitative Biology, Quantitative Finance, Statistics, Electrical Engineering and Systems Science, Economics). Returns all groups if not specified. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/arxiv/category-taxonomy.json`](../../../catalog/models/arxiv/category-taxonomy.json) · Store page: https://www.sandbase.ai/model/arxiv/category-taxonomy
