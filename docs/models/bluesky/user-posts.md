# Bluesky User Posts API: pricing, parameters and code examples

`bluesky/user-posts` · data API · Bluesky · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

List a Bluesky account's recent posts (text, author handle, like, reply, and repost counts) by handle as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bluesky/user-posts", "handle": "bsky.app"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bluesky/user-posts', {'handle': 'bsky.app'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bluesky/user-posts", {
  "handle": "bsky.app"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bluesky/user-posts", sandbase.Params{
	"handle": "bsky.app",
})
```

Same call via the path form: `POST /v1/api/bluesky/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Bluesky handle, e.g. "bsky.app" or "jay.bsky.team".  |

## Details

Returns a list of recent posts for a Bluesky account. Each post has its text, author details, a creation time, and like, reply, and repost counts. You send one input, the account `handle`.

### Use cases

- Track which posts from a brand account get the most likes and reposts.
- Pull the latest post text from an account to feed a news or monitoring dashboard.
- Compare reply counts across posts to find those that start the most discussion.
- Collect an account's recent posts for sentiment or topic analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bluesky/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "bsky.app"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Bluesky handle, e.g. "bsky.app" or "jay.bsky.team". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "posts": [
      {
        "authorHandle": "bsky.app",
        "authorImage": "https://cdn.bsky.app/img/avatar/plain/did:plc:z72i7hdynmk6r22z27h6tvur/bafkreihw…",
        "authorName": "Bluesky",
        "createdUtc": 1729148811,
        "id": "3l6oveex3ii2l",
        "likes": 63755,
        "replies": 8711,
        "reposts": 9552,
        "text": "👋  Bluesky is an open social network that gives creators independence from platf…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the lookup returned data. A lookup that finds nothing returns `found: false`. |
| `data.posts[].id` | Identifier of the post, a short string such as `3l6oveex3ii2l`. |
| `data.posts[].text` | Text of the post. |
| `data.posts[].createdUtc` | Creation time of the post as a Unix timestamp in seconds, in UTC. |
| `data.posts[].authorHandle / authorName` | Handle and display name of the account that wrote the post. |
| `data.posts[].authorImage` | URL of the author's avatar image. |
| `data.posts[].likes / replies / reposts` | Counts of likes, replies, and reposts the post has received. |

### Notes

- Pass the account handle in `handle`, for example `bsky.app` or `jay.bsky.team`. The request has no other parameters, so there is no pagination option.
- `authorHandle` can differ from the `handle` you sent, so check it if you only want posts written by that account.
- Call [Bluesky Profile](/apis/bluesky/profile) for details about the account itself.
- Call [Bluesky Post](/apis/bluesky/post) to look at a single post.

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bluesky/user-posts.json`](../../../catalog/models/bluesky/user-posts.json) · Store page: https://www.sandbase.ai/model/bluesky/user-posts
