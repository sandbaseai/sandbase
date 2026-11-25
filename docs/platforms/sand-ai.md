# Sand AI models API: 3 endpoints with pricing and code examples

Call 3 Sand AI models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`sandai/magi-2/image-to-video`](../models/sandai/magi-2/image-to-video.md) | MAGI-2 by Sand AI animates a first frame, or a first and last frame, into a 1080p video of 4 to 30 seconds with native audio. | from $0.32 to $2.4 per run, depending on parameters |
| [`sandai/magi-2/reference-to-video`](../models/sandai/magi-2/reference-to-video.md) | MAGI-2 by Sand AI creates a 1080p video of 4 to 30 seconds with native audio, guided by up to 10 reference images, 5 video clips and 5… | from $0.32 to $2.4 per run, depending on parameters |
| [`sandai/magi-2/text-to-video`](../models/sandai/magi-2/text-to-video.md) | MAGI-2 by Sand AI turns a text prompt into a 1080p video of 4 to 30 seconds with native audio, with strong instruction following, complex… | from $0.32 to $2.4 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sandai/magi-2/image-to-video", "aspect_ratio": "16:9", "duration": 5, "image": "https://static.sandbase.ai/examples/cf7d3354-3c3c-475c-93c0-74f31c6b084a/input/241be84a-97d7-4d77-9ca9-7fdb51507601.webp", "prompt": "The player jumps and shoots; the ball drops through the hoop and the friends on the court cheer. Handheld camera follows the shot."}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
