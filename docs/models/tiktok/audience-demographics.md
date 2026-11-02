# TikTok Audience Demographics API: pricing, parameters and code examples

`tiktok/audience-demographics` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.018 per call · **Modes:** sync

Get the audience country breakdown (follower count and share per country) for a TikTok creator by handle.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.018**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/audience-demographics", "handle": "shakira"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/audience-demographics', {'handle': 'shakira'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/audience-demographics", {
  "handle": "shakira"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/audience-demographics", sandbase.Params{
	"handle": "shakira",
})
```

Same call via the path form: `POST /v1/api/tiktok/audience-demographics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | TikTok username without the leading @ (e.g. "shakira").  |

## Details

Get the audience country breakdown (follower count and share per country) for a TikTok creator by handle.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/audience-demographics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "shakira"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | TikTok username without the leading @ (e.g. "shakira"). |

### Pricing

Billed at the actual cost of each call, usually $0.018 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/audience-demographics.json`](../../../catalog/models/tiktok/audience-demographics.json) · Store page: https://www.sandbase.ai/model/tiktok/audience-demographics
