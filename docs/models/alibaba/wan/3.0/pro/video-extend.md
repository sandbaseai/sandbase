# Wan 3.0 Pro Video Extend API: pricing, parameters and code examples

`alibaba/wan/3.0/pro/video-extend` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $3.6 per call · **Modes:** async

Wan 3.0 Pro Video Extend by Alibaba continues an input video forward from a text instruction, optionally guided by reference images and audio, with native audio, upscaled to 1080p, 2K, or 4K.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `params.video`, `usage.duration`).

Formula: `(((params.duration ?? 5) == "auto" ? Math.round(usage.duration ?? 30.0) : (params.duration ?? 5)) + Math.ceil(Math.min(media_duration(params.video) ?? 15.0, 15.0))) * ((params.resolution ?? "1080p") == "4k" ? 0.23 : (params.resolution ?? "1080p") == "2k" ? 0.20 : 0.18)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/3.0/pro/video-extend", "duration": 5, "prompt": "Extend Video 1 forward by 5s. Character A is a male with short dark brown hair wearing a black tailcoat, white shirt, black bow tie, and beige vest. Character B is a female with brown upswept hair wearing a beige puff-sleeve vintage long dress with black lace trim on the skirt, and dark teardrop earrings. Inside the ballroom, crystal chandelier light reflects off the marble floor. Guests chat in small groups, holding glasses and speaking in low voices. A graceful waltz string prelude slowly begins, and the guests'\'' conversations gradually quiet. Character B walks slowly from one side of the ballroom, her skirt hem lightly brushing the marble floor, her gaze surveying the room. Character A emerges from the crowd, walks past the guests directly to Character B, gives a slight bow and extends his right hand, his gaze warm and attentive. Character B lowers her eyes with a gentle smile, lightly placing her right hand on Character A'\''s palm. The two exchange a smile, and Character A leads Character B to the center of the dance floor. The surrounding guests naturally step back to make room, all eyes focused on the pair. Character A'\''s left hand holds Character B'\''s right hand raised, his right hand gently resting on her lower back. The two assume the waltz pose, stepping out on the downbeat of the strings, beginning to spin. The elegant atmosphere of a 19th-century court ball, warm golden tones.", "video": "https://static.sandbase.ai/examples/1bafed32-8bcb-4102-b3fd-fc58ebad06b9/input/6c526f9d-eee8-419d-9dca-a3040428cd0a.mp4"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/3.0/pro/video-extend', {'duration': 5, 'prompt': "Extend Video 1 forward by 5s. Character A is a male with short dark brown hair wearing a black tailcoat, white shirt, black bow tie, and beige vest. Character B is a female with brown upswept hair wearing a beige puff-sleeve vintage long dress with black lace trim on the skirt, and dark teardrop earrings. Inside the ballroom, crystal chandelier light reflects off the marble floor. Guests chat in small groups, holding glasses and speaking in low voices. A graceful waltz string prelude slowly begins, and the guests' conversations gradually quiet. Character B walks slowly from one side of the ballroom, her skirt hem lightly brushing the marble floor, her gaze surveying the room. Character A emerges from the crowd, walks past the guests directly to Character B, gives a slight bow and extends his right hand, his gaze warm and attentive. Character B lowers her eyes with a gentle smile, lightly placing her right hand on Character A's palm. The two exchange a smile, and Character A leads Character B to the center of the dance floor. The surrounding guests naturally step back to make room, all eyes focused on the pair. Character A's left hand holds Character B's right hand raised, his right hand gently resting on her lower back. The two assume the waltz pose, stepping out on the downbeat of the strings, beginning to spin. The elegant atmosphere of a 19th-century court ball, warm golden tones.", 'video': 'https://static.sandbase.ai/examples/1bafed32-8bcb-4102-b3fd-fc58ebad06b9/input/6c526f9d-eee8-419d-9dca-a3040428cd0a.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/3.0/pro/video-extend", {
  "duration": 5,
  "prompt": "Extend Video 1 forward by 5s. Character A is a male with short dark brown hair wearing a black tailcoat, white shirt, black bow tie, and beige vest. Character B is a female with brown upswept hair wearing a beige puff-sleeve vintage long dress with black lace trim on the skirt, and dark teardrop earrings. Inside the ballroom, crystal chandelier light reflects off the marble floor. Guests chat in small groups, holding glasses and speaking in low voices. A graceful waltz string prelude slowly begins, and the guests' conversations gradually quiet. Character B walks slowly from one side of the ballroom, her skirt hem lightly brushing the marble floor, her gaze surveying the room. Character A emerges from the crowd, walks past the guests directly to Character B, gives a slight bow and extends his right hand, his gaze warm and attentive. Character B lowers her eyes with a gentle smile, lightly placing her right hand on Character A's palm. The two exchange a smile, and Character A leads Character B to the center of the dance floor. The surrounding guests naturally step back to make room, all eyes focused on the pair. Character A's left hand holds Character B's right hand raised, his right hand gently resting on her lower back. The two assume the waltz pose, stepping out on the downbeat of the strings, beginning to spin. The elegant atmosphere of a 19th-century court ball, warm golden tones.",
  "video": "https://static.sandbase.ai/examples/1bafed32-8bcb-4102-b3fd-fc58ebad06b9/input/6c526f9d-eee8-419d-9dca-a3040428cd0a.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/3.0/pro/video-extend", sandbase.Params{
	"duration": 5,
	"prompt": "Extend Video 1 forward by 5s. Character A is a male with short dark brown hair wearing a black tailcoat, white shirt, black bow tie, and beige vest. Character B is a female with brown upswept hair wearing a beige puff-sleeve vintage long dress with black lace trim on the skirt, and dark teardrop earrings. Inside the ballroom, crystal chandelier light reflects off the marble floor. Guests chat in small groups, holding glasses and speaking in low voices. A graceful waltz string prelude slowly begins, and the guests' conversations gradually quiet. Character B walks slowly from one side of the ballroom, her skirt hem lightly brushing the marble floor, her gaze surveying the room. Character A emerges from the crowd, walks past the guests directly to Character B, gives a slight bow and extends his right hand, his gaze warm and attentive. Character B lowers her eyes with a gentle smile, lightly placing her right hand on Character A's palm. The two exchange a smile, and Character A leads Character B to the center of the dance floor. The surrounding guests naturally step back to make room, all eyes focused on the pair. Character A's left hand holds Character B's right hand raised, his right hand gently resting on her lower back. The two assume the waltz pose, stepping out on the downbeat of the strings, beginning to spin. The elegant atmosphere of a 19th-century court ball, warm golden tones.",
	"video": "https://static.sandbase.ai/examples/1bafed32-8bcb-4102-b3fd-fc58ebad06b9/input/6c526f9d-eee8-419d-9dca-a3040428cd0a.mp4",
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
| `prompt` | string | yes | Text instruction describing the extension. Refer to the input video as Video 1 and to reference images or audio as Image 1, Audio 1, and so on.  |
| `duration` | enum |  | Duration of the extension in seconds (2-30), or `auto` to let the model choose. The input video length plus this duration must not exceed 30 seconds. `auto` is pre-authorized at 30 seconds and billed on the actual… one of: `auto`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12` …; default `5` |
| `resolution` | string |  | Output resolution tier after FlashVSR super-resolution. one of: `1080p`, `2k`, `4k`; default `"1080p"` |
| `generate_audio` | boolean |  | Generate a synchronized audio track. Pricing is the same either way. default `true` |

