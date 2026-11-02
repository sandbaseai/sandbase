# Zhihu Search Recommendations API: pricing, parameters and code examples

`zhihu/web/search-recommend` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns recommended search queries and trending suggestions from Zhihu Web. Helps discover popular topics and keywords without providing input search criteria.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/search-recommend"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/search-recommend', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/search-recommend", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/search-recommend", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/zhihu/web/search-recommend` with the body above minus `model`.

## Details

Returns trending search suggestions and keyword recommendations from the Zhihu Web interface without requiring input query parameters.

### Use cases

- Display trending search topics in Zhihu discovery interfaces.
- Analyze popular search suggestions for keyword research.
- Provide auto-suggested topics on search entry pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/search-recommend" \
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
Machine-readable: [`catalog/models/zhihu/web/search-recommend.json`](../../../../catalog/models/zhihu/web/search-recommend.json) · Store page: https://www.sandbase.ai/model/zhihu/web/search-recommend
