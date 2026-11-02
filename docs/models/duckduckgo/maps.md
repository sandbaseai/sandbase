# DuckDuckGo Maps API: pricing, parameters and code examples

`duckduckgo/maps` · data API · DuckDuckGo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** async

Search DuckDuckGo Maps for places inside a viewport rectangle or around a center.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "duckduckgo/maps", "q": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('duckduckgo/maps', {'q': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("duckduckgo/maps", {
  "q": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "duckduckgo/maps", sandbase.Params{
	"q": "coffee",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/duckduckgo/maps` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Place or category query, up to 500 characters.  |
| `lat` | number |  | Viewport center latitude. Requires lon. range -90–90 |
| `lon` | number |  | Viewport center longitude. Requires lat. range -180–180 |
| `bbox` | string |  | Viewport rectangle as 'top,left,bottom,right'. Required unless lat and lon are supplied.  |
| `strict_bbox` | boolean |  | Exclude results outside the requested bounds. Default true.  |

## Details

Search DuckDuckGo Maps for places inside a viewport rectangle or around a center.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/duckduckgo/maps" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee", "lat": 40.7128, "lon": -74.006}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Place or category query, up to 500 characters. |
| `bbox` | string | No | Viewport rectangle as 'top,left,bottom,right'. Required unless lat and lon are supplied. |
| `lat` | number | No | Viewport center latitude. Requires lon. |
| `lon` | number | No | Viewport center longitude. Requires lat. |
| `strict_bbox` | boolean | No | Exclude results outside the requested bounds. Default true. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/duckduckgo/maps.json`](../../../catalog/models/duckduckgo/maps.json) · Store page: https://www.sandbase.ai/model/duckduckgo/maps
