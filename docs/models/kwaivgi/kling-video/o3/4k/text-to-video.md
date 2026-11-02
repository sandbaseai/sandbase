# Kling O3 4K Text to Video API: pricing, parameters and code examples

`kwaivgi/kling-video/o3/4k/text-to-video` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $1.26 to $3.36 per run, depending on parameters · **Modes:** async

Kling O3 4K Text to Video by Kuaishou turns a text prompt into a 3-15 second native 4K video with optional native audio.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=3 | 1.26 |
| duration=4 | 1.68 |
| duration=5 | 2.1 |
| duration=6 | 2.52 |
| duration=7 | 2.94 |
| duration=8 | 3.36 |

Formula: `(params.duration ?? 5) * 0.42`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/o3/4k/text-to-video", "prompt": "A mecha lands on the ground to save the city, and says \"I'\''m here\", in anime style"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/o3/4k/text-to-video', {'prompt': 'A mecha lands on the ground to save the city, and says "I\'m here", in anime style'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/o3/4k/text-to-video", {
  "prompt": "A mecha lands on the ground to save the city, and says \"I'm here\", in anime style"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/o3/4k/text-to-video", sandbase.Params{
	"prompt": "A mecha lands on the ground to save the city, and says \"I'm here\", in anime style",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Text prompt for video generation. Required unless multi_prompt is provided.  |
| `duration` | integer |  | Video duration in seconds (3-15s). one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `shot_type` | string |  | The type of multi-shot video generation. 'intelligent' lets the model automatically determine shot structure. one of: `customize`, `intelligent`; default `"customize"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`, `1:1`; default `"16:9"` |
| `multi_prompt` | array |  | List of prompts for multi-shot video generation.  |
| `generate_audio` | boolean |  | Whether to generate native audio for the video. default `false` |

## Details

Kling O3 4K text-to-video, native 4K output in one pass, without a separate upscale. Write a scene, optionally split into shots with `multi_prompt`, and get back a 3–15 second clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` | `16:9` | Output frame shape. |
| `duration` | 3–15 | 5 | Output length in seconds. |
| `generate_audio` | boolean | false | Generate native audio with the clip. |
| `multi_prompt` | object[] | — | Optional list of shots, each with its own prompt and duration. |
| `shot_type` | `customize` / `intelligent` | `customize` | `customize` follows your `multi_prompt` shot list; `intelligent` lets the model plan the cuts. |

### Billing

You pay $0.42 per output second, with or without audio.

| Output | Price |
|---|---|
| 3s | $1.26 |
| 5s (default) | $2.10 |
| 10s | $4.20 |
| 15s | $6.30 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera move, and light in order.
- For several shots, use `multi_prompt` with one entry per shot.

### Limits

- Clips are 3–15 seconds.

### Also on SandBase

Other Kling O3 4K endpoints and tiers: `kwaivgi/kling-video/o3/4k/image-to-video`, `kwaivgi/kling-video/o3/4k/reference-to-video`, `kwaivgi/kling-video/o3/4k/edit`, `kwaivgi/kling-video/o3/4k/video-to-video`, `kwaivgi/kling-video/o3/standard/text-to-video`, `kwaivgi/kling-video/o3/pro/text-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/o3/4k/text-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/o3/4k/text-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/o3/4k/text-to-video
