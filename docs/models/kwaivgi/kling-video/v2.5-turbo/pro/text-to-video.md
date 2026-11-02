# Kling V2.5 Turbo Pro Text to Video API: pricing, parameters and code examples

`kwaivgi/kling-video/v2.5-turbo/pro/text-to-video` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.35 to $0.7 per run, depending on parameters · **Modes:** async

Kling V2.5 Turbo Pro Text to Video by Kuaishou turns a text prompt into a 5 or 10 second 1080p video.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=5 | 0.35 |
| duration=10 | 0.7 |

Formula: `(params.duration ?? 5) * 0.07`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v2.5-turbo/pro/text-to-video", "prompt": "A noble lord walks among his people, his presence a comforting reassurance. He greets them with a gentle smile, embodying their hopes and earning their respect through simple interactions. The atmosphere is intimate and sincere, highlighting the bond between the leader and community."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v2.5-turbo/pro/text-to-video', {'prompt': 'A noble lord walks among his people, his presence a comforting reassurance. He greets them with a gentle smile, embodying their hopes and earning their respect through simple interactions. The atmosphere is intimate and sincere, highlighting the bond between the leader and community.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v2.5-turbo/pro/text-to-video", {
  "prompt": "A noble lord walks among his people, his presence a comforting reassurance. He greets them with a gentle smile, embodying their hopes and earning their respect through simple interactions. The atmosphere is intimate and sincere, highlighting the bond between the leader and community."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v2.5-turbo/pro/text-to-video", sandbase.Params{
	"prompt": "A noble lord walks among his people, his presence a comforting reassurance. He greets them with a gentle smile, embodying their hopes and earning their respect through simple interactions. The atmosphere is intimate and sincere, highlighting the bond between the leader and community.",
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

## Details

Kling V2.5 Turbo Pro text-to-video: fast, low-cost 5 or 10 second clips without audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` | `16:9` | Output frame shape. |
| `duration` | 5 / 10 | 5 | Output length in seconds. |

### Billing

$0.07 per output second.

| Output | Price |
|---|---|
| 5s (default) | $0.35 |
| 10s | $0.70 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera move, and light in order.

### Limits

- Clips are 5 or 10 seconds; no audio.

### Also on SandBase

Other V2.5 Turbo endpoints: `kwaivgi/kling-video/v2.5-turbo/pro/image-to-video`, `kwaivgi/kling-video/v2.5-turbo/standard/image-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v2.5-turbo/pro/text-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/v2.5-turbo/pro/text-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v2.5-turbo/pro/text-to-video
