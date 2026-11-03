# Weibo Post Comments API: pricing, parameters and code examples

`weibo/web-v2/post-comments` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the first-level comments on a Weibo post: comment text, author, time, likes and reply counts, with cursor pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/post-comments", "id": "5350554563773695"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/post-comments', {'id': '5350554563773695'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/post-comments", {
  "id": "5350554563773695"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/post-comments", sandbase.Params{
	"id": "5350554563773695",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Weibo post ID (required)  |
| `count` | integer |  | Number of comments (default 10) default `10` |
| `max_id` | string |  | Pagination cursor, pass empty for first request, use returned max_id for subsequent requests default `""` |

## Details

Pass a Weibo post ID and get its comments, page by page.

### Use cases

- Analyze reactions to a post.
- Collect customer feedback.
- Monitor comments on brand posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "5350554563773695"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Weibo post ID (required) |
| `count` | integer | No | Number of comments (default 10) |
| `max_id` | string | No | Pagination cursor, pass empty for first request, use returned max_id for subsequent requests |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "max_id": "<max_id>",
  "total_number": 34,
  "data": [
    {
      "id": 5350555695188006,
      "created_at": "Mon Oct 05 07:09:09 +0800 2026",
      "like_counts": 7,
      "total_number": 3,
      "source": "来自 上海",
      "text_raw": "也就是28天每天要么上新一个新功能/重置一次吗？ 还挺好的！[打call]刚开了Pro会员又可以尽…",
      "user": {
        "screen_name": "<user>"
      }
    }
  ]
}
```

### Notes

- Paginate with `max_id` from the previous response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Real-Time Hot Search](/apis/weibo/web-v2/hot-search): Get the Weibo real-time hot search ranking: trending keywords with rank, heat value and labels such as new or hot.
- [Weibo Hot Search List](/apis/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.

---
Machine-readable: [`catalog/models/weibo/web-v2/post-comments.json`](../../../../catalog/models/weibo/web-v2/post-comments.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/post-comments
