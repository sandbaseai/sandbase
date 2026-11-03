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

Searches Weibo video posts by keyword and returns matching posts with the post text, author details, video stream URLs, and like, comment and repost counts. It needs one input: `query`. You can also set `mode` and `page`.

### Use cases

- Collect Weibo video posts that mention a brand or product name such as `OpenAI`.
- Download or preview the video files attached to posts on a topic using the stream URLs.
- Find which accounts post videos about a keyword and link to their profile pages.
- Compare popular and all results for the same keyword by switching `mode`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/video-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required) |
| `mode` | string | No | Search mode hot=popular / all=all (default hot) |
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
        "content": "#OpenAI接连发生AI失控事件#【接连发生失控事件，OpenAI再次暂停其最先进模型训练】#OpenAI暂停新模型训练#当地时间9月26日获悉，美国开放人工…",
        "interaction": {
          "comment_count": 0,
          "like_count": 0,
          "repost_count": 0
        },
        "media": {
          "has_image": false,
          "has_video": true,
          "images": [],
          "videos": [
            {
              "fid": "1034:5347747881222210",
              "page_url": "sinaweibo://gotovideo?selected_containerid=231557_2024_1&is_url_decode=1&source=…",
              "src": "https://f.video.weibocdn.com/o0/kRf4Oa4Ilx08B7KhD6LC010412006GwY0E010.mp4?label=…",
              "streams": [
                "https://f.video.weibocdn.com/o0/kRf4Oa4Ilx08B7KhD6LC010412006GwY0E010.mp4?label=…"
              ],
              "type": "video"
            }
          ]
        },
        "post_url": "//weibo.com/2318910945/Rk1oY1UG2?refer_flag=1001030103_",
        "publish_time": "09月27日 11:19",
        "source": "微博视频号",
        "user_avatar": "https://tvax3.sinaimg.cn/crop.0.0.450.450.180/002wVUFrly8h8vgt7mcs2j60ci0ci0t002…",
        "user_name": "新浪热点",
        "user_nick": "新浪热点",
        "user_url": "//weibo.com/2318910945?refer_flag=1001030103_",
        "weibo_id": "5347719520456198",
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
| `parsed_data.results[].content` | Post text. Long posts are cut and may end with an ellipsis or a expand marker. |
| `parsed_data.results[].weibo_id` | ID of the post as a numeric string. |
| `parsed_data.results[].post_url` | Link to the post on weibo.com. It starts with `//` and has no scheme. |
| `parsed_data.results[].publish_time` | Publish time as display text, for example `10月09日 19:27`. It has no year. |
| `parsed_data.results[].user_name / user_nick` | Display name of the author. |
| `parsed_data.results[].user_url / user_avatar` | Link to the author's Weibo profile and to the author's avatar image. |
| `parsed_data.results[].interaction.like_count / comment_count / repost_count` | Engagement counts for the post. |
| `parsed_data.results[].media.videos[].src` | URL of the main video file for the post. |
| `parsed_data.results[].media.videos[].streams` | List of video file URLs at different quality levels. The `label` in each URL names the quality, such as `mp4_720p` or `mp4_hd`. |
| `parsed_data.results[].weibo_type` | Type of post. The sample results show `original`. |

### Notes

- The video URLs carry an `Expires` value in the query string, so download them soon after the call.
- `mode` accepts `hot` for popular results or `all` for all results. The default is `hot`.
- Use `page` to move through results. In the sample response `parsed_data.pagination` is empty, so step the page number yourself.
- To get full details for one post, pass its `weibo_id` to [Weibo Post Detail](/apis/weibo/web-v2/post-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/video-search.json`](../../../../catalog/models/weibo/web-v2/video-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/video-search
