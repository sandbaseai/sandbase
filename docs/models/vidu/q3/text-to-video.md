# Vidu Q3 Text to Video

`vidu/q3/text-to-video` · video · Vidu

Vidu Q3 is Shengshu's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic motion, lighting, and scene composition.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, resolution="360p" | 0.07 |
| duration=1, resolution="540p" | 0.07 |
| duration=1, resolution="720p" | 0.154 |
| duration=1, resolution="1080p" | 0.16 |
| duration=5, resolution="360p" | 0.35 |
| duration=5, resolution="540p" | 0.35 |
| duration=5, resolution="720p" | 0.77 |
| duration=5, resolution="1080p" | 0.8 |
| duration=16, resolution="360p" | 1.12 |
| duration=16, resolution="540p" | 1.12 |
| duration=16, resolution="720p" | 2.464 |
| duration=16, resolution="1080p" | 2.56 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "720p") == "1080p" ? 0.16 : (params.resolution ?? "720p") == "720p" ? 0.154 : 0.07)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "vidu/q3/text-to-video", "prompt": "In an ultra-realistic fashion photography style featuring light blue and pale amber tones, an astronaut in a spacesuit walks through the fog."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('vidu/q3/text-to-video', {'prompt': 'In an ultra-realistic fashion photography style featuring light blue and pale amber tones, an astronaut in a spacesuit walks through the fog.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("vidu/q3/text-to-video", {
  "prompt": "In an ultra-realistic fashion photography style featuring light blue and pale amber tones, an astronaut in a spacesuit walks through the fog."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "vidu/q3/text-to-video", sandbase.Params{
	"prompt": "In an ultra-realistic fashion photography style featuring light blue and pale amber tones, an astronaut in a spacesuit walks through the fog.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility. If None, a random seed is chosen.  |
| `audio` | boolean |  | Whether to use direct audio-video generation. When true, outputs video with sound. default `true` |
| `prompt` | string | yes | Text prompt for video generation, max 2000 characters  |
| `duration` | integer |  | Duration of the video in seconds default `5`; range 1–16 |
| `resolution` | string |  | Output video resolution one of: `360p`, `540p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`; default `"16:9"` |

## Details

Vidu Q3 turns a prompt into a 1–16 second clip with native audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,000 characters. |
| `aspect_ratio` | `16:9` / `9:16` / `4:3` / `3:4` / `1:1` | `16:9` | Output frame shape. |
| `audio` | boolean | true | Generate native audio. Same price on or off. |
| `resolution` | `360p` / `540p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–16 | 5 | Output length in seconds. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.07 at 360p or 540p, $0.154 at 720p, $0.16 at 1080p.

| Output | 540p | 720p | 1080p |
|---|---|---|---|
| 4s | $0.28 | $0.616 | $0.64 |
| 5s (default) | $0.35 | $0.77 | $0.80 |
| 8s | $0.56 | $1.232 | $1.28 |
| 16s | $1.12 | $2.464 | $2.56 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Vidu Q3 endpoints: `vidu/q3/image-to-video`, `vidu/q3/reference-to-video/mix`, `vidu/q3/text-to-video/turbo`, `vidu/q3/image-to-video/turbo`.

---
Machine-readable: [`catalog/models/vidu/q3/text-to-video.json`](../../../../catalog/models/vidu/q3/text-to-video.json) · Store page: https://www.sandbase.ai/model/vidu/q3/text-to-video
