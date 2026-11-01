# ElevenLabs Music

`elevenlabs/music` · audio · ElevenLabs

Music is ElevenLabs's AI audio generation model. Produce high-quality music tracks, sound effects, and audio landscapes from natural language prompts.

## Pricing

- Depends on parameters (`params.music_length_ms`).

| parameters | USD |
|---|---|
| music_length_ms=3000 | 0.6 |
| music_length_ms=600000 | 6 |

Formula: `Math.max(1.0, Math.ceil((params.music_length_ms ?? 60000) / 60000.0)) * 0.6`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "elevenlabs/music", "prompt": "Mysterious original soundtrack, themes of jungle, rainforest, nature, woodwinds, busy rhythmic tribal percussion."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('elevenlabs/music', {'prompt': 'Mysterious original soundtrack, themes of jungle, rainforest, nature, woodwinds, busy rhythmic tribal percussion.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("elevenlabs/music", {
  "prompt": "Mysterious original soundtrack, themes of jungle, rainforest, nature, woodwinds, busy rhythmic tribal percussion."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "elevenlabs/music", sandbase.Params{
	"prompt": "Mysterious original soundtrack, themes of jungle, rainforest, nature, woodwinds, busy rhythmic tribal percussion.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The text prompt describing the music to generate  |
| `music_length_ms` | integer |  | The length of the song to generate in milliseconds (3000-600000). If not provided, the model will choose a length based on the prompt. range 3000–600000 |
| `force_instrumental` | boolean |  | If true, guarantees that the generated song will be instrumental. default `false` |

## Details

ElevenLabs Music generates songs or instrumentals from a prompt, 3 seconds to 10 minutes long.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Genre, mood, instruments, vocals, and lyrics. |
| `force_instrumental` | boolean | false | Generate without vocals. |
| `music_length_ms` | integer 3000–600000 | — | Length in milliseconds (3,000–600,000). |

### Billing

$0.60 per started minute, with a one-minute minimum. Without `music_length_ms` the quote assumes 1 minute.

| Length | Price |
|---|---|
| 30s | $0.60 |
| 60s | $0.60 |
| 150s | $1.80 |
| 600s | $6.00 |

Failed runs are not charged.

### Prompting

- Describe structure and vocals; put lyrics in the prompt if you need exact words.

### Limits

- Up to 10 minutes.

### Also on SandBase

Other ElevenLabs Music versions: `elevenlabs/music/2`, `elevenlabs/music/2.5`.

---
Machine-readable: [`catalog/models/elevenlabs/music.json`](../../../catalog/models/elevenlabs/music.json) · Store page: https://www.sandbase.ai/model/elevenlabs/music
