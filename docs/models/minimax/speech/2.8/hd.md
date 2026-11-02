# MiniMax Speech 2.8 HD API: pricing, parameters and code examples

`minimax/speech/2.8/hd` · audio model · MiniMax · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.0026 per run, depending on parameters · **Modes:** async

MiniMax Speech 2.8 HD by MiniMax converts text into expressive, high-fidelity speech in 40+ languages with system or cloned voices and emotion control.

## Pricing

- Depends on parameters (`params.text`).

| parameters | USD |
|---|---|
| defaults | 0.0026 |

Formula: `len((params.text ?? "Hello, welcome to Sandbase")) / 1000 * 0.1`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/speech/2.8/hd", "text": "Hello, welcome to Sandbase", "voice_id": "Wise_Woman"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/speech/2.8/hd', {'text': 'Hello, welcome to Sandbase', 'voice_id': 'Wise_Woman'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/speech/2.8/hd", {
  "text": "Hello, welcome to Sandbase",
  "voice_id": "Wise_Woman"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/speech/2.8/hd", sandbase.Params{
	"text": "Hello, welcome to Sandbase",
	"voice_id": "Wise_Woman",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `text` | string | yes | Text to convert to speech. Use <#x#> between words to control pause duration (0.01-99.99s). default `"Hello, welcome to Sandbase"` |
| `pitch` | integer |  | Speech pitch. Range: -12 to 12, where 0 is normal pitch. default `0`; range -12–12 |
| `speed` | number |  | Speech speed. Range: 0.5-2.0, where 1.0 is normal speed. default `1`; range 0.5–2 |
| `format` | string |  | Format of generated sound. one of: `mp3`, `pcm`, `flac` |
| `volume` | number |  | Speech volume. Range: 0.1-10.0, where 1.0 is normal volume. default `1`; range 0.1–10 |
| `bitrate` | integer |  | Bitrate of generated sound. one of: `32000`, `64000`, `128000`, `256000` |
| `channel` | integer |  | The number of channels. 1: mono, 2: stereo. one of: `1`, `2` |
| `emotion` | string |  | The emotion of the generated speech. one of: `happy`, `sad`, `angry`, `fearful`, `disgusted`, `surprised`, `neutral`; default `"happy"` |
| `voice_id` | string | yes | Voice ID for speech synthesis. Use a predefined system voice or a custom cloned voice ID. default `"Wise_Woman"` |
| `sample_rate` | integer |  | Sample rate of generated sound. one of: `8000`, `16000`, `22050`, `24000`, `32000`, `44100` |
| `language_boost` | string |  | Enhance the ability to recognize specified languages and dialects. one of: `Chinese`, `Chinese,Yue`, `English`, `Arabic`, `Russian`, `Spanish`, `French`, `Portuguese`, `German`, `Turkish`, `Dutch`, `Ukrainian` … |
| `english_normalization` | boolean |  | Improves performance in number-reading scenarios. default `false` |

## Details

MiniMax Speech 2.8 HD: high-fidelity speech in 40+ languages with system or cloned voices, emotion control, and pitch, speed, and volume adjustment.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `text` | string, required | `Hello, welcome to Sandbase` | Text to speak. |
| `voice_id` | string, required | `Wise_Woman` | System voice or a cloned voice ID from `minimax/voice-clone`. |
| `speed` | number 0.5–2 | 1 | 0.5–2× speaking rate. |
| `volume` | number 0.1–10 | 1 | Loudness multiplier. |
| `pitch` | integer -12–12 | 0 | Semitones, −12 to 12. |
| `emotion` | `happy` / `sad` / `angry` / `fearful` / `disgusted` / `surprised` / `neutral` | `happy` | Delivery emotion. |
| `english_normalization` | boolean | false | Improves performance in number-reading scenarios. |
| `sample_rate` | 8000 / 16000 / 22050 / 24000 / 32000 / 44100 | — | Sample rate of generated sound. |
| `bitrate` | 32000 / 64000 / 128000 / 256000 | — | Bitrate of generated sound. |
| `channel` | 1 / 2 | — | The number of channels. |
| `format` | `mp3` / `pcm` / `flac` | — | Format of generated sound. |
| `language_boost` | `Chinese` / `Chinese,Yue` / `English` / `Arabic` / `Russian` / `Spanish` / `French` / `Portuguese` / `German` / `Turkish` / `Dutch` / `Ukrainian` / `Vietnamese` / `Indonesian` / `Japanese` / `Italian` / `Korean` / `Thai` / `Polish` / `Romanian` / `Greek` / `Czech` / `Finnish` / `Hindi` / `Bulgarian` / `Danish` / `Hebrew` / `Malay` / `Slovak` / `Swedish` / `Croatian` / `Hungarian` / `Norwegian` / `Slovenian` / `Catalan` / `Nynorsk` / `Afrikaans` / `auto` | — | Improve pronunciation for a specific language. |

### Billing

$0.10 per 1,000 characters, billed per character.

| Text | Price |
|---|---|
| 200 characters | $0.02 |
| 1,000 characters | $0.10 |
| 5,000 characters | $0.50 |

Failed runs are not charged.

### Prompting

- Use punctuation for pauses; MiniMax also reads pause tags such as `<#0.5#>`.

### Also on SandBase

Related: `minimax/speech/2.8/turbo`, `minimax/speech/2.6/hd`, `minimax/speech/2.6/turbo`, `minimax/voice-clone`, `minimax/voice-design`.

---
Machine-readable: [`catalog/models/minimax/speech/2.8/hd.json`](../../../../../catalog/models/minimax/speech/2.8/hd.json) · Store page: https://www.sandbase.ai/model/minimax/speech/2.8/hd
