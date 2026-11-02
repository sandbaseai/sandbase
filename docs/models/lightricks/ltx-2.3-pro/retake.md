# LTX 2.3 Pro Retake API: pricing, parameters and code examples

`lightricks/ltx-2.3-pro/retake` · video generation model · Lightricks · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2 to $2 per run, depending on parameters · **Modes:** async

Ltx 2.3 Pro Retake by Lightricks - AI-powered video editing and transformation. Apply style transfer, motion control, lip-sync, and visual effects to existing videos with natural language instructions.

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
  -d '{"model": "lightricks/ltx-2.3-pro/retake", "prompt": "Change flower to red rose", "video": "https://static.sandbase.ai/examples/ab43871c-ff3d-4c88-b2cf-b426f17f6b80/input/cce568b6-3e5b-4354-838c-5b2331f78ee9.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lightricks/ltx-2.3-pro/retake', {'prompt': 'Change flower to red rose', 'video': 'https://static.sandbase.ai/examples/ab43871c-ff3d-4c88-b2cf-b426f17f6b80/input/cce568b6-3e5b-4354-838c-5b2331f78ee9.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lightricks/ltx-2.3-pro/retake", {
  "prompt": "Change flower to red rose",
  "video": "https://static.sandbase.ai/examples/ab43871c-ff3d-4c88-b2cf-b426f17f6b80/input/cce568b6-3e5b-4354-838c-5b2331f78ee9.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lightricks/ltx-2.3-pro/retake", sandbase.Params{
	"prompt": "Change flower to red rose",
	"video": "https://static.sandbase.ai/examples/ab43871c-ff3d-4c88-b2cf-b426f17f6b80/input/cce568b6-3e5b-4354-838c-5b2331f78ee9.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | The URL of the video to retake  |
| `prompt` | string | yes | The prompt to retake the video with  |
| `duration` | integer |  | The duration of the video to retake in seconds default `5`; range 2–20 |

## Details

LTX 2.3 Pro retake: regenerate part of an existing clip from a prompt while keeping the rest.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `video` | video URL, required | — | Source clip. |
| `duration` | integer 2–20 | 5 | Length of the section to regenerate. |

### Billing

$0.10 per regenerated second.

| Output | Price |
|---|---|
| 2s | $0.20 |
| 5s (default) | $0.50 |
| 10s | $1.00 |

Failed runs are not charged.

### Prompting

- Describe what should happen in the retaken section.

### Also on SandBase

Other LTX 2.3 endpoints: `lightricks/ltx-2.3-pro/text-to-video`, `lightricks/ltx-2.3-pro/image-to-video`, `lightricks/ltx-2.3-pro/audio-to-video`, `lightricks/ltx-2.3-pro/video-extend`.

---
Machine-readable: [`catalog/models/lightricks/ltx-2.3-pro/retake.json`](../../../../catalog/models/lightricks/ltx-2.3-pro/retake.json) · Store page: https://www.sandbase.ai/model/lightricks/ltx-2.3-pro/retake
