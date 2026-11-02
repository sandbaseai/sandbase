# Kling V2.6 Pro Motion Control API: pricing, parameters and code examples

`kwaivgi/kling-video/v2.6/pro/motion-control` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.56 per call · **Modes:** async

Kling V2.6 Pro Motion Control by Kuaishou transfers the motion, expressions, and camera movement of a reference video onto the character in an image, producing a 1080p video up to 30 seconds.

## Pricing

- Depends on parameters (`params.video`).

Formula: `(media_duration(params.video) ?? 30.0) * 0.112`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v2.6/pro/motion-control", "image": "https://static.sandbase.ai/examples/7ea5d3fc-c67f-4205-a731-f34e4f201086/input/64642a15-ebac-47b9-a202-18a3938b2457.png", "prompt": "An african american woman dancing", "video": "https://static.sandbase.ai/examples/7ea5d3fc-c67f-4205-a731-f34e4f201086/input/c91b52fe-022d-486f-9b87-45ffb4837f21.mp4"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v2.6/pro/motion-control', {'image': 'https://static.sandbase.ai/examples/7ea5d3fc-c67f-4205-a731-f34e4f201086/input/64642a15-ebac-47b9-a202-18a3938b2457.png', 'prompt': 'An african american woman dancing', 'video': 'https://static.sandbase.ai/examples/7ea5d3fc-c67f-4205-a731-f34e4f201086/input/c91b52fe-022d-486f-9b87-45ffb4837f21.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v2.6/pro/motion-control", {
  "image": "https://static.sandbase.ai/examples/7ea5d3fc-c67f-4205-a731-f34e4f201086/input/64642a15-ebac-47b9-a202-18a3938b2457.png",
  "prompt": "An african american woman dancing",
  "video": "https://static.sandbase.ai/examples/7ea5d3fc-c67f-4205-a731-f34e4f201086/input/c91b52fe-022d-486f-9b87-45ffb4837f21.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v2.6/pro/motion-control", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/7ea5d3fc-c67f-4205-a731-f34e4f201086/input/64642a15-ebac-47b9-a202-18a3938b2457.png",
	"prompt": "An african american woman dancing",
	"video": "https://static.sandbase.ai/examples/7ea5d3fc-c67f-4205-a731-f34e4f201086/input/c91b52fe-022d-486f-9b87-45ffb4837f21.mp4",
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

Kling V2.6 Pro motion control: the character in `image` performs the moves of a reference `video`.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Optional scene and style direction. |
| `image` | image URL, required | — | Character to animate. JPEG, PNG, or WebP URL. |
| `video` | video URL, required | — | Reference video that supplies the motion. |
| `keep_original_sound` | boolean | true | Keep the reference video's audio track. |
| `character_orientation` | `image` / `video` | — | `video` follows the reference video's orientation (better for complex moves, up to 30s); `image` follows the image (better for camera moves, up to 10s). |

### Billing

You pay $0.112 per second of the reference video. The quote before submission assumes 30 seconds; the final charge uses the measured length.

| Reference video | Price |
|---|---|
| 5s reference | $0.56 |
| 10s reference | $1.12 |
| 30s reference | $3.36 |

Failed runs are not charged.

### Prompting

- Match the character image's framing to the person in the video.

### Limits

- Up to 30 seconds with `character_orientation: video`, 10 seconds with `image`.

### Also on SandBase

Related: `kwaivgi/kling-video/v2.6/standard/motion-control`, `kwaivgi/kling-video/v3/pro/motion-control` (newer).

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v2.6/pro/motion-control.json`](../../../../../../catalog/models/kwaivgi/kling-video/v2.6/pro/motion-control.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v2.6/pro/motion-control
