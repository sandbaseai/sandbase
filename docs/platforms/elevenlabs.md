# ElevenLabs models API: 12 endpoints with pricing and code examples

Call 12 ElevenLabs models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`elevenlabs/dubbing`](../models/elevenlabs/dubbing.md) | ElevenLabs Dubbing translates the speech in a video into another language while preserving each speaker's voice, timing, and background… | about $0.6 per call |
| [`elevenlabs/multilingual-v2`](../models/elevenlabs/multilingual-v2.md) | Eleven Multilingual v2 is ElevenLabs' stable, lifelike text-to-speech model for 29 languages. Choose a voice, set stability and speaking… | from $0.2 per run, depending on parameters |
| [`elevenlabs/music`](../models/elevenlabs/music.md) | Music is ElevenLabs's AI audio generation model. Produce high-quality music tracks, sound effects, and audio landscapes from natural… | from $0.6 to $6 per run, depending on parameters |
| [`elevenlabs/music/2`](../models/elevenlabs/music/2.md) | ElevenLabs Music v2 generates studio-quality songs and instrumentals with vocals from a text prompt, up to 10 minutes long. | from $0.75 to $7.5 per run, depending on parameters |
| [`elevenlabs/music/2.5`](../models/elevenlabs/music/2.5.md) | ElevenLabs Music v2.5 generates studio-quality songs and instrumentals with vocals from a text prompt, up to 10 minutes long. | from $0.75 to $7.5 per run, depending on parameters |
| [`elevenlabs/scribe-v2`](../models/elevenlabs/scribe-v2.md) | Scribe V2 is ElevenLabs's speech recognition model. Transcribe audio content with industry-leading accuracy across multiple languages and… | about $0.008 per call |
| [`elevenlabs/sound-effects-v2`](../models/elevenlabs/sound-effects-v2.md) | Sound Effects V2 by ElevenLabs - generate music, sound effects, and audio from text descriptions with AI. Create original compositions,… | from $0.001 to $0.044 per run, depending on parameters |
| [`elevenlabs/text-to-dialogue`](../models/elevenlabs/text-to-dialogue.md) | ElevenLabs Text to Dialogue uses Eleven v3 to turn a list of lines into a multi-speaker conversation, with a separate voice for each line… | about $0.2 per call |
| [`elevenlabs/turbo-v2.5`](../models/elevenlabs/turbo-v2.5.md) | Turbo V2.5 by ElevenLabs - convert text to natural-sounding speech with AI. Supports multiple voices, languages, emotions, and speaking… | from $0.1 per run, depending on parameters |
| [`elevenlabs/v3`](../models/elevenlabs/v3.md) | Eleven v3 is ElevenLabs' expressive multilingual text-to-speech model. It follows inline audio tags such as [whispers] or [laughs] to… | from $0.2 per run, depending on parameters |
| [`elevenlabs/v4`](../models/elevenlabs/v4.md) | Eleven v4 is ElevenLabs' most expressive text-to-speech model, with natural pacing, emotion and multilingual delivery. | from $0.08 per run, depending on parameters |
| [`elevenlabs/v4-turbo`](../models/elevenlabs/v4-turbo.md) | Eleven v4 Turbo is the low-latency tier of ElevenLabs' v4 text-to-speech generation, for real-time and high-volume narration. | from $0.04 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "elevenlabs/dubbing", "target_lang": "es", "video": "https://static.sandbase.ai/examples/8f64921f-0d6e-4239-a36a-7419390685bc/input/2515467e-312a-4f21-a8e1-763533464bb3.mp4"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
