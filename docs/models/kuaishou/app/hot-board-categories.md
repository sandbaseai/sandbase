# Kuaishou Hot Board Categories API: pricing, parameters and code examples

`kuaishou/app/hot-board-categories` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the active list of hot board categories available in the Kuaishou app. Use this endpoint to inspect category identifiers and names for trending content rankings.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/hot-board-categories"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/hot-board-categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/hot-board-categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/hot-board-categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/hot-board-categories` with the body above minus `model`.

## Details

Retrieves the available trending board categories from the Kuaishou application without requiring any input parameters.

### Use cases

- Discover available category classifications for trending Kuaishou content.
- Map category identifiers before querying specific trending leaderboards.
- Populate category navigation menus in social media analytics tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/hot-board-categories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Detail](/apis/kuaishou/app/hot-board-detail): Returns trending topics and search keywords from Kuaishou hot boards based on the specified board identifier and board type.

---
Machine-readable: [`catalog/models/kuaishou/app/hot-board-categories.json`](../../../../catalog/models/kuaishou/app/hot-board-categories.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/hot-board-categories
