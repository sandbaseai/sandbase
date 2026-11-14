# Wan 3.0 Pro Text to Video API: pricing, parameters and code examples

`alibaba/wan/3.0/pro/text-to-video` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.36 to $1.38 per run, depending on parameters · **Modes:** async

Wan 3.0 Pro by Alibaba turns a text prompt into a video of up to 30 seconds at 30fps, with native dialogue, music, and sound effects, upscaled to 1080p, 2K, or 4K.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=2, resolution="1080p" | 0.36 * |
| duration=2, resolution="2k" | 0.4 * |
| duration=2, resolution="4k" | 0.46 * |
| duration=3, resolution="1080p" | 0.54 * |
| duration=3, resolution="2k" | 0.6 * |
| duration=3, resolution="4k" | 0.69 * |
| duration=4, resolution="1080p" | 0.72 * |
| duration=4, resolution="2k" | 0.8 * |
| duration=4, resolution="4k" | 0.92 * |
| duration=5, resolution="1080p" | 0.9 * |
| duration=5, resolution="2k" | 1 * |
| duration=5, resolution="4k" | 1.15 * |
| duration=6, resolution="1080p" | 1.08 * |
| duration=6, resolution="2k" | 1.2 * |
| duration=6, resolution="4k" | 1.38 * |

\* estimate: assumes output duration equals requested duration.

