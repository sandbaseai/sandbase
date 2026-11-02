# Youku User Profile API: pricing, parameters and code examples

`youku/user-detail` · data API · Youku · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get a Youku user profile identified by UID. Use it to look up a known account for creator research, profile review, or related video discovery.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youku/user-detail", "uid": "UMTM2MTEzNzk5Ng=="}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youku/user-detail', {'uid': 'UMTM2MTEzNzk5Ng=='})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youku/user-detail", {
  "uid": "UMTM2MTEzNzk5Ng=="
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youku/user-detail", sandbase.Params{
	"uid": "UMTM2MTEzNzk5Ng==",
})
```

Same call via the path form: `POST /v1/api/youku/user-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | The unique identifier for the user.  |

## Details

Get a Youku user profile identified by UID. Use it to look up a known account for creator research, profile review, or related video discovery.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youku/user-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "UMTM2MTEzNzk5Ng=="}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | The unique identifier for the user. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/youku/user-detail.json`](../../../catalog/models/youku/user-detail.json) · Store page: https://www.sandbase.ai/model/youku/user-detail
