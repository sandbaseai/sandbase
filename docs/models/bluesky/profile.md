# Bluesky Profile API: pricing, parameters and code examples

`bluesky/profile` · data API · Bluesky · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Get a Bluesky user's public profile by handle - display name, bio, follower and post counts as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bluesky/profile", "handle": "bsky.app"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bluesky/profile', {'handle': 'bsky.app'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bluesky/profile", {
  "handle": "bsky.app"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bluesky/profile", sandbase.Params{
	"handle": "bsky.app",
})
```

Same call via the path form: `POST /v1/api/bluesky/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Bluesky handle, e.g. "bsky.app" or "jay.bsky.team".  |

## Details

Get a Bluesky user's public profile by handle - display name, bio, follower and post counts as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bluesky/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "bsky.app"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Bluesky handle, e.g. "bsky.app" or "jay.bsky.team". |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/bluesky/profile.json`](../../../catalog/models/bluesky/profile.json) · Store page: https://www.sandbase.ai/model/bluesky/profile
