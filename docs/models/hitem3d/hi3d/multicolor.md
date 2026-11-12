# Hitem3D Hi3D Multicolor API: pricing, parameters and code examples

`hitem3d/hi3d/multicolor` · image generation model · Hitem3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.4 per call · **Modes:** async

Hi3D Multicolor by Hitem3D converts a textured GLB model into a model with a limited set of flat colors, for multi-color 3D printing.

## Pricing

- **$0.4 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hitem3d/hi3d/multicolor", "model_url": "https://static.sandbase.ai/examples/cf921390-1a95-45c4-bce7-b2526b3601a9/input/6bef0b95-aca3-4a10-b781-41e037547768.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hitem3d/hi3d/multicolor', {'model_url': 'https://static.sandbase.ai/examples/cf921390-1a95-45c4-bce7-b2526b3601a9/input/6bef0b95-aca3-4a10-b781-41e037547768.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hitem3d/hi3d/multicolor", {
  "model_url": "https://static.sandbase.ai/examples/cf921390-1a95-45c4-bce7-b2526b3601a9/input/6bef0b95-aca3-4a10-b781-41e037547768.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hitem3d/hi3d/multicolor", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/cf921390-1a95-45c4-bce7-b2526b3601a9/input/6bef0b95-aca3-4a10-b781-41e037547768.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_url` | string | yes | URL of the input textured model. GLB only, up to 200MB.  |
| `export_format` | string |  | File format of the generated model. one of: `glb`, `obj`, `fbx`; default `"glb"` |
| `number_of_colors` | integer |  | Number of colors (1-8), or 0 for the maximum. default `4`; range 0–8 |

## Details

Hi3D Multicolor by Hitem3D converts a textured GLB model into a model with a limited set of flat colors, for multi-color 3D printing.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the input textured model. GLB only, up to 200MB. |
| `number_of_colors` | integer 0–8 | `4` | Number of colors (1-8), or 0 for the maximum. |
| `export_format` | `glb` / `obj` / `fbx` | `glb` | File format of the generated model. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.40 per request.
Failed runs are not charged.
### Also on SandBase
Other Hitem3D 3D endpoints: `hitem3d/hi3d/image-to-3d`, `hitem3d/hi3d/multi-view-to-3d`, `hitem3d/hi3d/split`, `hitem3d/hi3d/texture`.

---
Machine-readable: [`catalog/models/hitem3d/hi3d/multicolor.json`](../../../../catalog/models/hitem3d/hi3d/multicolor.json) · Store page: https://www.sandbase.ai/model/hitem3d/hi3d/multicolor
