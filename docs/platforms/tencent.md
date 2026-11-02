# Tencent models API: 8 endpoints with pricing and code examples

Call 8 Tencent models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`tencent/hunyuan-3d/3.0/image-to-3d`](../models/tencent/hunyuan-3d/3.0/image-to-3d.md) | Hunyuan 3d V3 is Tencent's image-to-3D AI model. Transform photographs into production-ready 3D meshes with accurate geometry and texture… | from $0.45 to $0.9 per run, depending on parameters |
| [`tencent/hunyuan-3d/3.1/pro/image-to-3d`](../models/tencent/hunyuan-3d/3.1/pro/image-to-3d.md) | Hunyuan 3d 3.1 Pro by Tencent - convert 2D images into 3D models with AI. Generate textured 3D assets from single photos for games, AR/VR,… | from $0.525 to $0.675 per run, depending on parameters |
| [`tencent/hunyuan-3d/3.1/pro/text-to-3d`](../models/tencent/hunyuan-3d/3.1/pro/text-to-3d.md) | Hunyuan 3d 3.1 Pro is Tencent's text-to-3D AI model. Turn written descriptions into textured 3D objects with realistic geometry and… | from $0.525 to $0.675 per run, depending on parameters |
| [`tencent/hunyuan-image/3.0`](../models/tencent/hunyuan-image/3.0.md) | Hunyuan Image 3.0 is Tencent's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural… | $0.1 per call |
| [`tencent/hunyuan-image/3.0/edit`](../models/tencent/hunyuan-image/3.0/edit.md) | Hunyuan Image 3.0 Edit by Tencent - AI-powered image editing, style transfer, and transformation. Edit photos with natural language… | $0.45 per call |
| [`tencent/hunyuan-video/1.5/text-to-video`](../models/tencent/hunyuan-video/1.5/text-to-video.md) | Hunyuan Video 1.5 is Tencent's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with… | about $0.375 per call |
| [`tencent/hy3`](../models/tencent/hy3.md) | Hy3 is a 295B-parameter Mixture-of-Experts model from Tencent (21B active, 192 experts with top-8 routing) built for reasoning, agentic… | $0.132 input / $0.528 output per 1M tokens |
| [`tencent/hy4-preview`](../models/tencent/hy4-preview.md) | Hy4 preview is Tencent Hunyuan's open-source preview of its Hy4 generation, a mixture-of-experts language model with 770B total and 49B… | $0.834 input / $2.501 output per 1M tokens |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-3d/3.0/image-to-3d", "image": "<image>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
