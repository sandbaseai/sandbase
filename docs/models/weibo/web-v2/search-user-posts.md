# Weibo User Post Search API: pricing, parameters and code examples

`weibo/web-v2/search-user-posts` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns posts from a specified Weibo user matching optional search keywords. Supports filtering by post types such as images, videos, and retweets, as well as date ranges.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/search-user-posts", "uid": "8431518763"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/search-user-posts', {'uid': '8431518763'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/search-user-posts", {
  "uid": "8431518763"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/search-user-posts", sandbase.Params{
	"uid": "8431518763",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/search-user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Search keyword (optional, empty string means search all content)  |
| `uid` | string | yes | User ID (required)  |
| `page` | integer |  | Page number, starts from 1 (default 1)  |
| `hasori` | integer |  | Include original posts (default 1 include)  |
| `haspic` | integer |  | Include image posts (default 1 include)  |
| `hasret` | integer |  | Include retweets (default 1 include)  |
| `endtime` |  |  | End timestamp (optional, Unix timestamp format)  |
| `hastext` | integer |  | Include text posts (default 1 include)  |
| `hasmusic` | integer |  | Include music posts (default 1 include)  |
| `hasvideo` | integer |  | Include video posts (default 1 include)  |
| `starttime` |  |  | Start timestamp (optional, Unix timestamp format)  |

## Details

Search posts from a specific Weibo account using `uid`. Filter results by keyword with `q`, media format flags, and Unix timestamp bounds.

### Use cases

- Search a specific Weibo creator timeline for keyword or brand mentions.
- Filter an account post history by media type such as images or videos.
- Retrieve user posts within a specific time range using timestamps.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/search-user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `q` | string | No | Search keyword (optional, empty string means search all content) |
| `page` | integer | No | Page number, starts from 1 (default 1) |
| `hasori` | integer | No | Include original posts (default 1 include) |
| `haspic` | integer | No | Include image posts (default 1 include) |
| `hasret` | integer | No | Include retweets (default 1 include) |
| `endtime` | string | No | End timestamp (optional, Unix timestamp format) |
| `hastext` | integer | No | Include text posts (default 1 include) |
| `hasmusic` | integer | No | Include music posts (default 1 include) |
| `hasvideo` | integer | No | Include video posts (default 1 include) |
| `starttime` | string | No | Start timestamp (optional, Unix timestamp format) |

### Notes

- `uid` is required, while `q` can be left empty to return all content.
- Pagination is handled with `page`, which defaults to 1.
- Date filters `starttime` and `endtime` accept Unix timestamps.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/search-user-posts.json`](../../../../catalog/models/weibo/web-v2/search-user-posts.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/search-user-posts
