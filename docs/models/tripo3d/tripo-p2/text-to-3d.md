# Tripo P2 Text to 3D API: pricing, parameters and code examples

`tripo3d/tripo-p2/text-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $1.2 to $1.56 per run, depending on parameters · **Modes:** async

Tripo P2 is Tripo3D's latest flagship 3D generation model. It turns a text description into a production-ready mesh with optional PBR textures.

## Pricing

- Depends on parameters (`params.pbr`, `params.texture`, `params.texture_quality`).

| parameters | USD |
|---|---|
| pbr=false, texture=false, texture_quality="fast" | 1.2 |
| pbr=false, texture=false, texture_quality="standard" | 1.2 |
| pbr=false, texture=false, texture_quality="detailed" | 1.2 |
| pbr=false, texture=false, texture_quality="extreme" | 1.2 |
| pbr=false, texture=true, texture_quality="fast" | 1.32 |
| pbr=false, texture=true, texture_quality="standard" | 1.32 |
| pbr=false, texture=true, texture_quality="detailed" | 1.44 |
| pbr=false, texture=true, texture_quality="extreme" | 1.56 |
| pbr=true, texture=false, texture_quality="fast" | 1.32 |
| pbr=true, texture=false, texture_quality="standard" | 1.32 |
| pbr=true, texture=false, texture_quality="detailed" | 1.44 |
| pbr=true, texture=false, texture_quality="extreme" | 1.56 |
| pbr=true, texture=true, texture_quality="fast" | 1.32 |
| pbr=true, texture=true, texture_quality="standard" | 1.32 |
| pbr=true, texture=true, texture_quality="detailed" | 1.44 |
| pbr=true, texture=true, texture_quality="extreme" | 1.56 |

Formula: `((params.texture ?? true) || (params.pbr ?? true)) ? ((params.texture_quality ?? "standard") == "extreme" ? 1.56 : (params.texture_quality ?? "standard") == "detailed" ? 1.44 : 1.32) : 1.20`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-p2/text-to-3d", "prompt": "An ornate Japanese stone lantern covered in patches of green moss"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-p2/text-to-3d', {'prompt': 'An ornate Japanese stone lantern covered in patches of green moss'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-p2/text-to-3d", {
  "prompt": "An ornate Japanese stone lantern covered in patches of green moss"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-p2/text-to-3d", sandbase.Params{
	"prompt": "An ornate Japanese stone lantern covered in patches of green moss",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pbr` | boolean |  | Generate PBR materials (also enables texture). default `true` |
| `quad` | boolean |  | Generate quad mesh topology instead of triangles. default `false` |
| `seed` | integer |  | Seed for reproducible geometry generation.  |
| `prompt` | string | yes | Text description of the 3D object to generate. Maximum 1024 characters.  |
| `texture` | boolean |  | Generate textures. Set both texture and pbr to false for an untextured model. default `true` |
| `face_limit` | integer |  | Maximum faces (quad meshes up to 25,000). range 48–50000 |
| `negative_prompt` | string |  | Features to avoid in the generated model.  |
| `texture_quality` | string |  | Texture quality tier. one of: `fast`, `standard`, `detailed`, `extreme`; default `"standard"` |

## Details

Tripo P2, Tripo's flagship 3D model, turns a text prompt into a production-ready mesh with optional PBR textures.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 1,024 characters. |
| `texture` | boolean | true | Generate textures. |
| `pbr` | boolean | true | PBR materials. |
| `quad` | boolean | false | Quad mesh output. |
| `face_limit` | integer 48–50000 | — | Maximum face count. |
| `texture_quality` | `fast` / `standard` / `detailed` / `extreme` | `standard` | Texture detail; higher costs more. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `negative_prompt` | string | — | What to avoid. |

### Billing

$1.32 per textured model at standard texture quality, $1.44 detailed, $1.56 extreme; $1.20 untextured.

| Texture | Price |
|---|---|
| standard | $1.32 |
| detailed | $1.44 |
| extreme | $1.56 |
| Untextured | $1.20 |

Failed runs are not charged.

### Also on SandBase

Other Tripo endpoints: `tripo3d/tripo-p2/image-to-3d`, `tripo3d/tripo-h3.1/text-to-3d`, `tripo3d/tripo-h3.1/image-to-3d`.

---
Machine-readable: [`catalog/models/tripo3d/tripo-p2/text-to-3d.json`](../../../../catalog/models/tripo3d/tripo-p2/text-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-p2/text-to-3d
