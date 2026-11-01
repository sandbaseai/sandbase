# Crunchbase Search Organizations

`crunchbase/search-organizations` · api · Crunchbase

Full-text search over Crunchbase organizations. Returns results with organization details including categories, location, employee count, rank, and operating status.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "crunchbase/search-organizations"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('crunchbase/search-organizations', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("crunchbase/search-organizations", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "crunchbase/search-organizations", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/crunchbase/search-organizations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Max results to return. range -9007199254740991–9007199254740991 |
| `query` | string |  | Search keyword for organization name (e.g. 'stripe', 'google'). Omitting returns all organizations.  |

## Details

Full-text search over Crunchbase organizations. Returns results with organization details including categories, location, employee count, rank, and operating status.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/crunchbase/search-organizations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Max results to return. |
| `query` | string | No | Search keyword for organization name (e.g. 'stripe', 'google'). Omitting returns all organizations. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/crunchbase/search-organizations.json`](../../../catalog/models/crunchbase/search-organizations.json) · Store page: https://www.sandbase.ai/model/crunchbase/search-organizations
