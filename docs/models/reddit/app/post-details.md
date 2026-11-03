# Reddit Post Details API: pricing, parameters and code examples

`reddit/app/post-details` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a Reddit post by ID, including engagement metrics, author info, and subreddit data. Supports optional comment context.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/post-details", "comment_id": "", "include_comment_id": false, "need_format": false, "post_id": "t3_1ojnh50"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/post-details', {'comment_id': '', 'include_comment_id': False, 'need_format': False, 'post_id': 't3_1ojnh50'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/post-details", {
  "comment_id": "",
  "include_comment_id": false,
  "need_format": false,
  "post_id": "t3_1ojnh50"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/post-details", sandbase.Params{
	"comment_id": "",
	"include_comment_id": false,
	"need_format": false,
	"post_id": "t3_1ojnh50",
})
```

Same call via the path form: `POST /v1/api/reddit/app/post-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_id` | string | yes | Post ID, format like "t3_XXXXXX"  |
| `comment_id` | string |  | Comment ID (used when include_comment_id is True), format like "t1_XXXXXX" default `""` |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `include_comment_id` | boolean |  | Whether to include specific comment ID, default False default `false` |

## Details

Retrieve comprehensive metadata and metrics for a Reddit submission using `post_id`. You can also supply `comment_id` to focus on specific comment context.

### Use cases

- Retrieve submission engagement metrics including score and comment count.
- Inspect subreddit and author details for a specific Reddit post.
- Access post permalinks and outbound link metadata by post ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/post-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_id": "t3_1ojnh50"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | Yes | Post ID, format like "t3_XXXXXX" |
| `comment_id` | string | No | Comment ID (used when include_comment_id is True), format like "t1_XXXXXX" |
| `need_format` | boolean | No | Whether to clean and format the data |
| `include_comment_id` | boolean | No | Whether to include specific comment ID, default False |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "postsInfoByIds": [
    {
      "__typename": "SubredditPost",
      "commentCount": 11406,
      "id": "t3_1ojnh50",
      "isAuthorBlocked": false,
      "isScoreHidden": false,
      "permalink": "/r/TikTokCringe/comments/1ojnh50/removed_by_moderator/",
      "postTitle": "[ Removed by moderator ]",
      "removedByCategory": "MODERATOR",
      "score": 33358,
      "url": "https://www.reddit.com/r/TikTokCringe/comments/1ojnh50/removed_by_moderator/",
      "authorInfo": {
        "__typename": "Redditor",
        "accountType": "USER",
        "id": "t2_n5zmzf3v0",
        "name": "ambachk"
      },
      "flair": {
        "__typename": "PostFlair",
        "text": "Cringe",
        "type": "text"
      },
      "outboundLink": {
        "url": "https://www.reddit.com/r/TikTokCringe/comments/1ojnh50/removed_by_moderator/"
      },
      "subreddit": {
        "__typename": "Subreddit",
        "id": "t5_mvcq5",
        "isTitleSafe": true,
        "name": "TikTokCringe",
        "prefixedName": "r/TikTokCringe",
        "subscribersCount": 5640715.0
      }
    }
  ]
}
```

### Notes

- `post_id` format follows the pattern `t3_XXXXXX`.
- `comment_id` uses the pattern `t1_XXXXXX` when `include_comment_id` is set to true.
- Set `need_format` to true to clean and format the returned data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/post-details.json`](../../../../catalog/models/reddit/app/post-details.json) · Store page: https://www.sandbase.ai/model/reddit/app/post-details
