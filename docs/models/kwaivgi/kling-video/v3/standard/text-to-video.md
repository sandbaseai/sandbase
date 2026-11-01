# Kling V3 Standard Text to Video

`kwaivgi/kling-video/v3/standard/text-to-video` · video · KwaiVGI

Kling V3 Standard Text to Video by Kuaishou turns a text prompt into a 3-15 second 720p video with optional native audio.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`).

| parameters | USD |
|---|---|
| duration=3, generate_audio=false | 0.252 |
| duration=3, generate_audio=true | 0.378 |
| duration=4, generate_audio=false | 0.336 |
| duration=4, generate_audio=true | 0.504 |
| duration=5, generate_audio=false | 0.42 |
| duration=5, generate_audio=true | 0.63 |
| duration=6, generate_audio=false | 0.504 |
| duration=6, generate_audio=true | 0.756 |
| duration=7, generate_audio=false | 0.588 |
| duration=7, generate_audio=true | 0.882 |
| duration=8, generate_audio=false | 0.672 |
| duration=8, generate_audio=true | 1.008 |

Formula: `(params.generate_audio ?? true) ? (params.duration ?? 5) * 0.126 : (params.duration ?? 5) * 0.084`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v3/standard/text-to-video", "prompt": "Cinematic drone shot flying through ancient stone ruins covered in moss and vines at golden hour. Camera starts low, rises through crumbling archways, revealing a vast misty valley beyond. Volumetric light rays pierce through gaps in the stone. Epic scale, photorealistic, 8K quality."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v3/standard/text-to-video', {'prompt': 'Cinematic drone shot flying through ancient stone ruins covered in moss and vines at golden hour. Camera starts low, rises through crumbling archways, revealing a vast misty valley beyond. Volumetric light rays pierce through gaps in the stone. Epic scale, photorealistic, 8K quality.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v3/standard/text-to-video", {
  "prompt": "Cinematic drone shot flying through ancient stone ruins covered in moss and vines at golden hour. Camera starts low, rises through crumbling archways, revealing a vast misty valley beyond. Volumetric light rays pierce through gaps in the stone. Epic scale, photorealistic, 8K quality."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v3/standard/text-to-video", sandbase.Params{
	"prompt": "Cinematic drone shot flying through ancient stone ruins covered in moss and vines at golden hour. Camera starts low, rises through crumbling archways, revealing a vast misty valley beyond. Volumetric light rays pierce through gaps in the stone. Epic scale, photorealistic, 8K quality.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Text prompt for video generation. Either prompt or multi_prompt must be provided, but not both.  |
| `duration` | integer |  | The duration of the generated video in seconds one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `shot_type` | string |  | The type of multi-shot video generation. 'intelligent' lets the model automatically determine shot structure. one of: `customize`, `intelligent`; default `"customize"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`, `1:1`; default `"16:9"` |
| `multi_prompt` | array |  | List of prompts for multi-shot video generation. If provided, overrides the single prompt and divides the video into multiple shots with specified prompts and durations.  |
| `generate_audio` | boolean |  | Whether to generate native audio for the video. Supports Chinese and English voice output. Other languages are automatically translated to English. For English speech, use lowercase letters; for acronyms or proper… default `true` |

## Details

Kling V3 Standard text-to-video: write a scene and get back a 3–15 second clip, with native audio and multi-shot control.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` | `16:9` | Output frame shape. |
| `duration` | 3–15 | 5 | Output length in seconds. |
| `generate_audio` | boolean | true | Generate native audio with the clip. |
| `shot_type` | `customize` / `intelligent` | `customize` | `customize` follows your `multi_prompt` shot list; `intelligent` lets the model plan the cuts. |
| `multi_prompt` | object[] | — | Optional list of shots, each with its own prompt and duration. |

### Billing

You pay for output seconds: $0.126 with audio (the default) and $0.084 without.

| Output | With audio | Without audio |
|---|---|---|
| 3s | $0.378 | $0.252 |
| 5s (default) | $0.63 | $0.42 |
| 10s | $1.26 | $0.84 |
| 15s | $1.89 | $1.26 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera move, and light in order.
- For several shots, use `multi_prompt` with one entry per shot.

### Limits

- Clips are 3–15 seconds.

### Also on SandBase

Other Kling V3 Standard endpoints and tiers: `kwaivgi/kling-video/v3/standard/image-to-video`, `kwaivgi/kling-video/v3/standard/motion-control`, `kwaivgi/kling-video/v3/pro/text-to-video`, `kwaivgi/kling-video/v3/4k/text-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v3/standard/text-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/v3/standard/text-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v3/standard/text-to-video
