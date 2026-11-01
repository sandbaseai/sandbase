# TikTok Profile Region

`tiktok/profile-region` · api · TikTok

Resolve the home region (country) of a TikTok creator by handle.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/profile-region", "handle": "stoolpresidente"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/profile-region', {'handle': 'stoolpresidente'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/profile-region", {
  "handle": "stoolpresidente"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/profile-region", sandbase.Params{
	"handle": "stoolpresidente",
})
```

Same call via the path form: `POST /v1/api/tiktok/profile-region` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | TikTok username without the leading @ (e.g. "stoolpresidente").  |

## Details

Resolve the home region (country) of a TikTok creator by handle.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/profile-region" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "stoolpresidente"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | TikTok username without the leading @ (e.g. "stoolpresidente"). |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/profile-region.json`](../../../catalog/models/tiktok/profile-region.json) · Store page: https://www.sandbase.ai/model/tiktok/profile-region
