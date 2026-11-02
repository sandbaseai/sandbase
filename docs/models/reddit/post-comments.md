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

List the comments on a Reddit post by URL (author, body, score, timestamp, parent comment). Replies carry the parentId of the comment they answer.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.reddit.com/r/IAmA/comments/z1c9z/i_am_barack_obama_president_of_the_united_states/"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Reddit post URL on reddit.com. A gallery link (https://www.reddit.com/gallery/<id>) is read as the post it belongs to, and a relative permalink (/r/<subreddit>/comments/<id>/...) as the same path on https://www.redd |
| `cursor` | string | No | Cursor from a previous response for more comments. |

### Pricing

Billed at the actual cost of each call, usually $0.0006 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/reddit/post-comments.json`](../../../catalog/models/reddit/post-comments.json) · Store page: https://www.sandbase.ai/model/reddit/post-comments
