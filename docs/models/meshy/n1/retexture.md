# Meshy N1 Retexture API: pricing, parameters and code examples

`meshy/n1/retexture` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.4 per call · **Modes:** async

Meshy N1 Retexture repaints an existing 3D model from one reference image or up to four reference views, producing a 2K base color texture.

## Pricing

- **$0.4 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/n1/retexture", "model_url": "https://static.sandbase.ai/examples/meshy/n1/retexture/input_model_url_0.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/n1/retexture', {'model_url': 'https://static.sandbase.ai/examples/meshy/n1/retexture/input_model_url_0.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/n1/retexture", {
  "model_url": "https://static.sandbase.ai/examples/meshy/n1/retexture/input_model_url_0.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/n1/retexture", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/meshy/n1/retexture/input_model_url_0.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_url` | string | yes | URL of the 3D model to texture. Supports .glb, .gltf, .obj, .fbx and .stl.  |
| `image_style_url` | string |  | Single reference image of the target texture, treated as the front view. Provide this or multiview_image_urls.  |
| `enable_original_uv` | boolean |  | Use the model's original UV mapping instead of generating new UVs. default `true` |
| `multiview_image_urls` | array |  | 1 to 4 reference views of the target texture; the first is the front view. Cannot be combined with image_style_url.  |

## Details

Meshy N1 Retexture repaints an existing 3D model from one reference image or up to four reference views, producing a 2K base color texture.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the 3D model to texture. Supports .glb, .gltf, .obj, .fbx and .stl. |
| `image_style_url` | image URL | — | Single reference image of the target texture, treated as the front view. Provide this or multiview_image_urls. |
| `multiview_image_urls` | image URLs (1–4) | — | 1 to 4 reference views of the target texture; the first is the front view. Cannot be combined with image_style_url. |
| `enable_original_uv` | boolean | `true` | Use the model's original UV mapping instead of generating new UVs. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.40 per request.
Failed runs are not charged.
### Also on SandBase
Other Meshy 3D endpoints: `meshy/6.0-lite/retexture`, `meshy/6.0/retexture`, `meshy/7.0/image-to-3d`, `meshy/7.0/multi-image-to-3d`.

---
Machine-readable: [`catalog/models/meshy/n1/retexture.json`](../../../../catalog/models/meshy/n1/retexture.json) · Store page: https://www.sandbase.ai/model/meshy/n1/retexture
