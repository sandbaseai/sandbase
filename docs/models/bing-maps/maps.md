# Bing Maps Maps

`bing-maps/maps` · api · Bing Maps

Search Bing Maps listings around a map center, or look up one entity by id.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing-maps/maps"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bing-maps/maps', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bing-maps/maps", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bing-maps/maps", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/bing-maps/maps` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Search query. Required unless place_id is supplied.  |
| `cp` | string |  | Map center as 'latitude~longitude', such as '47.6062~-122.3321'.  |
| `count` | integer |  | Number of listings, 1-30. Default 30. range 1–30 |
| `first` | integer |  | Listing offset, 0-10,000. Default 0. range 0–10000 |
| `setlang` | string |  | Interface language such as 'en-US'.  |
| `place_id` | string |  | Native Bing Maps entity ID for a detail lookup. Required unless q is supplied.  |

## Details

Search Bing Maps listings around a map center, or look up one entity by id.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bing-maps/maps" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee", "cp": "47.6062~-122.3321"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number of listings, 1-30. Default 30. |
| `cp` | string | No | Map center as 'latitude~longitude', such as '47.6062~-122.3321'. |
| `first` | integer | No | Listing offset, 0-10,000. Default 0. |
| `place_id` | string | No | Native Bing Maps entity ID for a detail lookup. Required unless q is supplied. |
| `q` | string | No | Search query. Required unless place_id is supplied. |
| `setlang` | string | No | Interface language such as 'en-US'. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bing-maps/maps.json`](../../../catalog/models/bing-maps/maps.json) · Store page: https://www.sandbase.ai/model/bing-maps/maps
