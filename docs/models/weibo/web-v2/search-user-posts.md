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

Returns posts from one Weibo user's timeline that match optional keywords. It needs the user's `uid` and accepts filters for post type and a Unix timestamp date range.

### Use cases

- Find every post where a Weibo creator mentions a brand or product name.
- Pull only the video or image posts from one account for content review.
- Collect an account's posts for a set time window by passing `starttime` and `endtime`.
- Check whether a user has posted about a topic by testing if `data.total` is above zero.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/search-user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `endtime` | string | No | End timestamp (optional, Unix timestamp format) |
| `hasmusic` | integer | No | Include music posts (default 1 include) |
| `hasori` | integer | No | Include original posts (default 1 include) |
| `haspic` | integer | No | Include image posts (default 1 include) |
| `hasret` | integer | No | Include retweets (default 1 include) |
| `hastext` | integer | No | Include text posts (default 1 include) |
| `hasvideo` | integer | No | Include video posts (default 1 include) |
| `page` | integer | No | Page number, starts from 1 (default 1) |
| `q` | string | No | Search keyword (optional, empty string means search all content) |
| `starttime` | string | No | Start timestamp (optional, Unix timestamp format) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "list": [],
    "total": 0
  },
  "ok": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `ok` | Status flag for the call. A value of `1` means the request went through. |
| `data.list` | List of matching posts for the requested page. It is an empty list when nothing matches, as in the sample call. |
| `data.total` | Count of posts that match the query and filters. It is `0` in the sample response, which has no matches. |

### Notes

- Get the `uid` from a user lookup such as [Weibo User Search](/apis/weibo/web-v2/user-search) or [Weibo User Basic Information](/apis/weibo/web-v2/user-basic-info).
- Use `page` to move through results. It starts at 1.
- An empty `data.list` with `data.total` of `0` means no posts matched the current `q`, type flags and time range.
- To list an account's posts without a keyword search, use [Weibo User Posts](/apis/weibo/web-v2/user-posts).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/search-user-posts.json`](../../../../catalog/models/weibo/web-v2/search-user-posts.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/search-user-posts
