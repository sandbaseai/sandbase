# Reddit App Comment Replies API: pricing, parameters and code examples

`reddit/app/comment-replies` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor. Supports custom sorting methods and data formatting options.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/comment-replies", "cursor": "commenttree:ex:(RjiJd", "post_id": "t3_1qmup73"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/comment-replies', {'cursor': 'commenttree:ex:(RjiJd', 'post_id': 't3_1qmup73'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/comment-replies", {
  "cursor": "commenttree:ex:(RjiJd",
  "post_id": "t3_1qmup73"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/comment-replies", sandbase.Params{
	"cursor": "commenttree:ex:(RjiJd",
	"post_id": "t3_1qmup73",
})
```

Same call via the path form: `POST /v1/api/reddit/app/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string | yes | Comment cursor from the more.cursor field in comment data, format like "commenttree:ex:(xxx)"  |
| `post_id` | string | yes | Post ID, format like "t3_XXXXXX"  |
| `sort_type` | string |  | Sort method, supports CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM  |
| `need_format` | boolean |  | Whether to clean and format the data  |

## Details

Returns the replies under one collapsed Reddit comment thread, plus basic info about the parent post and subreddit. It needs a `post_id` and a `cursor` taken from the `more.cursor` field of a comment tree.

### Use cases

- Expand a "load more replies" branch from a long Reddit thread to read the hidden comments.
- Collect reply text and author names for sentiment analysis on one discussion branch.
- Rebuild a full comment tree by following each reply back to its parent with `parentId`.
- Check which replies come from distinguished accounts, such as moderators.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cursor": "commenttree:ex:(RjiJd", "post_id": "t3_1qmup73"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | Yes | Comment cursor from the more.cursor field in comment data, format like "commenttree:ex:(xxx)" |
| `post_id` | string | Yes | Post ID, format like "t3_XXXXXX" |
| `need_format` | boolean | No | Whether to clean and format the data |
| `sort_type` | string | No | Sort method, supports CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "postInfoById": {
    "__typename": "SubredditPost",
    "commentCount": 3048,
    "commentForest": {
      "__typename": "CommentForest",
      "pageInfo": {
        "commentCount": 5,
        "hasNextPage": false
      },
      "trees": [
        {
          "childCount": 0,
          "depth": 0,
          "more": null,
          "node": {
            "__typename": "Comment",
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
                "url": "https://styles.redditmedia.com/t5_p96kp/styles/profileIcon_a0kdvkgnwc7c1.jpeg?wi…"
              },
              "id": "t2_236f6ttn",
              "isBlocked": false,
              "isCakeDayNow": false,
              "isPremiumAvatarTreatment": false,
              "name": "welfedad"
            },
            "commentStats": null,
            "content": {
              "__typename": "Content",
              "markdown": "Looks like an eye booger or am I missing something",
              "preview": "Looks like an eye booger or am I missing something",
              "richtext": "{\"document\":[{\"c\":[{\"e\":\"text\",\"t\":\"Looks like an eye booger or am I missing som…",
              "richtextMedia": [],
              "translationInfo": {
                "isTranslated": false,
                "translatedLanguage": null
              },
              "typeHint": "TEXT"
            },
            "createdAt": "2026-01-26T05:47:01.149000+0000",
            "distinguishedAs": null
          },
          "parentId": "t1_o1q99np"
        }
      ]
    },
    "id": "t3_1qmup73",
    "subreddit": {
      "allowedMediaInComments": [
        "GIPHY"
      ],
      "id": "t5_2qhta",
      "isQuarantined": false,
      "moderation": {
        "isShowCommentRemovalReasonPrompt": true
      },
      "name": "cats",
      "prefixedName": "r/cats",
      "tippingStatus": null
    },
    "title": "We found this poor little kitten in the woods, covered in ice, with her fur stuc…"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `postInfoById.title / postInfoById.id` | Title and ID of the post the replies belong to. The ID uses the `t3_` prefix. |
| `postInfoById.commentCount` | Total number of comments on the post, not only the replies in this response. |
| `postInfoById.commentForest.trees[]` | List of reply nodes returned for the cursor. Each item holds one comment in `node`. |
| `postInfoById.commentForest.trees[].node.content.markdown / postInfoById.commentForest.trees[].node.content.preview` | Text of the comment. `markdown` holds the full comment text and `preview` holds a short version. |
| `postInfoById.commentForest.trees[].node.authorInfo.name / postInfoById.commentForest.trees[].node.authorInfo.id` | Username and account ID of the comment author. The ID uses the `t2_` prefix. |
| `postInfoById.commentForest.trees[].node.createdAt` | Time the comment was posted, as an ISO 8601 timestamp with a `+0000` offset. |
| `postInfoById.commentForest.trees[].parentId` | ID of the parent comment, with the `t1_` prefix. |
| `postInfoById.commentForest.trees[].childCount / postInfoById.commentForest.trees[].depth` | Number of child replies under this comment and its depth value in the tree. |
| `postInfoById.commentForest.trees[].more` | Set when more replies are collapsed under this node. It is `null` when nothing more is hidden. |
| `postInfoById.commentForest.pageInfo.hasNextPage` | Tells you whether more replies are available after this page. |
| `postInfoById.subreddit.prefixedName` | Subreddit name with the `r/` prefix, for example `r/cats`. |

### Notes

- Take `cursor` from the `more.cursor` field of a comment tree item. It looks like `commenttree:ex:(xxx)`. Get the top-level comments first with [Reddit App Post Comments](/apis/reddit/app/post-comments).
- `post_id` must include the `t3_` prefix, for example `t3_1qmup73`.
- `sort_type` accepts `CONFIDENCE`, `NEW`, `TOP`, `HOT`, `CONTROVERSIAL`, `OLD` or `RANDOM`.
- If `hasNextPage` is `true`, or a node has a non-null `more`, use its cursor in a new call to get the rest.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.
- [Reddit Search](/apis/reddit/app/dynamic-search): Search Reddit posts, communities, comments, media and users with the Reddit app search.

---
Machine-readable: [`catalog/models/reddit/app/comment-replies.json`](../../../../catalog/models/reddit/app/comment-replies.json) · Store page: https://www.sandbase.ai/model/reddit/app/comment-replies
