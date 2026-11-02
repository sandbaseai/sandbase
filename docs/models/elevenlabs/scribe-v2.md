# Scribe V2 API: pricing, parameters and code examples

`elevenlabs/scribe-v2` · audio model · ElevenLabs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.008 per call · **Modes:** async

Scribe V2 is ElevenLabs's speech recognition model. Transcribe audio content with industry-leading accuracy across multiple languages and accents.

## Pricing

- Depends on parameters (`params.audio`).

Formula: `Math.max(1.0, Math.ceil((media_duration(params.audio) ?? 60.0) / 60.0)) * 0.008`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "elevenlabs/scribe-v2"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('elevenlabs/scribe-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("elevenlabs/scribe-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "elevenlabs/scribe-v2", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `audio` | string |  | URL of the audio file to transcribe  |
| `diarize` | boolean |  | Whether to annotate who is speaking default `true` |
| `language_code` | string |  | Language code of the audio  |
| `tag_audio_events` | boolean |  | Tag audio events like laughter, applause, etc. default `true` |

## Details

ElevenLabs Scribe v2 transcribes speech in 90+ languages with speaker diarization and tags for non-speech audio events.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `audio` | audio URL | — | Audio or video URL. |
| `tag_audio_events` | boolean | true | Mark laughter, music, and other events. |
| `diarize` | boolean | true | Label who is speaking. |
| `language_code` | string | — | Force a language; omit to detect. |

### Billing

$0.008 per started minute of audio. The quote before submission assumes 1 minute; the final charge uses the measured length.

| Audio | Price |
|---|---|
| 1 min | $0.008 |
| 10 min | $0.08 |
| 60 min | $0.48 |

Failed runs are not charged.

---
Machine-readable: [`catalog/models/elevenlabs/scribe-v2.json`](../../../catalog/models/elevenlabs/scribe-v2.json) · Store page: https://www.sandbase.ai/model/elevenlabs/scribe-v2
