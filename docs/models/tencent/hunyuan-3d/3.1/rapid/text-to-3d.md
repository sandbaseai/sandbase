# Hunyuan 3D 3.1 Rapid Text to 3D API: pricing, parameters and code examples

`tencent/hunyuan-3d/3.1/rapid/text-to-3d` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.27 to $0.375 per run, depending on parameters · **Modes:** async

Hunyuan 3D 3.1 Rapid by Tencent quickly generates a textured or geometry-only 3D model from a text prompt.

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
  -d '{"model": "tencent/hunyuan-3d/3.1/rapid/text-to-3d", "prompt": "A rustic wooden treasure chest with metal bands and ornate lock"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-3d/3.1/rapid/text-to-3d', {'prompt': 'A rustic wooden treasure chest with metal bands and ornate lock'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-3d/3.1/rapid/text-to-3d", {
  "prompt": "A rustic wooden treasure chest with metal bands and ornate lock"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-3d/3.1/rapid/text-to-3d", sandbase.Params{
	"prompt": "A rustic wooden treasure chest with metal bands and ornate lock",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Text description of the 3D object to generate. Max 200 characters.  |
| `enable_pbr` | boolean |  | Generate PBR materials (metallic, roughness, normal maps). Ignored when Geometry Only is on. default `false` |
| `enable_geometry` | boolean |  | Generate a geometry-only white model without textures. default `false` |

## Details

Hunyuan 3D 3.1 Rapid by Tencent quickly generates a textured or geometry-only 3D model from a text prompt.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text description of the 3D object to generate. Max 200 characters. |
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
Machine-readable: [`catalog/models/tencent/hunyuan-3d/3.1/rapid/text-to-3d.json`](../../../../../../catalog/models/tencent/hunyuan-3d/3.1/rapid/text-to-3d.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-3d/3.1/rapid/text-to-3d
