# Gemini 3.8 Flash TTS

`google/gemini-3.8-flash-tts` · audio · Google

Gemini 3.8 Flash TTS by Google turns text into expressive speech with 30 prebuilt voices and natural-language style direction.

## Pricing

- Depends on parameters (`params.prompt`).

| parameters | USD |
|---|---|
| defaults | 0.045 |

Formula: `Math.max(1.0, Math.ceil(len(params.prompt ?? "") / 1000.0)) * 0.045`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-3.8-flash-tts", "prompt": "Have a wonderful day!"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-3.8-flash-tts', {'prompt': 'Have a wonderful day!'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-3.8-flash-tts", {
  "prompt": "Have a wonderful day!"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-3.8-flash-tts", sandbase.Params{
	"prompt": "Have a wonderful day!",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `voice` | string |  | Prebuilt voice for single-speaker speech. one of: `Achernar`, `Achird`, `Algenib`, `Algieba`, `Alnilam`, `Aoede`, `Autonoe`, `Callirrhoe`, `Charon`, `Despina`, `Enceladus`, `Erinome` …; default `"Kore"` |
| `prompt` | string | yes | Verbatim text to speak. Put delivery directions in style_instructions; inline vocal events may use <laugh> or <sigh>. The provider limits the complete input to 8,192 tokens.  |
| `style_instructions` | string |  | Delivery style, separate from the spoken transcript.  |

## Details

Gemini 3.8 Flash TTS turns text into expressive speech with 30 prebuilt voices. Direct the delivery in plain language with `style_instructions`, such as tone, pace, or accent.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text to speak. |
| `style_instructions` | string | — | How to say it, e.g. “warm and unhurried, slight smile”. |
| `voice` | `Achernar` / `Achird` / `Algenib` / `Algieba` / `Alnilam` / `Aoede` / `Autonoe` / `Callirrhoe` / `Charon` / `Despina` / `Enceladus` / `Erinome` / `Fenrir` / `Gacrux` / `Iapetus` / `Kore` / `Laomedeia` / `Leda` / `Orus` / `Pulcherrima` / `Puck` / `Rasalgethi` / `Sadachbia` / `Sadaltager` / `Schedar` / `Sulafat` / `Umbriel` / `Vindemiatrix` / `Zephyr` / `Zubenelgenubi` | `Kore` | Prebuilt voice. |

### Billing

$0.045 per started 1,000 characters of text, with a one-unit minimum.

| Text | Price |
|---|---|
| 200 characters | $0.045 |
| 1,000 characters | $0.045 |
| 2,500 characters | $0.135 |

Failed runs are not charged.

### Prompting

- Put delivery direction in `style_instructions`, not in the text itself.

### Limits

- Single speaker per request.

### Also on SandBase

Related: `google/gemini-3.8-flash-lite-tts` (cheaper), `google/gemini-3.1-flash-tts` (multi-speaker).

---
Machine-readable: [`catalog/models/google/gemini-3.8-flash-tts.json`](../../../catalog/models/google/gemini-3.8-flash-tts.json) · Store page: https://www.sandbase.ai/model/google/gemini-3.8-flash-tts
