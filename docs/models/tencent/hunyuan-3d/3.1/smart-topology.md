# Hunyuan 3D 3.1 Smart Topology API: pricing, parameters and code examples

`tencent/hunyuan-3d/3.1/smart-topology` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.75 per call · **Modes:** async

Hunyuan 3D 3.1 Smart Topology by Tencent retopologizes a GLB or OBJ model into a clean triangle or quad mesh at a chosen polygon density.

## Pricing

- **$0.75 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-3d/3.1/smart-topology", "model_url": "https://static.sandbase.ai/examples/tencent/hunyuan-3d/3.1/smart-topology/input_input_file_url_0.glb"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-3d/3.1/smart-topology', {'model_url': 'https://static.sandbase.ai/examples/tencent/hunyuan-3d/3.1/smart-topology/input_input_file_url_0.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-3d/3.1/smart-topology", {
  "model_url": "https://static.sandbase.ai/examples/tencent/hunyuan-3d/3.1/smart-topology/input_input_file_url_0.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-3d/3.1/smart-topology", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/tencent/hunyuan-3d/3.1/smart-topology/input_input_file_url_0.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_url` | string | yes | URL of the GLB or OBJ model to retopologize. Max 200MB.  |
| `face_level` | string |  | Target polygon density: high keeps more detail, low gives fewer polygons. one of: `high`, `medium`, `low`; default `"medium"` |
| `polygon_type` | string |  | triangle: triangles only. quadrilateral: mixed quads and triangles. one of: `triangle`, `quadrilateral`; default `"triangle"` |
| `input_file_type` | string |  | Format of the input model. one of: `glb`, `obj`; default `"glb"` |

## Details

Hunyuan 3D 3.1 Smart Topology by Tencent retopologizes a GLB or OBJ model into a clean triangle or quad mesh at a chosen polygon density.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the GLB or OBJ model to retopologize. Max 200MB. |
| `input_file_type` | `glb` / `obj` | `glb` | Format of the input model. |
| `polygon_type` | `triangle` / `quadrilateral` | `triangle` | triangle: triangles only. quadrilateral: mixed quads and triangles. |
| `face_level` | `high` / `medium` / `low` | `medium` | Target polygon density: high keeps more detail, low gives fewer polygons. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
### Billing
$0.75 per request.
Failed runs are not charged.
### Also on SandBase
Other Tencent 3D endpoints: `tencent/hunyuan-3d/3.0/image-to-3d`, `tencent/hunyuan-3d/3.1/part`, `tencent/hunyuan-3d/3.1/pro/image-to-3d`, `tencent/hunyuan-3d/3.1/pro/text-to-3d`.

---
Machine-readable: [`catalog/models/tencent/hunyuan-3d/3.1/smart-topology.json`](../../../../../catalog/models/tencent/hunyuan-3d/3.1/smart-topology.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-3d/3.1/smart-topology
