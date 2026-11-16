# Kling V4 Flash Image to Video API: pricing, parameters and code examples

`kwaivgi/kling-video/v4/flash/image-to-video` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.282 to $1.88 per run, depending on parameters · **Modes:** async

Kling V4 Flash Image to Video by Kuaishou animates a start image into a 3-20 second 720p video at a lower price than Kling V4.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=3 | 0.282 |
| duration=5 | 0.47 |
| duration=20 | 1.88 |

Formula: `(params.duration ?? 5) * 0.094`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v4/flash/image-to-video", "image": "https://static.sandbase.ai/examples/f7115edf-3ff0-42a8-b28c-daa7bc658111/input/0554146a-a649-485b-be48-497e51131c34.png", "prompt": "The same elements in the reference are rigid: the fictional KITO Runner 01 low-top sneaker: off-white suede overlays (#EEE9DF) on a bone-coloured finely perforated engineered mesh upper, a sage-green suede heel tab (#8FA383), a natural gum-rubber cupsole with a fine herringbone edge, tonal off-white flat laces and tonal off-white stitching; the only marking is a small debossed \"KITO\" on the sage heel tab. It is a single right shoe standing on a warm light-grey paper seamless that curves up into the background with no visible horizon line. Preserve every element exactly; the shoe and the set are frozen, only the camera moves along the keyframed trajectory: one complete, eased 360-degree orbit around the shoe like a motion-control product rig, dipping slightly lower as it passes the back and the inner side, then rising and pushing in gently to finish on a slightly higher hero three-quarter view of the same outer side it started on.\nUNSEEN SIDES must be coherent with the visible ones: the heel shows the full sage-green suede heel tab with the small debossed '\''KITO'\'' centred on it; the medial (inner) side mirrors the lateral side'\''s off-white suede overlay layout on the perforated bone mesh; the gum cupsole wraps all the way round with the same height and herringbone edge; tonal off-white laces and stitching everywhere. The shoe is one pair-half: never a second shoe.\nLIGHT is fixed in the world: one large soft key from the upper left, so as the camera orbits the suede nap and perforations catch raking light on the far side and the gum sole glows slightly translucent when backlit; the soft contact shadow stays anchored to the floor.\nAVOID: the shoe rotating or sliding instead of the camera, sole thickness changing, extra eyelets, lace geometry re-tying itself, stripes or swoosh-like marks appearing, logo text anywhere except the heel tab, seamless edge or studio gear coming into frame, flicker, warped toe box."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v4/flash/image-to-video', {'image': 'https://static.sandbase.ai/examples/f7115edf-3ff0-42a8-b28c-daa7bc658111/input/0554146a-a649-485b-be48-497e51131c34.png', 'prompt': 'The same elements in the reference are rigid: the fictional KITO Runner 01 low-top sneaker: off-white suede overlays (#EEE9DF) on a bone-coloured finely perforated engineered mesh upper, a sage-green suede heel tab (#8FA383), a natural gum-rubber cupsole with a fine herringbone edge, tonal off-white flat laces and tonal off-white stitching; the only marking is a small debossed "KITO" on the sage heel tab. It is a single right shoe standing on a warm light-grey paper seamless that curves up into the background with no visible horizon line. Preserve every element exactly; the shoe and the set are frozen, only the camera moves along the keyframed trajectory: one complete, eased 360-degree orbit around the shoe like a motion-control product rig, dipping slightly lower as it passes the back and the inner side, then rising and pushing in gently to finish on a slightly higher hero three-quarter view of the same outer side it started on.\nUNSEEN SIDES must be coherent with the visible ones: the heel shows the full sage-green suede heel tab with the small debossed \'KITO\' centred on it; the medial (inner) side mirrors the lateral side\'s off-white suede overlay layout on the perforated bone mesh; the gum cupsole wraps all the way round with the same height and herringbone edge; tonal off-white laces and stitching everywhere. The shoe is one pair-half: never a second shoe.\nLIGHT is fixed in the world: one large soft key from the upper left, so as the camera orbits the suede nap and perforations catch raking light on the far side and the gum sole glows slightly translucent when backlit; the soft contact shadow stays anchored to the floor.\nAVOID: the shoe rotating or sliding instead of the camera, sole thickness changing, extra eyelets, lace geometry re-tying itself, stripes or swoosh-like marks appearing, logo text anywhere except the heel tab, seamless edge or studio gear coming into frame, flicker, warped toe box.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v4/flash/image-to-video", {
  "image": "https://static.sandbase.ai/examples/f7115edf-3ff0-42a8-b28c-daa7bc658111/input/0554146a-a649-485b-be48-497e51131c34.png",
  "prompt": "The same elements in the reference are rigid: the fictional KITO Runner 01 low-top sneaker: off-white suede overlays (#EEE9DF) on a bone-coloured finely perforated engineered mesh upper, a sage-green suede heel tab (#8FA383), a natural gum-rubber cupsole with a fine herringbone edge, tonal off-white flat laces and tonal off-white stitching; the only marking is a small debossed \"KITO\" on the sage heel tab. It is a single right shoe standing on a warm light-grey paper seamless that curves up into the background with no visible horizon line. Preserve every element exactly; the shoe and the set are frozen, only the camera moves along the keyframed trajectory: one complete, eased 360-degree orbit around the shoe like a motion-control product rig, dipping slightly lower as it passes the back and the inner side, then rising and pushing in gently to finish on a slightly higher hero three-quarter view of the same outer side it started on.\nUNSEEN SIDES must be coherent with the visible ones: the heel shows the full sage-green suede heel tab with the small debossed 'KITO' centred on it; the medial (inner) side mirrors the lateral side's off-white suede overlay layout on the perforated bone mesh; the gum cupsole wraps all the way round with the same height and herringbone edge; tonal off-white laces and stitching everywhere. The shoe is one pair-half: never a second shoe.\nLIGHT is fixed in the world: one large soft key from the upper left, so as the camera orbits the suede nap and perforations catch raking light on the far side and the gum sole glows slightly translucent when backlit; the soft contact shadow stays anchored to the floor.\nAVOID: the shoe rotating or sliding instead of the camera, sole thickness changing, extra eyelets, lace geometry re-tying itself, stripes or swoosh-like marks appearing, logo text anywhere except the heel tab, seamless edge or studio gear coming into frame, flicker, warped toe box."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v4/flash/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/f7115edf-3ff0-42a8-b28c-daa7bc658111/input/0554146a-a649-485b-be48-497e51131c34.png",
	"prompt": "The same elements in the reference are rigid: the fictional KITO Runner 01 low-top sneaker: off-white suede overlays (#EEE9DF) on a bone-coloured finely perforated engineered mesh upper, a sage-green suede heel tab (#8FA383), a natural gum-rubber cupsole with a fine herringbone edge, tonal off-white flat laces and tonal off-white stitching; the only marking is a small debossed \"KITO\" on the sage heel tab. It is a single right shoe standing on a warm light-grey paper seamless that curves up into the background with no visible horizon line. Preserve every element exactly; the shoe and the set are frozen, only the camera moves along the keyframed trajectory: one complete, eased 360-degree orbit around the shoe like a motion-control product rig, dipping slightly lower as it passes the back and the inner side, then rising and pushing in gently to finish on a slightly higher hero three-quarter view of the same outer side it started on.\nUNSEEN SIDES must be coherent with the visible ones: the heel shows the full sage-green suede heel tab with the small debossed 'KITO' centred on it; the medial (inner) side mirrors the lateral side's off-white suede overlay layout on the perforated bone mesh; the gum cupsole wraps all the way round with the same height and herringbone edge; tonal off-white laces and stitching everywhere. The shoe is one pair-half: never a second shoe.\nLIGHT is fixed in the world: one large soft key from the upper left, so as the camera orbits the suede nap and perforations catch raking light on the far side and the gum sole glows slightly translucent when backlit; the soft contact shadow stays anchored to the floor.\nAVOID: the shoe rotating or sliding instead of the camera, sole thickness changing, extra eyelets, lace geometry re-tying itself, stripes or swoosh-like marks appearing, logo text anywhere except the heel tab, seamless edge or studio gear coming into frame, flicker, warped toe box.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | First frame. Min 300x300 px, aspect ratio 0.4-2.5, up to 30 MB.  |
