# Y Combinator Search Founders

`ycombinator/search-founders` · api · Y Combinator

Search the YC founder directory via Algolia. Returns paginated results with founder metadata including name, current company, title, batches, and industries.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ycombinator/search-founders"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ycombinator/search-founders', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ycombinator/search-founders", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ycombinator/search-founders", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ycombinator/search-founders` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (0-indexed). range -9007199254740991–9007199254740991 |
| `limit` | integer |  | Results per page. range -9007199254740991–9007199254740991 |
| `query` | string |  | Search keyword for founder name or company.  |

## Details

Search the YC founder directory via Algolia. Returns paginated results with founder metadata including name, current company, title, batches, and industries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ycombinator/search-founders" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Results per page. |
| `page` | integer | No | Page number (0-indexed). |
| `query` | string | No | Search keyword for founder name or company. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ycombinator/search-founders.json`](../../../catalog/models/ycombinator/search-founders.json) · Store page: https://www.sandbase.ai/model/ycombinator/search-founders
