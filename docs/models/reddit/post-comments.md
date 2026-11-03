# Reddit Post Comments API: pricing, parameters and code examples

`reddit/post-comments` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0006 per call · **Modes:** sync

List the comments on a Reddit post by URL (author, body, score, timestamp, parent comment). Replies carry the parentId of the comment they answer.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/post-comments", "url": "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/post-comments', {'url': 'https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/post-comments", {
  "url": "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/post-comments", sandbase.Params{
	"url": "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/",
})
```

Same call via the path form: `POST /v1/api/reddit/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Reddit post URL on reddit.com. A gallery link (https://www.reddit.com/gallery/<id>) is read as the post it belongs to, and a relative permalink (/r/<subreddit>/comments/<id>/...) as the same path on…  |
| `cursor` | string |  | Cursor from a previous response for more comments.  |

## Details

Returns the comments on a Reddit post, with author, body, score, creation time and the parent comment for each reply. It needs the full URL of the post as `url`.

### Use cases

- Collect the replies to a popular AMA to study which questions got the most upvotes.
- Rebuild a comment thread as a tree by matching each `parentId` to a comment `id`.
- Pull the top-scored comments on a post to summarize what readers think.
- Link each comment back to its page on Reddit using its `url` to review or moderate it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Reddit post URL on reddit.com. A gallery link (https://www.reddit.com/gallery/<id>) is read as the post it belongs to, and a relative permalink (/r/<subreddit>/comments/<id>/...) as the same path on https://www.redd |
| `cursor` | string | No | Cursor from a previous response for more comments. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "comments": [
      {
        "author": "Biinaryy",
        "body": "Here is a collection of all the questions and answers:\n\nQuestion: [Link](http://…",
        "createdUtc": 1346276659,
        "id": "c60o0iw",
        "parentId": "",
        "score": 5399,
        "url": "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_…"
      }
    ],
    "media": null,
    "nextCursor": "cur_E_QuTid3jKG5pjQCweyA_g"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.comments[].author` | Reddit username of the person who wrote the comment. |
| `data.comments[].body` | Text of the comment. It uses Reddit markdown, so links and emphasis appear as markdown. |
| `data.comments[].id` | ID of the comment, for example `c60o0iw`. Replies point to it in `parentId`. |
| `data.comments[].parentId` | The `id` of the comment this one answers. It is an empty string for a top-level comment. |
| `data.comments[].score` | Score of the comment, as a number. |
| `data.comments[].createdUtc` | Creation time of the comment as a Unix timestamp in seconds (UTC). |
| `data.comments[].url` | Direct link to the comment on reddit.com. |
| `data.nextCursor` | Cursor for the next page of comments. Send it as `cursor` in the next request. |
| `data.media` | Media attached to the post. It is `null` in this response. |
| `found` | `true` when the post was found. A lookup that finds nothing returns `false`. |

### Notes

- Copy the post URL from Reddit. A gallery link or a relative permalink such as `/r/<subreddit>/comments/<id>/...` also works.
- To get more comments, repeat the request with the same `url` and the `nextCursor` value as `cursor`.
- Comments are listed in a flat array. Use `parentId` to see which comment each reply answers.

### Pricing

Billed at the actual cost of each call, about $0.0006 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/reddit/post-comments.json`](../../../catalog/models/reddit/post-comments.json) · Store page: https://www.sandbase.ai/model/reddit/post-comments
