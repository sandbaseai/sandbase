# Tripo Rig Check API: pricing, parameters and code examples

`tripo3d/tripo/rig-check` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** free · **Modes:** async

Tripo Rig Check tells whether a 3D model can be auto-rigged and which skeleton type fits it. Free.

## Pricing

- **Free**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/rig-check", "model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/character.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/rig-check', {'model_url': 'https://static.sandbase.ai/examples/tripo3d/tripo/shared/character.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/rig-check", {
  "model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/character.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/rig-check", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/character.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_url` | string | yes | URL of the 3D model (GLB, FBX, OBJ or STL, up to 150 MB).  |

## Details

Tripo Rig Check tells whether a 3D model can be auto-rigged and which skeleton type fits it. Free.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the 3D model (GLB, FBX, OBJ or STL, up to 150 MB). |
### Output
- `riggable`: true when the model can be rigged.
- `rig_type`: biped, quadruped, hexapod, octopod, avian, serpentine, aquatic or others.
### Billing
Free.
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/rig-check.json`](../../../../catalog/models/tripo3d/tripo/rig-check.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/rig-check
