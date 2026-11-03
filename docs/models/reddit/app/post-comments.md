# Reddit App Post Comments API: pricing, parameters and code examples

`reddit/app/post-comments` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comment trees for a specific Reddit post by its ID. Supports comment sorting by hot, new, top, best, or controversial, with optional pagination via a cursor.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/post-comments", "after": "", "need_format": false, "post_id": "t3_1ojnvca", "sort_type": "CONFIDENCE"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/post-comments', {'after': '', 'need_format': False, 'post_id': 't3_1ojnvca', 'sort_type': 'CONFIDENCE'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/post-comments", {
  "after": "",
  "need_format": false,
  "post_id": "t3_1ojnvca",
  "sort_type": "CONFIDENCE"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/post-comments", sandbase.Params{
	"after": "",
	"need_format": false,
	"post_id": "t3_1ojnvca",
	"sort_type": "CONFIDENCE",
})
```

Same call via the path form: `POST /v1/api/reddit/app/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `after` | string |  | Pagination parameter for fetching the next page, can be found in the last comment node in commentForest, e.g., $.data.postInfoById.commentForest.trees[-1].more.cursor default `""` |
| `post_id` | string | yes | Post ID, format like "t3_XXXXXX"  |
| `sort_type` | string |  | Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL default `"CONFIDENCE"` |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |

## Details

Returns the comment tree for one Reddit post, including each comment's author, text, timestamp, depth and reply count. It needs a `post_id` in the form `t3_XXXXXX`. You can choose the comment sort order and page through the results.

### Use cases

- Collect the top comments under a popular post to study how a community reacts to a news event.
- Pull the newest comments with `sort_type` set to `NEW` to monitor a live thread.
- Build a dataset of comment text and author names for sentiment analysis on one post.
- Check which comments come from moderators or bots using the `distinguishedAs` field.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_id": "t3_1ojnvca"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | Yes | Post ID, format like "t3_XXXXXX" |
| `after` | string | No | Pagination parameter for fetching the next page, can be found in the last comment node in commentForest, e.g., $.data.postInfoById.commentForest.trees[-1].more.cursor |
| `need_format` | boolean | No | Whether to clean and format the data |
| `sort_type` | string | No | Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "postInfoById": {
    "__typename": "SubredditPost",
    "commentCount": 1905,
    "commentForest": {
      "__typename": "CommentForest",
      "pageInfo": {
        "commentCount": 1802,
        "hasNextPage": true
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
                "url": "https://styles.redditmedia.com/t5_1yz875/styles/profileIcon_klqlly9fc4l41.png?wi…"
              },
              "id": "t2_6l4z3",
              "isBlocked": false,
              "isCakeDayNow": false,
              "isPremiumAvatarTreatment": true,
              "name": "AutoModerator"
            },
            "commentStats": null,
            "content": {
              "__typename": "Content",
              "markdown": "It looks like this post is about Politics. Various methods of filtering out cont…",
              "preview": "It looks like this post is about Politics. Various methods of filtering out cont…",
              "richtext": "{\"document\":[{\"c\":[{\"e\":\"text\",\"t\":\"It looks like this post is about Politics. V…",
              "richtextMedia": [],
              "translationInfo": {
                "isTranslated": false,
                "translatedLanguage": null
              },
              "typeHint": "TEXT"
            },
            "createdAt": "2025-10-30T02:17:24.998000+0000",
            "distinguishedAs": "MODERATOR"
          },
          "parentId": null
        }
      ]
    },
    "id": "t3_1ojnvca",
    "subreddit": {
      "allowedMediaInComments": [
        "GIPHY"
      ],
      "id": "t5_2qh0u",
      "isQuarantined": false,
      "moderation": {
        "isShowCommentRemovalReasonPrompt": true
      },
      "name": "pics",
      "prefixedName": "r/pics",
      "tippingStatus": null
    },
    "title": "Official photo of Trump-Xi meeting in Busan, South Korea"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `postInfoById.title` | Title of the post the comments belong to. |
| `postInfoById.commentCount` | Total comment count for the post. |
| `postInfoById.commentForest.pageInfo.hasNextPage` | `true` when more comments can be fetched with another page request. |
| `postInfoById.commentForest.pageInfo.commentCount` | Comment count reported for the forest in this response. |
| `postInfoById.commentForest.trees[].depth` | Nesting level of the comment. `0` is a top-level comment, `1` is a reply to it, and so on. |
| `postInfoById.commentForest.trees[].childCount` | Number of replies under this comment. |
| `postInfoById.commentForest.trees[].parentId` | ID of the parent comment, such as `t1_nm4jkk6`. It is `null` for top-level comments. |
| `postInfoById.commentForest.trees[].node.authorInfo.name / postInfoById.commentForest.trees[].node.authorInfo.id` | Username and user ID (format `t2_...`) of the comment author. |
| `postInfoById.commentForest.trees[].node.content.markdown / postInfoById.commentForest.trees[].node.content.preview` | Comment text as Markdown and as a short plain-text preview. |
| `postInfoById.commentForest.trees[].node.createdAt / postInfoById.commentForest.trees[].node.distinguishedAs` | ISO 8601 creation time of the comment, and a label such as `MODERATOR` when the comment is distinguished. The label is `null` otherwise. |

### Notes

- Pass `post_id` with the `t3_` prefix, for example `t3_1ojnvca`.
- `sort_type` accepts `HOT`, `NEW`, `TOP`, `BEST` and `CONTROVERSIAL`. The default is `CONFIDENCE`.
- When `hasNextPage` is `true`, take the cursor from the last item in `commentForest.trees[]` (its `more.cursor` value) and send it as `after`.
- To load the replies under a single comment, call [Reddit App Comment Replies](/apis/reddit/app/comment-replies). For the post itself, use [Reddit Post Details](/apis/reddit/app/post-details).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/post-comments.json`](../../../../catalog/models/reddit/app/post-comments.json) · Store page: https://www.sandbase.ai/model/reddit/app/post-comments
