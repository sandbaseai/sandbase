# Trustpilot Companies By Category

`trustpilot/companies-by-category` · api · Trustpilot

List companies within a specific category with pagination. Returns companies sorted by trust score.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trustpilot/companies-by-category", "slug": "bank"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trustpilot/companies-by-category', {'slug': 'bank'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trustpilot/companies-by-category", {
  "slug": "bank"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trustpilot/companies-by-category", sandbase.Params{
	"slug": "bank",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/trustpilot/companies-by-category` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number range -9007199254740991–9007199254740991 |
| `slug` | string | yes | Category slug from get_categories (e.g. 'bank', 'animals_pets', 'insurance_agency')  |

## Details

List companies within a specific category with pagination. Returns companies sorted by trust score.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/trustpilot/companies-by-category" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "bank", "page": 1}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Category slug from get_categories (e.g. 'bank', 'animals_pets', 'insurance_agency') |
| `page` | integer | No | Page number |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/trustpilot/companies-by-category.json`](../../../catalog/models/trustpilot/companies-by-category.json) · Store page: https://www.sandbase.ai/model/trustpilot/companies-by-category
