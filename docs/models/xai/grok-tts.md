# xAI Text to Speech

`xai/grok-tts` · audio · xAI

Grok Tts by xAI - convert text to natural-sounding speech with AI. Supports multiple voices, languages, emotions, and speaking styles for content creation and accessibility.

## Pricing

- Depends on parameters (`params.text`).

| parameters | USD |
|---|---|
| defaults | 0.015 |

Formula: `Math.max(1.0, Math.ceil(len(params.text ?? "") / 1000.0)) * 0.015`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-tts"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-tts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-tts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-tts", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `text` | string |  | The text to convert to speech. Maximum 15,000 characters. Supports speech tags for expressive delivery: inline tags like [laugh], [pause], [sigh] and wrapping tags like <whisper>text</whisper>, <slow>text</slow>.  |
| `voice` | string |  | The voice to use for speech synthesis. one of: `eve`, `ara`, `rex`, `sal`, `leo` |

## Details

xAI text-to-speech with five voices (Eve, Ara, Rex, Sal, Leo).

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `text` | string | — | Text to speak. |
| `voice` | `eve` / `ara` / `rex` / `sal` / `leo` | — | Voice. |

### Billing

$0.015 per started 1,000 characters, with a one-unit minimum.

| Text | Price |
|---|---|
| 200 characters | $0.015 |
| 1,000 characters | $0.015 |
| 2,500 characters | $0.045 |

Failed runs are not charged.

---
Machine-readable: [`catalog/models/xai/grok-tts.json`](../../../catalog/models/xai/grok-tts.json) · Store page: https://www.sandbase.ai/model/xai/grok-tts
