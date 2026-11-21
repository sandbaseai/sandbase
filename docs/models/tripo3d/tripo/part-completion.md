# Tripo Part Completion API: pricing, parameters and code examples

`tripo3d/tripo/part-completion` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.7 to $0.9 per run, depending on parameters · **Modes:** async

Tripo Part Completion splits a 3D model into parts and rebuilds the hidden or missing surfaces of each part in one call (Tripo Segment + Complete).

## Pricing

- Depends on parameters (`params.completion_mode`).

| parameters | USD |
|---|---|
| completion_mode="ai_completion" | 0.9 |
| completion_mode="quick_cap" | 0.7 |

Formula: `0.40 + ((params.completion_mode ?? "ai_completion") == "quick_cap" ? 0.30 : 0.50)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/part-completion", "model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/part-completion', {'model_url': 'https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/part-completion", {
  "model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/part-completion", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_url` | string | yes | URL of the input 3D model (GLB, GLTF, FBX, OBJ or STL, up to 150 MB).  |
| `ref_image` | string |  | v2.0 only. Reference image guiding the parts.  |
| `part_names` | array |  | Only complete these parts (tripo_part_0, tripo_part_1, ...). All parts when unset.  |
| `model_version` | string |  | v1.0-20250506 splits by geometry; v2.0-20260430 (beta) splits by meaning. one of: `v1.0-20250506`, `v2.0-20260430`; default `"v1.0-20250506"` |
| `completion_mode` | string |  | ai_completion rebuilds missing geometry; quick_cap closes holes quickly and costs less. one of: `ai_completion`, `quick_cap`; default `"ai_completion"` |
| `split_by_connectivity` | boolean |  | v2.0 only. Also split disconnected pieces. default `true` |
| `segmentation_granularity` | string |  | v2.0 only. one of: `simple`, `balanced`, `detailed`; default `"balanced"` |

## Details

Tripo Part Completion splits a 3D model into parts and rebuilds the hidden or missing surfaces of each part in one call (Tripo Segment + Complete).
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the input 3D model (GLB, GLTF, FBX, OBJ or STL, up to 150 MB). |
| `completion_mode` | `ai_completion` / `quick_cap` | `ai_completion` | ai_completion rebuilds missing geometry; quick_cap closes holes quickly and costs less. |
| `model_version` | `v1.0-20250506` / `v2.0-20260430` | `v1.0-20250506` | v1.0-20250506 splits by geometry; v2.0-20260430 (beta) splits by meaning. |
| `segmentation_granularity` | `simple` / `balanced` / `detailed` | `balanced` | v2.0 only. |
| `split_by_connectivity` | boolean | `true` | v2.0 only. Also split disconnected pieces. |
| `ref_image` | string | — | v2.0 only. Reference image guiding the parts. |
| `part_names` | array | — | Only complete these parts (tripo_part_0, tripo_part_1, ...). All parts when unset. |
### Output
- `url`: Completed parts model (GLB).
- `segmented`: Segmented model before completion.
- `thumbnail`: Preview render.
### Billing
| completion_mode | Price |
|---|---|
| ai_completion | $0.90 ($0.40 segment + $0.50 completion) |
| quick_cap | $0.70 ($0.40 + $0.30) |
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/part-completion.json`](../../../../catalog/models/tripo3d/tripo/part-completion.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/part-completion
