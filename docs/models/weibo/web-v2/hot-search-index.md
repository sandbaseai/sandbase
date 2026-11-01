# Weibo Hot Search Index

`weibo/web-v2/hot-search-index` · api · Weibo

Returns the top 10 hot search ranking items currently trending on Weibo. It delivers active search topics without requiring any input parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/hot-search-index"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/hot-search-index', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/hot-search-index", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/hot-search-index", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/hot-search-index` with the body above minus `model`.

## Details

Look up the top 10 hot search topics on Weibo. This endpoint does not require any request parameters.

### Use cases

- Track currently trending topics across Weibo.
- Display real-time hot search rankings in a media monitoring dashboard.
- Analyze popular cultural and news trends among Weibo users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/hot-search-index" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/hot-search-index.json`](../../../../catalog/models/weibo/web-v2/hot-search-index.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/hot-search-index
