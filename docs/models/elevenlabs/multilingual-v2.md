# Multilingual V2

`elevenlabs/multilingual-v2` · audio · ElevenLabs

Eleven Multilingual v2 is ElevenLabs' stable, lifelike text-to-speech model for 29 languages. Choose a voice, set stability and speaking speed, and turn written text into narration.

## Pricing

- Depends on parameters (`params.text`).

| parameters | USD |
|---|---|
| defaults | 0.2 |

Formula: `Math.max(1.0, Math.ceil(len(params.text ?? "") / 1000.0)) * 0.2`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "elevenlabs/multilingual-v2"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('elevenlabs/multilingual-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("elevenlabs/multilingual-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "elevenlabs/multilingual-v2", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `text` | string |  | The text to convert to speech  |
| `speed` | number |  | Speech speed (0.7-1.2). Values below 1.0 slow down the speech, above 1.0 speed it up. Extreme values may affect quality. default `1`; range 0.7–1.2 |
| `voice` | string |  | The voice to use for speech generation default `"Rachel"` |
| `stability` | number |  | Voice stability (0-1) default `0.5`; range 0–1 |
| `language_code` | string |  | Language code (ISO 639-1) used to enforce a language for the model. one of: ``, `en`, `ja`, `zh`, `de`, `hi`, `fr`, `ko`, `pt`, `it`, `es`, `id` … |

## Details

Eleven Multilingual v2: stable, lifelike speech in 29 languages.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `text` | string | — | Text to speak. |
| `voice` | string | `Rachel` | Voice name or ID. |
| `language_code` | `` / `en` / `ja` / `zh` / `de` / `hi` / `fr` / `ko` / `pt` / `it` / `es` / `id` / `nl` / `tr` / `fil` / `pl` / `sv` / `bg` / `ro` / `ar` / `cs` / `el` / `fi` / `hr` / `ms` / `sk` / `da` / `ta` / `uk` / `ru` | — | Force a language. |
| `stability` | number 0–1 | 0.5 | Lower is more expressive; higher is more consistent. |
| `speed` | number 0.7–1.2 | 1 | Speaking rate. |

### Billing

$0.20 per started 1,000 characters, with a one-unit minimum.

| Text | Price |
|---|---|
| 200 characters | $0.20 |
| 1,000 characters | $0.20 |
| 2,500 characters | $0.60 |

Failed runs are not charged.

### Prompting

- Use punctuation and line breaks to shape pauses.

### Also on SandBase

Other ElevenLabs voices: `elevenlabs/v4`, `elevenlabs/v4-turbo`, `elevenlabs/v3`.

---
Machine-readable: [`catalog/models/elevenlabs/multilingual-v2.json`](../../../catalog/models/elevenlabs/multilingual-v2.json) · Store page: https://www.sandbase.ai/model/elevenlabs/multilingual-v2
