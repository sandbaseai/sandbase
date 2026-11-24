# Crystal Video Upscaler API: pricing, parameters and code examples

`clarityai/crystal-video-upscaler` · video generation model · ClarityAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $1.037 per call · **Modes:** async

Crystal Video Upscaler by ClarityAI - AI-powered video editing and transformation. Apply style transfer, motion control, lip-sync, and visual effects to existing videos with natural language instructions.

## Pricing

- Depends on parameters (`params.video`, `usage.duration`, `usage.fps`, `usage.height`, `usage.width`).

Formula: `(usage.duration ?? media_duration(params.video) ?? 5.0) * (((usage.width ?? 1920.0) * (usage.height ?? 1080.0)) <= 1000000.0 ? 0.0922 : ((usage.width ?? 1920.0) * (usage.height ?? 1080.0)) <= 2500000.0 ? 0.2074 : ((usage.width ?? 1920.0) * (usage.height ?? 1080.0)) <= 5000000.0 ? 0.3687 : 0.8295) * Math.ceil((usage.fps ?? 30.0) / 30.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "clarityai/crystal-video-upscaler"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('clarityai/crystal-video-upscaler', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("clarityai/crystal-video-upscaler", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "clarityai/crystal-video-upscaler", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string |  | URL to the input video.  |
| `scale_factor` | number |  | Scale factor. The scale factor must be chosen such that the upscaled video does not exceed 5K resolution. default `2`; range 1–200 |

---
Machine-readable: [`catalog/models/clarityai/crystal-video-upscaler.json`](../../../catalog/models/clarityai/crystal-video-upscaler.json) · Store page: https://www.sandbase.ai/model/clarityai/crystal-video-upscaler
