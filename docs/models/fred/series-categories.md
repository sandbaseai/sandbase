# FRED Get Series Categories API: pricing, parameters and code examples

`fred/series-categories` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Series Categories from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/series-categories", "series_id": "GNPCA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/series-categories', {'series_id': 'GNPCA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/series-categories", {
  "series_id": "GNPCA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/series-categories", sandbase.Params{
	"series_id": "GNPCA",
})
```

Same call via the path form: `POST /v1/api/fred/series-categories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `series_id` | string | yes | The id for a series. string, required  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns the FRED categories that a data series belongs to. It needs a `series_id`, such as `GNPCA`. Each category comes with its `id`, `name` and `parent_id`.

### Use cases

- Find which FRED category holds a series so you can browse its sibling series.
- Build a breadcrumb or topic label for a series in a dashboard.
- Map a list of series IDs to their categories to group them by topic.
- Climb the category tree from a series by following `parent_id` values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series-categories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "GNPCA", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_id` | string | Yes | The id for a series. string, required |
| `file_type` | string | No | Response format. Only json is supported. |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "categories": [
    {
      "id": 106,
      "name": "GDP/GNP",
      "parent_id": 18
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `categories[]` | List of categories the series belongs to. A series can belong to more than one category. |
| `categories[].id` | Numeric ID of the category. Pass it as the category ID to the other FRED category APIs. |
| `categories[].name` | Display name of the category, for example `GDP/GNP`. |
| `categories[].parent_id` | `id` of the parent category. Use it to walk up the category tree. |

### Notes

- Get the `series_id` from the FRED series page URL, or from [FRED Search Series](/apis/fred/series-search).
- Use the returned `id` with [FRED Get Category Children](/apis/fred/category-children) to see subcategories, or with [FRED Get Category Series](/apis/fred/category-series) to list series in the category.
- `realtime_start` and `realtime_end` are optional and use `YYYY-MM-DD` format.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/series-categories.json`](../../../catalog/models/fred/series-categories.json) · Store page: https://www.sandbase.ai/model/fred/series-categories
