# Video Upscaler API: pricing, parameters and code examples

`sandbase-ai/video-upscaler` · video generation model · SandBase AI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.249 per call · **Modes:** async

Video Upscaler by SandBase AI - AI-powered video editing and transformation. Apply style transfer, motion control, lip-sync, and visual effects to existing videos with natural language instructions.

## Pricing

- Depends on parameters (`params.video`, `usage.duration`, `usage.height`, `usage.width`).

Formula: `(usage.duration ?? media_duration(params.video) ?? 5.0) * (((usage.width ?? 1920.0) * (usage.height ?? 1080.0)) <= 1000000.0 ? 0.0222 : ((usage.width ?? 1920.0) * (usage.height ?? 1080.0)) <= 2500000.0 ? 0.0498 : ((usage.width ?? 1920.0) * (usage.height ?? 1080.0)) <= 5000000.0 ? 0.0885 : 0.1991)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sandbase-ai/video-upscaler"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sandbase-ai/video-upscaler', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sandbase-ai/video-upscaler", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sandbase-ai/video-upscaler", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `scale` | number |  | The scale factor default `2`; range 1–8 |
| `video` | string |  | The URL of the video to upscale  |

---
Machine-readable: [`catalog/models/sandbase-ai/video-upscaler.json`](../../../catalog/models/sandbase-ai/video-upscaler.json) · Store page: https://www.sandbase.ai/model/sandbase-ai/video-upscaler
