# Reddit Post API: pricing, parameters and code examples

`reddit/post` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0005 per call · **Modes:** sync

Fetch a single Reddit post by URL, including its full body text, score, comment count, upvote ratio, and subreddit, as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0005**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/post", "url": "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/post', {'url': 'https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/post", {
  "url": "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/post", sandbase.Params{
	"url": "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/",
})
```

Same call via the path form: `POST /v1/api/reddit/post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Reddit post URL on reddit.com, e.g. "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/". The /r/<subreddit>/comments/<id>/, /user/<name>/comments/<id>/, /comments/<id>/ and…  |

## Details

Returns one Reddit post as JSON, including its title, full body text, author, score, comment count, upvote ratio, and subreddit. It needs a single Reddit post `url` on reddit.com.

### Use cases

- Archive the text and score of a specific Reddit thread for a research dataset.
- Check how well a linked post performed by reading its `score`, `numComments`, and `upvoteRatio`.
- Flag NSFW or locked posts before showing them in a content feed.
- Resolve a post URL to its `id`, `subreddit`, and `author` for later lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Reddit post URL on reddit.com, e.g. "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/". The /r/<subreddit>/comments/<id>/, /user/<name>/comments/<id>/, /comments/<id>/ and /g |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "author": "PresidentObama",
    "authorId": "8t1cq",
    "body": "Hi, I’m Barack Obama, President of the United States. Ask me anything. I’ll be t…",
    "createdUtc": 1346270496,
    "domain": "self.IAmA",
    "editedUtc": 1346276503,
    "id": "z1c9z",
    "image": "https://external-preview.redd.it/KftOKw5o_G5ug7ENkLFbplFDpcApH0MvkQoOQD4nKng.jpg…",
    "isArchived": true,
    "isLocked": false,
    "isNsfw": false,
    "numComments": 22716
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title` | Title of the post. |
| `data.body` | Full text of the post. Link or image posts may have little or no text here. |
| `data.author / data.authorId` | Username of the post author and the author's ID. |
| `data.subreddit` | Name of the subreddit the post belongs to, without the `r/` prefix. |
| `data.score / data.numComments` | Net score of the post and the number of comments on it. |
| `data.upvoteRatio` | Share of votes that were upvotes, as a decimal between 0 and 1. |
| `data.createdUtc / data.editedUtc` | Creation time and last edit time of the post, as Unix timestamps in seconds. |
| `data.isArchived / data.isLocked / data.isNsfw` | Boolean flags for archived, locked, and NSFW status. |
| `data.permalink / data.url` | Path of the post on Reddit and its full URL. |
| `found` | `true` when the post was found. A lookup that finds nothing returns `found: false`. |

### Notes

- Send the post link in `url`. The `/r/<subreddit>/comments/<id>/`, `/user/<name>/comments/<id>/`, `/comments/<id>/` and `/gallery/<id>` forms are accepted. Share links and links to other sites are refused as invalid input.
- The post `id` is the short code in the URL, such as `z1c9z`.
- To read the replies to a post, call [Reddit Post Comments](/apis/reddit/post-comments).
- To list more posts from the same community, call [Reddit Subreddit Posts](/apis/reddit/subreddit-posts).

### Pricing

Billed at the actual cost of each call, about $0.0005 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/reddit/post.json`](../../../catalog/models/reddit/post.json) · Store page: https://www.sandbase.ai/model/reddit/post
