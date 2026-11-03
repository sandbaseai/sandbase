# 1688 Category Info API: pricing, parameters and code examples

`1688/category/info` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get a 1688 category and its child categories by category ID, or the root categories when no ID is given.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/category/info"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/category/info', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/category/info", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/category/info", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/1688/category/info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `catId` | string |  | 1688 platform category ID.  |

## Details

Returns a 1688 category and its child categories. Send a `catId` to get that category with its children, or send no input to get the root categories.

### Use cases

- Build a full 1688 category tree by starting with no `catId` and walking down through `children[].id`.
- Map Chinese category names to English labels using `name` and `name_en` for a catalog or translation table.
- Check `children[].has_children` to decide which categories need another call to reach leaf categories.
- Collect category IDs to use when listing products in a category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/category/info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `catId` | string | No | 1688 platform category ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "children": [
    {
      "has_children": true,
      "id": "130823000",
      "level": 0,
      "name": "成人用品",
      "name_en": "Adult Products"
    }
  ],
  "id": "",
  "level": null,
  "name": "",
  "name_en": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `children[]` | List of child categories. With no `catId` in the request, this list holds the root categories. |
| `children[].id` | Category ID as a string. Use it as `catId` in the next call. |
| `children[].name` | Category name in Chinese. |
| `children[].name_en` | Category name in English. |
| `children[].has_children` | `true` when the category has child categories below it. Use it to decide whether to go deeper. |
| `children[].level` | Depth number of the child category. Root categories show `0`. |
| `id / name / name_en` | ID and names of the requested category. These are empty strings when no `catId` is sent. |
| `level` | Depth of the requested category. It is `null` when no `catId` is sent. |

### Notes

- Leave `catId` out to get the root categories. The top-level `id`, `name` and `name_en` are then empty and `level` is `null`.
- `id` values are strings, for example `"130823000"` and `"54"`. Pass them back unchanged as `catId`.
- To list products in a category, call [1688 Category Products](/apis/1688/category/items) with a category ID from this response.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/category/info.json`](../../../../catalog/models/1688/category/info.json) · Store page: https://www.sandbase.ai/model/1688/category/info
