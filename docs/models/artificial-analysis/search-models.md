# Artificial Analysis Search Models

`artificial-analysis/search-models` · api · Artificial Analysis

Search for models by name or slug. Performs client-side filtering against the full models list, matching the query string against model name, slug, and shortName fields (case-insensitive substring match).

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "artificial-analysis/search-models", "query": "gpt"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('artificial-analysis/search-models', {'query': 'gpt'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("artificial-analysis/search-models", {
  "query": "gpt"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "artificial-analysis/search-models", sandbase.Params{
	"query": "gpt",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/artificial-analysis/search-models` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword to match against model names, slugs, and short names (e.g., 'claude', 'gpt', 'llama')  |

## Details

Search for models by name or slug. Performs client-side filtering against the full models list, matching the query string against model name, slug, and shortName fields (case-insensitive substring match).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/artificial-analysis/search-models" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "gpt"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword to match against model names, slugs, and short names (e.g., 'claude', 'gpt', 'llama') |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/artificial-analysis/search-models.json`](../../../catalog/models/artificial-analysis/search-models.json) · Store page: https://www.sandbase.ai/model/artificial-analysis/search-models
