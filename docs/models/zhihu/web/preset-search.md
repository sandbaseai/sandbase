# Zhihu Preset Search API: pricing, parameters and code examples

`zhihu/web/preset-search` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves preset search recommendations and default placeholder queries from Zhihu Web. Returns trending search terms without requiring input parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/preset-search"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/preset-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/preset-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/preset-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/zhihu/web/preset-search` with the body above minus `model`.

## Details

Retrieves default preset search keywords and trending recommendations from Zhihu Web without requiring any request parameters.

### Use cases

- Display default search box placeholder queries in Zhihu integrations.
- Discover trending keywords currently promoted on the Zhihu search interface.
- Track changes in default suggested search terms over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/preset-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/preset-search.json`](../../../../catalog/models/zhihu/web/preset-search.json) · Store page: https://www.sandbase.ai/model/zhihu/web/preset-search
