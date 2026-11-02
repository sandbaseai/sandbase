# Facebook Ad Creative Details API: pricing, parameters and code examples

`facebook/ad-details-full` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00462 per call · **Modes:** sync

Pull one Meta Ad Library ad with its creative: every carousel variant, image and video URL, headline, body, and call to action.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00462**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/ad-details-full", "id": "962050096457659"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/ad-details-full', {'id': '962050096457659'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/ad-details-full", {
  "id": "962050096457659"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/ad-details-full", sandbase.Params{
	"id": "962050096457659",
})
```

Same call via the path form: `POST /v1/api/facebook/ad-details-full` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Meta Ad Library ad ID - the numeric id in an Ad Library URL (e.g. "962050096457659" from https://www.facebook.com/ads/library/?id=962050096457659).  |

## Details

Pull one Meta Ad Library ad with its creative: every carousel variant, image and video URL, headline, body, and call to action.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/ad-details-full" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "962050096457659"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Meta Ad Library ad ID - the numeric id in an Ad Library URL (e.g. "962050096457659" from https://www.facebook.com/ads/library/?id=962050096457659). |

### Pricing

Billed at the actual cost of each call, usually $0.00462 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/ad-details-full.json`](../../../catalog/models/facebook/ad-details-full.json) · Store page: https://www.sandbase.ai/model/facebook/ad-details-full
