# Kling V2.6 Pro Text to Video

`kwaivgi/kling-video/v2.6/pro/text-to-video` · video · KwaiVGI

Kling V2.6 Pro Text to Video by Kuaishou turns a text prompt into a 5 or 10 second 1080p video with optional native audio.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`).

| parameters | USD |
|---|---|
| duration=5, generate_audio=false | 0.35 |
| duration=5, generate_audio=true | 0.7 |
| duration=10, generate_audio=false | 0.7 |
| duration=10, generate_audio=true | 1.4 |

Formula: `(params.duration ?? 5) * ((params.generate_audio ?? true) ? 0.14 : 0.07)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v2.6/pro/text-to-video", "prompt": "Old friends reuniting at a train station after 20 years, one exclaims '\''Is that really you?!'\'' other tearfully replies '\''I promised I'\''d come back, didn'\''t I?'\'', train whistle, steam hissing, emotional orchestral swell, crowd murmur"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v2.6/pro/text-to-video', {'prompt': "Old friends reuniting at a train station after 20 years, one exclaims 'Is that really you?!' other tearfully replies 'I promised I'd come back, didn't I?', train whistle, steam hissing, emotional orchestral swell, crowd murmur"})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v2.6/pro/text-to-video", {
  "prompt": "Old friends reuniting at a train station after 20 years, one exclaims 'Is that really you?!' other tearfully replies 'I promised I'd come back, didn't I?', train whistle, steam hissing, emotional orchestral swell, crowd murmur"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v2.6/pro/text-to-video", sandbase.Params{
	"prompt": "Old friends reuniting at a train station after 20 years, one exclaims 'Is that really you?!' other tearfully replies 'I promised I'd come back, didn't I?', train whistle, steam hissing, emotional orchestral swell, crowd murmur",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Prompt  |
| `duration` | integer |  | The duration of the generated video in seconds one of: `5`, `10`; default `5` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`, `1:1`; default `"16:9"` |
| `generate_audio` | boolean |  | Whether to generate native audio for the video. Supports Chinese and English voice output. Other languages are automatically translated to English. For English speech, use lowercase letters; for acronyms or proper… default `true` |

## Details

Kling V2.6 Pro text-to-video with native audio, 5 or 10 seconds.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` | `16:9` | Output frame shape. |
| `duration` | 5 / 10 | 5 | Output length in seconds. |
| `generate_audio` | boolean | true | Native audio; on by default. |

### Billing

Per output second: $0.14 with audio, $0.07 silent.

| Output | With audio | Silent |
|---|---|---|
| 5s (default) | $0.70 | $0.35 |
| 10s | $1.40 | $0.70 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera move, and light in order.

### Limits

- Clips are 5 or 10 seconds.

### Also on SandBase

Related: `kwaivgi/kling-video/v2.6/pro/image-to-video`, `kwaivgi/kling-video/v3/pro/text-to-video` (newer).

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v2.6/pro/text-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/v2.6/pro/text-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v2.6/pro/text-to-video
