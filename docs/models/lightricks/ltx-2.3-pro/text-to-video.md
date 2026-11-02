# LTX 2.3 Pro Text to Video API: pricing, parameters and code examples

`lightricks/ltx-2.3-pro/text-to-video` · video generation model · Lightricks · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.48 to $3.2 per run, depending on parameters · **Modes:** async

Ltx 2.3 Pro is Lightricks's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic motion, lighting, and scene composition.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=6, resolution="1080p" | 0.48 |
| duration=6, resolution="1440p" | 0.96 |
| duration=6, resolution="2160p" | 1.92 |
| duration=8, resolution="1080p" | 0.64 |
| duration=8, resolution="1440p" | 1.28 |
| duration=8, resolution="2160p" | 2.56 |
| duration=10, resolution="1080p" | 0.8 |
| duration=10, resolution="1440p" | 1.6 |
| duration=10, resolution="2160p" | 3.2 |

Formula: `(params.resolution ?? "1080p") == "2160p" ? (params.duration ?? 6) * 0.32 : (params.resolution ?? "1080p") == "1440p" ? (params.duration ?? 6) * 0.16 : (params.duration ?? 6) * 0.08`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lightricks/ltx-2.3-pro/text-to-video", "prompt": "Through-the-veil shot of a bride'\''s face during an Indian wedding ceremony, camera positioned behind the sheer red dupatta fabric, the embroidered pattern creating a textured overlay on her face, her eyes lined with kohl looking down at henna-covered hands, marigold garlands in soft background bokeh, 85mm f/1.2 focused through the fabric layer, warm tungsten and candlelight, Mira Nair Monsoon Wedding intimacy"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lightricks/ltx-2.3-pro/text-to-video', {'prompt': "Through-the-veil shot of a bride's face during an Indian wedding ceremony, camera positioned behind the sheer red dupatta fabric, the embroidered pattern creating a textured overlay on her face, her eyes lined with kohl looking down at henna-covered hands, marigold garlands in soft background bokeh, 85mm f/1.2 focused through the fabric layer, warm tungsten and candlelight, Mira Nair Monsoon Wedding intimacy"})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lightricks/ltx-2.3-pro/text-to-video", {
  "prompt": "Through-the-veil shot of a bride's face during an Indian wedding ceremony, camera positioned behind the sheer red dupatta fabric, the embroidered pattern creating a textured overlay on her face, her eyes lined with kohl looking down at henna-covered hands, marigold garlands in soft background bokeh, 85mm f/1.2 focused through the fabric layer, warm tungsten and candlelight, Mira Nair Monsoon Wedding intimacy"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lightricks/ltx-2.3-pro/text-to-video", sandbase.Params{
	"prompt": "Through-the-veil shot of a bride's face during an Indian wedding ceremony, camera positioned behind the sheer red dupatta fabric, the embroidered pattern creating a textured overlay on her face, her eyes lined with kohl looking down at henna-covered hands, marigold garlands in soft background bokeh, 85mm f/1.2 focused through the fabric layer, warm tungsten and candlelight, Mira Nair Monsoon Wedding intimacy",
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
| `duration` | integer |  | The duration of the generated video in seconds one of: `6`, `8`, `10`; default `6` |
| `resolution` | string |  | The resolution of the generated video one of: `1080p`, `1440p`, `2160p`; default `"1080p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`; default `"16:9"` |
| `generate_audio` | boolean |  | Whether to generate audio for the generated video default `true` |

## Details

LTX 2.3 Pro text to video: 6–10 second clips with native audio at 1080p, 1440p, or 4K (2160p).

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `1080p` / `1440p` / `2160p` | `1080p` | Sets the per-second rate. |
| `duration` | 6 / 8 / 10 | 6 | Output length in seconds. |
| `generate_audio` | boolean | true | Native audio. |

### Billing

You pay for output seconds: $0.08 at 1080p, $0.16 at 1440p, $0.32 at 2160p.

| Output | 1080p | 1440p | 2160p |
|---|---|---|---|
| 6s (default) | $0.48 | $0.96 | $1.92 |
| 8s | $0.64 | $1.28 | $2.56 |
| 10s | $0.80 | $1.60 | $3.20 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other LTX 2.3 endpoints: `lightricks/ltx-2.3-pro/image-to-video`, `lightricks/ltx-2.3-pro/audio-to-video`, `lightricks/ltx-2.3-pro/retake`, `lightricks/ltx-2.3-pro/video-extend`.

---
Machine-readable: [`catalog/models/lightricks/ltx-2.3-pro/text-to-video.json`](../../../../catalog/models/lightricks/ltx-2.3-pro/text-to-video.json) · Store page: https://www.sandbase.ai/model/lightricks/ltx-2.3-pro/text-to-video
