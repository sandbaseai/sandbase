# Sound Effects V2

`elevenlabs/sound-effects-v2` · audio · ElevenLabs

Sound Effects V2 by ElevenLabs - generate music, sound effects, and audio from text descriptions with AI. Create original compositions, ambient sounds, and audio content for any creative project.

## Pricing

- Depends on parameters (`params.duration_seconds`).

| parameters | USD |
|---|---|
| duration_seconds=0.5 | 0.001 |
| duration_seconds=5 | 0.01 |
| duration_seconds=22 | 0.044 |

Formula: `(params.duration_seconds ?? 5) * 0.002`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "elevenlabs/sound-effects-v2"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('elevenlabs/sound-effects-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("elevenlabs/sound-effects-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "elevenlabs/sound-effects-v2", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `loop` | boolean |  | Whether to create a sound effect that loops smoothly. default `false` |
| `text` | string |  | The text describing the sound effect to generate  |
| `duration_seconds` | number |  | Duration in seconds (0.5-22). If not set, optimal duration will be determined from prompt. default `5`; range 0.5–22 |
| `prompt_influence` | number |  | How closely to follow the prompt (0-1). Higher values mean less variation. default `0.3`; range 0–1 |

## Details

ElevenLabs Sound Effects v2 creates sound effects and ambiences from a description, 0.5–22 seconds long, optionally loopable.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `text` | string | — | Describe the sound. |
| `prompt_influence` | number 0–1 | 0.3 | How strictly to follow the description. |
| `duration_seconds` | number 0.5–22 | 5 | Length in seconds (0.5–22). |
| `loop` | boolean | false | Make the clip loop seamlessly. |

### Billing

$0.002 per second of audio.

| Length | Price |
|---|---|
| 2s | $0.004 |
| 5s | $0.01 |
| 22s | $0.044 |

Failed runs are not charged.

### Prompting

- Be specific about source, space, and texture: “heavy wooden door creaks open in a stone hall”.

### Limits

- Up to 22 seconds.

---
Machine-readable: [`catalog/models/elevenlabs/sound-effects-v2.json`](../../../catalog/models/elevenlabs/sound-effects-v2.json) · Store page: https://www.sandbase.ai/model/elevenlabs/sound-effects-v2
