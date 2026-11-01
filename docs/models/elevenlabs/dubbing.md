# ElevenLabs Dubbing

`elevenlabs/dubbing` · video · ElevenLabs

ElevenLabs Dubbing translates the speech in a video into another language while preserving each speaker's voice, timing, and background audio.

## Pricing

- Depends on parameters (`params.video`, `usage.duration`).

Formula: `Math.ceil((media_duration(params.video) ?? usage.duration ?? 60.0) / 60.0) * 0.6`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "elevenlabs/dubbing", "target_lang": "es", "video": "https://static.sandbase.ai/examples/8f64921f-0d6e-4239-a36a-7419390685bc/input/2515467e-312a-4f21-a8e1-763533464bb3.mp4"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('elevenlabs/dubbing', {'target_lang': 'es', 'video': 'https://static.sandbase.ai/examples/8f64921f-0d6e-4239-a36a-7419390685bc/input/2515467e-312a-4f21-a8e1-763533464bb3.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("elevenlabs/dubbing", {
  "target_lang": "es",
  "video": "https://static.sandbase.ai/examples/8f64921f-0d6e-4239-a36a-7419390685bc/input/2515467e-312a-4f21-a8e1-763533464bb3.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "elevenlabs/dubbing", sandbase.Params{
	"target_lang": "es",
	"video": "https://static.sandbase.ai/examples/8f64921f-0d6e-4239-a36a-7419390685bc/input/2515467e-312a-4f21-a8e1-763533464bb3.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | URL of the video file to dub (MP4 / MOV). The dubbed result is returned as a video.  |
| `source_lang` | string |  | Source language code. If not provided, will be auto-detected.  |
| `target_lang` | string | yes | Target language code for dubbing (ISO 639-1)  |
| `num_speakers` | integer |  | Number of speakers in the audio. If not provided, will be auto-detected. range 1–50 |
| `highest_resolution` | boolean |  | Whether to use the highest resolution for dubbing. default `true` |

## Details

ElevenLabs Dubbing translates the speech in a video into another language while keeping each speaker's voice, timing, and the background audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `video` | video URL, required | — | Video to dub. |
| `source_lang` | string | — | Source language; omit to detect. |
| `num_speakers` | integer 1–50 | — | Speaker count; omit to detect. |
| `target_lang` | string, required | — | Language to dub into. |
| `highest_resolution` | boolean | true | Keep the source resolution. |

### Billing

$0.60 per started minute of video. The quote before submission assumes 1 minute; the final charge uses the measured length.

| Video | Price |
|---|---|
| 1 min | $0.60 |
| 5 min | $3.00 |
| 15 min | $9.00 |

Failed runs are not charged.

---
Machine-readable: [`catalog/models/elevenlabs/dubbing.json`](../../../catalog/models/elevenlabs/dubbing.json) · Store page: https://www.sandbase.ai/model/elevenlabs/dubbing
