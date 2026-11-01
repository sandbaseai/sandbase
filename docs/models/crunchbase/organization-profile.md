# Crunchbase Organization Profile

`crunchbase/organization-profile` · api · Crunchbase

Fetch a single organization's full profile by its slug (permalink). Returns the organization's properties including categories, location, employee count, rank, and funding status.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "crunchbase/organization-profile", "slug": "slack"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('crunchbase/organization-profile', {'slug': 'slack'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("crunchbase/organization-profile", {
  "slug": "slack"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "crunchbase/organization-profile", sandbase.Params{
	"slug": "slack",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/crunchbase/organization-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Organization permalink/slug (e.g. 'stripe', 'google', 'anthropic').  |

## Details

Fetch a single organization's full profile by its slug (permalink). Returns the organization's properties including categories, location, employee count, rank, and funding status.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/crunchbase/organization-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "slack"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Organization permalink/slug (e.g. 'stripe', 'google', 'anthropic'). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/crunchbase/organization-profile.json`](../../../catalog/models/crunchbase/organization-profile.json) · Store page: https://www.sandbase.ai/model/crunchbase/organization-profile
