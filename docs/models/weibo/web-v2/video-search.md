# Weibo Video Search API: pricing, parameters and code examples

`weibo/web-v2/video-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches Weibo video posts by keyword with sorting options for popular or all results, returning matching posts, user details, and engagement counts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/video-search", "query": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/video-search', {'query': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/video-search", {
  "query": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/video-search", sandbase.Params{
	"query": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/video-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mode` | string |  | Search mode hot=popular / all=all (default hot) default `"hot"` |
| `page` | integer |  | Page number (default 1) default `1` |
| `query` | string | yes | Search keyword (required)  |

## Details

Look up video content on Weibo matching a search `query`. Supports filtering by `mode` for either popular or all videos, with pagination via `page`.

### Use cases

- Track video posts related to specific brand or topic keywords.
- Discover popular video content on Weibo across different categories.
- Analyze engagement metrics for video posts matching targeted search queries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/video-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required) |
| `mode` | string | No | Search mode hot=popular / all=all (default hot) |
| `page` | integer | No | Page number (default 1) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "parsed_data": {
    "results": [
      {
        "content": "徐振轩超话对了那天说的臭豆腐火锅还可，油呛牛肉好吃！！#振在输入中…##十一休time#​",
        "post_url": "//weibo.com/5676102465/RlrmVtkxi?refer_flag=1001030103_",
        "publish_time": "今天19:15",
        "user_name": "<user>",
        "user_url": "<user>",
        "weibo_id": "5351100976990456",
        "weibo_type": "original",
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

### Notes

- Set `mode` to `hot` for popular results or `all` to return all videos (defaults to `hot`).
- Use `page` to paginate through search results (defaults to 1).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/video-search.json`](../../../../catalog/models/weibo/web-v2/video-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/video-search
