# Kling Create Voice API: pricing, parameters and code examples

`kwaivgi/kling-video/create-voice` · audio model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.035 per call · **Modes:** async

Kling Create Voice clones a reusable custom voice from a 5-30 second recording of a single speaker and returns a voice ID for Kling V4 reference-to-video, plus a short preview clip.

## Pricing

- **$0.035 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/create-voice", "voice_url": "https://static.sandbase.ai/examples/kwaivgi/kling-video/create-voice/input_voice_url_0.wav"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/create-voice', {'voice_url': 'https://static.sandbase.ai/examples/kwaivgi/kling-video/create-voice/input_voice_url_0.wav'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/create-voice", {
  "voice_url": "https://static.sandbase.ai/examples/kwaivgi/kling-video/create-voice/input_voice_url_0.wav"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/create-voice", sandbase.Params{
	"voice_url": "https://static.sandbase.ai/examples/kwaivgi/kling-video/create-voice/input_voice_url_0.wav",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `voice_url` | string | yes | Recording of the voice to clone: .mp3/.wav audio or .mp4/.mov video, 5-30 seconds, one clean speaker without background music or noise.  |
| `voice_name` | string |  | Display name for the voice (up to 20 characters). default `"sandbase-voice"` |

## Details

Kling Create Voice turns a short recording of one speaker into a reusable custom voice. The result is a `voice_id` you pass to Kling V4 reference-to-video so a character speaks in that voice, plus a short preview clip.

### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `voice_url` | audio/video URL, required | — | .mp3 / .wav / .mp4 / .mov, 5–30 seconds, one clean voice, no background music or noise. |
| `voice_name` | string | `sandbase-voice` | Display name, up to 20 characters. |

### Output
| Field | Notes |
|---|---|
| `voice_id` | Custom voice ID. |
| `url` | Preview clip spoken in the cloned voice. |

### Use the voice in a video
Pass the ID to [Kling V4 Reference to Video](https://www.sandbase.ai/model/kwaivgi/kling-video/v4/reference-to-video) in `voice_ids` (up to 2) and describe who speaks in the prompt, e.g. "The man from @Image1 says: \"Welcome back.\"". Voices cannot be combined with reference videos in the same request.

### Billing
$0.035 per created voice. Failed runs are not charged.

### Limits
- One speaker per recording; noisy or multi-speaker audio is rejected.
- Voice IDs work only with Kling models served through SandBase's Kling channel.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/create-voice.json`](../../../../catalog/models/kwaivgi/kling-video/create-voice.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/create-voice
