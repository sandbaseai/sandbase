# Weibo Real-Time Hot Search API: pricing, parameters and code examples

`weibo/web-v2/hot-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Get the Weibo real-time hot search ranking: trending keywords with rank, heat value and labels such as new or hot.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/hot-search"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/hot-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/hot-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/hot-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/hot-search` with the body above minus `model`.

## Details

Fetch the current Weibo hot search list with each topic's rank, heat value and label.

### Use cases

- Track trending topics in China.
- Alert when a brand enters the hot list.
- Build trend dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/hot-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "realtime": [
    {
      "label_name": "新",
      "num": 1413832,
      "rank": 0,
      "word": "诺贝尔物理学奖",
      "word_scheme": "诺贝尔物理学奖"
    }
  ]
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Hot Search List](/model/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.
- [Weibo Post Comments](/model/weibo/web-v2/post-comments): Get the first-level comments on a Weibo post: comment text, author, time, likes and reply counts, with cursor pagination.

---
Machine-readable: [`catalog/models/weibo/web-v2/hot-search.json`](../../../../catalog/models/weibo/web-v2/hot-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/hot-search
