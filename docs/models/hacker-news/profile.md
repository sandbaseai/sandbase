# Hacker News Profile

`hacker-news/profile` · api · Hacker News

Get a Hacker News user's public profile by username - karma, bio, and account details as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hacker-news/profile", "handle": "pg"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hacker-news/profile', {'handle': 'pg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hacker-news/profile", {
  "handle": "pg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hacker-news/profile", sandbase.Params{
	"handle": "pg",
})
```

Same call via the path form: `POST /v1/api/hacker-news/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Hacker News username, e.g. "pg".  |

## Details

Get a Hacker News user's public profile by username - karma, bio, and account details as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hacker-news/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "pg"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Hacker News username, e.g. "pg". |

### Pricing

Billed at the actual cost of each call, usually $0.0015 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/hacker-news/profile.json`](../../../catalog/models/hacker-news/profile.json) · Store page: https://www.sandbase.ai/model/hacker-news/profile
