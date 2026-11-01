# Reddit User Posts

`reddit/user-posts` · api · Reddit

List a Reddit user's posts by username, sorted by new, top, hot, or controversial, with cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00038**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/user-posts", "username": "spez"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/user-posts', {'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/user-posts", {
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/user-posts", sandbase.Params{
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort order for the user's posts. Defaults to new (most recent first). one of: `new`, `top`, `hot`, `controversial` |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it back to fetch the next page.  |
| `username` | string | yes | Reddit username without the leading u/ prefix (e.g. "spez").  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `isArchived` or `isLocked`, and it is served only by a source that…  |

## Details

List a Reddit user's posts by username, sorted by new, top, hot, or controversial, with cursor pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username without the leading u/ prefix (e.g. "spez"). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it back to fetch the next page. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `isArchived` or `isLocked`, and it is served only by a source that ret |
| `sort` | string | No | Sort order for the user's posts. Defaults to new (most recent first). One of: `new`, `top`, `hot`, `controversial`. |

### Pricing

Billed at the actual cost of each call, usually $0.00038 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/reddit/user-posts.json`](../../../catalog/models/reddit/user-posts.json) · Store page: https://www.sandbase.ai/model/reddit/user-posts
