# Wan 2.2 Animate Replace API: pricing, parameters and code examples

`alibaba/wan/2.2/animate/replace` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.75 per call · **Modes:** async

Wan 2.2 Animate Replace replaces the person in the reference video with the character from the image.

## Pricing

- Depends on parameters (`params.resolution`, `params.video`, `usage.duration`, `usage.fps`).

Formula: `((usage.duration ?? media_duration(params.video) ?? 5.0) * (usage.fps ?? 30.0) / 16.0) * ((params.resolution ?? "720p") == "720p" ? 0.08 : (params.resolution ?? "720p") == "580p" ? 0.06 : 0.04)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.2/animate/replace", "image": "https://static.sandbase.ai/examples/874ae93a-9288-40dc-b214-6c73426b2d22/input/e9a4fdfa-de1e-494c-a286-70452a235cf1.png", "video": "https://static.sandbase.ai/examples/874ae93a-9288-40dc-b214-6c73426b2d22/input/c93e1785-2391-4b49-805a-bd2bfe345c93.mp4"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.2/animate/replace', {'image': 'https://static.sandbase.ai/examples/874ae93a-9288-40dc-b214-6c73426b2d22/input/e9a4fdfa-de1e-494c-a286-70452a235cf1.png', 'video': 'https://static.sandbase.ai/examples/874ae93a-9288-40dc-b214-6c73426b2d22/input/c93e1785-2391-4b49-805a-bd2bfe345c93.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.2/animate/replace", {
  "image": "https://static.sandbase.ai/examples/874ae93a-9288-40dc-b214-6c73426b2d22/input/e9a4fdfa-de1e-494c-a286-70452a235cf1.png",
  "video": "https://static.sandbase.ai/examples/874ae93a-9288-40dc-b214-6c73426b2d22/input/c93e1785-2391-4b49-805a-bd2bfe345c93.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.2/animate/replace", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/874ae93a-9288-40dc-b214-6c73426b2d22/input/e9a4fdfa-de1e-494c-a286-70452a235cf1.png",
	"video": "https://static.sandbase.ai/examples/874ae93a-9288-40dc-b214-6c73426b2d22/input/c93e1785-2391-4b49-805a-bd2bfe345c93.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility. range 0–2147483647 |
| `image` | string | yes | Input image URL (face / character).  |
| `video` | string | yes | Reference video.  |
| `use_turbo` | boolean |  | Faster generation with quality enhancement. default `false` |
| `resolution` | string |  | Output resolution. one of: `480p`, `580p`, `720p`; default `"720p"` |

## Details

Swap the person in a reference `video` for the character in `image`. Motion, camera, and scene come from the video; the new character's look comes from the picture, relit to fit the scene.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Character image. JPEG, PNG, or WebP URL. |
| `video` | video URL, required | — | Reference video that supplies the motion. |
| `resolution` | `480p` / `580p` / `720p` | `720p` | Sets the rate. |
| `use_turbo` | boolean | false | Faster generation at some quality cost. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

Billing follows the upstream unit: output seconds counted at 16 frames per second, so a 30fps output bills about 1.9× its wall-clock length. Rates per counted second: $0.04 at 480p, $0.06 at 580p, $0.08 at 720p. The quote before submission assumes a 5-second, 30fps result; the final charge uses the measured output.

| Output | 480p | 580p | 720p |
|---|---|---|---|
| 5s at 30fps | $0.375 | $0.5625 | $0.75 |
| 10s at 30fps | $0.75 | $1.125 | $1.50 |
| 10s at 16fps | $0.40 | $0.60 | $0.80 |

Failed runs are not charged.

### Prompting

- Match the character image's pose and framing to the person in the video where possible.
- Avoid videos with several people overlapping the subject.

### Limits

- Output length follows the reference video.

### Also on SandBase

Other Wan 2.2 endpoints: `alibaba/wan/2.2/animate/move`, `alibaba/wan/2.2/speech-to-video`.

---
Machine-readable: [`catalog/models/alibaba/wan/2.2/animate/replace.json`](../../../../../../catalog/models/alibaba/wan/2.2/animate/replace.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.2/animate/replace
