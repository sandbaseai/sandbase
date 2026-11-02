# Kuaishou User Published Videos API: pricing, parameters and code examples

`kuaishou/user-video-list` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get public videos published by a Kuaishou user, with optional cursor-based pagination. Use it to review a creator's content history or select videos for detail and comment requests.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/user-video-list", "userId": "40300058"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/user-video-list', {'userId': '40300058'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/user-video-list", {
  "userId": "40300058"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/user-video-list", sandbase.Params{
	"userId": "40300058",
})
```

Same call via the path form: `POST /v1/api/kuaishou/user-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | The unique user ID on Kuaishou.  |
| `pcursor` | string |  | Pagination cursor for subsequent pages.  |

## Details

Get public videos published by a Kuaishou user, with optional cursor-based pagination. Use it to review a creator's content history or select videos for detail and comment requests.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/user-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "40300058"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | The unique user ID on Kuaishou. |
| `pcursor` | string | No | Pagination cursor for subsequent pages. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/kuaishou/user-video-list.json`](../../../catalog/models/kuaishou/user-video-list.json) · Store page: https://www.sandbase.ai/model/kuaishou/user-video-list
