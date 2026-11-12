# ReconViaGen 0.5 API: pricing, parameters and code examples

`reconviagen/reconviagen-0.5` · image generation model · reconviagen · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.25 to $0.35 per run, depending on parameters · **Modes:** async

ReconViaGen 0.5 reconstructs a textured 3D model (GLB with PBR materials) from one or more views of the same object; more views give a more accurate result.

## Pricing

- Depends on parameters (`params.resolution`).

| parameters | USD |
|---|---|
| resolution=512 | 0.25 |
| resolution=1024 | 0.3 |
| resolution=1536 | 0.35 |

Formula: `(params.resolution ?? 1024) == 512 ? 0.25 : ((params.resolution ?? 1024) == 1536 ? 0.35 : 0.3)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reconviagen/reconviagen-0.5", "images": ["https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/61e979cb-8ae9-4cee-a73e-c1402d05faed.png", "https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/3025d72b-49eb-4751-ad7d-502b2e8e7c90.png", "https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/f67785e3-394b-4c82-b251-28f0993af3a0.png"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reconviagen/reconviagen-0.5', {'images': ['https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/61e979cb-8ae9-4cee-a73e-c1402d05faed.png', 'https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/3025d72b-49eb-4751-ad7d-502b2e8e7c90.png', 'https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/f67785e3-394b-4c82-b251-28f0993af3a0.png']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reconviagen/reconviagen-0.5", {
  "images": [
    "https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/61e979cb-8ae9-4cee-a73e-c1402d05faed.png",
    "https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/3025d72b-49eb-4751-ad7d-502b2e8e7c90.png",
    "https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/f67785e3-394b-4c82-b251-28f0993af3a0.png"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reconviagen/reconviagen-0.5", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/61e979cb-8ae9-4cee-a73e-c1402d05faed.png", "https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/3025d72b-49eb-4751-ad7d-502b2e8e7c90.png", "https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/f67785e3-394b-4c82-b251-28f0993af3a0.png"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducible results.  |
| `images` | array | yes | 1 to 16 views of the same object.  |
| `resolution` | integer |  | Generation resolution. Higher is slower and more detailed, and changes the price. one of: `512`, `1024`, `1536`; default `1024` |
| `texture_size` | integer |  | Resolution of the baked texture image. Higher values keep finer surface detail but produce larger files. one of: `1024`, `2048`, `4096`; default `2048` |
| `decimation_target` | integer |  | Target number of vertices in the final mesh. Lower values give smaller files; 20k-50k suits web and mobile. default `500000`; range 5000–2000000 |

## Details

ReconViaGen 0.5 reconstructs a textured 3D model (GLB with PBR materials) from one or more views of the same object; more views give a more accurate result.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | image URLs (1–16), required | — | 1 to 16 views of the same object. |
| `resolution` | `512` / `1024` / `1536` | `1024` | Generation resolution. Higher is slower and more detailed, and changes the price. |
| `texture_size` | `1024` / `2048` / `4096` | `2048` | Resolution of the baked texture image. Higher values keep finer surface detail but produce larger files. |
| `decimation_target` | integer 5000–2000000 | `500000` | Target number of vertices in the final mesh. Lower values give smaller files; 20k-50k suits web and mobile. |
| `seed` | integer | — | Random seed for reproducible results. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
### Billing
$0.30 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| resolution = 512 | $0.25 |
| resolution = 1024 | $0.30 |
| resolution = 1536 | $0.35 |
Failed runs are not charged.

---
Machine-readable: [`catalog/models/reconviagen/reconviagen-0.5.json`](../../../catalog/models/reconviagen/reconviagen-0.5.json) · Store page: https://www.sandbase.ai/model/reconviagen/reconviagen-0.5
