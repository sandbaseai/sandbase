# Kling V2.6 Standard Motion Control API: pricing, parameters and code examples

`kwaivgi/kling-video/v2.6/standard/motion-control` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.35 per call · **Modes:** async

Kling V2.6 Standard Motion Control by Kuaishou transfers the motion, expressions, and camera movement of a reference video onto the character in an image, producing a 720p video up to 30 seconds.

## Pricing

- Depends on parameters (`params.video`).

Formula: `(media_duration(params.video) ?? 30.0) * 0.07`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v2.6/standard/motion-control", "image": "https://static.sandbase.ai/examples/ea2553a1-add0-4631-a324-0554c964aa3c/input/721ef941-d65a-4761-90d4-df1e8815d295.png", "prompt": "An african american woman dancing", "video": "https://static.sandbase.ai/examples/ea2553a1-add0-4631-a324-0554c964aa3c/input/7263169e-1828-48e1-beef-d055a6eabbaf.mp4"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v2.6/standard/motion-control', {'image': 'https://static.sandbase.ai/examples/ea2553a1-add0-4631-a324-0554c964aa3c/input/721ef941-d65a-4761-90d4-df1e8815d295.png', 'prompt': 'An african american woman dancing', 'video': 'https://static.sandbase.ai/examples/ea2553a1-add0-4631-a324-0554c964aa3c/input/7263169e-1828-48e1-beef-d055a6eabbaf.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v2.6/standard/motion-control", {
  "image": "https://static.sandbase.ai/examples/ea2553a1-add0-4631-a324-0554c964aa3c/input/721ef941-d65a-4761-90d4-df1e8815d295.png",
  "prompt": "An african american woman dancing",
  "video": "https://static.sandbase.ai/examples/ea2553a1-add0-4631-a324-0554c964aa3c/input/7263169e-1828-48e1-beef-d055a6eabbaf.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v2.6/standard/motion-control", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/ea2553a1-add0-4631-a324-0554c964aa3c/input/721ef941-d65a-4761-90d4-df1e8815d295.png",
	"prompt": "An african american woman dancing",
	"video": "https://static.sandbase.ai/examples/ea2553a1-add0-4631-a324-0554c964aa3c/input/7263169e-1828-48e1-beef-d055a6eabbaf.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Reference image URL. The characters, backgrounds, and other elements in the generated video are based on this reference image. Characters should have clear body proportions, avoid occlusion, and occupy more than 5% of…  |
| `video` | string | yes | Reference video URL. The character actions in the generated video will be consistent with this reference video. Should contain a realistic style character with entire body or upper body visible, including head, without…  |
| `prompt` | string |  | Prompt  |
| `keep_original_sound` | boolean |  | Whether to keep the original sound from the reference video. default `true` |
| `character_orientation` | string |  | Controls whether the output character's orientation matches the reference image or video. 'video': orientation matches reference video - better for complex motions (max 30s). 'image': orientation matches reference… one of: `image`, `video` |

## Details

Kling V2.6 Standard motion control: the character in `image` performs the moves of a reference `video`.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Optional scene and style direction. |
| `image` | image URL, required | — | Character to animate. JPEG, PNG, or WebP URL. |
| `video` | video URL, required | — | Reference video that supplies the motion. |
| `character_orientation` | `image` / `video` | — | `video` follows the reference video's orientation (better for complex moves, up to 30s); `image` follows the image (better for camera moves, up to 10s). |
| `keep_original_sound` | boolean | true | Keep the reference video's audio track. |

### Billing

You pay $0.07 per second of the reference video. The quote before submission assumes 30 seconds; the final charge uses the measured length.

| Reference video | Price |
|---|---|
| 5s reference | $0.35 |
| 10s reference | $0.70 |
| 30s reference | $2.10 |

Failed runs are not charged.

### Prompting

- Match the character image's framing to the person in the video.

### Limits

- Up to 30 seconds with `character_orientation: video`, 10 seconds with `image`.

### Also on SandBase

Related: `kwaivgi/kling-video/v2.6/pro/motion-control`, `kwaivgi/kling-video/v3/standard/motion-control` (newer).

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v2.6/standard/motion-control.json`](../../../../../../catalog/models/kwaivgi/kling-video/v2.6/standard/motion-control.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v2.6/standard/motion-control
