# Reddit User Comments API: pricing, parameters and code examples

`reddit/app/user-comments` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of comments submitted by a specified Reddit user. Supports multiple sorting options, customizable page sizes, and pagination tokens.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/user-comments", "username": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/user-comments', {'username': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/user-comments", {
  "username": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/user-comments", sandbase.Params{
	"username": "example",
})
```

Same call via the path form: `POST /v1/api/reddit/app/user-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial)  |
| `after` | string |  | Pagination parameter for fetching next page  |
| `username` | string | yes | Reddit username  |
| `page_size` | integer |  | Number of comments per page, default 25  |
| `need_format` | boolean |  | Whether to clean and format the data  |

## Details

Returns a page of comments written by one Reddit user, each with its text preview, score, creation time and the post it was made on. The only required input is `username`, and you can add `sort`, `page_size` and `after` to control the list.

### Use cases

- Pull the latest comments from an executive account such as `spez` to track public statements.
- Find the posts and subreddits where a user comments most often.
- Compare comment `score` values to spot the most upvoted or downvoted replies from a profile.
- Page through a user's full comment history and store it for moderation or research review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/user-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username |
| `after` | string | No | Pagination parameter for fetching next page |
| `need_format` | boolean | No | Whether to clean and format the data |
| `page_size` | integer | No | Number of comments per page, default 25 |
| `sort` | string | No | Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "redditorInfoByName": {
    "__typename": "Redditor",
    "comments": {
      "edges": [
        {
          "node": {
            "__typename": "Comment",
            "authorInfo": {
              "displayName": "spez"
            },
            "commentStats": null,
            "content": {
              "html": null,
              "preview": "Pretty simple. For people who are already coming to Reddit every week, we have t…"
            },
            "createdAt": "2026-10-29T22:42:06.463000+0000",
            "id": "t1_19ruo33ofgh8i",
            "postInfo": {
              "__typename": "SubredditPost",
              "id": "t3_1xiupuc",
              "subreddit": {
                "prefixedName": "r/RDDT"
              },
              "title": "Reddit Announces Q3’26 Earnings (plus AMA!)"
            },
            "score": -8
          }
        }
      ],
      "pageInfo": {
        "__typename": "PageInfo",
        "endCursor": "dDFfb3B0ZnlxbA==",
        "hasNextPage": true
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `redditorInfoByName.comments.edges[].node.id` | Comment ID in the form `t1_...`. |
| `redditorInfoByName.comments.edges[].node.content.preview` | Shortened text of the comment. The full text may be cut off with an ellipsis. |
| `redditorInfoByName.comments.edges[].node.content.html` | HTML version of the comment. It was `null` in this response. |
| `redditorInfoByName.comments.edges[].node.score` | Score of the comment. It can be negative. |
| `redditorInfoByName.comments.edges[].node.createdAt` | Time the comment was created, as an ISO 8601 string with a `+0000` offset. |
| `redditorInfoByName.comments.edges[].node.authorInfo.displayName` | Username of the comment author. |
| `redditorInfoByName.comments.edges[].node.postInfo.id / redditorInfoByName.comments.edges[].node.postInfo.title` | ID (form `t3_...`) and title of the post the comment was left on. |
| `redditorInfoByName.comments.edges[].node.postInfo.subreddit.prefixedName` | Subreddit of the post, such as `r/RDDT`. It is absent when `postInfo.__typename` is `ProfilePost`. |
| `redditorInfoByName.comments.pageInfo.hasNextPage` | `true` when more comments are available after this page. |
| `redditorInfoByName.comments.pageInfo.endCursor` | Cursor for the last item on this page. Use it as `after` to get the next page. |

### Notes

- Pass the `endCursor` value from `pageInfo` as `after` in the next request, and stop when `hasNextPage` is `false`.
- Comments on a user's own profile post have `postInfo.__typename` set to `ProfilePost` and no `subreddit` object.
- `sort` accepts `NEW`, `TOP`, `HOT` and `CONTROVERSIAL`. `page_size` defaults to 25.
- To see the user's posts instead of comments, call [Reddit User Posts](/apis/reddit/app/user-posts).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/user-comments.json`](../../../../catalog/models/reddit/app/user-comments.json) · Store page: https://www.sandbase.ai/model/reddit/app/user-comments
