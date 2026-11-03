# Weibo Topic Search API: pricing, parameters and code examples

`weibo/web-v2/topic-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches Weibo topics matching a keyword and returns topic names, URLs, discussion counts, and read metrics across paginated results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/topic-search", "query": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/topic-search', {'query': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/topic-search", {
  "query": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/topic-search", sandbase.Params{
	"query": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/topic-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (default 1) default `1` |
| `query` | string | yes | Search keyword (required)  |

## Details

This API searches Weibo topics that match a keyword. It returns each topic's hashtag name, search URL, discussion count, read count, cover image and a short description. It needs a `query` keyword and accepts an optional `page` number.

### Use cases

- Find hashtags that Weibo users have created around a brand or product name such as `OpenAI`.
- Rank topics for a keyword by `read_count` or `discuss_count` to see which hashtags draw the most attention.
- Collect topic URLs to open the matching Weibo search page for each hashtag.
- Compare how many topics exist for several competing keywords by checking `parsed_data.count`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/topic-search" \
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
    "count": 19,
    "items": [
      {
        "cover": {
          "large": "https://wx1.sinaimg.cn/large/0024cZx9ly8hqa409rwgkj6050050wej02.jpg",
          "thumb": "https://wx1.sinaimg.cn/thumb180/0024cZx9ly8hqa409rwgkj6050050wej02.jpg"
        },
        "desc": null,
        "discuss_count": 78000,
        "read_count": 110000000,
        "topic": {
          "name": "#openai#",
          "name_plain": "openai",
          "url": "https://s.weibo.com/weibo/%23openai%23"
        }
      }
    ],
    "parse_success": true
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `parsed_data.count` | Number of topic items in this response. |
| `parsed_data.items[].topic.name` | Topic hashtag as written on Weibo, wrapped in `#` characters. |
| `parsed_data.items[].topic.name_plain` | Topic name without the `#` characters. |
| `parsed_data.items[].topic.url` | Weibo search URL for the topic. |
| `parsed_data.items[].discuss_count` | Discussion count for the topic. For example, `78000` for `#openai#`. |
| `parsed_data.items[].read_count` | Read count for the topic. For example, `110000000` for `#openai#`. |
| `parsed_data.items[].desc` | Short text description of the topic. It is `null` when the topic has none. |
| `parsed_data.items[].cover.large / parsed_data.items[].cover.thumb` | Image URLs for the topic cover, in a large and a thumbnail version. |
| `parsed_data.parse_success` | Shows `true` when the response was parsed into the fields above. |

### Notes

- `query` is required. Use any keyword, in English or Chinese.
- Send `page` to get further results. It starts at `1`.
- `desc` can be `null`, so check for it before you display it.
- To search posts instead of topics, call [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/topic-search.json`](../../../../catalog/models/weibo/web-v2/topic-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/topic-search
