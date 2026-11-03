# Bluesky Post API: pricing, parameters and code examples

`bluesky/post` · data API · Bluesky · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Get a single Bluesky post by URL - text, author handle, like, reply, and repost counts as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bluesky/post", "url": "https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bluesky/post', {'url': 'https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bluesky/post", {
  "url": "https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bluesky/post", sandbase.Params{
	"url": "https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l",
})
```

Same call via the path form: `POST /v1/api/bluesky/post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Bluesky post URL, e.g. "https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l".  |

## Details

Returns one Bluesky post: its text, author handle and name, creation time, and like, reply, and repost counts. It needs the full post URL in the `url` parameter.

### Use cases

- Show the current like, reply, and repost counts for a Bluesky post on a dashboard.
- Save the text and author of a post that a user shares as a link.
- Compare engagement across a list of posts by looking up each URL.
- Check whether a post link still resolves by reading the `found` flag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bluesky/post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Bluesky post URL, e.g. "https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "authorHandle": "bsky.app",
    "authorImage": "https://cdn.bsky.app/img/avatar/plain/did:plc:z72i7hdynmk6r22z27h6tvur/bafkreihw…",
    "authorName": "Bluesky",
    "createdUtc": 1729148811,
    "id": "3l6oveex3ii2l",
    "likes": 63755,
    "replies": 8711,
    "reposts": 9552,
    "text": "👋  Bluesky is an open social network that gives creators independence from platf…"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the post was found. A lookup that finds nothing returns `false`. |
| `data.text` | Text of the post. Long posts may be cut short in this example. |
| `data.authorHandle / data.authorName` | Handle (for example `bsky.app`) and display name of the account that wrote the post. |
| `data.authorImage` | URL of the author's avatar image. |
| `data.id` | Post ID. It matches the last part of the post URL, for example `3l6oveex3ii2l`. |
| `data.createdUtc` | Time the post was created, as a Unix timestamp in seconds. |
| `data.likes / data.replies / data.reposts` | Number of likes, replies, and reposts the post has. |

### Notes

- Copy the `url` from the Bluesky web app. It has the form `https://bsky.app/profile/<handle>/post/<id>`.
- The result is in `outputs[0].data`. Check `found` before reading the other fields.
- To look up the author, call [Bluesky Profile](/apis/bluesky/profile) with `data.authorHandle`. To list more of their posts, use [Bluesky User Posts](/apis/bluesky/user-posts).

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bluesky/post.json`](../../../catalog/models/bluesky/post.json) · Store page: https://www.sandbase.ai/model/bluesky/post
