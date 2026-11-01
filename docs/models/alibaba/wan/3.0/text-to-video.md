# Wan 3.0 Text to Video

`alibaba/wan/3.0/text-to-video` · video · Alibaba

Wan 3.0 by Alibaba turns a text prompt into a video of up to 30 seconds at 30fps, with native dialogue, music, and sound effects.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=2, resolution="480p" | 0.1 * |
| duration=2, resolution="720p" | 0.2 * |
| duration=2, resolution="1080p" | 0.4 * |
| duration=3, resolution="480p" | 0.15 * |
| duration=3, resolution="720p" | 0.3 * |
| duration=3, resolution="1080p" | 0.6 * |
| duration=4, resolution="480p" | 0.2 * |
| duration=4, resolution="720p" | 0.4 * |
| duration=4, resolution="1080p" | 0.8 * |
| duration=5, resolution="480p" | 0.25 * |
| duration=5, resolution="720p" | 0.5 * |
| duration=5, resolution="1080p" | 1 * |
| duration=6, resolution="480p" | 0.3 * |
| duration=6, resolution="720p" | 0.6 * |
| duration=6, resolution="1080p" | 1.2 * |

\* estimate: assumes output duration equals requested duration.

Formula: `((params.duration ?? 5) == "auto" ? Math.round(usage.duration ?? 30.0) : (params.duration ?? 5)) * ((params.resolution ?? "720p") == "1080p" ? 0.20 : (params.resolution ?? "720p") == "480p" ? 0.05 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/3.0/text-to-video", "duration": 20, "prompt": "A 20-second ultra-widescreen plush universe adventure clip, featuring ultra-fine plush textures throughout, cinematic space scale, a contrast between cute appearances and intense action, exaggerated FPV camera movements, and realistic soft-body physics. A spaceship made of plush fabric, buttons, zippers, and stuffing cotton carries three small plush animals — a rabbit, a fox, and a crow — fleeing at high speed through a universe composed of giant yarn planets, fluffy nebulae, and puppet giant beasts. A massive interstellar whale beast covered in deep blue long fur with eyes like two glass buttons chases the ship from within the nebula. The dynamics include the zipper ship launching via catapult, high-speed orbiting around a yarn planet, the giant whale bursting out from behind, navigating through a button asteroid belt, being swallowed by the whale beast, escaping through a golden zipper on its back, the whale slowly deflating as if losing its stuffing cotton, and finally flying through a pink-purple fluffy nebula toward a colorful button sun."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/3.0/text-to-video', {'duration': 20, 'prompt': 'A 20-second ultra-widescreen plush universe adventure clip, featuring ultra-fine plush textures throughout, cinematic space scale, a contrast between cute appearances and intense action, exaggerated FPV camera movements, and realistic soft-body physics. A spaceship made of plush fabric, buttons, zippers, and stuffing cotton carries three small plush animals — a rabbit, a fox, and a crow — fleeing at high speed through a universe composed of giant yarn planets, fluffy nebulae, and puppet giant beasts. A massive interstellar whale beast covered in deep blue long fur with eyes like two glass buttons chases the ship from within the nebula. The dynamics include the zipper ship launching via catapult, high-speed orbiting around a yarn planet, the giant whale bursting out from behind, navigating through a button asteroid belt, being swallowed by the whale beast, escaping through a golden zipper on its back, the whale slowly deflating as if losing its stuffing cotton, and finally flying through a pink-purple fluffy nebula toward a colorful button sun.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/3.0/text-to-video", {
  "duration": 20,
  "prompt": "A 20-second ultra-widescreen plush universe adventure clip, featuring ultra-fine plush textures throughout, cinematic space scale, a contrast between cute appearances and intense action, exaggerated FPV camera movements, and realistic soft-body physics. A spaceship made of plush fabric, buttons, zippers, and stuffing cotton carries three small plush animals — a rabbit, a fox, and a crow — fleeing at high speed through a universe composed of giant yarn planets, fluffy nebulae, and puppet giant beasts. A massive interstellar whale beast covered in deep blue long fur with eyes like two glass buttons chases the ship from within the nebula. The dynamics include the zipper ship launching via catapult, high-speed orbiting around a yarn planet, the giant whale bursting out from behind, navigating through a button asteroid belt, being swallowed by the whale beast, escaping through a golden zipper on its back, the whale slowly deflating as if losing its stuffing cotton, and finally flying through a pink-purple fluffy nebula toward a colorful button sun."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/3.0/text-to-video", sandbase.Params{
	"duration": 20,
	"prompt": "A 20-second ultra-widescreen plush universe adventure clip, featuring ultra-fine plush textures throughout, cinematic space scale, a contrast between cute appearances and intense action, exaggerated FPV camera movements, and realistic soft-body physics. A spaceship made of plush fabric, buttons, zippers, and stuffing cotton carries three small plush animals — a rabbit, a fox, and a crow — fleeing at high speed through a universe composed of giant yarn planets, fluffy nebulae, and puppet giant beasts. A massive interstellar whale beast covered in deep blue long fur with eyes like two glass buttons chases the ship from within the nebula. The dynamics include the zipper ship launching via catapult, high-speed orbiting around a yarn planet, the giant whale bursting out from behind, navigating through a button asteroid belt, being swallowed by the whale beast, escaping through a golden zipper on its back, the whale slowly deflating as if losing its stuffing cotton, and finally flying through a pink-purple fluffy nebula toward a colorful button sun.",
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
| `resolution` | string |  | Output video resolution tier. one of: `480p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Defaults to 16:9. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`; default `"16:9"` |
| `generate_audio` | boolean |  | Generate a synchronized audio track. Pricing is the same either way. default `true` |

## Details

Write a scene and get back a 2–30 second, 30fps clip with matching dialogue, music, and sound effects. No images or reference media are needed.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `duration` | 2–30 or `auto` | 5 | `auto` lets the model pick the length. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `aspect_ratio` | `adaptive` / `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `adaptive` | `adaptive` follows the prompt and inputs. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds only: $0.05 at 480p, $0.10 at 720p, $0.20 at 1080p. Input images, audio, and video are not metered.

