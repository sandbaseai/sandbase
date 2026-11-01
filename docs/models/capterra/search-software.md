# Capterra Search Software

`capterra/search-software` · api · Capterra

Search for software products by keyword. Returns matching products with name, numeric ID, URL slug, and full URL.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "capterra/search-software", "query": "CRM"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('capterra/search-software', {'query': 'CRM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("capterra/search-software", {
  "query": "CRM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "capterra/search-software", sandbase.Params{
	"query": "CRM",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/capterra/search-software` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The search keyword (e.g. 'CRM', 'project management', 'accounting').  |

## Details

Search for software products by keyword. Returns matching products with name, numeric ID, URL slug, and full URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/capterra/search-software" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "CRM"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The search keyword (e.g. 'CRM', 'project management', 'accounting'). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/capterra/search-software.json`](../../../catalog/models/capterra/search-software.json) · Store page: https://www.sandbase.ai/model/capterra/search-software
