# Douyin DOU+ Talent Categories API: pricing, parameters and code examples

`douyin/douplus/talent-categories` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the Douyin DOU+ talent category directory. Use this endpoint to retrieve category hierarchies for talent discovery and promotional workflows.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/talent-categories"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/talent-categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/talent-categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/talent-categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/douplus/talent-categories` with the body above minus `model`.

## Details

Retrieve the Douyin DOU+ talent category list to structure creator categorization without requiring any request parameters.

### Use cases

- Browse the official Douyin DOU+ talent category taxonomy.
- Populate category selector menus in talent discovery tools.
- Group Douyin creators by verified DOU+ content classifications.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/talent-categories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin DOU+ Promotable Items](/apis/douyin/douplus/promotable-item-list): Returns the promotable video item list for a Douyin account on the DOU+ promotion page.
- [Douyin DOU+ User Search](/apis/douyin/douplus/search-user): Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname.
- [Douyin DOU+ Talents by Category](/apis/douyin/douplus/talents-by-category): Returns a list of DOU+ talents filtered by category name or keyword.

---
Machine-readable: [`catalog/models/douyin/douplus/talent-categories.json`](../../../../catalog/models/douyin/douplus/talent-categories.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/talent-categories
