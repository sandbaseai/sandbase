# G2 Search Software API: pricing, parameters and code examples

`g2/search-software` · data API · G2 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

Full-text search over G2's software product catalog. Returns matching products with name, slug, rating, review count, and description.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "g2/search-software", "query": "crm"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('g2/search-software', {'query': 'crm'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("g2/search-software", {
  "query": "crm"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "g2/search-software", sandbase.Params{
	"query": "crm",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/g2/search-software` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword or query string (e.g. 'slack', 'hubspot', 'project management')  |

## Details

Full-text search over G2's software product catalog. Returns matching products with name, slug, rating, review count, and description.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/g2/search-software" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "crm"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword or query string (e.g. 'slack', 'hubspot', 'project management') |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/g2/search-software.json`](../../../catalog/models/g2/search-software.json) · Store page: https://www.sandbase.ai/model/g2/search-software
