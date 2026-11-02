# Gemini 3.1 Flash Tts API: pricing, parameters and code examples

`google/gemini-3.1-flash-tts` · audio model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.05 per run, depending on parameters · **Modes:** async

Gemini 3.1 Flash Tts by Google - convert text to natural-sounding speech with AI. Supports multiple voices, languages, emotions, and speaking styles for content creation and accessibility.

## Pricing

- Depends on parameters (`params.prompt`).

| parameters | USD |
|---|---|
| defaults | 0.05 |

Formula: `Math.max(1.0, Math.ceil(len(params.prompt ?? "") / 1000.0)) * 0.05`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-3.1-flash-tts", "prompt": "I can'\''t believe it worked! [laughing] After all those hours of debugging [sigh] it was just a missing semicolon."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-3.1-flash-tts', {'prompt': "I can't believe it worked! [laughing] After all those hours of debugging [sigh] it was just a missing semicolon."})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-3.1-flash-tts", {
  "prompt": "I can't believe it worked! [laughing] After all those hours of debugging [sigh] it was just a missing semicolon."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-3.1-flash-tts", sandbase.Params{
	"prompt": "I can't believe it worked! [laughing] After all those hours of debugging [sigh] it was just a missing semicolon.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `voice` | string |  | Voice preset for single-speaker synthesis. 30 distinct voices are available. Ignored when speakers is set. Popular choices: Kore (strong, firm female), Puck (upbeat, lively male), Charon (calm, professional male),… one of: `Achernar`, `Achird`, `Algenib`, `Algieba`, `Alnilam`, `Aoede`, `Autonoe`, `Callirrhoe`, `Charon`, `Despina`, `Enceladus`, `Erinome` …; default `"Kore"` |
