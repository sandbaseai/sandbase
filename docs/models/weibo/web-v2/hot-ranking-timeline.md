# Weibo Hot Ranking Timeline API: pricing, parameters and code examples

`weibo/web-v2/hot-ranking-timeline` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns popular posts from Weibo hot rankings based on a specified ranking type. Supports pagination using cursor and identifier parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/hot-ranking-timeline", "count": 10, "max_id": "0", "ranking_type": "hour", "since_id": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/hot-ranking-timeline', {'count': 10, 'max_id': '0', 'ranking_type': 'hour', 'since_id': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/hot-ranking-timeline", {
  "count": 10,
  "max_id": "0",
  "ranking_type": "hour",
  "since_id": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/hot-ranking-timeline", sandbase.Params{
	"count": 10,
	"max_id": "0",
	"ranking_type": "hour",
	"since_id": "0",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/hot-ranking-timeline` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count (default 10) default `10` |
| `max_id` | string |  | Pagination cursor, pass "0" for first request default `"0"` |
| `since_id` | string |  | Pagination identifier, default is 0 default `"0"` |
| `ranking_type` | string | yes | Ranking type (required)  |

## Details

This endpoint retrieves trending Weibo posts for a specified `ranking_type`. Use `count`, `max_id`, and `since_id` to page through ranked timeline entries.

### Use cases

- Monitoring trending topics and top-ranked posts on Weibo in real time.
- Analyzing engagement metrics such as likes and comment volumes on viral content.
- Tracking popular discussions within Weibo super topics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/hot-ranking-timeline" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ranking_type": "hour"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ranking_type` | string | Yes | Ranking type (required) |
| `count` | integer | No | Count (default 10) |
| `max_id` | string | No | Pagination cursor, pass "0" for first request |
| `since_id` | string | No | Pagination identifier, default is 0 |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "statuses": [
    {
      "attitudes_count": 149055,
      "attitudes_status": 0,
      "comments_count": 28209,
      "content_auth": 0,
      "id": 5351100492286270,
      "isLongText": false,
      "mblog_vip_type": 0,
      "mblogtype": 0,
      "mixed_count": 0,
      "pic_num": 1,
      "comment_manage_info": {
        "approval_comment_type": 0,
        "comment_anon_type": 0,
        "comment_permission_type": -1,
        "comment_sort_type": 0
      },
      "number_display_strategy": {
        "display_text": "100万+",
        "display_text_min_number": 1000000
      },
      "title_source": {
        "name": "黄星Eliot超话",
        "url": "https://huati.weibo.com/k/%E9%BB%84%E6%98%9FEliot"
      },
      "user": {
        "following": false,
        "id": 2211239502,
        "mbrank": 2,
        "mbtype": 12,
        "profile_image_url": "https://tvax1.sinaimg.cn/crop.0.0.1080.1080.50/83ccd64ely8hxgoqcpkn1j20u00u0q5f.…",
        "profile_url": "/u/2211239502"
      }
    }
  ]
}
```

### Notes

- Specify the category or timeframe using `ranking_type`.
- Pass "0" to `max_id` on the initial call to start pagination from the beginning.
- Control the number of returned posts per request with `count`, which defaults to 10.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/hot-ranking-timeline.json`](../../../../catalog/models/weibo/web-v2/hot-ranking-timeline.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/hot-ranking-timeline
