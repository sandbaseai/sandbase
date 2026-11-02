# Topaz Labs models API: 2 endpoints with pricing and code examples

Call 2 Topaz Labs models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`topaz/upscale/image`](../models/topaz/upscale/image.md) | Upscale Image is Topaz Labs's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from… | about $0.08 per call |
| [`topaz/upscale/video`](../models/topaz/upscale/video.md) | Upscale Video is Topaz Labs's video-to-video AI model. Transform, enhance, and edit video content using text prompts - from style changes… | about $0.1 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "topaz/upscale/image", "crop_to_fill": false, "enhancement_model": "High Fidelity V2", "face_enhancement": false, "image": "https://static.sandbase.ai/examples/5f434c76-3c13-4430-ac6e-a044487d42b4/input/235e21e0-6bcc-4297-853b-0d3db8894545.png", "output_format": "png", "prompt": "Preserve the original panoramic composition, geometry, colors, and details while increasing resolution. Do not crop, reframe, or add new objects.", "upscale_factor": 2.844444444444445}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