| `prompt` | string | yes | Describe subject, action, camera and light.  |
| `duration` | integer |  | Output length in seconds (3-20). default `5`; range 3–20 |

## Details

Kling V4 Flash image-to-video animates a start image into a 3–20 second 720p clip with sound, at a lower price than Kling V4.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | What moves and how the camera moves. |
| `image` | image URL, required | — | First frame. Min 300×300 px, aspect ratio 0.4–2.5, up to 30 MB. |
| `duration` | 3–20 | 5 | Output length in seconds. |
### Billing
Billed per output second: $0.094 at 720p.
| Output | Price |
|---|---|
| 5s (default) | $0.47 |
| 10s | $0.94 |
| 20s | $1.88 |
Failed runs are not charged.
### Prompting
- Describe what moves and how the camera moves; the image sets the look.
### Limits
- Output is 720p only; clips are 3–20 seconds.
- Start frame only. For an end frame, use `kwaivgi/kling-video/v4/image-to-video`.
### Also on SandBase
Other Kling V4 Flash endpoints: `kwaivgi/kling-video/v4/flash/text-to-video`, `kwaivgi/kling-video/v4/flash/image-to-video`, `kwaivgi/kling-video/v4/flash/reference-to-video`, `kwaivgi/kling-video/v4/flash/video-edit`. For 1080p or clips up to 30 seconds, use Kling V4 (`kwaivgi/kling-video/v4/text-to-video` and its siblings).

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v4/flash/image-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/v4/flash/image-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v4/flash/image-to-video
