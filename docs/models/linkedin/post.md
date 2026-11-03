# LinkedIn Post API: pricing, parameters and code examples

`linkedin/post` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

Fetch a single LinkedIn post or article by URL (title, text, author, like and comment counts, publish date).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/post", "url": "https://www.linkedin.com/posts/stripe_last-week-agent-traffic-surpassed-human-activity-7470882737390940160-2Nxs"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/post', {'url': 'https://www.linkedin.com/posts/stripe_last-week-agent-traffic-surpassed-human-activity-7470882737390940160-2Nxs'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/post", {
  "url": "https://www.linkedin.com/posts/stripe_last-week-agent-traffic-surpassed-human-activity-7470882737390940160-2Nxs"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/post", sandbase.Params{
	"url": "https://www.linkedin.com/posts/stripe_last-week-agent-traffic-surpassed-human-activity-7470882737390940160-2Nxs",
})
```

Same call via the path form: `POST /v1/api/linkedin/post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full LinkedIn post or article URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `image`, and it is served only by a source that returns every one of…  |

## Details

Returns one LinkedIn post or article as a JSON object with its title, text, author, like and comment counts, and publish time. It needs the full post or article `url`.

### Use cases

- Pull the text and engagement counts of a competitor's post to track how it performs.
- Archive the title, text and author of a post you want to cite or review later.
- Check the `likes` and `comments` of a campaign post that you have the link for.
- Resolve a shared LinkedIn link into the author name and profile URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/posts/stripe_last-week-agent-traffic-surpassed-human-activity-7470882737390940160-2Nxs"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full LinkedIn post or article URL. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `image`, and it is served only by a source that returns every one of t |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "author": "Stripe",
    "authorImage": null,
    "authorUrl": "https://www.linkedin.com/company/stripe",
    "comments": 37,
    "createdUtc": 1781197246,
    "image": null,
    "likes": 221,
    "text": "Last week, agent traffic surpassed human traffic on the internet for the first t…",
    "title": "Last week, agent traffic surpassed human traffic on the internet for the first t…",
    "url": "https://www.linkedin.com/posts/stripe_last-week-agent-traffic-surpassed-human-ac…"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the post was located. The call still succeeds with `found: false` when nothing matches. |
| `data.title` | Title of the post or article. For a short post it matches the opening line of the text. |
| `data.text` | Body text of the post. |
| `data.author / data.authorUrl` | Display name of the author and the link to the author's LinkedIn page. For a company post, the URL points to the company page. |
| `data.likes / data.comments` | Number of likes and number of comments on the post. |
| `data.createdUtc` | Publish time as a Unix timestamp in seconds. |
| `data.authorImage / data.image` | Author picture and post image. Both can be `null`, as in this response. |
| `data.url` | The post URL that was looked up. |

### Notes

- Copy the `url` from the post's share link or the browser address bar. It must be the full LinkedIn post or article URL.
- `authorImage` and `image` can come back `null`. Pass them in `requireFields` to be served only by a source that returns them. The price can rise when this applies.
- To read the discussion on a post, call [LinkedIn Post Comments](/apis/linkedin/post-comments). For who reacted, call [LinkedIn Post Reactions](/apis/linkedin/post-reactions).

### Pricing

Billed at the actual cost of each call, about $0.0008 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/post.json`](../../../catalog/models/linkedin/post.json) · Store page: https://www.sandbase.ai/model/linkedin/post
