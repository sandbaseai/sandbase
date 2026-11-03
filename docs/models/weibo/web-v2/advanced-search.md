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

Returns Weibo posts that match a keyword. Each result has the post text, author, publish time, post link, media and interaction counts. The only required input is the search keyword `q`. You can narrow results with time range, post type and content type filters.

### Use cases

- Track mentions of a brand or product such as OpenAI on Weibo.
- Collect posts about an event inside a custom date range.
- Pull only original or verified-account posts on a topic.
- Gather image or video posts about a keyword and read their media URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/advanced-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Search keyword (required) |
| `include_type` | string | No | Include type (all/pic/video/music/link) |
| `page` | integer | No | Page number (default 1) |
| `search_type` | string | No | Search type (all/hot/original/verified/media/viewpoint) |
| `timescope` | string | No | Time scope (format: custom:start_date:end_date, e.g. custom:2025-09-01-0:2025-09-08-23) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "parsed_data": {
    "pagination": {},
    "parse_success": true,
    "result_count": 21,
    "results": [
      {
        "content": "nice，dsh可以接openai ​​​​",
        "interaction": {
          "comment_count": 0,
          "like_count": 0,
          "repost_count": 0
        },
        "media": {
          "has_image": true,
          "has_video": false,
          "images": [
            "https://wx4.sinaimg.cn/large/005BSIfegy1iiox5o7o5dj313g0g478w.jpg"
          ],
          "videos": []
        },
        "post_url": "//weibo.com/5140428384/RpERF7Wch?refer_flag=1001030103_",
        "publish_time": "今天12:58",
        "source": "微博网页版",
        "user_avatar": "https://tvax1.sinaimg.cn/crop.0.0.828.828.180/005BSIfely8gsohng3cyuj30n00n0wfd.j…",
        "user_name": "北漂民工的日常",
        "user_nick": "北漂民工的日常",
        "user_url": "//weibo.com/5140428384?refer_flag=1001030103_",
        "weibo_id": "5361152871892009",
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
| `parsed_data.results[].content` | Text of the post. |
| `parsed_data.results[].weibo_id` | ID of the post. Use it to look up the post in other Weibo APIs. |
| `parsed_data.results[].publish_time` | Publish time as shown on Weibo, such as `今天12:58` or `10月31日 16:45`. It is a display string, not a full timestamp. |
| `parsed_data.results[].user_name / user_nick` | Display name of the author. |
| `parsed_data.results[].user_url / post_url` | Links to the author profile and to the post. Both start with `//weibo.com/`. |
| `parsed_data.results[].interaction.comment_count / like_count / repost_count` | Number of comments, likes and reposts on the post. |
| `parsed_data.results[].media.has_image / has_video` | Flags that show whether the post carries images or videos. |
| `parsed_data.results[].media.images[] / media.videos[].src` | Image URLs and video file URLs. Each video also lists alternate quality links in `streams`. |
| `parsed_data.results[].weibo_type` | Type label of the post, such as `original`. |
| `parsed_data.result_count` | Number of posts in this response. |

### Notes

- Set `page` to get further result pages. The default is 1.
- Write `timescope` as `custom:YYYY-MM-DD-H:YYYY-MM-DD-H`, for example `custom:2025-09-01-0:2025-09-08-23`.
- `search_type` accepts `all`, `hot`, `original`, `verified`, `media` or `viewpoint`. `include_type` accepts `all`, `pic`, `video`, `music` or `link`.
- Pass a `weibo_id` to [Weibo Post Detail](/apis/weibo/web-v2/post-detail) for the full post data.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Hot Search List](/apis/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.
- [Weibo Post Detail](/apis/weibo/web-v2/post-detail): Get the full data of a single Weibo post by its ID: text (including long posts), author, publish time, location and repost, comment and like counts.
- [Weibo AI Search Content Extension](/apis/weibo/web-v2/ai-related-search): Get content extensions related to keyword (related questions, blogger recommendations, reference posts).

---
Machine-readable: [`catalog/models/weibo/web-v2/advanced-search.json`](../../../../catalog/models/weibo/web-v2/advanced-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/advanced-search
