# MiniMax Voice Clone API: pricing, parameters and code examples

`minimax/voice-clone` · audio model · MiniMax · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $1.8 per run, depending on parameters · **Modes:** async

MiniMax Voice Clone by MiniMax creates a reusable custom voice from a reference recording of at least 10 seconds and returns a short preview spoken in that voice.

## Pricing

- Depends on parameters (`params.text`).

| parameters | USD |
|---|---|
| defaults | 1.8 |

Formula: `1.5 + Math.ceil(len(params.text ?? "Hello, this is a preview of your cloned voice! I hope you like it!") / 1000) * 0.3`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/voice-clone", "audio": "https://static.sandbase.ai/examples/b8385a7a-19fa-40da-94b1-92e4cb727d8b/input/6a966bba-4ecf-4735-ac78-1429b82245cf.wav"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/voice-clone', {'audio': 'https://static.sandbase.ai/examples/b8385a7a-19fa-40da-94b1-92e4cb727d8b/input/6a966bba-4ecf-4735-ac78-1429b82245cf.wav'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/voice-clone", {
  "audio": "https://static.sandbase.ai/examples/b8385a7a-19fa-40da-94b1-92e4cb727d8b/input/6a966bba-4ecf-4735-ac78-1429b82245cf.wav"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/voice-clone", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/b8385a7a-19fa-40da-94b1-92e4cb727d8b/input/6a966bba-4ecf-4735-ac78-1429b82245cf.wav",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `text` | string |  | Text to generate a TTS preview with the cloned voice (optional) default `"Hello, this is a preview of your cloned voice! I hope you like it!"` |
| `audio` | string | yes | URL of the input audio file for voice cloning. Should be at least 10 seconds long. To retain the voice permanently, use it with a TTS (text-to-speech) endpoint at least once within 7 days. Otherwise, it will be…  |
| `accuracy` | number |  | Text validation accuracy threshold (0-1) range 0–1 |
| `noise_reduction` | boolean |  | Enable noise reduction for the cloned voice default `false` |
| `need_volume_normalization` | boolean |  | Enable volume normalization for the cloned voice default `false` |

## Details

Create a reusable custom voice from a reference recording of at least 10 seconds. The response includes the voice ID and a short spoken preview.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `audio` | audio URL, required | — | Reference recording, 10 seconds or longer. |
| `text` | string | `Hello, this is a preview of your cloned voice! I hope you like it!` | Preview sentence spoken in the new voice. |
| `need_volume_normalization` | boolean | false | Normalize the recording level. |
| `noise_reduction` | boolean | false | Clean background noise first. |
| `accuracy` | number 0–1 | — | Text-validation threshold for the recording. |

### Billing

$1.50 per cloned voice plus $0.30 per started 1,000 preview characters.

| Request | Price |
|---|---|
| One voice | $1.80 |

Failed runs are not charged.

### Prompting

- Record in a quiet room with one speaker.

### Limits

- Use the returned voice ID as `voice_id` in MiniMax Speech.

### Also on SandBase

Related: `minimax/speech/2.8/hd`, `minimax/speech/2.8/turbo`, `minimax/voice-design`.

---
Machine-readable: [`catalog/models/minimax/voice-clone.json`](../../../catalog/models/minimax/voice-clone.json) · Store page: https://www.sandbase.ai/model/minimax/voice-clone
