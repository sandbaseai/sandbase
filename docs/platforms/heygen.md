# HeyGen models API: 10 endpoints with pricing and code examples

Call 10 HeyGen models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`heygen/avatar5/digital-twin`](../models/heygen/avatar5/digital-twin.md) | Avatar5 Digital Twin by HeyGen - generate cinematic videos from text descriptions with AI. Create high-quality video content with natural… | about $0.6 per call |
| [`heygen/heygen-avatar4/image-to-video`](../models/heygen/heygen-avatar4/image-to-video.md) | Heygen Avatar4 is HeyGen's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and… | about $0.5 per call |
| [`heygen/heygen-video/image-to-video`](../models/heygen/heygen-video/image-to-video.md) | HeyGen Video Image to Video animates a first-frame image into a 5-15 second video at up to 2K resolution. | from $0.1 to $1.5 per run, depending on parameters |
| [`heygen/heygen-video/reference-to-video`](../models/heygen/heygen-video/reference-to-video.md) | HeyGen Video Reference to Video generates a 5-15 second video guided by reference images, videos and audio. | from $0.35 to $2.7 per run, depending on parameters |
| [`heygen/heygen-video/text-to-video`](../models/heygen/heygen-video/text-to-video.md) | HeyGen Video Text to Video turns a text prompt into a 5-15 second video at up to 2K resolution. | from $0.1 to $0.9 per run, depending on parameters |
| [`heygen/heygen-voice`](../models/heygen/heygen-voice.md) | HeyGen Voice turns text into natural speech in 39 languages, with 24 public voices or a cloned voice from a reference recording. | from $0.03 per run, depending on parameters |
| [`heygen/heygen-voice/turbo`](../models/heygen/heygen-voice/turbo.md) | HeyGen Voice Turbo is the faster, lower-cost HeyGen text-to-speech model, with the same voices, languages and voice cloning. | from $0.004 per run, depending on parameters |
| [`heygen/lipsync/precision`](../models/heygen/lipsync/precision.md) | HeyGen v3 Lipsync (precision) replaces the speech in a video and re-syncs the speaker's lips to the new audio. | about $0.5 per call |
| [`heygen/lipsync/speed`](../models/heygen/lipsync/speed.md) | HeyGen v3 Lipsync (speed) replaces the speech in a video and re-syncs the speaker's lips to the new audio. | about $0.25 per call |
| [`heygen/video-agent/v3`](../models/heygen/video-agent/v3.md) | Heygen Video Agent V3 is HeyGen's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with… | about $1.02 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "heygen/avatar5/digital-twin", "prompt": "Hello and welcome to this demonstration of HeyGen Avatar V."}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
