# Twitter Check user live status API: pricing, parameters and code examples

`twitter/web/user-live-status` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Check user live status on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-live-status", "rest_id": "44196397"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-live-status', {'rest_id': '44196397'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-live-status", {
  "rest_id": "44196397"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-live-status", sandbase.Params{
	"rest_id": "44196397",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-live-status` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `rest_id` | string | yes | User Rest ID  |

## Details

Check user live status on Twitter. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-live-status" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"rest_id": "44196397"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `rest_id` | string | Yes | User Rest ID |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/twitter/web/user-live-status.json`](../../../../catalog/models/twitter/web/user-live-status.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-live-status