## Details

Continue a clip past its last frame. The model carries over the subject, look, and camera language of the source and generates the next beat you describe. The response contains the new segment only, so you can cut it onto the original yourself. Pro runs the same Wan 3.0 model, then upscales the result with FlashVSR, so output comes back at 1080p, 2K, or 4K. For 480p or 720p use the non-Pro endpoints.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `video` | video URL, required | — | Source clip, Video 1 in the prompt. MP4/MOV, 1–15s, ≥16fps, 240–4096px per side, ≤100MB. |
| `images` | image URL[] (≤10) | — | Referenced as Image 1, Image 2, … |
| `audios` | audio URL[] (≤5) | — | WAV/MP3, 1–15s each, 15s total, ≤15MB. Referenced as Audio 1, … |
| `duration` | 2–30 or `auto` | 5 | Length of the new segment. Source + duration ≤ 30s. |
| `resolution` | `1080p` / `2k` / `4k` | `1080p` | Output tier after FlashVSR super-resolution; sets the per-second rate. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

The aspect ratio always follows the source, so there is no `aspect_ratio` field.

### Billing

Following the Wan 3.0 Pro rule, billed seconds are the source clip length (rounded up) plus the new segment: $0.18 at 1080p, $0.20 at 2K, $0.23 at 4K per second. References are not metered. If the source length cannot be read, 15s is assumed, which is also what the listed starting price uses.

| Source + new segment | Billed | 1080p | 2K | 4K |
|---|---|---|---|---|
| 5s + 5s | 10s | $1.80 | $2.00 | $2.30 |
| 10s + 5s | 15s | $2.70 | $3.00 | $3.45 |
| 15s + 5s (default) | 20s | $3.60 | $4.00 | $4.60 |
| 15s + 15s | 30s | $5.40 | $6.00 | $6.90 |

With `duration: "auto"` the run is pre-authorized at 30 seconds, then settled on the length that was actually generated. Failed runs are not charged. Output files are copied to SandBase storage and the returned URL stays valid for 7 days; download anything you need to keep.

### Prompting

- Describe what happens next, not what the source already shows: “Extend Video 1 forward: the baker carries the tray to the oven and the camera follows.”
- Mention the subject and direction of movement again if continuity matters.
- Keep the source short when you need a long extension; both count toward 30 seconds.

### Limits

- The returned video is the extension only; the source is not included.
- To change the existing footage instead, use video-edit.

### Also on SandBase

Other Wan 3.0 Pro endpoints: `alibaba/wan/3.0/pro/video` (all modes in one schema), `alibaba/wan/3.0/pro/text-to-video`, `alibaba/wan/3.0/pro/image-to-video`, `alibaba/wan/3.0/pro/reference-to-video`, `alibaba/wan/3.0/pro/video-edit`.

---
Machine-readable: [`catalog/models/alibaba/wan/3.0/pro/video-extend.json`](../../../../../../catalog/models/alibaba/wan/3.0/pro/video-extend.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/3.0/pro/video-extend
