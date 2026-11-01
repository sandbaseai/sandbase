# Kling V3 Standard Motion Control

`kwaivgi/kling-video/v3/standard/motion-control` · video · KwaiVGI

Kling V3 Standard Motion Control by Kuaishou transfers the motion, expressions, and camera movement of a reference video onto the character in an image, producing a 720p video up to 30 seconds.

## Pricing

- Depends on parameters (`params.video`).

Formula: `(media_duration(params.video) ?? 30.0) * 0.126`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v3/standard/motion-control", "image": "https://static.sandbase.ai/examples/c1db68ea-7172-405b-8987-c7dcefab1504/input/6636801e-5178-4cc0-bf52-f75f3ec82d05.png", "prompt": "An man dancing", "video": "https://static.sandbase.ai/examples/c1db68ea-7172-405b-8987-c7dcefab1504/input/b284089a-8264-4863-a3b1-3aecb37e4db8.mp4"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v3/standard/motion-control', {'image': 'https://static.sandbase.ai/examples/c1db68ea-7172-405b-8987-c7dcefab1504/input/6636801e-5178-4cc0-bf52-f75f3ec82d05.png', 'prompt': 'An man dancing', 'video': 'https://static.sandbase.ai/examples/c1db68ea-7172-405b-8987-c7dcefab1504/input/b284089a-8264-4863-a3b1-3aecb37e4db8.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v3/standard/motion-control", {
  "image": "https://static.sandbase.ai/examples/c1db68ea-7172-405b-8987-c7dcefab1504/input/6636801e-5178-4cc0-bf52-f75f3ec82d05.png",
  "prompt": "An man dancing",
  "video": "https://static.sandbase.ai/examples/c1db68ea-7172-405b-8987-c7dcefab1504/input/b284089a-8264-4863-a3b1-3aecb37e4db8.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v3/standard/motion-control", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/c1db68ea-7172-405b-8987-c7dcefab1504/input/6636801e-5178-4cc0-bf52-f75f3ec82d05.png",
	"prompt": "An man dancing",
	"video": "https://static.sandbase.ai/examples/c1db68ea-7172-405b-8987-c7dcefab1504/input/b284089a-8264-4863-a3b1-3aecb37e4db8.mp4",
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

Kling V3 Standard motion control: make the character in `image` perform the moves of a reference `video`, with body, hands, and expression following the source.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Optional scene and style direction. |
| `image` | image URL, required | — | Character to animate. JPEG, PNG, or WebP URL. |
| `video` | video URL, required | — | Reference video that supplies the motion. |
| `keep_original_sound` | boolean | true | Keep the reference video's audio track. |
| `character_orientation` | `image` / `video` | — | `video` follows the reference video's orientation (better for complex moves, up to 30s); `image` follows the image (better for camera moves, up to 10s). |

### Billing

You pay $0.126 per second of the reference video. The quote before submission assumes 30 seconds; the final charge uses the measured length.

| Reference video | Price |
|---|---|
| 5s reference | $0.63 |
| 10s reference | $1.26 |
| 30s reference | $3.78 |

Failed runs are not charged.

### Prompting

- Use a character image whose framing matches the person in the video.
- Pick `character_orientation` by what matters more: complex moves (`video`) or camera moves (`image`).

### Limits

- Up to 30 seconds with `character_orientation: video`, 10 seconds with `image`.

### Also on SandBase

Other Kling V3 Standard endpoints and tiers: `kwaivgi/kling-video/v3/standard/text-to-video`, `kwaivgi/kling-video/v3/standard/image-to-video`, `kwaivgi/kling-video/v3/pro/motion-control`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v3/standard/motion-control.json`](../../../../../../catalog/models/kwaivgi/kling-video/v3/standard/motion-control.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v3/standard/motion-control
