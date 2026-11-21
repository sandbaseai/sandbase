# Tripo Smart UV API: pricing, parameters and code examples

`tripo3d/tripo/smart-uv` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.2 per call · **Modes:** async

Tripo Smart UV unwraps an existing 3D model into a clean UV layout, optionally baking the textures onto it.

## Pricing

- **$0.2 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/smart-uv", "model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/smart-uv', {'model_url': 'https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/smart-uv", {
  "model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/smart-uv", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bake` | boolean |  | Bake the existing textures onto the new UVs. false returns UVs only. default `true` |
| `compress` | string |  | geometry applies meshopt compression to reduce file size. one of: `geometry` |
| `model_url` | string | yes | URL of the input 3D model, up to 80,000 triangles (a quad counts as 2).  |
| `export_orientation` | string |  | Forward axis of the exported model. Leave unset if you will post-process the model. one of: `+x`, `-x`, `+y`, `-y` |

## Details

Tripo Smart UV unwraps an existing 3D model into a clean UV layout, optionally baking the textures onto it.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the input 3D model, up to 80,000 triangles (a quad counts as 2). |
| `bake` | boolean | `true` | Bake the existing textures onto the new UVs. false returns UVs only. |
| `export_orientation` | `+x` / `-x` / `+y` / `-y` | — | Forward axis of the exported model. Leave unset if you will post-process the model. |
| `compress` | `geometry` | — | geometry applies meshopt compression to reduce file size. |
### Output
- `url`: GLB with the new UVs.
- `uv_render`: UV atlas preview.
### Billing
$0.20 per model.
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/smart-uv.json`](../../../../catalog/models/tripo3d/tripo/smart-uv.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/smart-uv
