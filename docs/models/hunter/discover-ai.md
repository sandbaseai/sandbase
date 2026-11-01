# Hunter Discover Ai

`hunter/discover-ai` · api · Hunter

Describe target companies in plain language; an AI picks the filters and runs the search.

## Pricing

- **$0.1 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hunter/discover-ai", "query": "AI startups in Paris"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hunter/discover-ai', {'query': 'AI startups in Paris'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hunter/discover-ai", {
  "query": "AI startups in Paris"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hunter/discover-ai", sandbase.Params{
	"query": "AI startups in Paris",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/hunter/discover-ai` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Companies per page. Default and max 100. range 1–100 |
| `query` | string | yes | Natural-language description of the target companies, e.g. 'fintech startups in Singapore founded after 2020'.  |
| `offset` | integer |  | Companies to skip. Max 10,000. range 0–10000 |

## Details

Describe target companies in plain language; an AI picks the filters and runs the search.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hunter/discover-ai" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "AI startups in Paris"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Natural-language description of the target companies, e.g. 'fintech startups in Singapore founded after 2020'. |
| `limit` | integer | No | Companies per page. Default and max 100. |
| `offset` | integer | No | Companies to skip. Max 10,000. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hunter/discover-ai.json`](../../../catalog/models/hunter/discover-ai.json) · Store page: https://www.sandbase.ai/model/hunter/discover-ai
