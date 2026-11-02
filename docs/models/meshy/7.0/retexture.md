# Meshy 7 Retexture API: pricing, parameters and code examples

`meshy/7.0/retexture` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.33 to $0.5 per run, depending on parameters · **Modes:** async

Meshy 7 Retexture repaints an existing 3D model from a text or image style, with optional PBR maps and up to 8K textures.

## Pricing

- Depends on parameters (`params.texture_resolution`).

| parameters | USD |
|---|---|
| texture_resolution="2k" | 0.33 |
| texture_resolution="4k" | 0.33 |
| texture_resolution="8k" | 0.5 |

Formula: `(params.texture_resolution ?? "2k") == "8k" ? 0.5 : 0.33`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/7.0/retexture", "model_url": "<model_url>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/7.0/retexture', {'model_url': '<model_url>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/7.0/retexture", {
  "model_url": "<model_url>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/7.0/retexture", sandbase.Params{
	"model_url": "<model_url>",
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
| `texture_resolution` | string |  | Base color resolution. 8k costs more; at 8k PBR maps are 4k. one of: `2k`, `4k`, `8k`; default `"2k"` |

## Details

Meshy 7 Retexture repaints an existing 3D model from a text or image style, with optional PBR maps and up to 8K textures.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | 3D model URL, required | — | .glb, .gltf, .obj, .fbx or .stl. |
| `text_style_prompt` | string | — | Texture style, up to 600 characters. Required when `image_style_url` is not set. |
| `image_style_url` | image URL | — | JPG or PNG style reference; takes precedence over the text prompt. |
| `texture_resolution` | `2k` / `4k` / `8k` | `2k` | Base color resolution; 8k costs more and its PBR maps are 4k. |
| `enable_pbr` | boolean | false | Also generate metallic, roughness and normal maps. |
| `enable_original_uv` | boolean | true | Keep the model's UV layout. |
### Billing
$0.33 per retextured model at 2k or 4k, $0.50 at 8k; PBR maps are included.
| Request | Price |
|---|---|
| 2k (default) | $0.33 |
| 4k + PBR | $0.33 |
| 8k | $0.50 |
Failed runs are not charged.
### Prompting
- Name materials and finish, e.g. "weathered bronze with green patina".
- Provide either `text_style_prompt` or `image_style_url`.
### Also on SandBase
Other retexture models: `meshy/6.0/retexture`, `meshy/6.0-lite/retexture`. Generate a model first with `meshy/7.1/text-to-3d` or `meshy/7.1/image-to-3d`.

---
Machine-readable: [`catalog/models/meshy/7.0/retexture.json`](../../../../catalog/models/meshy/7.0/retexture.json) · Store page: https://www.sandbase.ai/model/meshy/7.0/retexture
