# GetApp Compare Software

`getapp/compare-software` · api · GetApp

Compare two software products side-by-side, including features, pricing, reviews, pros/cons, and support options. slug1 is the full product path, slug2 is the comparison product slug.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "getapp/compare-software", "slug1": "collaboration-software/a/monday-com", "slug2": "trello"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('getapp/compare-software', {'slug1': 'collaboration-software/a/monday-com', 'slug2': 'trello'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("getapp/compare-software", {
  "slug1": "collaboration-software/a/monday-com",
  "slug2": "trello"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "getapp/compare-software", sandbase.Params{
	"slug1": "collaboration-software/a/monday-com",
	"slug2": "trello",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/getapp/compare-software` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug1` | string | yes | Full product URL path for the first product (e.g. 'collaboration-software/a/monday-com').  |
| `slug2` | string | yes | Product slug for the second product to compare (e.g. 'notion', 'trello'). Obtainable from popular_comparisons in get_software_details.  |

## Details

Compare two software products side-by-side, including features, pricing, reviews, pros/cons, and support options. slug1 is the full product path, slug2 is the comparison product slug.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/getapp/compare-software" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug1": "collaboration-software/a/monday-com", "slug2": "trello"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug1` | string | Yes | Full product URL path for the first product (e.g. 'collaboration-software/a/monday-com'). |
| `slug2` | string | Yes | Product slug for the second product to compare (e.g. 'notion', 'trello'). Obtainable from popular_comparisons in get_software_details. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/getapp/compare-software.json`](../../../catalog/models/getapp/compare-software.json) · Store page: https://www.sandbase.ai/model/getapp/compare-software
