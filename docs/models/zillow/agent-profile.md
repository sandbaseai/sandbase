# Zillow Agent Profile API: pricing, parameters and code examples

`zillow/agent-profile` · data API · Zillow · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0008 per call (free daily quota) · **Modes:** sync

Fetch one Zillow real estate agent's profile by URL: name, phone, email, brokerage, rating, review count, sales, and service areas.

## Pricing

- **$0.0008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zillow/agent-profile", "url": "https://www.zillow.com/profile/gregorycarlsonATX/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zillow/agent-profile', {'url': 'https://www.zillow.com/profile/gregorycarlsonATX/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zillow/agent-profile", {
  "url": "https://www.zillow.com/profile/gregorycarlsonATX/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zillow/agent-profile", sandbase.Params{
	"url": "https://www.zillow.com/profile/gregorycarlsonATX/",
})
```

Same call via the path form: `POST /v1/api/zillow/agent-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Zillow agent profile URL (e.g. https://www.zillow.com/profile/gregorycarlsonATX/).  |

## Details

Fetch one Zillow real estate agent's profile by URL: name, phone, email, brokerage, rating, review count, sales, and service areas.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "zillow/agent-profile", "url": "https://www.zillow.com/profile/gregorycarlsonATX/"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Zillow agent profile URL (e.g. https://www.zillow.com/profile/gregorycarlsonATX/). |

### Pricing

Flat $0.0008 per call. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/zillow/agent-profile.json`](../../../catalog/models/zillow/agent-profile.json) · Store page: https://www.sandbase.ai/model/zillow/agent-profile
