# Kling V2.6 Pro Image to Video

`kwaivgi/kling-video/v2.6/pro/image-to-video` · video · KwaiVGI

Kling V2.6 Pro Image to Video by Kuaishou animates a start image, optionally toward an end image, into a 5 or 10 second 1080p video with optional native audio and voice control.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`, `params.voice_ids`).

| parameters | USD |
|---|---|
| duration=5, generate_audio=false | 0.35 |
| duration=5, generate_audio=true | 0.7 |
| duration=10, generate_audio=false | 0.7 |
| duration=10, generate_audio=true | 1.4 |

Formula: `(params.duration ?? 5) * ((params.generate_audio ?? true) ? (len(params.voice_ids ?? []) > 0 ? 0.168 : 0.14) : 0.07)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v2.6/pro/image-to-video", "image": "https://static.sandbase.ai/examples/232fd0ea-384f-46ba-8343-39f1dac143b3/input/edc1c83b-9ec7-4f43-aa2b-43c8af7fd6d2.png", "prompt": "A king walks slowly and says \"My people, here I am! I am here to save you all\""}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v2.6/pro/image-to-video', {'image': 'https://static.sandbase.ai/examples/232fd0ea-384f-46ba-8343-39f1dac143b3/input/edc1c83b-9ec7-4f43-aa2b-43c8af7fd6d2.png', 'prompt': 'A king walks slowly and says "My people, here I am! I am here to save you all"'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v2.6/pro/image-to-video", {
  "image": "https://static.sandbase.ai/examples/232fd0ea-384f-46ba-8343-39f1dac143b3/input/edc1c83b-9ec7-4f43-aa2b-43c8af7fd6d2.png",
  "prompt": "A king walks slowly and says \"My people, here I am! I am here to save you all\""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v2.6/pro/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/232fd0ea-384f-46ba-8343-39f1dac143b3/input/edc1c83b-9ec7-4f43-aa2b-43c8af7fd6d2.png",
	"prompt": "A king walks slowly and says \"My people, here I am! I am here to save you all\"",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | URL of the image to be used for the video  |
| `prompt` | string | yes | Prompt  |
| `duration` | integer |  | The duration of the generated video in seconds one of: `5`, `10`; default `5` |
| `end_image` | string |  | URL of the image to be used for the end of the video  |
| `voice_ids` | array |  | Optional Voice IDs for video generation. Reference voices in your prompt with <<<voice_1>>> and <<<voice_2>>> (maximum 2 voices per task). Get voice IDs from the `kwaivgi/kling-video/create-voice` model.  |
| `generate_audio` | boolean |  | Whether to generate native audio for the video. Supports Chinese and English voice output. Other languages are automatically translated to English. For English speech, use lowercase letters; for acronyms or proper… default `true` |

## Details

Kling V2.6 Pro image-to-video with native audio. Add `voice_ids` to have characters speak in a chosen voice.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `duration` | 5 / 10 | 5 | Output length in seconds. |
| `generate_audio` | boolean | true | Native audio; on by default. |
| `voice_ids` | string[] | — | Optional Kling voice IDs for spoken lines. |

### Billing

Per output second: $0.07 silent, $0.14 with audio, $0.168 with audio and custom voices.

| Output | Silent | With audio | With voices |
|---|---|---|---|
| 5s (default) | $0.35 | $0.70 | $0.84 |
| 10s | $0.70 | $1.40 | $1.68 |

Failed runs are not charged.

### Prompting

- Quote dialogue and name the speaker.

### Limits

- Clips are 5 or 10 seconds.

### Also on SandBase

Related: `kwaivgi/kling-video/v2.6/pro/text-to-video`, `kwaivgi/kling-video/v3/pro/image-to-video` (newer).

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v2.6/pro/image-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/v2.6/pro/image-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v2.6/pro/image-to-video
