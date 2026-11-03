# Reddit Subreddit Search API: pricing, parameters and code examples

`reddit/subreddit-search` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00035 per call · **Modes:** sync

Search posts within a single subreddit by query, sort, and timeframe.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00035**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/subreddit-search", "subreddit": "Fitness"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/subreddit-search', {'subreddit': 'Fitness'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/subreddit-search", {
  "subreddit": "Fitness"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/subreddit-search", sandbase.Params{
	"subreddit": "Fitness",
})
```

Same call via the path form: `POST /v1/api/reddit/subreddit-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Optional sort order: relevance, hot, top, new, comments. one of: `relevance`, `hot`, `top`, `new`, `comments` |
| `query` | string |  | Optional search query to match posts (e.g. 'push ups').  |
| `cursor` | string |  | Optional pagination token from a previous response. Include `nextCursor` in requireFields on the first request to make sure a source that supports pagination serves it.  |
| `subreddit` | string | yes | Subreddit name without the r/ prefix (e.g. 'Fitness').  |
| `timeframe` | string |  | Optional time filter: all, year, month, week, day, hour. one of: `all`, `year`, `month`, `week`, `day`, `hour` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor` or `selftext`, and it is served only by a source that…  |

## Details

Returns Reddit posts from one subreddit that match a search query. It needs a `subreddit` name without the r/ prefix, and it accepts an optional `query`, `sort` and `timeframe`.

### Use cases

- Find past discussions of a topic, such as push-ups, inside r/Fitness.
- Rank the top posts of a subreddit for a keyword by `score` or `numComments` to see which threads got the most attention.
- Collect post titles and text from a community to study how people talk about a topic.
- Track new posts that mention a brand or term in a subreddit by sorting with `new`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/subreddit-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "push ups", "subreddit": "Fitness"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit` | string | Yes | Subreddit name without the r/ prefix (e.g. 'Fitness'). |
| `cursor` | string | No | Optional pagination token from a previous response. Include `nextCursor` in requireFields on the first request to make sure a source that supports pagination serves it. |
| `query` | string | No | Optional search query to match posts (e.g. 'push ups'). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor` or `selftext`, and it is served only by a source that ret |
| `sort` | string | No | Optional sort order: relevance, hot, top, new, comments. |
| `timeframe` | string | No | Optional time filter: all, year, month, week, day, hour. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_vSRO4dkJp_Wni4NIHlJvKQ",
    "posts": [
      {
        "author": "Yea_Red",
        "authorId": "j6hq9",
        "createdUtc": 1428859519,
        "id": "32cksu",
        "nsfw": false,
        "numComments": 528,
        "permalink": "/r/Fitness/comments/32cksu/how_much_will_pushups_help_my_chest/",
        "score": 2003,
        "selftext": "I try to do 100 a day. Is this doing anything for me, or should I just focus on …",
        "subreddit": "Fitness",
        "title": "How much will push-ups help my chest?",
        "url": "https://www.reddit.com/r/Fitness/comments/32cksu/how_much_will_pushups_help_my_c…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[].title` | Title of the post. |
| `data.posts[].selftext` | Body text of the post. Long text may be cut, and link posts may have none. |
| `data.posts[].score` | Score of the post. |
| `data.posts[].numComments` | Number of comments on the post. |
| `data.posts[].author / data.posts[].authorId` | Username and ID of the post author. |
| `data.posts[].createdUtc` | Creation time of the post as a Unix timestamp in seconds (UTC). |
| `data.posts[].id` | Short ID of the post, such as `32cksu`. |
| `data.posts[].permalink / data.posts[].url` | Path and full URL of the post on Reddit. |
| `data.posts[].nsfw` | `true` if the post is marked NSFW. |
| `data.nextCursor` | Token to pass as `cursor` to get the next page of results. |

### Notes

- Pass the subreddit name without the r/ prefix, for example `Fitness`.
- For more than the first page, add `nextCursor` to `requireFields` on the first request. Then send the returned `data.nextCursor` as `cursor` on the next call.
- Add `selftext`, `isArchived` or `isLocked` to `requireFields` if you need those fields on every post.
- To read the comments of a post, call [Reddit Post Comments](/apis/reddit/post-comments) with the post.

### Pricing

Billed at the actual cost of each call, about $0.00035 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/reddit/subreddit-search.json`](../../../catalog/models/reddit/subreddit-search.json) · Store page: https://www.sandbase.ai/model/reddit/subreddit-search
