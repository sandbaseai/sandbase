# Wan 3.0 Video Edit

`alibaba/wan/3.0/video-edit` · video · Alibaba

Wan 3.0 Video Edit by Alibaba restyles or modifies an input video from a text instruction, optionally guided by reference images and audio, keeping the original length.

## Pricing

- Depends on parameters (`params.resolution`, `params.video`, `usage.duration`).

Formula: `2 * Math.round(usage.duration ?? media_duration(params.video) ?? 5.0) * ((params.resolution ?? "720p") == "1080p" ? 0.20 : (params.resolution ?? "720p") == "480p" ? 0.05 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/3.0/video-edit", "prompt": "Convert the entire scene to clay style", "video": "https://static.sandbase.ai/examples/d2c29bdb-fa51-4c8d-8cdc-f3bfa6f5fccc/input/fe903192-9db0-40ad-8d3f-149e3cd21c99.mp4"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/3.0/video-edit', {'prompt': 'Convert the entire scene to clay style', 'video': 'https://static.sandbase.ai/examples/d2c29bdb-fa51-4c8d-8cdc-f3bfa6f5fccc/input/fe903192-9db0-40ad-8d3f-149e3cd21c99.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/3.0/video-edit", {
  "prompt": "Convert the entire scene to clay style",
  "video": "https://static.sandbase.ai/examples/d2c29bdb-fa51-4c8d-8cdc-f3bfa6f5fccc/input/fe903192-9db0-40ad-8d3f-149e3cd21c99.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/3.0/video-edit", sandbase.Params{
	"prompt": "Convert the entire scene to clay style",
	"video": "https://static.sandbase.ai/examples/d2c29bdb-fa51-4c8d-8cdc-f3bfa6f5fccc/input/fe903192-9db0-40ad-8d3f-149e3cd21c99.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed (0-2147483647) for reproducible results. Omit for a random seed; the same seed may still produce slightly different results. range 0–2147483647 |
| `video` | string | yes | URL of the input video (MP4 or MOV; 1-15 seconds, at least 16 fps, 240-4096px per side, under 100MB).  |
| `audios` | array |  | Up to 5 optional reference audio URLs (WAV or MP3; 1-15s each, 15s total, under 15MB each).  |
| `images` | array |  | Up to 10 optional reference image URLs (JPEG, PNG, BMP, or WebP; up to 20MB each). Refer to them in the prompt as Image 1, Image 2, and so on.  |
| `prompt` | string | yes | Text instruction describing the editing. Refer to the input video as Video 1 and to reference images or audio as Image 1, Audio 1, and so on.  |
| `resolution` | string |  | Output video resolution tier. one of: `480p`, `720p`, `1080p`; default `"720p"` |
| `generate_audio` | boolean |  | Generate a synchronized audio track. Pricing is the same either way. default `true` |

## Details

Change an existing clip with a sentence: restyle it, swap a subject or prop, or rework the setting. Optional reference images and audio guide the change. The result keeps the length and framing of the source.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `video` | video URL, required | — | Source clip, Video 1 in the prompt. MP4/MOV, 1–15s, ≥16fps, 240–4096px per side, ≤100MB. |
| `images` | image URL[] (≤10) | — | Referenced as Image 1, Image 2, … |
| `audios` | audio URL[] (≤5) | — | WAV/MP3, 1–15s each, 15s total, ≤15MB. Referenced as Audio 1, … |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

There is no `duration` field; the output is as long as the source.

### Billing

Like the official Wan 3.0 rate, billing counts the source clip and the edited output, which are the same length, so each source second bills twice: $0.10 at 480p, $0.20 at 720p, $0.40 at 1080p. References are not metered.

| Source clip | Billed | 480p | 720p | 1080p |
|---|---|---|---|---|
| 2s | 4s | $0.20 | $0.40 | $0.80 |
| 5s | 10s | $0.50 | $1.00 | $2.00 |
| 10s | 20s | $1.00 | $2.00 | $4.00 |
| 15s | 30s | $1.50 | $3.00 | $6.00 |

The quote shown before submission assumes a 5-second source ($1.00 at 720p); the final charge uses the measured length. Failed runs are not charged. Output files are copied to SandBase storage and the returned URL stays valid for 7 days; download anything you need to keep.

### Prompting

- Lead with the change and state what must stay: “turn the scene into clay animation; keep her face and the camera motion”.
- Refer to the source as Video 1 and to references as Image 1 or Audio 1.
- Draft at 480p; edits cost twice the source length.

### Limits

- The output aspect ratio follows the source video.
- To add new footage after the clip, use video-extend.

### Also on SandBase

Other Wan 3.0 endpoints: `alibaba/wan/3.0/video` (all modes in one schema), `alibaba/wan/3.0/text-to-video`, `alibaba/wan/3.0/image-to-video`, `alibaba/wan/3.0/reference-to-video`, `alibaba/wan/3.0/video-extend`.

---
Machine-readable: [`catalog/models/alibaba/wan/3.0/video-edit.json`](../../../../../catalog/models/alibaba/wan/3.0/video-edit.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/3.0/video-edit
