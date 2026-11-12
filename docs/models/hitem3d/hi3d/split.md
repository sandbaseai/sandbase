# Hitem3D Hi3D Split API: pricing, parameters and code examples

`hitem3d/hi3d/split` · image generation model · Hitem3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.4 per call · **Modes:** async

Hi3D Split by Hitem3D splits a 3D model into parts, either by a humanoid character template with optional joints or by granularity for general objects.

## Pricing

- **$0.4 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hitem3d/hi3d/split", "model_url": "https://static.sandbase.ai/examples/ab183559-ca86-4f65-8726-fb4f14c115d7/input/a94a552e-b3b8-4893-a2d6-c3fc02919038.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hitem3d/hi3d/split', {'model_url': 'https://static.sandbase.ai/examples/ab183559-ca86-4f65-8726-fb4f14c115d7/input/a94a552e-b3b8-4893-a2d6-c3fc02919038.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hitem3d/hi3d/split", {
  "model_url": "https://static.sandbase.ai/examples/ab183559-ca86-4f65-8726-fb4f14c115d7/input/a94a552e-b3b8-4893-a2d6-c3fc02919038.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hitem3d/hi3d/split", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/ab183559-ca86-4f65-8726-fb4f14c115d7/input/a94a552e-b3b8-4893-a2d6-c3fc02919038.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `part` | string |  | Character split template: a 6 parts, b 5, c 4 without head, d 4 with head, e 3, f 2. one of: `a`, `b`, `c`, `d`, `e`, `f`; default `"a"` |
| `joint` | string |  | Joint type added between character parts. one of: `none`, `ball`, `dovetail`; default `"ball"` |
| `level` | string |  | Split granularity for general mode. one of: `low`, `medium`, `high`; default `"medium"` |
| `model_url` | string | yes | URL of the input model. GLB, STL or OBJ, up to 200MB.  |
| `split_mode` | string |  | character splits humanoid models using a template; general splits any model by granularity. one of: `character`, `general`; default `"character"` |
| `export_format` | string |  | File format of the generated model. Character split supports only glb. one of: `glb`, `obj`, `stl`, `fbx`, `usdz`; default `"glb"` |

## Details

Hi3D Split by Hitem3D splits a 3D model into parts, either by a humanoid character template with optional joints or by granularity for general objects.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the input model. GLB, STL or OBJ, up to 200MB. |
| `split_mode` | `character` / `general` | `character` | character splits humanoid models using a template; general splits any model by granularity. |
| `part` | `a` / `b` / `c` / `d` / `e` / `f` | `a` | Character split template: a 6 parts, b 5, c 4 without head, d 4 with head, e 3, f 2. |
| `joint` | `none` / `ball` / `dovetail` | `ball` | Joint type added between character parts. |
| `level` | `low` / `medium` / `high` | `medium` | Split granularity for general mode. |
| `export_format` | `glb` / `obj` / `stl` / `fbx` / `usdz` | `glb` | File format of the generated model. Character split supports only glb. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.40 per request.
Failed runs are not charged.
### Also on SandBase
Other Hitem3D 3D endpoints: `hitem3d/hi3d/image-to-3d`, `hitem3d/hi3d/multi-view-to-3d`, `hitem3d/hi3d/multicolor`, `hitem3d/hi3d/texture`.

---
Machine-readable: [`catalog/models/hitem3d/hi3d/split.json`](../../../../catalog/models/hitem3d/hi3d/split.json) · Store page: https://www.sandbase.ai/model/hitem3d/hi3d/split
