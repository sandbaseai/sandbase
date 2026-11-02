# Instagram User Reposts API: pricing, parameters and code examples

`instagram/user-reposts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

List the posts a public Instagram account has reposted to its feed, with cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/user-reposts", "userId": "787132"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/user-reposts', {'userId': '787132'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/user-reposts", {
  "userId": "787132"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/user-reposts", sandbase.Params{
	"userId": "787132",
})
```

Same call via the path form: `POST /v1/api/instagram/user-reposts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `userId` | string | yes | Instagram's numeric account id, as returned by instagram.profile.  |

## Details

List the posts a public Instagram account has reposted to its feed, with cursor pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/user-reposts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "787132"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | Instagram's numeric account id, as returned by instagram.profile. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/user-reposts.json`](../../../catalog/models/instagram/user-reposts.json) · Store page: https://www.sandbase.ai/model/instagram/user-reposts
