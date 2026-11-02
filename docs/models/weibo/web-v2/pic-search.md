# Weibo Picture Search API: pricing, parameters and code examples

`weibo/web-v2/pic-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns picture content and associated post details matching a search query on Weibo. Results include image URLs, post text, and user profile information.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/pic-search", "page": 1, "query": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/pic-search', {'page': 1, 'query': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/pic-search", {
  "page": 1,
  "query": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/pic-search", sandbase.Params{
	"page": 1,
	"query": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/pic-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (default 1) default `1` |
| `query` | string | yes | Search keyword (required)  |

## Details

Look up Weibo images and associated post metadata based on a specified `query`. Supports pagination through the optional `page` parameter.

### Use cases

- Search for Weibo images matching specific keywords or brand terms.
- Collect media assets and post text for social sentiment analysis.
- Track visual content shared by users around current events.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/pic-search" \
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
  "pic_list": [
    {
      "forward_id": 0,
      "sub_name": "郑总i",
      "sub_text": "AMD首席执行官苏姿丰表示，当前AI芯片市场需求...",
      "text": "AMD首席执行官苏姿丰表示，当前AI芯片市场需求非常旺盛，就算AMD持续提升产能，市场需求依旧大于供给。并表示公司后续将会持续大幅扩产，加码AI加速芯片、服务器CPU的产能投放。…",
      "url": "//wx3.sinaimg.cn/thumb180/bbd55d63gy1ihswq5iaauj20u00ehjvc.jpg",
      "user": {
        "name": "郑总i",
        "profile_image_url": "//tvax2.sinaimg.cn/crop.0.0.1080.1080.50/bbd55d63ly8i3xfxp27klj20u00u0gp1.jpg?KID=imgbed,…",
        "profile_url": "//weibo.com/zhengbinqiang"
      }
    }
  ]
}
```

### Notes

- Paginate results using `page`, which defaults to 1.
- The `query` parameter is required.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/pic-search.json`](../../../../catalog/models/weibo/web-v2/pic-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/pic-search
