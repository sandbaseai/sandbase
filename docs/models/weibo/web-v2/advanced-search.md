# Weibo Advanced Search API: pricing, parameters and code examples

`weibo/web-v2/advanced-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links). Returns post text, author, time and engagement.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/advanced-search", "page": 1, "q": "华为 高通 专利许可协议", "search_type": "hot", "timescope": "custom:2026-09-30-0:2026-10-07-9"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/advanced-search', {'page': 1, 'q': '华为 高通 专利许可协议', 'search_type': 'hot', 'timescope': 'custom:2026-09-30-0:2026-10-07-9'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/advanced-search", {
  "page": 1,
  "q": "华为 高通 专利许可协议",
  "search_type": "hot",
  "timescope": "custom:2026-09-30-0:2026-10-07-9"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/advanced-search", sandbase.Params{
	"page": 1,
	"q": "华为 高通 专利许可协议",
	"search_type": "hot",
	"timescope": "custom:2026-09-30-0:2026-10-07-9",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/advanced-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Search keyword (required)  |
| `page` | integer |  | Page number (default 1) default `1` |
| `timescope` |  |  | Time scope (format: custom:start_date:end_date, e.g. custom:2025-09-01-0:2025-09-08-23)  |
| `search_type` |  |  | Search type (all/hot/original/verified/media/viewpoint)  |
| `include_type` |  |  | Include type (all/pic/video/music/link)  |

## Details

Search Weibo for a keyword and narrow the results by time range, post type and content type. Each result includes the post text, author, publish time, link and interaction counts.

### Use cases

- Monitor brand or product mentions on Weibo.
- Collect posts about an event within a custom date range.
- Find original or verified-account posts on a topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/advanced-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Search keyword (required) |
| `page` | integer | No | Page number (default 1) |
| `timescope` | string | No | Time scope (format: custom:start_date:end_date, e.g. custom:2025-09-01-0:2025-09-08-23) |
| `search_type` | string | No | Search type (all/hot/original/verified/media/viewpoint) |
| `include_type` | string | No | Include type (all/pic/video/music/link) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "parsed_data": {
    "result_count": 19,
    "results": [
      {
        "weibo_id": "5350554563773695",
        "content": "OpenAI Codex 承诺连续 28 天：每天上新，否则重置额度OpenAI 给 Codex 用户立了个 28 天的规矩：每天要么上线一项多数人用得上的明…",
        "publish_time": "10月05日 07:04",
        "user_nick": "<user>",
        "post_url": "//weibo.com/1727858283/Rld9CfPI3",
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

- `timescope` format: `custom:YYYY-MM-DD-H:YYYY-MM-DD-H`, e.g. `custom:2025-09-01-0:2025-09-08-23`.
- Use `page` to paginate.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Hot Search List](/model/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.
- [Weibo Post Detail](/model/weibo/web-v2/post-detail): Get the full data of a single Weibo post by its ID: text (including long posts), author, publish time, location and repost, comment and like counts.
- [Weibo AI Search Content Extension](/model/weibo/web-v2/ai-related-search): Get content extensions related to keyword (related questions, blogger recommendations, reference posts).

---
Machine-readable: [`catalog/models/weibo/web-v2/advanced-search.json`](../../../../catalog/models/weibo/web-v2/advanced-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/advanced-search