| `prompt` | string | yes | The text to convert to speech. Gemini 3.1 Flash TTS supports natural-language prompting for style, pace, accent, and emotional expression — include delivery instructions inline with the text (e.g. 'Say cheerfully: Have…  |
| `speakers` | array |  | Multi-speaker voice configuration. When set, enables multi-speaker synthesis where different parts of the text are spoken by different voices. Each speaker needs a voice and a speaker_id (alias) that matches prefixes…  |
| `temperature` | number |  | Controls the randomness of the speech output. Higher values produce more creative and varied delivery, while lower values make the output more predictable and focused. default `1`; range 0–2 |
| `language_code` | string |  | Language for multilingual synthesis. When set, steers the model to speak in the specified language. If not set, the model auto-detects the language from the text. one of: `Arabic (Egypt)`, `Bangla (Bangladesh)`, `Dutch (Netherlands)`, `English (India)`, `English (US)`, `French (France)`, `German (Germany)`, `Hindi (India)`, `Indonesian (Indonesia)`, `Italian (Italy)`, `Japanese (Japan)`, `Korean (South Korea)` … |
| `output_format` | string |  | Audio output format. mp3: compressed, small file size (recommended). wav: uncompressed PCM wrapped in WAV (24 kHz, 16-bit mono). ogg_opus: Ogg container with Opus codec, good quality-to-size ratio. one of: `wav`, `mp3`, `ogg_opus`; default `"mp3"` |
| `style_instructions` | string |  | Optional style and delivery instructions prepended to the prompt. Controls expressiveness, accent, pace, tone, and emotional expression using natural language. Use this to separate style control from the text content.…  |

## Details

Gemini 3.1 Flash TTS speaks text in dozens of languages with 30 prebuilt voices, and supports two-speaker dialogue through `speakers`. Steer tone and pace with `style_instructions`.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text to speak. For dialogue, prefix lines with the speaker names defined in `speakers`. |
| `output_format` | `wav` / `mp3` / `ogg_opus` | `mp3` | Output file format. |
| `temperature` | number 0–2 | 1 | Higher values give more varied delivery. |
| `speakers` | object[] | — | Optional speaker-to-voice list for multi-speaker dialogue. |
| `language_code` | `Arabic (Egypt)` / `Bangla (Bangladesh)` / `Dutch (Netherlands)` / `English (India)` / `English (US)` / `French (France)` / `German (Germany)` / `Hindi (India)` / `Indonesian (Indonesia)` / `Italian (Italy)` / `Japanese (Japan)` / `Korean (South Korea)` / `Marathi (India)` / `Polish (Poland)` / `Portuguese (Brazil)` / `Romanian (Romania)` / `Russian (Russia)` / `Spanish (Spain)` / `Tamil (India)` / `Telugu (India)` / `Thai (Thailand)` / `Turkish (Turkey)` / `Ukrainian (Ukraine)` / `Vietnamese (Vietnam)` / `Afrikaans (South Africa)` / `Albanian (Albania)` / `Amharic (Ethiopia)` / `Arabic (World)` / `Armenian (Armenia)` / `Azerbaijani (Azerbaijan)` / `Basque (Spain)` / `Belarusian (Belarus)` / `Bulgarian (Bulgaria)` / `Burmese (Myanmar)` / `Catalan (Spain)` / `Cebuano (Philippines)` / `Chinese Mandarin (China)` / `Chinese Mandarin (Taiwan)` / `Croatian (Croatia)` / `Czech (Czech Republic)` / `Danish (Denmark)` / `English (Australia)` / `English (UK)` / `Estonian (Estonia)` / `Filipino (Philippines)` / `Finnish (Finland)` / `French (Canada)` / `Galician (Spain)` / `Georgian (Georgia)` / `Greek (Greece)` / `Gujarati (India)` / `Haitian Creole (Haiti)` / `Hebrew (Israel)` / `Hungarian (Hungary)` / `Icelandic (Iceland)` / `Javanese (Java)` / `Kannada (India)` / `Konkani (India)` / `Lao (Laos)` / `Latin (Vatican City)` / `Latvian (Latvia)` / `Lithuanian (Lithuania)` / `Luxembourgish (Luxembourg)` / `Macedonian (North Macedonia)` / `Maithili (India)` / `Malagasy (Madagascar)` / `Malay (Malaysia)` / `Malayalam (India)` / `Mongolian (Mongolia)` / `Nepali (Nepal)` / `Norwegian Bokmal (Norway)` / `Norwegian Nynorsk (Norway)` / `Odia (India)` / `Pashto (Afghanistan)` / `Persian (Iran)` / `Portuguese (Portugal)` / `Punjabi (India)` / `Serbian (Serbia)` / `Sindhi (India)` / `Sinhala (Sri Lanka)` / `Slovak (Slovakia)` / `Slovenian (Slovenia)` / `Spanish (Latin America)` / `Spanish (Mexico)` / `Swahili (Kenya)` / `Swedish (Sweden)` / `Urdu (Pakistan)` | — | Spoken language. |
| `voice` | `Achernar` / `Achird` / `Algenib` / `Algieba` / `Alnilam` / `Aoede` / `Autonoe` / `Callirrhoe` / `Charon` / `Despina` / `Enceladus` / `Erinome` / `Fenrir` / `Gacrux` / `Iapetus` / `Kore` / `Laomedeia` / `Leda` / `Orus` / `Pulcherrima` / `Puck` / `Rasalgethi` / `Sadachbia` / `Sadaltager` / `Schedar` / `Sulafat` / `Umbriel` / `Vindemiatrix` / `Zephyr` / `Zubenelgenubi` | `Kore` | Prebuilt voice for single-speaker requests. |
| `style_instructions` | string | — | How to say it. |

### Billing

$0.05 per started 1,000 characters of text.

| Text | Price |
|---|---|
| 200 characters | $0.05 |
| 1,000 characters | $0.05 |
| 2,500 characters | $0.15 |

Failed runs are not charged.

### Prompting

- For dialogue, write `Name: line` and map each name to a voice in `speakers`.

### Also on SandBase

Related: `google/gemini-3.8-flash-tts` (newer, cheaper).

---
Machine-readable: [`catalog/models/google/gemini-3.1-flash-tts.json`](../../../catalog/models/google/gemini-3.1-flash-tts.json) · Store page: https://www.sandbase.ai/model/google/gemini-3.1-flash-tts
