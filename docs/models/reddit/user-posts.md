# Reddit User Posts API: pricing, parameters and code examples

`reddit/user-posts` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00038 per call · **Modes:** sync

List a Reddit user's posts by username, sorted by new, top, hot, or controversial, with cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00038**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/user-posts", "username": "spez"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/user-posts', {'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/user-posts", {
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/user-posts", sandbase.Params{
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort order for the user's posts. Defaults to new (most recent first). one of: `new`, `top`, `hot`, `controversial` |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it back to fetch the next page.  |
| `username` | string | yes | Reddit username without the leading u/ prefix (e.g. "spez").  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `isArchived` or `isLocked`, and it is served only by a source that…  |

## Details

Returns a list of posts written by one Reddit user, with title, score, comment count, and link for each post. It needs a `username` without the `u/` prefix. You can sort by `new`, `top`, `hot`, or `controversial`.

### Use cases

- Track what an official or public account has posted recently.
- Pull a user's top posts to see which of their threads got the most votes.
- Check how much discussion a user's posts get by comparing `numComments` and `upvoteRatio`.
- Build an archive of a user's posts with their text and permalinks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username without the leading u/ prefix (e.g. "spez"). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it back to fetch the next page. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `isArchived` or `isLocked`, and it is served only by a source that ret |
| `sort` | string | No | Sort order for the user's posts. Defaults to new (most recent first). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": null,
    "posts": [
      {
        "author": "spez",
        "authorId": "1w72",
        "createdUtc": 1793304517,
        "id": "1xiupm0",
        "media": [],
        "nsfw": false,
        "numComments": 481,
        "permalink": "/user/spez/comments/1xiupm0/about_that_login_screen/",
        "score": 0,
        "selftext": "I want to talk about a big change we're making on Reddit: we're going to evolve …",
        "subreddit": "",
        "title": "About that login screen"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[].id` | The post ID. It is a short base-36 style string such as `1xiupm0`. |
| `data.posts[].title` | The title of the post. |
| `data.posts[].selftext` | The body text of the post. It can be missing on posts without text. |
| `data.posts[].author / data.posts[].authorId` | The username of the author and the author's ID. |
| `data.posts[].createdUtc` | When the post was created, as a Unix timestamp in seconds. |
| `data.posts[].score / data.posts[].numComments` | The post's score and the number of comments on it. |
| `data.posts[].upvoteRatio` | The share of votes that were upvotes, as a number between 0 and 1. |
| `data.posts[].permalink / data.posts[].url` | The relative path of the post and its full `reddit.com` URL. |
| `data.posts[].nsfw` | `true` when the post is marked NSFW. |
| `data.nextCursor` | The cursor for the next page. It is `null` when there are no more pages. |

### Notes

- Pass `data.nextCursor` back as `cursor` to get the next page. Keep the same `username` and `sort`.
- The `subreddit` field can be an empty string, as in the sample response for posts made on a user profile.
- Add `isArchived` or `isLocked` to `requireFields` if you need those fields in the output.
- To read the comments on a post, call [Reddit Post Comments](/apis/reddit/post-comments). For a user's comments instead of posts, use [Reddit User Comments](/apis/reddit/user-comments).

### Pricing

Billed at the actual cost of each call, about $0.00038 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/reddit/user-posts.json`](../../../catalog/models/reddit/user-posts.json) · Store page: https://www.sandbase.ai/model/reddit/user-posts
