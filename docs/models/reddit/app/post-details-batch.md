# Reddit Batch Post Details API: pricing, parameters and code examples

`reddit/app/post-details-batch` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Returns detailed post data for up to five Reddit posts specified by ID. Supports optional comment context and structured data formatting.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/post-details-batch", "post_ids": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/post-details-batch', {'post_ids': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/post-details-batch", {
  "post_ids": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/post-details-batch", sandbase.Params{
	"post_ids": "example",
})
```

Same call via the path form: `POST /v1/api/reddit/app/post-details-batch` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_ids` | string | yes | Post IDs comma-separated, format like "t3_XXXXXX,t3_YYYYYY", max 5 posts  |
| `comment_id` | string |  | Comment ID (used when include_comment_id is True), format like "t1_XXXXXX"  |
| `need_format` | boolean |  | Whether to clean and format the data  |
| `include_comment_id` | boolean |  | Whether to include specific comment ID, default False  |

## Details

Returns detailed data for up to five Reddit posts in one call. You pass the post IDs as a comma-separated string in `post_ids`, such as `t3_1ojnh50,t3_1ok432f`. Each result includes the author, flair, comment count, and status flags for the post.

### Use cases

- Fetch current comment counts and lock status for a short list of posts you already track.
- Check which saved post IDs now return `DeletedSubredditPost` because the post was removed.
- Read the flair text and link domain of several posts to sort them into topics or sources.
- Pull author names and account IDs for a set of posts to build a list of posters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/post-details-batch" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_ids": "t3_1ojnh50,t3_1ok432f,t3_1nwil8j"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_ids` | string | Yes | Post IDs comma-separated, format like "t3_XXXXXX,t3_YYYYYY", max 5 posts |
| `comment_id` | string | No | Comment ID (used when include_comment_id is True), format like "t1_XXXXXX" |
| `include_comment_id` | boolean | No | Whether to include specific comment ID, default False |
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "postsInfoByIds": [
    {
      "__typename": "SubredditPost",
      "attributionInfo": null,
      "authorCommunityBadge": null,
      "authorFlair": null,
      "authorInfo": {
        "__typename": "Redditor",
        "accountType": "USER",
        "iconSmall": {
          "__typename": "MediaSource",
          "dimensions": {
            "height": 50,
            "width": 50
          },
          "url": "https://styles.redditmedia.com/t5_9uhspc/styles/profileIcon_snoo-nftv2_bmZ0X2Vpc…"
        },
        "id": "t2_n5zmzf3v0",
        "isBlocked": false,
        "isCakeDayNow": false,
        "name": "ambachk",
        "newIcon": {
          "__typename": "MediaSource",
          "dimensions": {
            "height": 256,
            "width": 256
          },
          "url": "https://styles.redditmedia.com/t5_9uhspc/styles/profileIcon_snoo-nftv2_bmZ0X2Vpc…"
        }
      },
      "awardings": [
        {
          "__typename": "AwardingTotal",
          "award": {
            "__typename": "Award",
            "id": "award_wholesome_seal",
            "name": "Wholesome Seal",
            "static_icon_16": {
              "__typename": "MediaSource",
              "dimensions": {
                "height": 16,
                "width": 16
              },
              "url": "https://www.redditstatic.com/marketplace-assets/v1/core/awards/wholsome_v1_16.pn…"
            },
            "static_icon_24": {
              "__typename": "MediaSource",
              "dimensions": {
                "height": 24,
                "width": 24
              },
              "url": "https://www.redditstatic.com/marketplace-assets/v1/core/awards/wholsome_v1_24.pn…"
            },
            "static_icon_32": {
              "__typename": "MediaSource",
              "dimensions": {
                "height": 32,
                "width": 32
              },
              "url": "https://www.redditstatic.com/marketplace-assets/v1/core/awards/wholsome_v1_32.pn…"
            },
            "static_icon_48": {
              "__typename": "MediaSource",
              "dimensions": {
                "height": 48,
                "width": 48
              },
              "url": "https://www.redditstatic.com/marketplace-assets/v1/core/awards/wholsome_v1_48.pn…"
            },
            "static_icon_64": {
              "__typename": "MediaSource",
              "dimensions": {
                "height": 64,
                "width": 64
              },
              "url": "https://www.redditstatic.com/marketplace-assets/v1/core/awards/wholsome_v1_64.pn…"
            }
          },
          "total": 1
        }
      ],
      "awardingsInfo": null,
      "commentCount": 11404,
      "content": null,
      "createdAt": "2025-10-30T01:58:59.142000+0000",
      "crosspostRoot": null,
      "crowdControlLevel": "OFF"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `postsInfoByIds[]` | One entry per requested post ID, in the order of the request. Posts that no longer exist come back as an entry with only `__typename` set to `DeletedSubredditPost`. |
| `postsInfoByIds[].__typename` | Type of the entry. `SubredditPost` means the post data is present. `DeletedSubredditPost` means no data is available. |
| `postsInfoByIds[].id` | Post ID in the `t3_` format, for example `t3_1ojnh50`. |
| `postsInfoByIds[].createdAt` | Creation time of the post as an ISO 8601 timestamp with a UTC offset. |
| `postsInfoByIds[].commentCount` | Number of comments on the post. |
| `postsInfoByIds[].authorInfo.name / postsInfoByIds[].authorInfo.id` | Username of the author and the author's account ID in the `t2_` format. |
| `postsInfoByIds[].flair.text` | Text of the post flair, for example `Cringe`. |
| `postsInfoByIds[].domain` | Domain the post links to. The value `v.redd.it` marks a video hosted on Reddit. |
| `postsInfoByIds[].isLocked / postsInfoByIds[].isNsfw / postsInfoByIds[].isSpoiler / postsInfoByIds[].isStickied` | Boolean flags that show whether the post is locked, marked NSFW, marked as a spoiler, or pinned. |
| `postsInfoByIds[].awardings[].award.name / postsInfoByIds[].awardings[].total` | Name of each award on the post and how many times it was given. |

### Notes

- `post_ids` takes up to 5 IDs in the `t3_XXXXXX` format, separated by commas.
- Use `comment_id` in the `t1_XXXXXX` format together with `include_comment_id` set to true to add context for one comment.
- Deleted posts still take a slot in the list, so match results to your request by position and by `id`.
- For comment threads, call [Reddit App Post Comments](/apis/reddit/app/post-comments). For more than five posts, use [Reddit Post Details Large Batch](/apis/reddit/app/post-details-batch-large).

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/post-details-batch.json`](../../../../catalog/models/reddit/app/post-details-batch.json) · Store page: https://www.sandbase.ai/model/reddit/app/post-details-batch
