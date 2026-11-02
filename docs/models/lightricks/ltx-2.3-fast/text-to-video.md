# LTX 2.3 Fast Text to Video API: pricing, parameters and code examples

`lightricks/ltx-2.3-fast/text-to-video` · video generation model · Lightricks · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.36 to $3.84 per run, depending on parameters · **Modes:** async

Ltx 2.3 Fast by Lightricks - generate cinematic videos from text descriptions with AI. Create high-quality video content with natural motion, camera control, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=6, resolution="1080p" | 0.36 |
| duration=6, resolution="1440p" | 0.72 |
| duration=6, resolution="2160p" | 1.44 |
| duration=8, resolution="1080p" | 0.48 |
| duration=8, resolution="1440p" | 0.96 |
| duration=8, resolution="2160p" | 1.92 |
| duration=10, resolution="1080p" | 0.6 |
| duration=10, resolution="1440p" | 1.2 |
| duration=10, resolution="2160p" | 2.4 |
| duration=12, resolution="1080p" | 0.72 |
| duration=12, resolution="1440p" | 1.44 |
| duration=12, resolution="2160p" | 2.88 |
| duration=14, resolution="1080p" | 0.84 |
| duration=14, resolution="1440p" | 1.68 |
| duration=14, resolution="2160p" | 3.36 |
| duration=16, resolution="1080p" | 0.96 |
| duration=16, resolution="1440p" | 1.92 |
| duration=16, resolution="2160p" | 3.84 |

Formula: `(params.resolution ?? "1080p") == "2160p" ? (params.duration ?? 6) * 0.24 : (params.resolution ?? "1080p") == "1440p" ? (params.duration ?? 6) * 0.12 : (params.duration ?? 6) * 0.06`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lightricks/ltx-2.3-fast/text-to-video", "prompt": "Drone descent through the open oculus of a derelict Soviet-era radio telescope dish, spiraling downward into the rusted parabolic bowl where a lone botanist catalogs wildflowers growing through cracked concrete, her red jacket the only color against oxidized metal and grey sky, 24mm on a caged FPV drone, the descent creating a vertigo spiral, Tarkovsky Stalker zones of alien beauty reclaiming technology, science swallowed by nature"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lightricks/ltx-2.3-fast/text-to-video', {'prompt': 'Drone descent through the open oculus of a derelict Soviet-era radio telescope dish, spiraling downward into the rusted parabolic bowl where a lone botanist catalogs wildflowers growing through cracked concrete, her red jacket the only color against oxidized metal and grey sky, 24mm on a caged FPV drone, the descent creating a vertigo spiral, Tarkovsky Stalker zones of alien beauty reclaiming technology, science swallowed by nature'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lightricks/ltx-2.3-fast/text-to-video", {
  "prompt": "Drone descent through the open oculus of a derelict Soviet-era radio telescope dish, spiraling downward into the rusted parabolic bowl where a lone botanist catalogs wildflowers growing through cracked concrete, her red jacket the only color against oxidized metal and grey sky, 24mm on a caged FPV drone, the descent creating a vertigo spiral, Tarkovsky Stalker zones of alien beauty reclaiming technology, science swallowed by nature"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lightricks/ltx-2.3-fast/text-to-video", sandbase.Params{
	"prompt": "Drone descent through the open oculus of a derelict Soviet-era radio telescope dish, spiraling downward into the rusted parabolic bowl where a lone botanist catalogs wildflowers growing through cracked concrete, her red jacket the only color against oxidized metal and grey sky, 24mm on a caged FPV drone, the descent creating a vertigo spiral, Tarkovsky Stalker zones of alien beauty reclaiming technology, science swallowed by nature",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The prompt to use for the generated video  |
| `duration` | integer |  | The duration of the generated video in seconds. The fast model supports 6-20 seconds. Note: Durations longer than 10 seconds (12, 14, 16, 18, 20) are only supported with 25 FPS and 1080p resolution. one of: `6`, `8`, `10`, `12`, `14`, `16`, `18`, `20`; default `6` |
| `resolution` | string |  | The resolution of the generated video one of: `1080p`, `1440p`, `2160p`; default `"1080p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`; default `"16:9"` |
| `generate_audio` | boolean |  | Whether to generate audio for the generated video default `true` |

## Details

LTX 2.3 Fast text to video: up to 20 second clips with native audio at 1080p, 1440p, or 4K (2160p).

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `1080p` / `1440p` / `2160p` | `1080p` | Sets the per-second rate. |
| `duration` | 6 / 8 / 10 / 12 / 14 / 16 / 18 / 20 | 6 | Output length in seconds. |
| `generate_audio` | boolean | true | Native audio. |

### Billing

You pay for output seconds: $0.06 at 1080p, $0.12 at 1440p, $0.24 at 2160p.

| Output | 1080p | 1440p | 2160p |
|---|---|---|---|
| 6s (default) | $0.36 | $0.72 | $1.44 |
| 10s | $0.60 | $1.20 | $2.40 |
| 20s | $1.20 | $2.40 | $4.80 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other LTX 2.3 endpoints: `lightricks/ltx-2.3-pro/text-to-video`, `lightricks/ltx-2.3-pro/image-to-video`, `lightricks/ltx-2.3-pro/audio-to-video`, `lightricks/ltx-2.3-pro/retake`.

---
Machine-readable: [`catalog/models/lightricks/ltx-2.3-fast/text-to-video.json`](../../../../catalog/models/lightricks/ltx-2.3-fast/text-to-video.json) · Store page: https://www.sandbase.ai/model/lightricks/ltx-2.3-fast/text-to-video
