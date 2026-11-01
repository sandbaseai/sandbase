# ElevenLabs Eleven v4 Turbo

`elevenlabs/v4-turbo` · audio · ElevenLabs

Eleven v4 Turbo is the low-latency tier of ElevenLabs' v4 text-to-speech generation, for real-time and high-volume narration.

## Pricing

- Depends on parameters (`params.text`).

| parameters | USD |
|---|---|
| defaults | 0.04 |

Formula: `Math.max(1.0, Math.ceil(len(params.text ?? "") / 1000.0)) * 0.04`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "elevenlabs/v4-turbo", "text": "Hello from SandBase."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('elevenlabs/v4-turbo', {'text': 'Hello from SandBase.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("elevenlabs/v4-turbo", {
  "text": "Hello from SandBase."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "elevenlabs/v4-turbo", sandbase.Params{
	"text": "Hello from SandBase.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Seed for best-effort reproducibility. Identical output is not guaranteed. range 0–4294967295 |
| `text` | string | yes | The text to convert to speech. Supports audio tags such as [whispering] and IPA pronunciation enclosed in forward slashes.  |
| `voice` | string |  | The voice to use for speech generation default `"Rachel"` |
| `stability` | number |  | Voice stability. Lower values allow more expressive delivery; higher values make delivery more consistent. default `0.5`; range 0–1 |
| `timestamps` | boolean |  | Whether to return character-level timing information with the generated audio. default `false` |
| `language_code` | string |  | Language code (ISO 639-1) for speech generation and text normalization.  |
| `output_format` | string |  | Output format of the generated audio. Formatted as codec_sample_rate_bitrate. one of: `mp3_22050_32`, `mp3_44100_32`, `mp3_44100_64`, `mp3_44100_96`, `mp3_44100_128`, `mp3_44100_192`, `opus_48000_32`, `opus_48000_64`, `opus_48000_96`, `opus_48000_128`, `opus_48000_192`; default `"mp3_44100_128"` |
| `similarity_boost` | number |  | How closely the output follows the reference voice. Higher values increase similarity but may reduce naturalness. default `0.75`; range 0–1 |
| `apply_text_normalization` | string |  | Whether to normalize text such as numbers and dates before generation. one of: `auto`, `on`, `off`; default `"auto"` |

## Details

Eleven v4 Turbo, the low-latency v4 tier for real-time and high-volume narration.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `text` | string, required | — | Text to speak. |
| `output_format` | `mp3_22050_32` / `mp3_44100_32` / `mp3_44100_64` / `mp3_44100_96` / `mp3_44100_128` / `mp3_44100_192` / `opus_48000_32` / `opus_48000_64` / `opus_48000_96` / `opus_48000_128` / `opus_48000_192` | `mp3_44100_128` | Output file format. |
| `seed` | integer 0–4294967295 | random | Fix it to compare prompt changes. |
| `stability` | number 0–1 | 0.5 | Lower is more expressive; higher is more consistent. |
| `similarity_boost` | number 0–1 | 0.75 | How closely to match the voice. |
| `apply_text_normalization` | `auto` / `on` / `off` | `auto` | Whether to normalize text such as numbers and dates before generation. |
| `language_code` | string | — | Force a language. |
| `timestamps` | boolean | false | Return word timings. |
| `voice` | string | `Rachel` | Voice name or ID. |

### Billing

$0.04 per started 1,000 characters, with a one-unit minimum.

| Text | Price |
|---|---|
| 200 characters | $0.04 |
| 1,000 characters | $0.04 |
| 2,500 characters | $0.12 |

Failed runs are not charged.

### Prompting

- Use punctuation and line breaks to shape pauses.

### Also on SandBase

Other ElevenLabs voices: `elevenlabs/v4`, `elevenlabs/v3`, `elevenlabs/multilingual-v2`.

---
Machine-readable: [`catalog/models/elevenlabs/v4-turbo.json`](../../../catalog/models/elevenlabs/v4-turbo.json) · Store page: https://www.sandbase.ai/model/elevenlabs/v4-turbo
