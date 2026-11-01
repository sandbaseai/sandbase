# Built In Suggest Job Titles

`builtin/suggest-job-titles` · api · Built In

Returns up to 10 autocomplete suggestions for job title searches, matching the query prefix against Built In's job title index. Useful for building type-ahead search interfaces.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "builtin/suggest-job-titles", "query": "software engineer"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('builtin/suggest-job-titles', {'query': 'software engineer'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("builtin/suggest-job-titles", {
  "query": "software engineer"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "builtin/suggest-job-titles", sandbase.Params{
	"query": "software engineer",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/builtin/suggest-job-titles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Partial job title prefix to get suggestions for  |

## Details

Returns up to 10 autocomplete suggestions for job title searches, matching the query prefix against Built In's job title index. Useful for building type-ahead search interfaces.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/builtin/suggest-job-titles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "software engineer"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Partial job title prefix to get suggestions for |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/builtin/suggest-job-titles.json`](../../../catalog/models/builtin/suggest-job-titles.json) · Store page: https://www.sandbase.ai/model/builtin/suggest-job-titles
