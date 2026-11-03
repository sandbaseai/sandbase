# Reddit User Comments API: pricing, parameters and code examples

`reddit/user-comments` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0006 per call · **Modes:** sync

List a Reddit user's comments by username, sorted by new, top, hot, or controversial, with the parent post title and subreddit on every item and cursor pagination. Comment text may be truncated to a roughly 300-character preview, and this endpoint carries no per-comment permalink; use reddit.post_comments for full comment bodies and comment URLs on a given post.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/user-comments", "username": "spez"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/user-comments', {'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/user-comments", {
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/user-comments", sandbase.Params{
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/user-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort order for the user's comments. Defaults to new (most recent first). one of: `new`, `top`, `hot`, `controversial` |
| `limit` | integer |  | Page size to ask for (up to 100, default 25). Some sources honor it; others always return their whole page of about 25 comments. A page is never trimmed after the call, so pass nextCursor back as cursor to continue… default `25`; range 1–100 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it back to fetch the next page.  |
| `username` | string | yes | Reddit username, without the u/ prefix. Example: "spez".  |

## Details

Returns a page of a Reddit user's comments, each with a text preview, score, timestamp, and the parent post's title and subreddit. It needs a Reddit `username` without the `u/` prefix.

### Use cases

- Review what a public figure has said in recent threads, such as an executive's replies during an AMA.
- Find a user's highest-scored comments by setting `sort` to `top`.
- Track which subreddits and posts a user comments on most.
- Pull a user's comment history to check how they engage across communities.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/user-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username, without the u/ prefix. Example: "spez". |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it back to fetch the next page. |
| `limit` | integer | No | Page size to ask for (up to 100, default 25). Some sources honor it; others always return their whole page of about 25 comments. A page is never trimmed after the call, so pass nextCursor back as cursor to continue exact |
| `sort` | string | No | Sort order for the user's comments. Defaults to new (most recent first). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "comments": [
      {
        "author": "spez",
        "bodyPreview": "Pretty simple. For people who are already coming to Reddit every week, we have t…",
        "createdUtc": 1793324526,
        "id": "19ruo33ofgh8i",
        "postId": "1xiupuc",
        "postTitle": "Reddit Announces Q3’26 Earnings (plus AMA!)",
        "score": -9,
        "subreddit": "RDDT"
      }
    ],
    "nextCursor": "cur_uHC_PYNAJi9Hh4rl4wAw2w"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.comments[].id` | Identifier of the comment. |
| `data.comments[].bodyPreview` | Start of the comment text. It can be cut short and ends with an ellipsis when truncated. |
| `data.comments[].createdUtc` | Time the comment was posted, as a Unix timestamp. |
| `data.comments[].score` | Comment score. It can be negative. |
| `data.comments[].postId / data.comments[].postTitle` | ID and title of the post the comment was made on. |
| `data.comments[].subreddit` | Subreddit of the parent post. It can be an empty string. |
| `data.comments[].author` | Username of the comment author. |
| `data.nextCursor` | Cursor for the next page. Pass it back as `cursor`. |
| `found` | `true` when the user lookup returned data. |

### Notes

- Pass `data.nextCursor` as `cursor` to fetch the next page. Keep the same `username` and `sort`.
- Comments have no permalink here. Call [Reddit Post Comments](/apis/reddit/post-comments) with the `postId` to get full comment bodies and comment URLs.
- `subreddit` can be empty on some items, so do not rely on it being set.
- To see the user's posts instead of comments, use [Reddit User Posts](/apis/reddit/user-posts).

### Pricing

Billed at the actual cost of each call, about $0.0006 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/reddit/user-comments.json`](../../../catalog/models/reddit/user-comments.json) · Store page: https://www.sandbase.ai/model/reddit/user-comments
