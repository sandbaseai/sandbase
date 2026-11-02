# Meta models API: 3 endpoints with pricing and code examples

Call 3 Meta models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`meta/llama-3.3-70b-instruct`](../models/meta/llama-3.3-70b-instruct.md) | Llama 3.3 70B Instruct is Meta's instruction-tuned, text-only multilingual model released on December 6, 2024, built on an optimized… | $0.1 input / $0.32 output per 1M tokens |
| [`meta/sam-3/3d-objects`](../models/meta/sam-3/3d-objects.md) | Sam 3 3d Objects by Meta - convert 2D images into 3D models with AI. Generate textured 3D assets from single photos for games, AR/VR,… | from $0.024 per run, depending on parameters |
| [`meta/sam-3/image`](../models/meta/sam-3/image.md) | SAM 3 Image is Meta's segmentation model. It finds objects in an image from a text, point, or box prompt and returns masks and the masked… | $0.005 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meta/llama-3.3-70b-instruct"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
