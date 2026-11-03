# Zhihu Recommended Followees API: pricing, parameters and code examples

`zhihu/web/recommend-followees` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of recommended users to follow on Zhihu. Access personalized author and contributor suggestions directly from Zhihu web.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/recommend-followees"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/recommend-followees', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/recommend-followees", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/recommend-followees", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/zhihu/web/recommend-followees` with the body above minus `model`.

## Details

Access recommended Zhihu users to follow through this web endpoint. It returns suggested profiles without requiring request parameters.

### Use cases

- Discover active and relevant Zhihu creators to track.
- Populate user onboarding screens with suggested accounts.
- Analyze suggested network connections and top platform contributors.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/recommend-followees" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/recommend-followees.json`](../../../../catalog/models/zhihu/web/recommend-followees.json) · Store page: https://www.sandbase.ai/model/zhihu/web/recommend-followees
