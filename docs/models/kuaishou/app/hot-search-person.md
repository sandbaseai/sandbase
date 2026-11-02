# Kuaishou Hot Search Person Board API: pricing, parameters and code examples

`kuaishou/app/hot-search-person` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the current Kuaishou hot search person board rankings. Delivers real-time trending individuals and popular figures featured across the platform.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/hot-search-person"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/hot-search-person', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/hot-search-person", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/hot-search-person", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/hot-search-person` with the body above minus `model`.

## Details

Retrieves the current trending individuals leaderboard from the Kuaishou app hot search person board without requiring input parameters.

### Use cases

- Track trending personalities and influencers on Kuaishou in real time.
- Analyze shifts in celebrity and creator popularity across the platform.
- Identify viral figures for social media monitoring and talent research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/hot-search-person" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/hot-search-person.json`](../../../../catalog/models/kuaishou/app/hot-search-person.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/hot-search-person
