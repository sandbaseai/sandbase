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

Get a single Bluesky post by URL - text, author handle, like, reply, and repost counts as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bluesky/post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Bluesky post URL, e.g. "https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l". |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/bluesky/post.json`](../../../catalog/models/bluesky/post.json) · Store page: https://www.sandbase.ai/model/bluesky/post
