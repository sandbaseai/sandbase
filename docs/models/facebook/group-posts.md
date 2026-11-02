# Facebook Group Posts API: pricing, parameters and code examples

`facebook/group-posts` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch recent posts from any public Facebook group by URL: text, author, reactions, and comment counts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/group-posts", "url": "https://www.facebook.com/groups/instantpotcommunity/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/group-posts', {'url': 'https://www.facebook.com/groups/instantpotcommunity/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/group-posts", {
  "url": "https://www.facebook.com/groups/instantpotcommunity/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/group-posts", sandbase.Params{
	"url": "https://www.facebook.com/groups/instantpotcommunity/",
})
```

Same call via the path form: `POST /v1/api/facebook/group-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The URL of a public Facebook group to fetch posts from (e.g. https://www.facebook.com/groups/instantpotcommunity/).  |
| `sort` | string |  | Ordering for the returned posts (e.g. TOP_POSTS). one of: `TOP_POSTS`, `RECENT_ACTIVITY`, `CHRONOLOGICAL`, `CHRONOLOGICAL_LISTINGS` |
| `cursor` | string |  | Pagination cursor from a previous response to fetch the next page.  |

## Details

Fetch recent posts from any public Facebook group by URL: text, author, reactions, and comment counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/group-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/groups/instantpotcommunity/"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The URL of a public Facebook group to fetch posts from (e.g. https://www.facebook.com/groups/instantpotcommunity/). |
| `cursor` | string | No | Pagination cursor from a previous response to fetch the next page. |
| `sort` | string | No | Ordering for the returned posts (e.g. TOP_POSTS). One of: `TOP_POSTS`, `RECENT_ACTIVITY`, `CHRONOLOGICAL`, `CHRONOLOGICAL_LISTINGS`. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/group-posts.json`](../../../catalog/models/facebook/group-posts.json) · Store page: https://www.sandbase.ai/model/facebook/group-posts
