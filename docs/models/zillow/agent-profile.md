# Zillow Agent Profile

`zillow/agent-profile` · api · Zillow

Retrieve a real estate agent's full profile by their username/URL slug. Returns sales stats, reviews, listings, service areas, and professional information.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zillow/agent-profile", "username": "everydoorrealestate"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zillow/agent-profile', {'username': 'everydoorrealestate'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zillow/agent-profile", {
  "username": "everydoorrealestate"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zillow/agent-profile", sandbase.Params{
	"username": "everydoorrealestate",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/zillow/agent-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Agent's Zillow profile username/slug (e.g., 'everydoorrealestate')  |

## Details

Retrieve a real estate agent's full profile by their username/URL slug. Returns sales stats, reviews, listings, service areas, and professional information.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zillow/agent-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "everydoorrealestate"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Agent's Zillow profile username/slug (e.g., 'everydoorrealestate') |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zillow/agent-profile.json`](../../../catalog/models/zillow/agent-profile.json) · Store page: https://www.sandbase.ai/model/zillow/agent-profile
