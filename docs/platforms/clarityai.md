# ClarityAI models API: 1 endpoints with pricing and code examples

Call 1 ClarityAI models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`clarity-ai/clarity-upscaler`](../models/clarity-ai/clarity-upscaler.md) | Clarity Upscaler by ClarityAI - AI-powered image editing, style transfer, and transformation. Edit photos with natural language… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "clarity-ai/clarity-upscaler", "prompt": "masterpiece, best quality, highres", "image": "https://static.sandbase.ai/examples/bytedance/seedvr/upscale/image/input_image_0.png"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
