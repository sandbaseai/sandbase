# Reddit Subreddit Posts API: pricing, parameters and code examples

`reddit/subreddit-posts` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00038 per call · **Modes:** sync

Fetch posts from a subreddit listing (hot, new, or top).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00038**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/subreddit-posts", "subreddit": "programming"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/subreddit-posts', {'subreddit': 'programming'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/subreddit-posts", {
  "subreddit": "programming"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/subreddit-posts", sandbase.Params{
	"subreddit": "programming",
})
```

Same call via the path form: `POST /v1/api/reddit/subreddit-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Listing sort order. one of: `hot`, `new`, `top`; default `"hot"` |
| `after` | string |  | Legacy pagination alias. Prefer `cursor`; omit both fields for the first page.  |
| `limit` | integer |  | Page size to ask for (up to 100). Some sources honor it; others always return their whole page of about 25 posts. A page is never trimmed after the call, so pass nextCursor back as cursor to continue exactly where this… default `25`; range 1–100 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's `nextCursor`; omit for the first page.  |
| `subreddit` | string | yes | Subreddit name without the leading r/ (e.g. "golang").  |
| `timeframe` | string |  | Time window, applied when sort is "top" (e.g. "year" for the year's top posts). Ignored for hot/new. Omit to default to the current day for top. one of: `all`, `year`, `month`, `week`, `day`, `hour` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `isArchived` or `selftext`, and it is served only by a source that…  |

## Details

Returns a page of posts from a subreddit listing, sorted by `hot`, `new` or `top`. It needs a `subreddit` name without the leading r/, such as `programming`.

### Use cases

- Track new posts in a subreddit by polling the `new` sort and storing each post `id`.
- Build a weekly digest of the best posts in a community using `sort` set to `top` and `timeframe` set to `week`.
- Collect link posts and their `url` values to monitor which sites and videos a community shares.
- Compare `score` and `upvoteRatio` across posts to see which topics get approval or push back.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/subreddit-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 5, "subreddit": "programming"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit` | string | Yes | Subreddit name without the leading r/ (e.g. "golang"). |
| `after` | string | No | Legacy pagination alias. Prefer `cursor`; omit both fields for the first page. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's `nextCursor`; omit for the first page. |
| `limit` | integer | No | Page size to ask for (up to 100). Some sources honor it; others always return their whole page of about 25 posts. A page is never trimmed after the call, so pass nextCursor back as cursor to continue exactly where this r |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `isArchived` or `selftext`, and it is served only by a source that ret |
| `sort` | string | No | Listing sort order. |
| `timeframe` | string | No | Time window, applied when sort is "top" (e.g. "year" for the year's top posts). Ignored for hot/new. Omit to default to the current day for top. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_eQ7nxx9EkQ_JKD3XB66aFA",
    "posts": [
      {
        "author": "grahamperrin",
        "authorId": "5mpae",
        "createdUtc": 1793670897,
        "id": "1xmgayd",
        "nsfw": false,
        "numComments": 1,
        "permalink": "/r/programming/comments/1xmgayd/a_decade_of_kill_bugs_alan_grow/",
        "score": 36,
        "selftext": ">… A bug in kill was so surprising that, once I'd found it, I couldn't stop ther…",
        "subreddit": "programming",
        "title": "A Decade of Kill Bugs – Alan Grow",
        "upvoteRatio": 0.95
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[].id` | Short ID of the post. Use it to identify the post and to look it up with other Reddit APIs. |
| `data.posts[].title` | Title of the post. |
| `data.posts[].author / data.posts[].authorId` | Username of the poster and the poster's account ID. |
| `data.posts[].createdUtc` | Creation time of the post as a Unix timestamp in seconds, in UTC. |
| `data.posts[].score` | Net score of the post, as shown on Reddit. |
| `data.posts[].upvoteRatio` | Share of votes that are upvotes, as a number between 0 and 1. |
| `data.posts[].numComments` | Number of comments on the post. |
| `data.posts[].url` | Link the post points to. This can be an external page, a video, or a Reddit link. |
| `data.posts[].permalink` | Path of the post on Reddit, starting with `/r/` or `/user/`. Add the Reddit domain to build a full link. |
| `data.posts[].selftext` | Body text of a text post. It is an empty string for posts without body text. Long bodies may be cut. |
| `data.nextCursor` | Cursor for the next page. Pass it back as `cursor`. |

### Notes

- Pass `data.nextCursor` as `cursor` to get the next page. Omit `cursor` for the first page. Prefer `cursor` over the legacy `after` field.
- `timeframe` only applies when `sort` is `top`. Without it, `top` covers the current day.
- Set `requireFields` to `isArchived`, `isLocked` or `selftext` if you need those fields. This may route the call to a dearer source.
- To read the discussion on a post, call [Reddit Post Comments](/apis/reddit/post-comments). For full post data, call [Reddit Post](/apis/reddit/post).

### Pricing

Billed at the actual cost of each call, about $0.00038 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/reddit/subreddit-posts.json`](../../../catalog/models/reddit/subreddit-posts.json) · Store page: https://www.sandbase.ai/model/reddit/subreddit-posts
