# Z-Image models API: 1 endpoints with pricing and code examples

Call 1 Z-Image models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`z-image/turbo`](../models/z-image/turbo.md) | Turbo is Z-Image's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural language… | $0.015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "z-image/turbo", "aspect_ratio": "9:16", "prompt": "A red paper lantern in a quiet bamboo forest at dusk"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
