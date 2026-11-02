# Reddit User Comments API: pricing, parameters and code examples

`reddit/user-comments` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0006 per call · **Modes:** sync

List a Reddit user's comments by username, sorted by new, top, hot, or controversial, with the parent post title and subreddit on every item and cursor pagination. Comment text may be truncated to a roughly 300-character preview, and this endpoint carries no per-comment permalink; use reddit.post_comments for full comment bodies and comment URLs on a given post.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/user-comments", "username": "spez"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/user-comments', {'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/user-comments", {
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/user-comments", sandbase.Params{
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/user-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort order for the user's comments. Defaults to new (most recent first). one of: `new`, `top`, `hot`, `controversial` |
| `limit` | integer |  | Page size to ask for (up to 100, default 25). Some sources honor it; others always return their whole page of about 25 comments. A page is never trimmed after the call, so pass nextCursor back as cursor to continue… default `25`; range 1–100 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it back to fetch the next page.  |
| `username` | string | yes | Reddit username, without the u/ prefix. Example: "spez".  |

## Details

List a Reddit user's comments by username, sorted by new, top, hot, or controversial, with the parent post title and subreddit on every item and cursor pagination. Comment text may be truncated to a roughly 300-character preview, and this endpoint carries no per-comment permalink; use reddit.post_comments for full comment bodies and comment URLs on a given post.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/user-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username, without the u/ prefix. Example: "spez". |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it back to fetch the next page. |
| `limit` | integer | No | Page size to ask for (up to 100, default 25). Some sources honor it; others always return their whole page of about 25 comments. A page is never trimmed after the call, so pass nextCursor back as cursor to continue exact |
| `sort` | string | No | Sort order for the user's comments. Defaults to new (most recent first). One of: `new`, `top`, `hot`, `controversial`. |

### Pricing

Billed at the actual cost of each call, usually $0.0006 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/reddit/user-comments.json`](../../../catalog/models/reddit/user-comments.json) · Store page: https://www.sandbase.ai/model/reddit/user-comments
