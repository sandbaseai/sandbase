# MiniMax Voice Design API: pricing, parameters and code examples

`minimax/voice-design` · audio model · MiniMax · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $3.03 per run, depending on parameters · **Modes:** async

MiniMax Voice Design by MiniMax creates a new reusable voice from a text description of its timbre, age, and style, and returns a spoken preview.

## Pricing

- Depends on parameters (`params.prompt`).

| parameters | USD |
|---|---|
| defaults | 3.03 |

Formula: `3.00 + Math.ceil(len(params.prompt ?? "") / 1000) * 0.03`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/voice-design", "prompt": "Bubbly and excitable female pop star interviewee, youthful, slightly breathless, and very enthusiastic"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/voice-design', {'prompt': 'Bubbly and excitable female pop star interviewee, youthful, slightly breathless, and very enthusiastic'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/voice-design", {
  "prompt": "Bubbly and excitable female pop star interviewee, youthful, slightly breathless, and very enthusiastic"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/voice-design", sandbase.Params{
	"prompt": "Bubbly and excitable female pop star interviewee, youthful, slightly breathless, and very enthusiastic",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Voice description prompt for generating a personalized voice  |
| `preview_text` | string |  | Text for audio preview. Limited to 500 characters. A fee of $30 per 1M characters will be charged for the generation of the preview audio.  |

## Details

Design a new reusable voice from a text description of its timbre, age, and style. The response includes the voice ID and a spoken preview.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Describe the voice: gender, age, timbre, accent, and mood. |
| `preview_text` | string | — | Sentence spoken in the new voice. |

### Billing

$3.00 per designed voice plus $0.03 per started 1,000 description characters.

| Request | Price |
|---|---|
| One voice | $3.00 |

Failed runs are not charged.

### Prompting

- Be concrete: “warm, low female voice in her 40s, slight British accent, calm”.

### Limits

- Use the returned voice ID as `voice_id` in MiniMax Speech.

### Also on SandBase

Related: `minimax/speech/2.8/hd`, `minimax/speech/2.8/turbo`, `minimax/voice-clone`.

---
Machine-readable: [`catalog/models/minimax/voice-design.json`](../../../catalog/models/minimax/voice-design.json) · Store page: https://www.sandbase.ai/model/minimax/voice-design
