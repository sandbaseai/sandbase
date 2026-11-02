# PixVerse models API: 2 endpoints with pricing and code examples

Call 2 PixVerse models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`pixverse/c1/image-to-video`](../models/pixverse/c1/image-to-video.md) | C1 is PixVerse's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and… | from $0.03 to $1.8 per run, depending on parameters |
| [`pixverse/v6/image-to-video`](../models/pixverse/v6/image-to-video.md) | V6 is PixVerse's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and… | from $0.025 to $1.725 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pixverse/c1/image-to-video", "prompt": "<prompt>", "image": "<image>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
