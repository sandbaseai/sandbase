# Hunyuan Video 1.5 Text to Video

`tencent/hunyuan-video/1.5/text-to-video` · video · Tencent

Hunyuan Video 1.5 is Tencent's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic motion, lighting, and scene composition.

## Pricing

- Depends on parameters (`usage.duration`).

Formula: `(usage.duration ?? 5.0) * 0.075`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-video/1.5/text-to-video", "prompt": "A stylish woman walks down a Tokyo street filled with warm glowing neon and animated city signage."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-video/1.5/text-to-video', {'prompt': 'A stylish woman walks down a Tokyo street filled with warm glowing neon and animated city signage.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-video/1.5/text-to-video", {
  "prompt": "A stylish woman walks down a Tokyo street filled with warm glowing neon and animated city signage."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-video/1.5/text-to-video", sandbase.Params{
	"prompt": "A stylish woman walks down a Tokyo street filled with warm glowing neon and animated city signage.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducible generation. range 0–2147483647 |
| `prompt` | string | yes | The prompt to generate the video.  |
| `resolution` | string |  | The resolution of the video. one of: `480p`; default `"480p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`; default `"16:9"` |

## Details

Hunyuan Video 1.5, Tencent's open video model, turns a prompt into a short 480p clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `480p` | `480p` | Sets the per-second rate. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

$0.075 per output second. The quote before submission assumes 5 seconds.

| Output | Price |
|---|---|
| 5s | $0.375 |

Failed runs are not charged.

### Prompting

- Describe subject, action, and camera.

### Limits

- 480p only.

---
Machine-readable: [`catalog/models/tencent/hunyuan-video/1.5/text-to-video.json`](../../../../../catalog/models/tencent/hunyuan-video/1.5/text-to-video.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-video/1.5/text-to-video
