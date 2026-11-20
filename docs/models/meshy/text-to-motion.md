# Meshy Text to Motion API: pricing, parameters and code examples

`meshy/text-to-motion` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.12 to $0.4 per run, depending on parameters · **Modes:** async

Meshy Text to Motion generates a standalone character motion clip from a text prompt, as FBX (prime) or BVH (swift).

## Pricing

- Depends on parameters (`params.motion_mode`).

| parameters | USD |
|---|---|
| motion_mode="prime" | 0.4 |
| motion_mode="swift" | 0.12 |

Formula: `(params.motion_mode ?? "prime") == "swift" ? 0.12 : 0.4`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/text-to-motion", "prompt": "A red fox in a snowy forest at sunrise, photorealistic"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/text-to-motion', {'prompt': 'A red fox in a snowy forest at sunrise, photorealistic'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/text-to-motion", {
  "prompt": "A red fox in a snowy forest at sunrise, photorealistic"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/text-to-motion", sandbase.Params{
	"prompt": "A red fox in a snowy forest at sunrise, photorealistic",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Describe the motion, up to 400 characters.  |
| `duration` | number |  | Clip length in seconds, 2–10 in 0.5 s steps. default `3`; range 2–10 |
| `motion_mode` | string |  | prime: higher quality FBX clip; swift: faster BVH clip. one of: `prime`, `swift`; default `"prime"` |

## Details

Meshy Text to Motion generates a standalone character motion clip from a text prompt, as FBX (prime) or BVH (swift).
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Describe the motion, up to 400 characters. |
| `duration` | number 2–10 | `3` | Clip length in seconds, 2–10 in 0.5 s steps. |
| `motion_mode` | `prime` / `swift` | `"prime"` | prime: higher quality FBX clip; swift: faster BVH clip. |
### Output
- `url`: Motion clip. prime returns an FBX file; swift returns BVH text content, stored with a `.bin` file name, so save it as `.bvh` before importing.
- `format`: `fbx` or `bvh`.
### Billing
$0.40 per clip (prime), $0.12 (swift).

---
Machine-readable: [`catalog/models/meshy/text-to-motion.json`](../../../catalog/models/meshy/text-to-motion.json) · Store page: https://www.sandbase.ai/model/meshy/text-to-motion
