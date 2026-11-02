# Lyria 3.5 API: pricing, parameters and code examples

`google/lyria-3.5` · audio model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0 input / $0 output per 1M tokens · **Modes:** async

Lyria 3.5 is Google's flagship music generation model for full-length songs up to a few minutes, with verses, choruses, bridges, expressive vocals, timed lyrics, and rich instrumental arrangements. It generates high-quality 44.1kHz stereo audio from a text prompt, optionally guided by an image.

## Pricing

- Input **$0** / output **$0** per 1M tokens (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/lyria-3.5", "prompt": "A 30-second upbeat synthwave instrumental with punchy drums and a soaring lead synth."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/lyria-3.5', {'prompt': 'A 30-second upbeat synthwave instrumental with punchy drums and a soaring lead synth.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/lyria-3.5", {
  "prompt": "A 30-second upbeat synthwave instrumental with punchy drums and a soaring lead synth."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/lyria-3.5", sandbase.Params{
	"prompt": "A 30-second upbeat synthwave instrumental with punchy drums and a soaring lead synth.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string |  | Optional image used as inspiration; the music will match the mood and theme of the image.  |
| `prompt` | string | yes | The text prompt describing the music you want to generate. Include genre, mood, instrumentation, tempo, vocals, and structure. Use duration hints (e.g. 'a 2-minute track') or section markers like '[0:00-0:30] Intro:…  |

## Details

Lyria 3.5 is Google's music model for full songs: verses, choruses, and bridges with expressive vocals, timed lyrics, and full arrangements. An optional image sets the mood.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Genre, mood, instruments, tempo, vocal style, and lyrics. Up to 5,000 characters. |
| `image` | image URL | — | Optional image whose mood the music should match. |

### Billing

$0.10 per song.

| Request | Price |
|---|---|
| One song | $0.10 |

Failed runs are not charged.

### Prompting

- Name the genre, tempo, and instrumentation first, then the vocal style.
- Mark lyric sections, e.g. `[Verse]`, `[Chorus]`.

### Limits

- One song per request.

---
Machine-readable: [`catalog/models/google/lyria-3.5.json`](../../../catalog/models/google/lyria-3.5.json) · Store page: https://www.sandbase.ai/model/google/lyria-3.5
