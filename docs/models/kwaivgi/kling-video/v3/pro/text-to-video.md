# Kling V3 Pro Text to Video

`kwaivgi/kling-video/v3/pro/text-to-video` · video · KwaiVGI

Kling V3 Pro Text to Video by Kuaishou turns a text prompt into a 3-15 second 1080p video with optional native audio.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`).

| parameters | USD |
|---|---|
| duration=3, generate_audio=false | 0.336 |
| duration=3, generate_audio=true | 0.504 |
| duration=4, generate_audio=false | 0.448 |
| duration=4, generate_audio=true | 0.672 |
| duration=5, generate_audio=false | 0.56 |
| duration=5, generate_audio=true | 0.84 |
| duration=6, generate_audio=false | 0.672 |
| duration=6, generate_audio=true | 1.008 |
| duration=7, generate_audio=false | 0.784 |
| duration=7, generate_audio=true | 1.176 |
| duration=8, generate_audio=false | 0.896 |
| duration=8, generate_audio=true | 1.344 |

Formula: `(params.generate_audio ?? true) ? (params.duration ?? 5) * 0.168 : (params.duration ?? 5) * 0.112`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v3/pro/text-to-video", "prompt": "Close-up of glowing fireflies dancing in a dark forest at twilight. Soft bioluminescent particles float through the air. Shallow depth of field, bokeh lights in background. Magical atmosphere, gentle movement."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v3/pro/text-to-video', {'prompt': 'Close-up of glowing fireflies dancing in a dark forest at twilight. Soft bioluminescent particles float through the air. Shallow depth of field, bokeh lights in background. Magical atmosphere, gentle movement.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v3/pro/text-to-video", {
  "prompt": "Close-up of glowing fireflies dancing in a dark forest at twilight. Soft bioluminescent particles float through the air. Shallow depth of field, bokeh lights in background. Magical atmosphere, gentle movement."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v3/pro/text-to-video", sandbase.Params{
	"prompt": "Close-up of glowing fireflies dancing in a dark forest at twilight. Soft bioluminescent particles float through the air. Shallow depth of field, bokeh lights in background. Magical atmosphere, gentle movement.",
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

Kling V3 Pro text-to-video: write a scene and get back a 3–15 second clip, with native audio and multi-shot control.

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

You pay for output seconds: $0.168 with audio (the default) and $0.112 without.

| Output | With audio | Without audio |
|---|---|---|
| 3s | $0.504 | $0.336 |
| 5s (default) | $0.84 | $0.56 |
| 10s | $1.68 | $1.12 |
| 15s | $2.52 | $1.68 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera move, and light in order.
- For several shots, use `multi_prompt` with one entry per shot.

### Limits

- Clips are 3–15 seconds.

### Also on SandBase

Other Kling V3 Pro endpoints and tiers: `kwaivgi/kling-video/v3/pro/image-to-video`, `kwaivgi/kling-video/v3/pro/motion-control`, `kwaivgi/kling-video/v3/standard/text-to-video`, `kwaivgi/kling-video/v3/4k/text-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v3/pro/text-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/v3/pro/text-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v3/pro/text-to-video
