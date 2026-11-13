# GitHub User Pull Requests API: pricing, parameters and code examples

`github/user-pull-requests` · data API · GitHub · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List a GitHub user's public pull requests by handle (title, repository, state, creation date, and URL) with optional date filtering and pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "github/user-pull-requests", "handle": "torvalds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('github/user-pull-requests', {'handle': 'torvalds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("github/user-pull-requests", {
  "handle": "torvalds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "github/user-pull-requests", sandbase.Params{
	"handle": "torvalds",
})
```

Same call via the path form: `POST /v1/api/github/user-pull-requests` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `since` | string |  | Only include pull requests opened on or after this date (YYYY-MM-DD).  |
| `until` | string |  | Only include pull requests opened on or before this date (YYYY-MM-DD).  |
| `cursor` | string |  | Pagination cursor from a previous response (page number, defaults to 1).  |
| `handle` | string | yes | GitHub username.  |

## Details

List a GitHub user's public pull requests by handle (title, repository, state, creation date, and URL) with optional date filtering and pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "github/user-pull-requests", "handle": "torvalds"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | GitHub username. |
| `cursor` | string | No | Pagination cursor from a previous response (page number, defaults to 1). |
| `since` | string | No | Only include pull requests opened on or after this date (YYYY-MM-DD). |
| `until` | string | No | Only include pull requests opened on or before this date (YYYY-MM-DD). |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/github/user-pull-requests.json`](../../../catalog/models/github/user-pull-requests.json) · Store page: https://www.sandbase.ai/model/github/user-pull-requests
