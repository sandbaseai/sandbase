# Reddit User Posts API: pricing, parameters and code examples

`reddit/app/user-posts` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of posts submitted by a specified Reddit user. Results can be sorted by new, top, hot, or controversial order with optional formatting.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/user-posts", "after": "", "need_format": false, "sort": "NEW", "username": "spez"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/user-posts', {'after': '', 'need_format': False, 'sort': 'NEW', 'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/user-posts", {
  "after": "",
  "need_format": false,
  "sort": "NEW",
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/user-posts", sandbase.Params{
	"after": "",
	"need_format": false,
	"sort": "NEW",
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/app/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial) default `"NEW"` |
| `after` | string |  | Pagination parameter for fetching next page default `""` |
| `username` | string | yes | Reddit username  |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |

## Details

Returns a feed of posts submitted by one Reddit user, with the post text, comment count and author details for each post. It needs a Reddit `username` and can sort the posts by new, top, hot or controversial.

### Use cases

- Pull the latest posts from an executive or public figure account to monitor what they announce.
- Archive the full text of a user's posts in Markdown or HTML for research.
- Compare comment counts across a user's posts to see which ones drew the most discussion.
- Page through an account's post history with the `after` cursor to build a posting timeline.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/user-posts" \
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
| `sort` | string | No | Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "identity": {
    "settings": {
      "postSetSettings": {
        "maxPostsPerPostSet": 5
      }
    }
  },
  "postFeed": {
    "__typename": "Redditor",
    "elements": {
      "dist": null,
      "edges": [
        {
          "node": {
            "__typename": "ProfilePost",
            "adSupplementaryTextRichtext": null,
            "attributionInfo": null,
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
                "url": "https://styles.redditmedia.com/t5_3k30p/styles/profileIcon_uj015iwx9s7g1.png?wid…"
              },
              "id": "t2_1w72",
              "isBlocked": false,
              "isCakeDayNow": false,
              "name": "spez",
              "newIcon": {
                "__typename": "MediaSource",
                "dimensions": {
                  "height": 256,
                  "width": 256
                },
                "url": "https://styles.redditmedia.com/t5_3k30p/styles/profileIcon_uj015iwx9s7g1.png?fra…"
              }
            },
            "callToAction": null,
            "commentCount": 481,
            "content": {
              "html": "I want to talk about a big change we're making on Reddit: we're going to evolve …",
              "markdown": "I want to talk about a big change we're making on Reddit: we're going to evolve …",
              "preview": "I want to talk about a big change we're making on Reddit: we're going to evolve …",
              "richtext": "{\"document\":[{\"c\":[{\"e\":\"text\",\"t\":\"I want to talk about a big change we're maki…",
              "richtextMedia": []
            }
          }
        }
      ],
      "pageInfo": {
        "__typename": "PageInfo",
        "endCursor": "dDNfM2N4ZWRu",
        "hasNextPage": false
      }
    },
    "profile": {
      "__typename": "Profile",
      "stickyPosts": []
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `postFeed.elements.edges[].node.__typename` | Type of the feed item. The value `ProfilePost` marks a post on the user's profile. |
| `postFeed.elements.edges[].node.commentCount` | Number of comments on the post. |
| `postFeed.elements.edges[].node.content.markdown / postFeed.elements.edges[].node.content.html` | Post body as Markdown or HTML. Some posts return only `preview`, so check which keys are present. |
| `postFeed.elements.edges[].node.content.preview` | Short plain-text excerpt of the post body. Long text is cut off. |
| `postFeed.elements.edges[].node.content.richtext` | Post body as a JSON string in Reddit's rich text document format. |
| `postFeed.elements.edges[].node.authorInfo.name` | Username of the post author. |
| `postFeed.elements.edges[].node.authorInfo.id` | Author account ID, which starts with `t2_`. |
| `postFeed.elements.edges[].node.authorInfo.newIcon.url / postFeed.elements.edges[].node.authorInfo.iconSmall.url` | Links to the author's profile icon in a 256 by 256 size and a 50 by 50 size. |
| `postFeed.elements.pageInfo.endCursor` | Cursor for the last post on this page. |
| `postFeed.elements.pageInfo.hasNextPage` | Tells you whether another page of posts exists. It is `false` in this response. |

### Notes

- Pass `pageInfo.endCursor` as `after` in the next request when `hasNextPage` is `true`.
- Set `sort` to `NEW`, `TOP`, `HOT` or `CONTROVERSIAL`. The default is `NEW`.
- Set `need_format` to `true` to have the data cleaned and formatted.
- To fetch the comments a user wrote instead of their posts, call [Reddit User Comments](/apis/reddit/app/user-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/user-posts.json`](../../../../catalog/models/reddit/app/user-posts.json) · Store page: https://www.sandbase.ai/model/reddit/app/user-posts
