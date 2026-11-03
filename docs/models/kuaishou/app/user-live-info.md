# Kuaishou User Broadcast Details API: pricing, parameters and code examples

`kuaishou/app/user-live-info` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns broadcast information and stream status for a specified Kuaishou account. Requests target a creator profile using the unique user identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/user-live-info", "user_id": "3795214411"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/user-live-info', {'user_id': '3795214411'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/user-live-info", {
  "user_id": "3795214411"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/user-live-info", sandbase.Params{
	"user_id": "3795214411",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/user-live-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | 用户ID/User ID  |

## Details

Retrieve streaming details for a Kuaishou user by providing the `user_id` parameter. It returns broadcast activity and stream host data for the requested account.

### Use cases

- Check whether a specific Kuaishou creator is currently streaming.
- Inspect broadcast details and host metadata for a creator profile.
- Integrate creator stream status monitoring into analytics dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/user-live-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3795214411"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | — |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/user-live-info.json`](../../../../catalog/models/kuaishou/app/user-live-info.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/user-live-info
