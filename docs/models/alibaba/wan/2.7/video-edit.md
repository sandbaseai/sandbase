# Wan 2.7 Video Edit

`alibaba/wan/2.7/video-edit` · video · Alibaba

Alibaba Wan 2.7 video editing model.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `params.video`, `usage.duration`).

Formula: `((params.duration ?? 0) > 0 ? params.duration : Math.ceil(usage.duration ?? media_duration(params.video) ?? 5.0)) * ((params.resolution ?? "720p") == "1080p" ? 0.15 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.7/video-edit", "prompt": "Change the video to an 8-bit pixel style", "video": "https://static.sandbase.ai/examples/d2517981-e23d-4629-a811-791107b46f0d/input/776801b8-88cf-4cfe-8ae6-b3b3f695f1e3.mp4"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.7/video-edit', {'prompt': 'Change the video to an 8-bit pixel style', 'video': 'https://static.sandbase.ai/examples/d2517981-e23d-4629-a811-791107b46f0d/input/776801b8-88cf-4cfe-8ae6-b3b3f695f1e3.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.7/video-edit", {
  "prompt": "Change the video to an 8-bit pixel style",
  "video": "https://static.sandbase.ai/examples/d2517981-e23d-4629-a811-791107b46f0d/input/776801b8-88cf-4cfe-8ae6-b3b3f695f1e3.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.7/video-edit", sandbase.Params{
	"prompt": "Change the video to an 8-bit pixel style",
	"video": "https://static.sandbase.ai/examples/d2517981-e23d-4629-a811-791107b46f0d/input/776801b8-88cf-4cfe-8ae6-b3b3f695f1e3.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed (0-2147483647) for reproducible results. Omit for a random seed.  |
| `video` | string | yes | The URL of the input video to edit.  |
| `images` | array |  | Reference images to guide the video editing.  |
| `prompt` | string | yes | The editing instruction describing what changes to make.  |
| `duration` | integer |  | Output video duration in seconds. 0 means match input video duration. When set (2-10), truncates from the start. one of: `0`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`; default `0` |
| `resolution` | string |  | The resolution of the output video. one of: `720p`, `1080p`; default `"720p"` |
| `audio_setting` | string |  | Audio handling. 'auto': model decides whether to regenerate audio. 'origin': preserve original audio from input video. one of: `auto`, `origin`; default `"auto"` |

## Details

Change an existing clip with a sentence: restyle it, swap an object or outfit, or rework the background. The edit is carried through every frame so motion and timing from the source are kept. Optional reference images guide the new look.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `video` | video URL, required | — | Source clip, Video 1 in the prompt. |
| `images` | image URL[] | — | Optional reference images, Image 1, Image 2, … |
| `audio_setting` | `auto` / `origin` | `auto` | `auto` regenerates audio to match the edit; `origin` keeps the source track. |
| `duration` | 0 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 | 0 | `0` keeps the source length; 2–10 trims or sets the output length. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.10 at 720p and $0.15 at 1080p, the same as Alibaba's list price. With `duration: 0` the output matches the source, so you pay for the source length; the quote before submission assumes 5 seconds and the final charge uses the measured length. Input video is not metered separately.

| Output | 720p | 1080p |
|---|---|---|
| 5s source, `duration: 0` | $0.50 | $0.75 |
| 10s source, `duration: 0` | $1.00 | $1.50 |
| Any source, `duration: 3` | $0.30 | $0.45 |

Failed runs are not charged.

### Prompting

- Lead with the change and say what must stay: “turn the street into a snowy night; keep the cyclist and the camera move”.
- Refer to the source as Video 1 and to references as Image 1, Image 2.
- Draft at 720p and short `duration` before running the full clip.

### Limits

- Output framing follows the source video.
- To add footage after the clip, use `alibaba/wan/2.7/video-extend`.

### Also on SandBase

Other Wan 2.7 endpoints: `alibaba/wan/2.7/text-to-video`, `alibaba/wan/2.7/image-to-video`, `alibaba/wan/2.7/reference-to-video`, `alibaba/wan/2.7/video-extend`, `alibaba/wan/3.0/video` (newer, up to 30s).

---
Machine-readable: [`catalog/models/alibaba/wan/2.7/video-edit.json`](../../../../../catalog/models/alibaba/wan/2.7/video-edit.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.7/video-edit
