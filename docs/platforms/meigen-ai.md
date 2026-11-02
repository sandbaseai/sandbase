# MeiGen-AI models API: 3 endpoints with pricing and code examples

Call 3 MeiGen-AI models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`meigen/infinitetalk/image-to-video`](../models/meigen/infinitetalk/image-to-video.md) | InfiniteTalk turns a portrait image and speech audio into a long-form talking video with natural lip sync, head and body motion. | about $2.32 per call |
| [`meigen/infinitetalk/text-to-video`](../models/meigen/infinitetalk/text-to-video.md) | InfiniteTalk speaks the given text with a chosen voice and animates the portrait into a talking video. | about $2.32 per call |
| [`meigen/infinitetalk/video-to-video`](../models/meigen/infinitetalk/video-to-video.md) | InfiniteTalk dubs an existing video: it re-animates lips, face and body to match new speech audio. | about $3.48 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meigen/infinitetalk/image-to-video", "audio": "https://static.sandbase.ai/examples/d33fa92a-e37d-4e1b-ae63-7dc37efcf42f/input/eb358b1f-cd6a-45d4-b926-27a4bdc68388.mp3", "image": "https://static.sandbase.ai/examples/d33fa92a-e37d-4e1b-ae63-7dc37efcf42f/input/cd175c0b-f141-4ec1-8f8b-9fcf5c063865.png", "num_frames": 41, "prompt": "A woman with colorful hair talking on a podcast.", "resolution": "480p"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
