# HeyGen Voice Turbo

`heygen/heygen-voice/turbo` · audio · HeyGen

HeyGen Voice Turbo is the faster, lower-cost HeyGen text-to-speech model, with the same voices, languages and voice cloning.

## Pricing

- Depends on parameters (`params.text`).

| parameters | USD |
|---|---|
| defaults | 0.004 |

Formula: `Math.max(1.0, Math.ceil(len(params.text ?? "") / 1000.0)) * 0.004`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "heygen/heygen-voice/turbo", "text": "Welcome to SandBase. One API key gives you thousands of AI models for images, video, audio and text.", "voice": "Jonah"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('heygen/heygen-voice/turbo', {'text': 'Welcome to SandBase. One API key gives you thousands of AI models for images, video, audio and text.', 'voice': 'Jonah'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("heygen/heygen-voice/turbo", {
  "text": "Welcome to SandBase. One API key gives you thousands of AI models for images, video, audio and text.",
  "voice": "Jonah"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "heygen/heygen-voice/turbo", sandbase.Params{
	"text": "Welcome to SandBase. One API key gives you thousands of AI models for images, video, audio and text.",
	"voice": "Jonah",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `text` | string | yes | Text to speak, up to 5,000 characters.  |
| `voice` | string |  | HeyGen public voice. Ignored when reference_audio is set. one of: `Jonah`, `Nadine`, `Tabitha`, `Soren`, `Elowen`, `Vincent`, `Jocelyn`, `Marielle`, `Corinne`, `Lucian`, `Kieran`, `Hugh` …; default `"Jonah"` |
| `language` | string |  | Language of the text. Detected automatically when omitted. one of: `ar`, `be`, `bg`, `ca`, `cs`, `da`, `de`, `el`, `en`, `es`, `fa`, `fi` … |
| `reference_audio` | string |  | Optional single-speaker recording to clone instead of a public voice. Only the first 3 minutes are used.  |

## Details

HeyGen Voice Turbo is the faster, lower-cost HeyGen text-to-speech model, with the same voices, languages and voice cloning as HeyGen Voice.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `text` | string, required | — | Up to 5,000 characters. |
| `voice` | 24 public voices | `Jonah` | Ignored when `reference_audio` is set. |
| `language` | ISO 639-1 code (39 languages) | auto | Language of the text. |
| `reference_audio` | audio URL | — | Single-speaker recording to clone; the first 3 minutes are used. |
### Billing
$0.004 per started 1,000 characters of input text.
| Text | Price |
|---|---|
| Up to 1,000 characters | $0.004 |
| 2,500 characters | $0.012 |
| 5,000 characters | $0.02 |
Failed runs are not charged.
### Limits
- Up to 5,000 characters per request.
### Also on SandBase
Higher-quality tier: `heygen/heygen-voice`.

---
Machine-readable: [`catalog/models/heygen/heygen-voice/turbo.json`](../../../../catalog/models/heygen/heygen-voice/turbo.json) · Store page: https://www.sandbase.ai/model/heygen/heygen-voice/turbo
