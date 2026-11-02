# Kuaishou User Profile API: pricing, parameters and code examples

`kuaishou/user-detail` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get the public profile for a Kuaishou user identified by user ID. Use it to inspect an account found through user or video results.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/user-detail", "userId": "40300058"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/user-detail', {'userId': '40300058'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/user-detail", {
  "userId": "40300058"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/user-detail", sandbase.Params{
	"userId": "40300058",
})
```

Same call via the path form: `POST /v1/api/kuaishou/user-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | The unique user ID on Kuaishou.  |

## Details

Get the public profile for a Kuaishou user identified by user ID. Use it to inspect an account found through user or video results.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/user-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "40300058"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | The unique user ID on Kuaishou. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/kuaishou/user-detail.json`](../../../catalog/models/kuaishou/user-detail.json) · Store page: https://www.sandbase.ai/model/kuaishou/user-detail
