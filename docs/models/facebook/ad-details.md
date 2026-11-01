# Facebook Ad Details

`facebook/ad-details` · api · Facebook

Look up a single Meta Ad Library ad by ID or URL and get the advertiser, creative text, call-to-action, platforms, and run dates as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/ad-details"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/ad-details', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/ad-details", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/ad-details", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/facebook/ad-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | Meta Ad Library ad ID (e.g. "702369045530963"). Provide either id or url.  |
| `url` | string |  | Meta Ad Library ad URL (e.g. "https://www.facebook.com/ads/library?id=1185617869915074"). Provide either id or url.  |

## Details

Look up a single Meta Ad Library ad by ID or URL and get the advertiser, creative text, call-to-action, platforms, and run dates as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/ad-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "962050096457659"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | Meta Ad Library ad ID (e.g. "702369045530963"). Provide either id or url. |
| `url` | string | No | Meta Ad Library ad URL (e.g. "https://www.facebook.com/ads/library?id=1185617869915074"). Provide either id or url. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/ad-details.json`](../../../catalog/models/facebook/ad-details.json) · Store page: https://www.sandbase.ai/model/facebook/ad-details
