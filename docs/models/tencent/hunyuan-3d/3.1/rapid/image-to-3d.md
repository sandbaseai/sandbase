# Hunyuan 3D 3.1 Rapid Image to 3D API: pricing, parameters and code examples

`tencent/hunyuan-3d/3.1/rapid/image-to-3d` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.27 to $0.375 per run, depending on parameters · **Modes:** async

Hunyuan 3D 3.1 Rapid by Tencent quickly turns a single image into a textured or geometry-only 3D model.

## Pricing

- Depends on parameters (`params.enable_pbr`).

| parameters | USD |
|---|---|
| enable_pbr=false | 0.27 |
| enable_pbr=true | 0.375 |

Formula: `(params.enable_pbr ?? false) ? 0.375 : 0.27`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-3d/3.1/rapid/image-to-3d", "image": "https://static.sandbase.ai/examples/tencent/hunyuan-3d/3.1/rapid/image-to-3d/input_image_0.png"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-3d/3.1/rapid/image-to-3d', {'image': 'https://static.sandbase.ai/examples/tencent/hunyuan-3d/3.1/rapid/image-to-3d/input_image_0.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-3d/3.1/rapid/image-to-3d", {
  "image": "https://static.sandbase.ai/examples/tencent/hunyuan-3d/3.1/rapid/image-to-3d/input_image_0.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-3d/3.1/rapid/image-to-3d", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/tencent/hunyuan-3d/3.1/rapid/image-to-3d/input_image_0.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Front view image URL. 128-5000px, max 8MB, JPG/PNG/WEBP. Works best with a single object on a simple background.  |
| `enable_pbr` | boolean |  | Generate PBR materials (metallic, roughness, normal maps). Ignored when Geometry Only is on. default `false` |
| `enable_geometry` | boolean |  | Generate a geometry-only white model without textures. default `false` |

## Details

Hunyuan 3D 3.1 Rapid by Tencent quickly turns a single image into a textured or geometry-only 3D model.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Front view image URL. 128-5000px, max 8MB, JPG/PNG/WEBP. Works best with a single object on a simple background. |
| `enable_pbr` | boolean | `false` | Generate PBR materials (metallic, roughness, normal maps). Ignored when Geometry Only is on. |
| `enable_geometry` | boolean | `false` | Generate a geometry-only white model without textures. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.27 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| enable_pbr on | $0.375 |
| enable_pbr off | $0.27 |
Failed runs are not charged.
### Also on SandBase
Other Tencent 3D endpoints: `tencent/hunyuan-3d/3.0/image-to-3d`, `tencent/hunyuan-3d/3.1/part`, `tencent/hunyuan-3d/3.1/pro/image-to-3d`, `tencent/hunyuan-3d/3.1/pro/text-to-3d`.

---
Machine-readable: [`catalog/models/tencent/hunyuan-3d/3.1/rapid/image-to-3d.json`](../../../../../../catalog/models/tencent/hunyuan-3d/3.1/rapid/image-to-3d.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-3d/3.1/rapid/image-to-3d
