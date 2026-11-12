# Meshy 6 Lite Retexture API: pricing, parameters and code examples

`meshy/6.0-lite/retexture` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.36 per call · **Modes:** async

Meshy 6 Lite Retexture is the lower-cost Meshy retexturing model: repaint an existing 3D model from a text or image style.

## Pricing

- **$0.36 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/6.0-lite/retexture", "model_url": "https://static.sandbase.ai/examples/0e3ef03d-79e9-4c67-8540-181fe8251040/input/93745c11-502e-46fa-bc71-ed5454ae3b85.glb", "text_style_prompt": "weathered bronze robot with green patina and gold trim"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/6.0-lite/retexture', {'model_url': 'https://static.sandbase.ai/examples/0e3ef03d-79e9-4c67-8540-181fe8251040/input/93745c11-502e-46fa-bc71-ed5454ae3b85.glb', 'text_style_prompt': 'weathered bronze robot with green patina and gold trim'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/6.0-lite/retexture", {
  "model_url": "https://static.sandbase.ai/examples/0e3ef03d-79e9-4c67-8540-181fe8251040/input/93745c11-502e-46fa-bc71-ed5454ae3b85.glb",
  "text_style_prompt": "weathered bronze robot with green patina and gold trim"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/6.0-lite/retexture", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/0e3ef03d-79e9-4c67-8540-181fe8251040/input/93745c11-502e-46fa-bc71-ed5454ae3b85.glb",
	"text_style_prompt": "weathered bronze robot with green patina and gold trim",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_url` | string | yes | 3D model to texture: .glb, .gltf, .obj, .fbx or .stl URL.  |
| `enable_pbr` | boolean |  | Also generate metallic, roughness and normal maps. default `false` |
| `image_style_url` | string |  | 2D image that guides the texture (JPG or PNG). Takes precedence over text_style_prompt.  |
| `text_style_prompt` | string |  | Describe the texture style, up to 600 characters. Required when image_style_url is not set.  |
| `enable_original_uv` | boolean |  | Use the model's existing UV layout instead of generating new UVs. default `true` |

## Details

Meshy 6 Lite Retexture is the lower-cost Meshy retexturing model: repaint an existing 3D model from a text or image style.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | 3D model URL, required | — | .glb, .gltf, .obj, .fbx or .stl. |
| `text_style_prompt` | string | — | Texture style, up to 600 characters. Required when `image_style_url` is not set. |
| `image_style_url` | image URL | — | JPG or PNG style reference; takes precedence over the text prompt. |
| `enable_pbr` | boolean | false | Also generate metallic, roughness and normal maps. |
| `enable_original_uv` | boolean | true | Keep the model's UV layout. |
### Billing
$0.36 per retextured model; PBR maps are included.
| Request | Price |
|---|---|
| Retexture | $0.36 |
| Retexture + PBR | $0.36 |
Failed runs are not charged.
### Prompting
- Name materials and finish, e.g. "weathered bronze with green patina".
- Provide either `text_style_prompt` or `image_style_url`.
### Also on SandBase
Higher-detail retexture models: `meshy/7.0/retexture`, `meshy/6.0/retexture`.

---
Machine-readable: [`catalog/models/meshy/6.0-lite/retexture.json`](../../../../catalog/models/meshy/6.0-lite/retexture.json) · Store page: https://www.sandbase.ai/model/meshy/6.0-lite/retexture
