# Weibo Real-Time Search API: pricing, parameters and code examples

`weibo/web-v2/realtime-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Search the latest Weibo posts for a keyword, sorted by time: post text, author, publish time and interaction counts.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/realtime-search", "page": 1, "query": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/realtime-search', {'page': 1, 'query': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/realtime-search", {
  "page": 1,
  "query": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/realtime-search", sandbase.Params{
	"page": 1,
	"query": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/realtime-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (default 1) default `1` |
| `query` | string | yes | Search keyword (required)  |

## Details

Search Weibo for a keyword and get the newest matching posts first.

### Use cases

- Real-time brand and crisis monitoring.
- Track breaking discussion on a topic.
- Feed social listening dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/realtime-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required) |
| `page` | integer | No | Page number (default 1) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "parsed_data": {
    "results": [
      {
        "weibo_id": "5351092588119068",
        "content": "OpenAI发布了textGrain文本水印技术，走的是\"非默认、API用户自选开启\"路线——不改动原文内容，只嵌入人…",
        "publish_time": "6分钟前",
        "weibo_type": "original",
        "user_name": "<user>",
        "interaction": {
          "comment_count": 0,
          "like_count": 0,
          "repost_count": 0
        }
      }
    ]
  }
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Real-Time Hot Search](/model/weibo/web-v2/hot-search): Get the Weibo real-time hot search ranking: trending keywords with rank, heat value and labels such as new or hot.
- [Weibo Hot Search List](/model/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.

---
Machine-readable: [`catalog/models/weibo/web-v2/realtime-search.json`](../../../../catalog/models/weibo/web-v2/realtime-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/realtime-search
