# Reddit Trending Posts API: pricing, parameters and code examples

`reddit/trending-posts` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0003 per call · **Modes:** sync

Get currently trending Reddit posts across all subreddits with stable cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0003**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/trending-posts"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/trending-posts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/trending-posts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/trending-posts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/reddit/trending-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `after` | string |  | Pagination cursor from a previous response's nextCursor. Omit for the first page.  |
| `limit` | integer |  | Maximum number of trending posts to return (1-100, default 25). default `25`; range 1–100 |

## Details

Returns a list of Reddit posts that are currently trending across all subreddits. Each post includes its title, subreddit, author, score, comment count, and link. The only inputs are an optional page size (`limit`) and an optional cursor (`after`).

### Use cases

- Track which topics are trending on Reddit right now and in which subreddits.
- Build a feed or dashboard that shows the top trending posts with their scores and comment counts.
- Spot fast-growing posts by comparing `score` and `numComments` across calls.
- Collect trending post links and `domain` values to see which sites and image hosts get shared most.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/trending-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 25}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `after` | string | No | Pagination cursor from a previous response's nextCursor. Omit for the first page. |
| `limit` | integer | No | Maximum number of trending posts to return (1-100, default 25). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "t3_1xmlmgw",
    "posts": [
      {
        "author": "Negative_1by12_aura",
        "authorId": "2eyayz4qcy",
        "createdUtc": 1793676776,
        "domain": "i.redd.it",
        "id": "1xmids8",
        "isArchived": false,
        "isLocked": false,
        "nsfw": false,
        "numComments": 801,
        "permalink": "/r/interesting/comments/1xmids8/hiv_is_no_longer_a_terminal_disease/",
        "score": 21475,
        "selftext": ""
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[].id` | Post ID without a prefix. Use it to look up the post in other APIs. |
| `data.posts[].title` | Title of the post. |
| `data.posts[].subreddit` | Name of the subreddit where the post was made. |
| `data.posts[].author / data.posts[].authorId` | Username and ID of the post author. |
| `data.posts[].score / data.posts[].numComments` | Post score and number of comments. |
| `data.posts[].upvoteRatio` | Share of votes that are upvotes, as a decimal between 0 and 1 (for example `0.94`). |
| `data.posts[].createdUtc` | Creation time of the post as a Unix timestamp in seconds. |
| `data.posts[].permalink / data.posts[].url` | `permalink` is the Reddit path of the post. `url` is the link the post points to, such as an image. |
| `data.posts[].isArchived / data.posts[].isLocked / data.posts[].nsfw` | Boolean flags for archived posts, locked posts, and posts marked NSFW. |
| `data.nextCursor` | Cursor for the next page. Pass it as `after` in the next request. |

### Notes

- For the first page, omit `after`. For the next page, send the value of `data.nextCursor` as `after`.
- `limit` accepts 1 to 100 and defaults to 25.
- `selftext` is empty for link and image posts, so text only appears for text posts.
- To read a post in full, call [Reddit Post Details](/apis/reddit/app/post-details). To list comments, use [Reddit Post Comments](/apis/reddit/post-comments).

### Pricing

Billed at the actual cost of each call, about $0.0003 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/reddit/trending-posts.json`](../../../catalog/models/reddit/trending-posts.json) · Store page: https://www.sandbase.ai/model/reddit/trending-posts
