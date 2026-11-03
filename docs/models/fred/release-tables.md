# FRED Get Release Tables API: pricing, parameters and code examples

`fred/release-tables` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Release Tables from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/release-tables", "release_id": 53}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/release-tables', {'release_id': 53})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/release-tables", {
  "release_id": 53
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/release-tables", sandbase.Params{
	"release_id": 53,
})
```

Same call via the path form: `POST /v1/api/fred/release-tables` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `element_id` | integer |  | The release table element id you would like to retrieve. integer, optional When the parameter is not passed, the root(top most) element for the release is given.  |
| `release_id` | integer | yes | The id for a release. integer, required  |
| `observation_date` | string |  | The observation date to be included with the returned release table. YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) default `"9999-12-31"` |
| `include_observation_values` | string |  | A flag to indicate that observations need to be returned. Observation value and date will only be returned for a series type element. One of the following strings: 'true', 'false'. optional, default: false one of: `true`, `false`; default `"false"` |

## Details

Returns the table structure of a FRED release as a set of elements, such as sections, groups and series. It needs a `release_id`. Without an `element_id`, it returns the top-level elements of the release.

### Use cases

- List the top-level sections of a release, for example the sections of release 53.
- Walk a release table one element at a time by passing each `element_id` back into the request.
- Find the `series_id` behind a table line so you can pull its data.
- Add `include_observation_values` to get observation values and dates for series elements in a table.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/release-tables" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"release_id": 53, "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `release_id` | integer | Yes | The id for a release. integer, required |
| `element_id` | integer | No | The release table element id you would like to retrieve. integer, optional When the parameter is not passed, the root(top most) element for the release is given. |
| `file_type` | string | No | Response format. Only json is supported. |
| `include_observation_values` | string | No | A flag to indicate that observations need to be returned. Observation value and date will only be returned for a series type element. One of the following strings: 'true', 'false'. optional, default: false |
| `observation_date` | string | No | The observation date to be included with the returned release table. YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "elements": {
    "13690": {
      "children": [],
      "element_id": 13690,
      "level": "0",
      "line": null,
      "name": "Section 1 - Domestic Product and Income",
      "parent_id": null,
      "release_id": 53,
      "series_id": null,
      "type": "section"
    },
    "15424": {
      "children": [],
      "element_id": 15424,
      "level": "0",
      "line": null,
      "name": "Section 6 - Income and Employment by Industry",
      "parent_id": null,
      "release_id": 53,
      "series_id": null,
      "type": "section"
    },
    "15425": {
      "children": [],
      "element_id": 15425,
      "level": "0",
      "line": null,
      "name": "Section 7 - Supplemental Tables",
      "parent_id": null,
      "release_id": 53,
      "series_id": null,
      "type": "section"
    },
    "291652": {
      "children": [],
      "element_id": 291652,
      "level": "0",
      "line": null,
      "name": "Section 8 - Not Seasonally Adjusted",
      "parent_id": null,
      "release_id": 53,
      "series_id": null,
      "type": "section"
    },
    "4081": {
      "children": [],
      "element_id": 4081,
      "level": "0",
      "line": null,
      "name": "Section 2 - Personal Income and Outlays",
      "parent_id": null,
      "release_id": 53,
      "series_id": null,
      "type": "section"
    },
    "5221": {
      "children": [],
      "element_id": 5221,
      "level": "0",
      "line": null,
      "name": "Section 3 - Government Current Receipts and Expenditures",
      "parent_id": null,
      "release_id": 53,
      "series_id": null,
      "type": "section"
    },
    "5402": {
      "children": [],
      "element_id": 5402,
      "level": "0",
      "line": null,
      "name": "Section 4 - Foreign Transactions",
      "parent_id": null,
      "release_id": 53,
      "series_id": null,
      "type": "section"
    },
    "7579": {
      "children": [],
      "element_id": 7579,
      "level": "0",
      "line": null,
      "name": "Section 5 - Saving and Investment",
      "parent_id": null,
      "release_id": 53,
      "series_id": null,
      "type": "section"
    }
  },
  "release_id": "53"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `elements` | Object keyed by element id. Each value describes one element of the release table. |
| `elements.*.element_id` | Numeric id of the element. Pass it as `element_id` to request that element. |
| `elements.*.name` | Display name of the element, such as `Section 1 - Domestic Product and Income`. |
| `elements.*.type` | Kind of element. In this response all elements are `section`. |
| `elements.*.children` | List of child elements under this element. It is empty in this response. |
| `elements.*.parent_id` | Element id of the parent. It is `null` for top-level elements. |
| `elements.*.level` | Depth of the element in the table, as a string. Top-level sections show `0`. |
| `elements.*.series_id / elements.*.line` | FRED series id and table line for the element. Both are `null` for sections. |
| `release_id` | The release id that the table belongs to, returned as a string. |

### Notes

- Get the `release_id` from [FRED Get Releases](/apis/fred/releases). Example: `53`.
- Element ids are the keys of `elements`. Use one as `element_id` to look at that part of the table.
- Observation values and dates appear only for series type elements, and only when `include_observation_values` is `true`.
- Use `observation_date` in `YYYY-MM-DD` format to pick the date for the returned observations. Use [FRED Get Series Observations](/apis/fred/series-observations) for the full history of a series.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/release-tables.json`](../../../catalog/models/fred/release-tables.json) · Store page: https://www.sandbase.ai/model/fred/release-tables