Formula: `((params.duration ?? 5) == "auto" ? Math.round(usage.duration ?? 30.0) : (params.duration ?? 5)) * ((params.resolution ?? "1080p") == "4k" ? 0.23 : (params.resolution ?? "1080p") == "2k" ? 0.20 : 0.18)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/3.0/pro/text-to-video", "aspect_ratio": "16:9", "duration": 8, "prompt": "An 8-second ultra-widescreen plush universe adventure clip, featuring ultra-fine plush textures throughout, cinematic space scale, a contrast between cute appearances and intense action, exaggerated FPV camera movements, and realistic soft-body physics. A spaceship made of plush fabric, buttons, zippers, and stuffing cotton carries three small plush animals — a rabbit, a fox, and a crow — fleeing at high speed through a universe composed of giant yarn planets, fluffy nebulae, and puppet giant beasts. A massive interstellar whale beast covered in deep blue long fur with eyes like two glass buttons chases the ship from within the nebula. The dynamics include the zipper ship launching via catapult, high-speed orbiting around a yarn planet, the giant whale bursting out from behind, navigating through a button asteroid belt, being swallowed by the whale beast, escaping through a golden zipper on its back, the whale slowly deflating as if losing its stuffing cotton, and finally flying through a pink-purple fluffy nebula toward a colorful button sun."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/3.0/pro/text-to-video', {'aspect_ratio': '16:9', 'duration': 8, 'prompt': 'An 8-second ultra-widescreen plush universe adventure clip, featuring ultra-fine plush textures throughout, cinematic space scale, a contrast between cute appearances and intense action, exaggerated FPV camera movements, and realistic soft-body physics. A spaceship made of plush fabric, buttons, zippers, and stuffing cotton carries three small plush animals — a rabbit, a fox, and a crow — fleeing at high speed through a universe composed of giant yarn planets, fluffy nebulae, and puppet giant beasts. A massive interstellar whale beast covered in deep blue long fur with eyes like two glass buttons chases the ship from within the nebula. The dynamics include the zipper ship launching via catapult, high-speed orbiting around a yarn planet, the giant whale bursting out from behind, navigating through a button asteroid belt, being swallowed by the whale beast, escaping through a golden zipper on its back, the whale slowly deflating as if losing its stuffing cotton, and finally flying through a pink-purple fluffy nebula toward a colorful button sun.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/3.0/pro/text-to-video", {
  "aspect_ratio": "16:9",
  "duration": 8,
  "prompt": "An 8-second ultra-widescreen plush universe adventure clip, featuring ultra-fine plush textures throughout, cinematic space scale, a contrast between cute appearances and intense action, exaggerated FPV camera movements, and realistic soft-body physics. A spaceship made of plush fabric, buttons, zippers, and stuffing cotton carries three small plush animals — a rabbit, a fox, and a crow — fleeing at high speed through a universe composed of giant yarn planets, fluffy nebulae, and puppet giant beasts. A massive interstellar whale beast covered in deep blue long fur with eyes like two glass buttons chases the ship from within the nebula. The dynamics include the zipper ship launching via catapult, high-speed orbiting around a yarn planet, the giant whale bursting out from behind, navigating through a button asteroid belt, being swallowed by the whale beast, escaping through a golden zipper on its back, the whale slowly deflating as if losing its stuffing cotton, and finally flying through a pink-purple fluffy nebula toward a colorful button sun."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/3.0/pro/text-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"duration": 8,
	"prompt": "An 8-second ultra-widescreen plush universe adventure clip, featuring ultra-fine plush textures throughout, cinematic space scale, a contrast between cute appearances and intense action, exaggerated FPV camera movements, and realistic soft-body physics. A spaceship made of plush fabric, buttons, zippers, and stuffing cotton carries three small plush animals — a rabbit, a fox, and a crow — fleeing at high speed through a universe composed of giant yarn planets, fluffy nebulae, and puppet giant beasts. A massive interstellar whale beast covered in deep blue long fur with eyes like two glass buttons chases the ship from within the nebula. The dynamics include the zipper ship launching via catapult, high-speed orbiting around a yarn planet, the giant whale bursting out from behind, navigating through a button asteroid belt, being swallowed by the whale beast, escaping through a golden zipper on its back, the whale slowly deflating as if losing its stuffing cotton, and finally flying through a pink-purple fluffy nebula toward a colorful button sun.",
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
| `prompt` | string | yes | Text prompt for the generated video.  |
| `duration` | enum |  | Output duration in seconds (2-30), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 30 seconds and billed on the actual output length. one of: `auto`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12` …; default `5` |
| `resolution` | string |  | Output resolution tier after FlashVSR super-resolution. one of: `1080p`, `2k`, `4k`; default `"1080p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Defaults to 16:9. one of: `16:9`, `4:3`, `1:1`, `3:4`, `9:16`; default `"16:9"` |
| `generate_audio` | boolean |  | Generate a synchronized audio track. Pricing is the same either way. default `true` |

## Details

Write a scene and get back a 2–30 second, 30fps clip with matching dialogue, music, and sound effects. No images or reference media are needed. Pro runs the same Wan 3.0 model, then upscales the result with FlashVSR, so output comes back at 1080p, 2K, or 4K. For 480p or 720p use the non-Pro endpoints.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `duration` | 2–30 or `auto` | 5 | `auto` lets the model pick the length. |
| `resolution` | `1080p` / `2k` / `4k` | `1080p` | Output tier after FlashVSR super-resolution; sets the per-second rate. |
| `aspect_ratio` | `adaptive` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `adaptive` | `adaptive` follows the prompt and inputs. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds only: $0.18 at 1080p, $0.20 at 2K, $0.23 at 4K. Input images, audio, and video are not metered.

| Output | Billed | 1080p | 2K | 4K |
|---|---|---|---|---|
| 2s | 2s | $0.36 | $0.40 | $0.46 |
| 5s (default) | 5s | $0.90 | $1.00 | $1.15 |
| 10s | 10s | $1.80 | $2.00 | $2.30 |
| 30s | 30s | $5.40 | $6.00 | $6.90 |

With `duration: "auto"` the run is pre-authorized at 30 seconds, then settled on the length that was actually generated. Failed runs are not charged. Output files are copied to SandBase storage and the returned URL stays valid for 7 days; download anything you need to keep.

### Prompting

- Cover subject, action, setting, camera, light, and sound in one or two sentences each.
- Spell out camera timing, e.g. “holds for two seconds, then cranes up over the rooftops”.
- Quote dialogue and say who speaks it.

> At night a kitten trots along a wet rooftop; neon signs flicker across the city behind it. Low tracking shot that rises as it leaps a gap, soft rain and distant traffic.

### Limits

- This endpoint accepts no media inputs. To animate a picture use image-to-video; to steer with references use reference-to-video.

### Also on SandBase

Other Wan 3.0 Pro endpoints: `alibaba/wan/3.0/pro/video` (all modes in one schema), `alibaba/wan/3.0/pro/image-to-video`, `alibaba/wan/3.0/pro/reference-to-video`, `alibaba/wan/3.0/pro/video-edit`, `alibaba/wan/3.0/pro/video-extend`.

---
Machine-readable: [`catalog/models/alibaba/wan/3.0/pro/text-to-video.json`](../../../../../../catalog/models/alibaba/wan/3.0/pro/text-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/3.0/pro/text-to-video
