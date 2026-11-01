# Truth Social User Posts

`truth-social/user-posts` · api · Truth Social

List a Truth Social account's recent posts by handle - text, engagement (likes, comments, shares), and timestamps as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "truth-social/user-posts", "handle": "realDonaldTrump"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('truth-social/user-posts', {'handle': 'realDonaldTrump'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("truth-social/user-posts", {
  "handle": "realDonaldTrump"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "truth-social/user-posts", sandbase.Params{
	"handle": "realDonaldTrump",
})
```

Same call via the path form: `POST /v1/api/truth-social/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; a page holds 20 posts.  |
| `handle` | string | yes | Truth Social handle without the @, e.g. "realDonaldTrump".  |

## Details

List a Truth Social account's recent posts by handle - text, engagement (likes, comments, shares), and timestamps as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/truth-social/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "realDonaldTrump"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Truth Social handle without the @, e.g. "realDonaldTrump". |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; a page holds 20 posts. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/truth-social/user-posts.json`](../../../catalog/models/truth-social/user-posts.json) · Store page: https://www.sandbase.ai/model/truth-social/user-posts
