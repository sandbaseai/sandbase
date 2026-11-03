# Weibo User Posts API: pricing, parameters and code examples

`weibo/web-v2/user-posts` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the posts published by a Weibo user: text, publish time, images, videos and repost, comment and like counts, with pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-posts", "uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-posts', {'uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-posts", {
  "uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-posts", sandbase.Params{
	"uid": "example",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `page` | integer |  | Page number, starts from 1 (default 1)  |
| `feature` | integer |  | Data feature value (default 0)  |
| `since_id` | string |  | Pagination identifier for next page  |

## Details

Pass a Weibo user ID and get that account's posts with engagement metrics, page by page.

### Use cases

- Monitor official accounts and media.
- Analyze content performance of an account.
- Archive posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "2803301701"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `page` | integer | No | Page number, starts from 1 (default 1) |
| `feature` | integer | No | Data feature value (default 0) |
| `since_id` | string | No | Pagination identifier for next page |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "since_id": "<since_id>",
    "list": [
      {
        "id": 5348998178410235,
        "created_at": "Thu Oct 01 00:00:08 +0800 2026",
        "reposts_count": 825698,
        "comments_count": 19113,
        "attitudes_count": 103953,
        "text_raw": "【此刻，转发接力：#我爱你中国#[心]】#庆祝新中国成立77周年#，今天共同传递：惟愿山河锦绣、国泰民安！祝福伟大祖国…",
        "user": {
          "id": 2803301701,
          "screen_name": "人民日报"
        }
      }
    ]
  }
}
```

### Notes

- Paginate with `page` or `since_id` from the previous response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Real-Time Hot Search](/apis/weibo/web-v2/hot-search): Get the Weibo real-time hot search ranking: trending keywords with rank, heat value and labels such as new or hot.
- [Weibo Hot Search List](/apis/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-posts.json`](../../../../catalog/models/weibo/web-v2/user-posts.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-posts
