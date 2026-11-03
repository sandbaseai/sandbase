# Weibo Real-Time Search API: pricing, parameters and code examples

`weibo/web-v2/realtime-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search the latest Weibo posts for a keyword, sorted by time: post text, author, publish time and interaction counts.

## Pricing

- **$0.001 per call** (USD)
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

This API returns the latest Weibo posts that match a keyword, newest first. Each post includes the text, author, relative publish time, interaction counts and media links. It needs one input: a search keyword in `query`.

### Use cases

- Watch new posts that mention a brand such as `OpenAI` as they appear.
- Collect fresh posts on a breaking topic for a social listening dashboard.
- Spot new accounts that post about a keyword by reading `user_name` and `user_url`.
- Pull image links from recent posts to review visual coverage of a topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/realtime-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required) |
| `page` | integer | No | Page number (default 1) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "parsed_data": {
    "pagination": {},
    "parse_success": true,
    "result_count": 10,
    "results": [
      {
        "content": "AI早报 2026/11/03:🔹 OpenAI推出LifeVal日常任务评测基准OpenAI发布LifeVal，用于衡量AI协助人们完成日常任务的能力。覆盖找…",
        "interaction": {
          "comment_count": 0,
          "like_count": 0,
          "repost_count": 0
        },
        "media": {
          "has_image": true,
          "has_video": false,
          "images": [
            "https://wx2.sinaimg.cn/large/008DDhL5gy1iip1ud1n8ej30u018e7ek.jpg"
          ],
          "videos": []
        },
        "post_url": "//weibo.com/7914702819/RpFXAafan?refer_flag=1001030103_",
        "publish_time": "34秒前",
        "source": "iPhone 16 Pro",
        "user_avatar": "https://tvax2.sinaimg.cn/crop.0.0.1080.1080.180/008DDhL5ly8ia4ygap5r5j30u00u0q5o…",
        "user_name": "樱花美神",
        "user_nick": "樱花美神",
        "user_url": "//weibo.com/7914702819?refer_flag=1001030103_",
        "weibo_id": "5361194982441583",
        "weibo_type": "original"
      }
    ],
    "search_stats": {}
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `parsed_data.results[].weibo_id` | ID of the post, as a string. Use it to identify the post in your own storage. |
| `parsed_data.results[].content` | Text of the post. Long posts appear cut, and some entries are headline article posts. |
| `parsed_data.results[].publish_time` | Relative publish time as shown on Weibo, such as `34秒前` (34 seconds ago) or `10分钟前` (10 minutes ago). |
| `parsed_data.results[].weibo_type` | Type of the post. The sample posts show `original`. |
| `parsed_data.results[].user_name / parsed_data.results[].user_nick` | Display name of the author. |
| `parsed_data.results[].user_url / parsed_data.results[].post_url` | Links to the author profile and to the post on weibo.com. Both start with `//weibo.com/`. |
| `parsed_data.results[].interaction.comment_count / parsed_data.results[].interaction.like_count / parsed_data.results[].interaction.repost_count` | Number of comments, likes and reposts on the post. |
| `parsed_data.results[].media.has_image / parsed_data.results[].media.has_video` | Flags that show whether the post has images or videos. |
| `parsed_data.results[].media.images[]` | Image URLs attached to the post. The list is empty when the post has no images. |
| `parsed_data.results[].source` | Client or app the author posted from, for example `iPhone 16 Pro` or `微博网页版`. |

### Notes

- Pass `page` to get further result pages. It starts at 1.
- `publish_time` is relative text, not a timestamp. Store the time you made the call if you need to compute an absolute time.
- `parsed_data.result_count` gives the number of posts in the current response.
- To see one post with more detail, call [Weibo Post Detail](/apis/weibo/web-v2/post-detail). To filter by time range or post type, use [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Real-Time Hot Search](/apis/weibo/web-v2/hot-search): Get the Weibo real-time hot search ranking: trending keywords with rank, heat value and labels such as new or hot.
- [Weibo Hot Search List](/apis/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.

---
Machine-readable: [`catalog/models/weibo/web-v2/realtime-search.json`](../../../../catalog/models/weibo/web-v2/realtime-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/realtime-search
