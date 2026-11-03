# FRED category API: pricing, parameters and code examples

`fred/category` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

category from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/category"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/category', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/category", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/category", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/fred/category` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `category_id` | integer |  | The id for a category. integer, default: 0 (root category) default `0` |

## Details

Returns the name and parent of one FRED category. It takes an optional `category_id`, and the default `0` returns the root category.

### Use cases

- Look up the name of a FRED category when you only have its numeric id.
- Walk up the FRED category tree by following `parent_id` from a known category.
- Confirm that a `category_id` exists before you request its child categories or series.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/category" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_id` | integer | No | The id for a category. integer, default: 0 (root category) |
| `file_type` | string | No | Response format. Only json is supported. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "categories": [
    {
      "id": 0,
      "name": "Categories",
      "parent_id": 0
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `categories[]` | List of matching categories. It holds one item for the requested `category_id`. |
| `categories[].id` | Numeric id of the category. The root category has `id` `0`. |
| `categories[].name` | Display name of the category. The root category is named `Categories`. |
| `categories[].parent_id` | Id of the parent category. The root category shows `0` as its own parent. |

### Notes

- Leave out `category_id` or send `0` to get the root category.
- Call [FRED Get Category Children](/apis/fred/category-children) to list the categories below this one.
- Call [FRED Get Category Series](/apis/fred/category-series) to list the data series inside a category.
- `file_type` accepts only `json`.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/category.json`](../../../catalog/models/fred/category.json) · Store page: https://www.sandbase.ai/model/fred/category
