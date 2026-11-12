# Tripo P1 Text to 3D API: pricing, parameters and code examples

`tripo3d/tripo-p1/text-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.36 to $0.48 per run, depending on parameters · **Modes:** async

Tripo P1 is Tripo3D's text-to-3D model. It generates a 3D mesh with optional textures from a text description.

## Pricing

- Depends on parameters (`params.texture`).

| parameters | USD |
|---|---|
| texture=false | 0.36 |
| texture=true | 0.48 |

Formula: `(params.texture ?? true) ? 0.48 : 0.36`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-p1/text-to-3d", "prompt": "A potted bonsai tree with twisted trunk and lush green foliage in a glazed blue pot"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-p1/text-to-3d', {'prompt': 'A potted bonsai tree with twisted trunk and lush green foliage in a glazed blue pot'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-p1/text-to-3d", {
  "prompt": "A potted bonsai tree with twisted trunk and lush green foliage in a glazed blue pot"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-p1/text-to-3d", sandbase.Params{
	"prompt": "A potted bonsai tree with twisted trunk and lush green foliage in a glazed blue pot",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Seed for reproducible geometry generation.  |
| `prompt` | string | yes | Text description of the 3D object to generate. Maximum 1024 characters.  |
| `texture` | boolean |  | Generate textures. Set to false for an untextured mesh (cheaper). default `true` |
| `face_limit` | integer |  | Target face count of the mesh. Adaptive when unset. range 48–20000 |

## Details

Tripo P1 is Tripo3D's text-to-3D model. It generates a 3D mesh with optional textures from a text description.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text description of the 3D object to generate. Maximum 1024 characters. |
| `texture` | boolean | `true` | Generate textures. Set to false for an untextured mesh (cheaper). |
| `face_limit` | integer 48–20000 | — | Target face count of the mesh. Adaptive when unset. |
| `seed` | integer | — | Seed for reproducible geometry generation. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.48 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| texture on | $0.48 |
| texture off | $0.36 |
Failed runs are not charged.
### Also on SandBase
Other Tripo3D 3D endpoints: `tripo3d/tripo-h3.1/image-to-3d`, `tripo3d/tripo-h3.1/multiview-to-3d`, `tripo3d/tripo-h3.1/text-to-3d`, `tripo3d/tripo-p1/image-to-3d`.

---
Machine-readable: [`catalog/models/tripo3d/tripo-p1/text-to-3d.json`](../../../../catalog/models/tripo3d/tripo-p1/text-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-p1/text-to-3d
