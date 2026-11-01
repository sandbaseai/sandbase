# Reddit Trending Posts

`reddit/trending-posts` · api · Reddit

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

Get currently trending Reddit posts across all subreddits with stable cursor pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/trending-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 25}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `after` | string | No | Pagination cursor from a previous response's nextCursor. Omit for the first page. |
| `limit` | integer | No | Maximum number of trending posts to return (1-100, default 25). |

### Pricing

Billed at the actual cost of each call, usually $0.0003 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/reddit/trending-posts.json`](../../../catalog/models/reddit/trending-posts.json) · Store page: https://www.sandbase.ai/model/reddit/trending-posts
