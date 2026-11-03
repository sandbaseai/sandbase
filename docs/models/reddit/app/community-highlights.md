# Reddit Community Highlights API: pricing, parameters and code examples

`reddit/app/community-highlights` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID. Supports optional response data formatting.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/community-highlights", "need_format": false, "subreddit_id": "t5_2qh0u"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/community-highlights', {'need_format': False, 'subreddit_id': 't5_2qh0u'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/community-highlights", {
  "need_format": false,
  "subreddit_id": "t5_2qh0u"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/community-highlights", sandbase.Params{
	"need_format": false,
	"subreddit_id": "t5_2qh0u",
})
```

Same call via the path form: `POST /v1/api/reddit/app/community-highlights` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `subreddit_id` | string | yes | Subreddit ID starting with "t5_", can be obtained from fetch_subreddit_info endpoint  |

## Details

Returns the posts a moderator has highlighted in a subreddit, such as announcements and contest threads. It needs a `subreddit_id` that starts with `t5_`. The response includes the subreddit ID and name plus each highlighted post's text, flair, author icon and comment count.

### Use cases

- Show a subreddit's pinned announcements on a community dashboard.
- Track which contest or event threads a subreddit's moderators highlight.
- Read the markdown text of highlighted posts to archive subreddit announcements.
- Check the flair and comment count of highlighted threads to see how active they are.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/community-highlights" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit_id": "t5_2qh0u"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit_id` | string | Yes | Subreddit ID starting with "t5_", can be obtained from fetch_subreddit_info endpoint |
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "subredditInfoById": {
    "__typename": "Subreddit",
    "highlightedPosts": [
      {
        "expiresAt": null,
        "label": null,
        "post": {
          "__typename": "SubredditPost",
          "authorInfo": {
            "__typename": "Redditor",
            "icon": {
              "url": "https://styles.redditmedia.com/t5_3kici/styles/profileIcon_snooc32509c3-18e5-4c1…"
            }
          },
          "commentCount": 92,
          "content": {
            "markdown": "**It's a Halloween Photo Contest!**\n\nPost your best costume, carved pumpkin, spo…",
            "richtext": "{\"document\":[{\"c\":[{\"e\":\"text\",\"f\":[[1,0,31]],\"t\":\"It's a Halloween Photo Contes…"
          },
          "createdAt": "2026-10-14T22:48:30.525000+0000",
          "devvit": null,
          "flair": {
            "__typename": "PostFlair",
            "richtext": null,
            "template": {
              "backgroundColor": null,
              "id": "f988392c-41f4-11ea-856e-0e3f43166111",
              "isEditable": false
            },
            "text": "Judging in progress...",
            "textColor": "DARK",
            "type": "text"
          },
          "id": "t3_1x65iks"
        }
      }
    ],
    "id": "t5_2qh0u",
    "modPermissions": null,
    "name": "pics"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `subredditInfoById.id / subredditInfoById.name` | The ID of the subreddit (`t5_2qh0u`) and its name (`pics`). |
| `subredditInfoById.highlightedPosts[]` | The list of highlighted posts. Each item wraps one post in its `post` object. |
| `subredditInfoById.highlightedPosts[].post.id` | The post ID, in the form `t3_1x65iks`. |
| `subredditInfoById.highlightedPosts[].post.content.markdown` | The post body as markdown text. |
| `subredditInfoById.highlightedPosts[].post.content.richtext` | The post body as a rich text document in a JSON string. |
| `subredditInfoById.highlightedPosts[].post.commentCount` | The number of comments on the post. |
| `subredditInfoById.highlightedPosts[].post.createdAt` | When the post was created, as an ISO 8601 timestamp with a `+0000` offset. |
| `subredditInfoById.highlightedPosts[].post.flair.text` | The text of the post flair, for example `Judging in progress...`. |
| `subredditInfoById.highlightedPosts[].post.authorInfo.icon.url` | The URL of the author's profile icon image. |
| `subredditInfoById.highlightedPosts[].expiresAt / subredditInfoById.highlightedPosts[].label` | Expiry time and label of the highlight. Both are `null` in this response. |

### Notes

- Get `subreddit_id` from [Reddit App Subreddit Info](/apis/reddit/app/subreddit-info). It starts with `t5_`.
- Set `need_format` to `true` to clean and format the response data. It defaults to `false`.
- Post IDs start with `t3_`. To read a full post, call [Reddit Post Details](/apis/reddit/app/post-details).
- To list regular posts from the same subreddit, call [Reddit Subreddit Feed](/apis/reddit/app/subreddit-feed).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Search](/apis/reddit/app/dynamic-search): Search Reddit posts, communities, comments, media and users with the Reddit app search.

---
Machine-readable: [`catalog/models/reddit/app/community-highlights.json`](../../../../catalog/models/reddit/app/community-highlights.json) · Store page: https://www.sandbase.ai/model/reddit/app/community-highlights
