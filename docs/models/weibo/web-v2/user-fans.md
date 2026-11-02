# Weibo User Follower List API: pricing, parameters and code examples

`weibo/web-v2/user-fans` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a paginated list of accounts following a specified Weibo user profile by ID, including follower metrics and profile summaries.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-fans", "uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-fans', {'uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-fans", {
  "uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-fans", sandbase.Params{
	"uid": "example",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-fans` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `page` | integer |  | Page number, starts from 0 (default 0)  |

## Details

Retrieve the list of followers for any target account by specifying `uid` and an optional `page` number.

### Use cases

- Inspect follower profiles and audience composition for a specific Weibo account.
- Browse paginated lists of users who follow an influencer or brand profile.
- Extract engagement statistics and follower counts for audience analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-fans" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `page` | integer | No | Page number, starts from 0 (default 0) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "users": [
    {
      "auth_status": 1,
      "bi_followers_count": 132,
      "block_word": 1,
      "brand_account": 0,
      "credit_score": 80,
      "delete_mode_time": 0,
      "description": "教授新手使用微博方法专业户，每天推荐方法介绍、微博热点...有问题请call我，@、私信都可以，欢迎骚扰~",
      "favourites_count": 2643,
      "followers_count": 165078910,
      "followers_count_str": "1.65亿",
      "insecurity": {
        "sexual_content": false
      },
      "status_total_counter": {
        "comment_cnt": 3906988,
        "comment_like_cnt": 376936,
        "like_cnt": 19747921,
        "repost_cnt": 7908170,
        "total_cnt": 31940015
      },
      "video_total_counter": {
        "play_cnt": 147182632
      }
    }
  ]
}
```

### Notes

- `page` starts from 0 and defaults to 0.
- `uid` is required to specify the target user account.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-fans.json`](../../../../catalog/models/weibo/web-v2/user-fans.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-fans
