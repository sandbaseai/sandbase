# Luma models API: 2 endpoints with pricing and code examples

Call 2 Luma models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`luma/ray/3.2/image-to-video`](../models/luma/ray/3.2/image-to-video.md) | Agent Ray 3.2 by Luma - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion,… | from $0.5 to $12 per run, depending on parameters |
| [`luma/ray/3.2/text-to-video`](../models/luma/ray/3.2/text-to-video.md) | Agent Ray 3.2 is Luma's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic… | from $0.5 to $4 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "luma/ray/3.2/image-to-video", "prompt": "<prompt>", "image": "<image>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
