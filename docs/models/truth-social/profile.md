# Truth Social Profile API: pricing, parameters and code examples

`truth-social/profile` · data API · Truth Social · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Get a Truth Social account's public profile by handle - display name, bio, follower/following counts, and post count as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "truth-social/profile", "handle": "DevinNunes"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('truth-social/profile', {'handle': 'DevinNunes'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("truth-social/profile", {
  "handle": "DevinNunes"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "truth-social/profile", sandbase.Params{
	"handle": "DevinNunes",
})
```

Same call via the path form: `POST /v1/api/truth-social/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Truth Social handle without the @, e.g. "realDonaldTrump".  |

## Details

Get a Truth Social account's public profile by handle - display name, bio, follower/following counts, and post count as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/truth-social/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "DevinNunes"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Truth Social handle without the @, e.g. "realDonaldTrump". |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/truth-social/profile.json`](../../../catalog/models/truth-social/profile.json) · Store page: https://www.sandbase.ai/model/truth-social/profile
