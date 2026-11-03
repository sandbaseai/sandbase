# Reddit Post Details Large Batch API: pricing, parameters and code examples

`reddit/app/post-details-batch-large` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.025 per call · **Modes:** sync

Returns details for up to 30 Reddit posts in a single request using comma-separated post IDs. Supports optional comment context and formatted output data.

## Pricing

- **$0.025 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/post-details-batch-large", "post_ids": "t3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/post-details-batch-large', {'post_ids': 't3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/post-details-batch-large", {
  "post_ids": "t3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/post-details-batch-large", sandbase.Params{
	"post_ids": "t3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd",
})
```

Same call via the path form: `POST /v1/api/reddit/app/post-details-batch-large` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_ids` | string | yes | Post IDs comma-separated, format like "t3_XXXXXX,t3_YYYYYY,...", max 30 posts  |
| `comment_id` | string |  | Comment ID (used when include_comment_id is True), format like "t1_XXXXXX"  |
| `need_format` | boolean |  | Whether to clean and format the data  |
| `include_comment_id` | boolean |  | Whether to include specific comment ID, default False  |

## Details

Returns details for up to 30 Reddit posts in one request. You pass the post IDs as a comma-separated string in `post_ids`, each with the `t3_` prefix. The response lists one entry per ID, in a `postsInfoByIds` array.

### Use cases

- Pull the comment count, flair and lock status for a list of posts you track.
- Check which posts in a saved list were deleted by looking for `DeletedSubredditPost` entries.
- Collect author names and award totals for a set of posts to compare them.
- Refresh stored metadata for many post IDs with one call instead of one call per post.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/post-details-batch-large" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_ids": "t3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_ids` | string | Yes | Post IDs comma-separated, format like "t3_XXXXXX,t3_YYYYYY,...", max 30 posts |
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
| `postsInfoByIds[]` | One entry per requested post ID. Deleted posts appear as an entry that holds only `__typename`. |
| `postsInfoByIds[].__typename` | Entry type. `SubredditPost` is a live post. `DeletedSubredditPost` is a deleted post with no other fields. |
| `postsInfoByIds[].id` | Post ID with the `t3_` prefix. |
| `postsInfoByIds[].createdAt` | Creation time of the post as an ISO 8601 timestamp with a `+0000` offset. |
| `postsInfoByIds[].commentCount` | Number of comments on the post. |
| `postsInfoByIds[].authorInfo.name / postsInfoByIds[].authorInfo.id` | Username of the post author and the author ID with the `t2_` prefix. |
| `postsInfoByIds[].flair.text` | Text of the post flair, such as `Cringe`. |
| `postsInfoByIds[].awardings[].award.name / postsInfoByIds[].awardings[].total` | Name of each award on the post and how many times it was given. |
| `postsInfoByIds[].domain` | Domain of the linked content, such as `v.redd.it` for Reddit-hosted video. |
| `postsInfoByIds[].isLocked / postsInfoByIds[].isNsfw / postsInfoByIds[].isSelfPost` | Flags for whether the post is locked, marked NSFW, or a text post. |

### Notes

- Build `post_ids` from IDs that start with `t3_`. Separate them with commas and send at most 30.
- Check `__typename` on each entry. A `DeletedSubredditPost` entry has no other fields.
- Set `include_comment_id` to `true` and pass a `t1_` ID in `comment_id` to add a specific comment.
- To read the comments of a post, call [Reddit App Post Comments](/apis/reddit/app/post-comments). For a single post, use [Reddit Post Details](/apis/reddit/app/post-details).

### Pricing

$0.025 per successful call. Failed calls are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/post-details-batch-large.json`](../../../../catalog/models/reddit/app/post-details-batch-large.json) · Store page: https://www.sandbase.ai/model/reddit/app/post-details-batch-large