| Output | Billed | 480p | 720p | 1080p |
|---|---|---|---|---|
| 2s | 2s | $0.10 | $0.20 | $0.40 |
| 5s (default) | 5s | $0.25 | $0.50 | $1.00 |
| 10s | 10s | $0.50 | $1.00 | $2.00 |
| 30s | 30s | $1.50 | $3.00 | $6.00 |

With `duration: "auto"` the run is pre-authorized at 30 seconds, then settled on the length that was actually generated. Failed runs are not charged. Output files are copied to SandBase storage and the returned URL stays valid for 7 days; download anything you need to keep.

### Prompting

- Cover subject, action, setting, camera, light, and sound in one or two sentences each.
- Spell out camera timing, e.g. “holds for two seconds, then cranes up over the rooftops”.
- Quote dialogue and say who speaks it.

> At night a kitten trots along a wet rooftop; neon signs flicker across the city behind it. Low tracking shot that rises as it leaps a gap, soft rain and distant traffic.

### Limits

- This endpoint accepts no media inputs. To animate a picture use image-to-video; to steer with references use reference-to-video.

### Also on SandBase

Other Wan 3.0 endpoints: `alibaba/wan/3.0/video` (all modes in one schema), `alibaba/wan/3.0/image-to-video`, `alibaba/wan/3.0/reference-to-video`, `alibaba/wan/3.0/video-edit`, `alibaba/wan/3.0/video-extend`.

---
Machine-readable: [`catalog/models/alibaba/wan/3.0/text-to-video.json`](../../../../../catalog/models/alibaba/wan/3.0/text-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/3.0/text-to-video
