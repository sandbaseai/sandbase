# Weibo Hot Search List

`weibo/web-v2/hot-search-summary` · api · Weibo

Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.

## Pricing

- **$0.00225 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/hot-search-summary"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/hot-search-summary', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/hot-search-summary", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/hot-search-summary", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/hot-search-summary` with the body above minus `model`.

## Details

Fetch the current Weibo hot search list in one call. Each entry includes its rank, keyword, tag (such as hot or new) and a link to the topic search.

### Use cases

- Track trending topics in China in real time.
- Trigger alerts when a brand enters the hot list.
- Build daily trend reports.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/hot-search-summary" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "total": 52,
  "data": [
    {
      "rank": 3,
      "keyword": "国庆假期返程天气指南",
      "keyword_url": "/weibo?q=%23%E5%9B%BD%E5%BA%86%E5%81%87%E6%9C%9F%E8%BF%94%E7%A8%8B%E5%A4%A9%E6%B0%94%E6%8C%87%E5%8D%97%23&t=31&band_rank=3&Refer=top"
    }
  ]
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Post Detail](/model/weibo/web-v2/post-detail): Get the full data of a single Weibo post by its ID: text (including long posts), author, publish time, location and repost, comment and like counts.
- [Weibo AI Search Content Extension](/model/weibo/web-v2/ai-related-search): Get content extensions related to keyword (related questions, blogger recommendations, reference posts).

---
Machine-readable: [`catalog/models/weibo/web-v2/hot-search-summary.json`](../../../../catalog/models/weibo/web-v2/hot-search-summary.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/hot-search-summary
