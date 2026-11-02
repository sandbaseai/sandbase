# Hunter Companies Find API: pricing, parameters and code examples

`hunter/companies-find` · data API · Hunter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0049 per call (free daily quota) · **Modes:** async

Look up a company's full profile — industry, size, location, tech stack — from its domain.

## Pricing

- **$0.0049 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hunter/companies-find", "domain": "stripe.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hunter/companies-find', {'domain': 'stripe.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hunter/companies-find", {
  "domain": "stripe.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hunter/companies-find", sandbase.Params{
	"domain": "stripe.com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/hunter/companies-find` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | Domain name, e.g. 'stripe.com'. Preferred over company — it skips the name-to-domain conversion.  |

## Details

Look up a company's full profile — industry, size, location, tech stack — from its domain.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hunter/companies-find" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "stripe.com"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | Domain name, e.g. 'stripe.com'. Preferred over company — it skips the name-to-domain conversion. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hunter/companies-find.json`](../../../catalog/models/hunter/companies-find.json) · Store page: https://www.sandbase.ai/model/hunter/companies-find
