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

Get Release Tables from FRED. Returns the official FRED API response unchanged.

The response is the official FRED API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/release-tables" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"release_id": 53, "file_type": "json"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `element_id` | integer | No | The release table element id you would like to retrieve. integer, optional When the parameter is not passed, the root(top most) element for the release is given |
| `file_type` | string | No | Response format. Only json is supported. |
| `include_observation_values` | string | No | A flag to indicate that observations need to be returned. Observation value and date will only be returned for a series type element. One of the following strin |
| `observation_date` | string | No | The observation date to be included with the returned release table. YYYY-MM-DD formatted string, optional, default: 9999-12-31 (latest available) |
| `release_id` | integer | Yes | The id for a release. integer, required |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/fred/release-tables.json`](../../../catalog/models/fred/release-tables.json) · Store page: https://www.sandbase.ai/model/fred/release-tables
