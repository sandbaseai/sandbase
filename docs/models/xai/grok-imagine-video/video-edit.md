# Grok Imagine Video Edit

`xai/grok-imagine-video/video-edit` · video · xAI

Grok Imagine Video Edit is xAI's video-to-video AI model. Transform, enhance, and edit video content using text prompts - from style changes to object manipulation and scene modification.

## Pricing

- Depends on parameters (`params.resolution`, `params.video`, `usage.duration`).

Formula: `(params.resolution ?? "auto") == "720p" ? (usage.duration ?? media_duration(params.video) ?? 5.0) * 0.08 : (usage.duration ?? media_duration(params.video) ?? 5.0) * 0.06`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-video/video-edit", "prompt": "Colorize the video", "video": "https://static.sandbase.ai/examples/11481268-9367-44ba-92ab-8d9e12ea1ca5/input/4a83fad0-72ea-4512-87e8-53f73b2c3b94.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-video/video-edit', {'prompt': 'Colorize the video', 'video': 'https://static.sandbase.ai/examples/11481268-9367-44ba-92ab-8d9e12ea1ca5/input/4a83fad0-72ea-4512-87e8-53f73b2c3b94.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-video/video-edit", {
  "prompt": "Colorize the video",
  "video": "https://static.sandbase.ai/examples/11481268-9367-44ba-92ab-8d9e12ea1ca5/input/4a83fad0-72ea-4512-87e8-53f73b2c3b94.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-video/video-edit", sandbase.Params{
	"prompt": "Colorize the video",
	"video": "https://static.sandbase.ai/examples/11481268-9367-44ba-92ab-8d9e12ea1ca5/input/4a83fad0-72ea-4512-87e8-53f73b2c3b94.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | URL of the input video to edit. The video will be resized to a maximum area of 854x480 pixels and truncated to 8 seconds.  |
| `prompt` | string | yes | Text description of the desired edit.  |
| `resolution` | string |  | Resolution of the output video. one of: `auto`, `480p`, `720p`; default `"auto"` |

## Details

Grok Imagine Video edit: change an existing clip with an instruction while keeping its motion.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 4,096 characters. |
| `video` | video URL, required | — | Source clip. |
| `resolution` | `auto` / `480p` / `720p` | `auto` | Sets the per-second rate. |

### Billing

$0.08 per output second at 720p and $0.06 otherwise; the output matches the source length. The quote before submission assumes 5 seconds.

| Output | auto | 480p | 720p |
|---|---|---|---|
| 3s source | $0.18 | $0.18 | $0.24 |
| 5s source | $0.30 | $0.30 | $0.40 |
| 8s source | $0.48 | $0.48 | $0.64 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Grok Imagine Video endpoints: `xai/grok-imagine-video/text-to-video`, `xai/grok-imagine-video/image-to-video`, `xai/grok-imagine-video/reference-to-video`, `xai/grok-imagine-video/video-extend`, `xai/grok-imagine-video/1.5/text-to-video` (1.5, newer).

---
Machine-readable: [`catalog/models/xai/grok-imagine-video/video-edit.json`](../../../../catalog/models/xai/grok-imagine-video/video-edit.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-video/video-edit
