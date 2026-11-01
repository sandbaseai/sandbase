# Wellfound Job Autocomplete Roles

`wellfound/job-autocomplete-roles` · api · Wellfound

Get a list of common job role slugs available on Wellfound. These slugs can be used to construct Wellfound role search URLs.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wellfound/job-autocomplete-roles"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wellfound/job-autocomplete-roles', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wellfound/job-autocomplete-roles", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wellfound/job-autocomplete-roles", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/wellfound/job-autocomplete-roles` with the body above minus `model`.

## Details

Get a list of common job role slugs available on Wellfound. These slugs can be used to construct Wellfound role search URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wellfound/job-autocomplete-roles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

This API takes no parameters.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wellfound/job-autocomplete-roles.json`](../../../catalog/models/wellfound/job-autocomplete-roles.json) · Store page: https://www.sandbase.ai/model/wellfound/job-autocomplete-roles
