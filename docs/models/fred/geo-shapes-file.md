# FRED GeoFRED Shape Files

`fred/geo-shapes-file` · api · FRED

GeoFRED Shape Files from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/geo-shapes-file", "shape": "bea"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/geo-shapes-file', {'shape': 'bea'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/geo-shapes-file", {
  "shape": "bea"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/geo-shapes-file", sandbase.Params{
	"shape": "bea",
})
```

Same call via the path form: `POST /v1/api/fred/geo-shapes-file` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shape` | string | yes | The type of shape you want to pull GeoJSON data for. Available Shape Types: bea (Bureau of Economic Anaylis Region) msa (Metropolitan Statistical Area) frb (Federal Reserve Bank Districts) necta (New England City and… one of: `bea`, `msa`, `frb`, `necta`, `state`, `country`, `county`, `censusregion`, `censusdivision` |

## Details

GeoFRED Shape Files from FRED. Returns the official FRED API response unchanged.

The response is the official FRED API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/geo-shapes-file" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shape": "bea"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shape` | string | Yes | The type of shape you want to pull GeoJSON data for. Available Shape Types: bea (Bureau of Economic Anaylis Region) msa (Metropolitan Statistical Area) frb (Fed |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/fred/geo-shapes-file.json`](../../../catalog/models/fred/geo-shapes-file.json) · Store page: https://www.sandbase.ai/model/fred/geo-shapes-file
