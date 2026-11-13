# GitHub User Repositories API: pricing, parameters and code examples

`github/user-repositories` · data API · GitHub · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List a GitHub user's public repositories (name, description, language, stars, and forks) with sorting and cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "github/user-repositories", "handle": "torvalds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('github/user-repositories', {'handle': 'torvalds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("github/user-repositories", {
  "handle": "torvalds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "github/user-repositories", sandbase.Params{
	"handle": "torvalds",
})
```

Same call via the path form: `POST /v1/api/github/user-repositories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Repository ordering. one of: `created`, `updated`, `pushed`, `full_name`; default `"updated"` |
| `type` | string |  | Which repositories to include: owner (default), all, or member. one of: `owner`, `all`, `member` |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it back to fetch the next page.  |
| `handle` | string | yes | GitHub username.  |
| `direction` | string |  | Sort direction, ascending or descending, paired with sort. one of: `asc`, `desc` |

## Details

List a GitHub user's public repositories (name, description, language, stars, and forks) with sorting and cursor pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "github/user-repositories", "handle": "torvalds"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | GitHub username. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it back to fetch the next page. |
| `direction` | string | No | Sort direction, ascending or descending, paired with sort. One of: `asc`, `desc`. |
| `sort` | string | No | Repository ordering. One of: `created`, `updated`, `pushed`, `full_name`. Default `"updated"`. |
| `type` | string | No | Which repositories to include: owner (default), all, or member. One of: `owner`, `all`, `member`. |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/github/user-repositories.json`](../../../catalog/models/github/user-repositories.json) · Store page: https://www.sandbase.ai/model/github/user-repositories
