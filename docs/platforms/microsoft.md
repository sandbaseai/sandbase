# Microsoft models API: 8 endpoints with pricing and code examples

Call 8 Microsoft models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`microsoft/mai-image-2.5-pro/edit`](../models/microsoft/mai-image-2.5-pro/edit.md) | Mai Image 2.5 Pro Edit by Microsoft - AI-powered image editing, style transfer, and transformation. Edit photos with natural language… | from $0.29 per run, depending on parameters |
| [`microsoft/mai-image-2.5/edit`](../models/microsoft/mai-image-2.5/edit.md) | Mai Image 2.5 Edit by Microsoft - AI-powered image editing, style transfer, and transformation. Edit photos with natural language… | $0.05 per call |
| [`microsoft/mai-image-2.7`](../models/microsoft/mai-image-2.7.md) | MAI Image 2.7 by Microsoft turns a text prompt into a high-quality image, with optional transparent background. | from $0.07 per run, depending on parameters |
| [`microsoft/mai-image-2.7-flash`](../models/microsoft/mai-image-2.7-flash.md) | MAI Image 2.7 Flash by Microsoft turns a text prompt into a high-quality image, with optional transparent background. | from $0.025 per run, depending on parameters |
| [`microsoft/mai-image-2.7-flash/edit`](../models/microsoft/mai-image-2.7-flash/edit.md) | MAI Image 2.7 Flash Edit by Microsoft edits images from a text instruction, combining up to five reference images. | from $0.025 per run, depending on parameters |
| [`microsoft/mai-image-2.7/edit`](../models/microsoft/mai-image-2.7/edit.md) | MAI Image 2.7 Edit by Microsoft edits images from a text instruction, combining up to five reference images. | from $0.07 per run, depending on parameters |
| [`microsoft/moge-2`](../models/microsoft/moge-2.md) | MoGe-2 by Microsoft estimates metric 3D geometry from a single image and returns a textured GLB mesh, a PLY point cloud, and depth, normal… | $0.05 per call |
| [`microsoft/moge-3`](../models/microsoft/moge-3.md) | MoGe-3 by Microsoft estimates metric 3D geometry from a single image, refining depth with a sparse 3D refiner, and returns a textured GLB… | $0.075 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "microsoft/mai-image-2.5-pro/edit", "prompt": "Turn this into a clean, futuristic product shot with soft studio lighting.", "image": "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input.png"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
