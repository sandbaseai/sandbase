# LTX 2.3 Pro Video Extend

`lightricks/ltx-2.3-pro/video-extend` · video · Lightricks

Ltx 2.3 Pro Extend by Lightricks - AI-powered video editing and transformation. Apply style transfer, motion control, lip-sync, and visual effects to existing videos with natural language instructions.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=2 | 0.2 |
| duration=5 | 0.5 |
| duration=20 | 2 |

Formula: `(params.duration ?? 5) * 0.10`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lightricks/ltx-2.3-pro/video-extend", "prompt": "Continue the motion smoothly", "video": "https://static.sandbase.ai/examples/dbd7d6a6-b2a4-4fcb-a88c-ab762951fb12/input/d3e86131-4af5-4826-9dc1-4dcbdef35e3b.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lightricks/ltx-2.3-pro/video-extend', {'prompt': 'Continue the motion smoothly', 'video': 'https://static.sandbase.ai/examples/dbd7d6a6-b2a4-4fcb-a88c-ab762951fb12/input/d3e86131-4af5-4826-9dc1-4dcbdef35e3b.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lightricks/ltx-2.3-pro/video-extend", {
  "prompt": "Continue the motion smoothly",
  "video": "https://static.sandbase.ai/examples/dbd7d6a6-b2a4-4fcb-a88c-ab762951fb12/input/d3e86131-4af5-4826-9dc1-4dcbdef35e3b.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lightricks/ltx-2.3-pro/video-extend", sandbase.Params{
	"prompt": "Continue the motion smoothly",
	"video": "https://static.sandbase.ai/examples/dbd7d6a6-b2a4-4fcb-a88c-ab762951fb12/input/d3e86131-4af5-4826-9dc1-4dcbdef35e3b.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | The URL of the video to extend  |
| `prompt` | string | yes | Description of what should happen in the extended portion of the video.  |
| `duration` | integer |  | Duration in seconds to extend the video. Maximum 20 seconds. default `5`; range 2–20 |

## Details

LTX 2.3 Pro extend: continue a clip with 2–20 seconds of new footage.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `video` | video URL, required | — | Clip to continue. |
| `duration` | integer 2–20 | 5 | Seconds of new footage. |

### Billing

$0.10 per new second.

| Output | Price |
|---|---|
| 2s | $0.20 |
| 5s (default) | $0.50 |
| 10s | $1.00 |
| 20s | $2.00 |

Failed runs are not charged.

### Prompting

- Describe what happens next.

### Also on SandBase

Other LTX 2.3 endpoints: `lightricks/ltx-2.3-pro/text-to-video`, `lightricks/ltx-2.3-pro/image-to-video`, `lightricks/ltx-2.3-pro/audio-to-video`, `lightricks/ltx-2.3-pro/retake`.

---
Machine-readable: [`catalog/models/lightricks/ltx-2.3-pro/video-extend.json`](../../../../catalog/models/lightricks/ltx-2.3-pro/video-extend.json) · Store page: https://www.sandbase.ai/model/lightricks/ltx-2.3-pro/video-extend
