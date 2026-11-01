# GetApp Blog Research

`getapp/blog-research` · api · GetApp

Retrieve blog posts and software research guides from GetApp's resources section. Returns all published posts with metadata, topics, and content hubs.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "getapp/blog-research"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('getapp/blog-research', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("getapp/blog-research", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "getapp/blog-research", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/getapp/blog-research` with the body above minus `model`.

## Details

Retrieve blog posts and software research guides from GetApp's resources section. Returns all published posts with metadata, topics, and content hubs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/getapp/blog-research" \
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
Machine-readable: [`catalog/models/getapp/blog-research.json`](../../../catalog/models/getapp/blog-research.json) · Store page: https://www.sandbase.ai/model/getapp/blog-research
