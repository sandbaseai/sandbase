# Stable Audio 3 Small Music API: pricing, parameters and code examples

`stability-ai/stable-audio/3/small/music/text-to-audio` · audio model · stability-ai · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0217 per call · **Modes:** async

Stable Audio 3 Small Music by Stability AI is a fast, low-cost music generator producing tracks up to 2 minutes from a text prompt.

## Pricing

- **$0.0217 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "stability-ai/stable-audio/3/small/music/text-to-audio", "duration": 10, "prompt": "calm lo-fi piano loop"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('stability-ai/stable-audio/3/small/music/text-to-audio', {'duration': 10, 'prompt': 'calm lo-fi piano loop'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("stability-ai/stable-audio/3/small/music/text-to-audio", {
  "duration": 10,
  "prompt": "calm lo-fi piano loop"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "stability-ai/stable-audio/3/small/music/text-to-audio", sandbase.Params{
	"duration": 10,
	"prompt": "calm lo-fi piano loop",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducible outputs.  |
| `prompt` | string | yes | Text description of the audio to generate.  |
| `duration` | integer |  | Duration in seconds (1–120). default `30`; range 1–120 |
| `output_format` | string |  | Audio container format. one of: `mp3`, `wav`, `flac`, `ogg`, `opus`, `m4a`, `aac`; default `"mp3"` |
| `negative_prompt` | string |  | Qualities to avoid in the output. default `""` |

## Details

Stable Audio 3 Small Music: fast, low-cost music tracks up to 2 minutes.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `duration` | integer 1–120 | 30 | Length in seconds (1–120). |
| `output_format` | `mp3` / `wav` / `flac` / `ogg` / `opus` / `m4a` / `aac` | `mp3` | Output file format. |
| `negative_prompt` | string | — | What to avoid. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.0217 per generation.

| Request | Price |
|---|---|
| One track | $0.0217 |

Failed runs are not charged.

### Prompting

- Name genre, instruments, tempo, and mood.

### Also on SandBase

Related: `stability-ai/stable-audio/3/medium/text-to-audio`.

---
Machine-readable: [`catalog/models/stability-ai/stable-audio/3/small/music/text-to-audio.json`](../../../../../../../catalog/models/stability-ai/stable-audio/3/small/music/text-to-audio.json) · Store page: https://www.sandbase.ai/model/stability-ai/stable-audio/3/small/music/text-to-audio
