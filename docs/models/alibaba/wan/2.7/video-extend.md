# Wan 2.7 Video Extend

`alibaba/wan/2.7/video-extend` · video · Alibaba

Alibaba Wan 2.7 Video Extend continues an input clip from a text instruction, optionally ending on a chosen last frame, for a total length of up to 15 seconds.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=2, resolution="720p" | 0.2 |
| duration=2, resolution="1080p" | 0.3 |
| duration=3, resolution="720p" | 0.3 |
| duration=3, resolution="1080p" | 0.45 |
| duration=4, resolution="720p" | 0.4 |
| duration=4, resolution="1080p" | 0.6 |
| duration=5, resolution="720p" | 0.5 |
| duration=5, resolution="1080p" | 0.75 |
| duration=6, resolution="720p" | 0.6 |
| duration=6, resolution="1080p" | 0.9 |
| duration=7, resolution="720p" | 0.7 |
| duration=7, resolution="1080p" | 1.05 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "720p") == '1080p' ? 0.15 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.7/video-extend", "prompt": "The baker brings over the glazed bread, sets the brush aside, and the camera follows him to the oven at the back to bake it. The baker closes the oven door, stands beside it watching the bread, smells the aroma, and says, \"so good\".", "video": "https://static.sandbase.ai/examples/e1e1d989-70de-4368-b8d6-3a0919be90be/input/3627aff0-af0f-4067-813d-02de847a28b4.mp4"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.7/video-extend', {'prompt': 'The baker brings over the glazed bread, sets the brush aside, and the camera follows him to the oven at the back to bake it. The baker closes the oven door, stands beside it watching the bread, smells the aroma, and says, "so good".', 'video': 'https://static.sandbase.ai/examples/e1e1d989-70de-4368-b8d6-3a0919be90be/input/3627aff0-af0f-4067-813d-02de847a28b4.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.7/video-extend", {
  "prompt": "The baker brings over the glazed bread, sets the brush aside, and the camera follows him to the oven at the back to bake it. The baker closes the oven door, stands beside it watching the bread, smells the aroma, and says, \"so good\".",
  "video": "https://static.sandbase.ai/examples/e1e1d989-70de-4368-b8d6-3a0919be90be/input/3627aff0-af0f-4067-813d-02de847a28b4.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.7/video-extend", sandbase.Params{
	"prompt": "The baker brings over the glazed bread, sets the brush aside, and the camera follows him to the oven at the back to bake it. The baker closes the oven door, stands beside it watching the bread, smells the aroma, and says, \"so good\".",
	"video": "https://static.sandbase.ai/examples/e1e1d989-70de-4368-b8d6-3a0919be90be/input/3627aff0-af0f-4067-813d-02de847a28b4.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed (0-2147483647) for reproducible results. Omit for a random seed. range 0–2147483647 |
| `video` | string | yes | URL of the source clip to continue (MP4 or MOV, 2-10 seconds, 240-4096px per side, up to 100MB).  |
| `prompt` | string | yes | What happens after the source clip ends: action, camera movement, scene progression, and sound. Up to 5,000 characters.  |
| `duration` | integer |  | Total length of the output in seconds, including the source clip (2-15). For a 3-second source and duration 10, the model adds 7 seconds. Must be longer than the source clip. one of: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13` …; default `5` |
| `end_image` | string |  | Optional last frame the continuation should end on (JPEG, PNG, BMP, or WebP; 240-8000px per side, up to 20MB).  |
| `resolution` | string |  | The resolution of the video to generate. one of: `720p`, `1080p`; default `"720p"` |

## Details

Continue an existing clip. Wan 2.7 picks up from the last frame of `video` and generates new footage that follows your prompt; add `end_image` to say where the continuation should land.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `video` | video URL, required | — | Clip to continue. |
| `end_image` | image URL | — | Optional frame the new footage should end on. |
| `duration` | 2–15 | 5 | Length of the new footage in seconds. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.10 at 720p and $0.15 at 1080p, the same as Alibaba's list price. Only the new footage is billed.

| New footage | 720p | 1080p |
|---|---|---|
| 2s | $0.20 | $0.30 |
| 5s (default) | $0.50 | $0.75 |
| 10s | $1.00 | $1.50 |
| 15s | $1.50 | $2.25 |

Failed runs are not charged.

### Prompting

- Describe what happens next, not what is already in the clip.
- Match the source's camera style unless you want a deliberate change.
- Use `end_image` when the shot must finish on a specific composition.

### Limits

- The returned video contains the continuation; join it to the source in your editor if you need one file.

### Also on SandBase

Other Wan 2.7 endpoints: `alibaba/wan/2.7/text-to-video`, `alibaba/wan/2.7/image-to-video`, `alibaba/wan/2.7/reference-to-video`, `alibaba/wan/2.7/video-edit`, `alibaba/wan/3.0/video` (newer, up to 30s).

---
Machine-readable: [`catalog/models/alibaba/wan/2.7/video-extend.json`](../../../../../catalog/models/alibaba/wan/2.7/video-extend.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.7/video-extend
