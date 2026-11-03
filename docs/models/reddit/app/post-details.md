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

Returns metadata for one Reddit post, including the author, flair, awards, lock status and comment count. It needs a `post_id` in the form `t3_XXXXXX`. The result comes back as a list under `postsInfoByIds`.

### Use cases

- Check how many comments a Reddit post has and whether it is locked.
- Read the author's account ID and name for a given post.
- Read the flair text and domain of a post to classify it.
- List the awards a post has received.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/post-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_id": "t3_1ojnh50"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | Yes | Post ID, format like "t3_XXXXXX" |
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
| `postsInfoByIds[]` | List of posts found for the requested ID. A single `post_id` returns one item. |
| `postsInfoByIds[].id` | Post ID in the `t3_XXXXXX` format. |
| `postsInfoByIds[].commentCount` | Number of comments on the post. |
| `postsInfoByIds[].createdAt` | Creation time of the post as an ISO 8601 timestamp with a UTC offset. |
| `postsInfoByIds[].authorInfo.name / postsInfoByIds[].authorInfo.id` | Username of the author and their account ID in the `t2_` format. |
| `postsInfoByIds[].authorInfo.accountType` | Account type of the author, such as `USER`. |
| `postsInfoByIds[].flair.text` | Text of the post flair, for example `Cringe`. |
| `postsInfoByIds[].awardings[].award.name / postsInfoByIds[].awardings[].total` | Name of each award on the post and how many times it was given. |
| `postsInfoByIds[].domain` | Domain the post links to. The value `v.redd.it` marks a Reddit-hosted video. |
| `postsInfoByIds[].isLocked / postsInfoByIds[].isNsfw / postsInfoByIds[].isStickied` | Flags that show if the post is locked, marked NSFW, or stickied. |

### Notes

- Pass `post_id` with the `t3_` prefix, for example `t3_1ojnh50`.
- Set `include_comment_id` to `true` and pass a `comment_id` in the `t1_XXXXXX` format to add comment context.
- To fetch the comments of a post, call [Reddit App Post Comments](/apis/reddit/app/post-comments).
- To look up many posts in one call, use [Reddit Batch Post Details](/apis/reddit/app/post-details-batch).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/post-details.json`](../../../../catalog/models/reddit/app/post-details.json) · Store page: https://www.sandbase.ai/model/reddit/app/post-details
