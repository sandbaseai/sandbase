# Kling V4 Flash Reference to Video API: pricing, parameters and code examples

`kwaivgi/kling-video/v4/flash/reference-to-video` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.47 per call · **Modes:** async

Kling V4 Flash Reference to Video by Kuaishou generates a 3-20 second 720p video that keeps characters, objects and motion from reference images and videos.

## Pricing

- Depends on parameters (`params.duration`, `params.videos`).

Formula: `len(params.videos ?? []) > 0 ? 0.063 * ((params.duration ?? 5) * 1.0 + Math.max((params.duration ?? 5) * 1.0, media_duration(params.videos) ?? 20.0)) : (params.duration ?? 5) * 0.094`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v4/flash/reference-to-video", "aspect_ratio": "16:9", "images": ["https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/3f37b438-31f7-40e3-83a2-f07ca1a7a364.png", "https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/34423a11-3143-42fa-b016-f38ffd07ec35.png", "https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/475de517-faa0-4318-a194-ea7679683fe3.png", "https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/54f8f7ad-2075-49c6-a036-7d29525b5fd0.png"], "prompt": "Macro product film for the watchmaker AUREL on black velvet under one raking strip light. @Image1 is the dial, @Image2 the movement seen through the caseback, @Image3 the case flank, @Image4 the strap. Slow precise shots with hard cuts: the dial with the seconds hand sweeping, the balance wheel ticking through the caseback, light gliding along the brushed case flank, then the full watch resting on velvet. Quiet mechanical ticking."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v4/flash/reference-to-video', {'aspect_ratio': '16:9', 'images': ['https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/3f37b438-31f7-40e3-83a2-f07ca1a7a364.png', 'https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/34423a11-3143-42fa-b016-f38ffd07ec35.png', 'https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/475de517-faa0-4318-a194-ea7679683fe3.png', 'https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/54f8f7ad-2075-49c6-a036-7d29525b5fd0.png'], 'prompt': 'Macro product film for the watchmaker AUREL on black velvet under one raking strip light. @Image1 is the dial, @Image2 the movement seen through the caseback, @Image3 the case flank, @Image4 the strap. Slow precise shots with hard cuts: the dial with the seconds hand sweeping, the balance wheel ticking through the caseback, light gliding along the brushed case flank, then the full watch resting on velvet. Quiet mechanical ticking.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v4/flash/reference-to-video", {
  "aspect_ratio": "16:9",
  "images": [
    "https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/3f37b438-31f7-40e3-83a2-f07ca1a7a364.png",
    "https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/34423a11-3143-42fa-b016-f38ffd07ec35.png",
    "https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/475de517-faa0-4318-a194-ea7679683fe3.png",
    "https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/54f8f7ad-2075-49c6-a036-7d29525b5fd0.png"
  ],
  "prompt": "Macro product film for the watchmaker AUREL on black velvet under one raking strip light. @Image1 is the dial, @Image2 the movement seen through the caseback, @Image3 the case flank, @Image4 the strap. Slow precise shots with hard cuts: the dial with the seconds hand sweeping, the balance wheel ticking through the caseback, light gliding along the brushed case flank, then the full watch resting on velvet. Quiet mechanical ticking."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v4/flash/reference-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"images": []any{"https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/3f37b438-31f7-40e3-83a2-f07ca1a7a364.png", "https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/34423a11-3143-42fa-b016-f38ffd07ec35.png", "https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/475de517-faa0-4318-a194-ea7679683fe3.png", "https://static.sandbase.ai/examples/876cfe40-c2cf-4869-91fb-457ac514139b/input/54f8f7ad-2075-49c6-a036-7d29525b5fd0.png"},
	"prompt": "Macro product film for the watchmaker AUREL on black velvet under one raking strip light. @Image1 is the dial, @Image2 the movement seen through the caseback, @Image3 the case flank, @Image4 the strap. Slow precise shots with hard cuts: the dial with the seconds hand sweeping, the balance wheel ticking through the caseback, light gliding along the brushed case flank, then the full watch resting on velvet. Quiet mechanical ticking.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array |  | Up to 10 reference images, referenced as @Image1, @Image2, ...  |
| `prompt` | string | yes | Text prompt. Refer to references as @Image1, @Video1, ...  |
| `videos` | array |  | Up to 5 reference videos (3-20s each, 20s combined), referenced as @Video1, ... Video references switch to the input-plus-output price.  |
| `duration` | integer |  | Output length in seconds (3-20). default `5`; range 3–20 |
| `aspect_ratio` | string |  | Output frame shape. Leave empty to follow the references (adaptive). one of: `21:9`, `16:9`, `9:16`, `1:1` |

## Details

Kling V4 Flash reference-to-video keeps characters, objects and motion from reference images and videos in a new 3–20 second 720p clip.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Refer to inputs as `@Image1`, `@Video1`, … |
| `images` | image URL[] | — | Up to 10 reference images. |
| `videos` | video URL[] | — | Up to 5 reference videos, 3–20s each, 20s combined. |
| `aspect_ratio` | `21:9` / `16:9` / `9:16` / `1:1` | — | Leave empty to follow the references. |
| `duration` | 3–20 | 5 | Output length in seconds. |
### Billing
Without reference videos: $0.094 per output second.
With reference videos: $0.063 per second of output plus input, where the input side counts at least as long as the output. The quote before submission assumes 20 seconds of reference video when the length cannot be read.
| Request | Price |
|---|---|
| 5s, images only (default) | $0.47 |
| 10s, images only | $0.94 |
| 5s, 8s reference video | $0.819 |
| 10s, 4s reference video | $1.26 |
Failed runs are not charged.
### Prompting
- Name each reference in the prompt, e.g. "@Image1 walks into the scene from @Video1".
### Limits
- Output is 720p only; clips are 3–20 seconds; reference videos 3–20 seconds.
- Custom voices (`voice_ids`) are only on `kwaivgi/kling-video/v4/reference-to-video`.
### Also on SandBase
Other Kling V4 Flash endpoints: `kwaivgi/kling-video/v4/flash/text-to-video`, `kwaivgi/kling-video/v4/flash/image-to-video`, `kwaivgi/kling-video/v4/flash/reference-to-video`, `kwaivgi/kling-video/v4/flash/video-edit`. For 1080p or clips up to 30 seconds, use Kling V4 (`kwaivgi/kling-video/v4/text-to-video` and its siblings).

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v4/flash/reference-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/v4/flash/reference-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v4/flash/reference-to-video
