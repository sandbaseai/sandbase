# BFL models API: 22 endpoints with pricing and code examples

Call 22 BFL models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`bfl/flux-1/schnell`](../models/bfl/flux-1/schnell.md) | Flux 1 Schnell by BFL - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and… | $0.003 per call |
| [`bfl/flux-2/dev`](../models/bfl/flux-2/dev.md) | Flux 2 Dev by BFL - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and… | $0.012 per call |
| [`bfl/flux-2/dev/edit`](../models/bfl/flux-2/dev/edit.md) | Flux 2 Dev Edit is BFL's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from… | $0.024 per call |
| [`bfl/flux-2/flash`](../models/bfl/flux-2/flash.md) | Flux 2 Flash by BFL - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and… | from $0.025 per run, depending on parameters |
| [`bfl/flux-2/flash/edit`](../models/bfl/flux-2/flash/edit.md) | Flux 2 Flash Edit is BFL's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from… | from $0.03 per run, depending on parameters |
| [`bfl/flux-2/flex`](../models/bfl/flux-2/flex.md) | Flux 2 Flex is BFL's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural language… | from $0.06 per run, depending on parameters |
| [`bfl/flux-2/flex/edit`](../models/bfl/flux-2/flex/edit.md) | Flux 2 Flex Edit by BFL - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions,… | $0.12 per call |
| [`bfl/flux-2/klein/4b`](../models/bfl/flux-2/klein/4b.md) | Flux 2 Klein 4b is BFL's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural… | $0.008 per call |
| [`bfl/flux-2/klein/4b/edit`](../models/bfl/flux-2/klein/4b/edit.md) | Flux 2 Klein 4b by BFL - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions,… | $0.02 per call |
| [`bfl/flux-2/klein/9b`](../models/bfl/flux-2/klein/9b.md) | Flux 2 Klein 9b is BFL's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural… | $0.01 per call |
| [`bfl/flux-2/klein/9b/edit`](../models/bfl/flux-2/klein/9b/edit.md) | Flux 2 Klein 9b by BFL - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions,… | $0.022 per call |
| [`bfl/flux-2/kontext/dev`](../models/bfl/flux-2/kontext/dev.md) | Flux 2 Kontext Dev by BFL - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions,… | $0.025 per call |
| [`bfl/flux-2/max`](../models/bfl/flux-2/max.md) | Flux 2 Max by BFL - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and… | $0.07 per call |
| [`bfl/flux-2/max/edit`](../models/bfl/flux-2/max/edit.md) | Flux 2 Max Edit is BFL's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from… | $0.1 per call |
| [`bfl/flux-2/pro`](../models/bfl/flux-2/pro.md) | Flux 2 Pro by BFL - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and… | $0.03 per call |
| [`bfl/flux-2/pro/edit`](../models/bfl/flux-2/pro/edit.md) | Flux 2 Pro Edit is BFL's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from… | $0.06 per call |
| [`bfl/flux-2/turbo`](../models/bfl/flux-2/turbo.md) | Flux 2 Turbo by BFL - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and… | $0.04 per call |
| [`bfl/flux-2/turbo/edit`](../models/bfl/flux-2/turbo/edit.md) | Flux 2 Turbo Edit is BFL's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from… | from $0.048 per run, depending on parameters |
| [`bfl/flux-3/edit`](../models/bfl/flux-3/edit.md) | FLUX 3 by Black Forest Labs edits up to 10 reference images from a text instruction, with strong prompt adherence and typography at 512px… | from $0.041 to $0.607 per run, depending on parameters |
| [`bfl/flux-3/image-to-video`](../models/bfl/flux-3/image-to-video.md) | Flux 3 is BFL's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and… | from $0.85 to $2.9 per run, depending on parameters |
| [`bfl/flux-3/text-to-image`](../models/bfl/flux-3/text-to-image.md) | FLUX 3 by Black Forest Labs generates images from a text prompt, with strong prompt adherence and typography at 512px to 4K resolution… | from $0.041 to $0.607 per run, depending on parameters |
| [`bfl/flux-3/text-to-video`](../models/bfl/flux-3/text-to-video.md) | Flux 3 by BFL - generate cinematic videos from text descriptions with AI. Create high-quality video content with natural motion, camera… | from $0.85 to $2.9 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-1/schnell", "aspect_ratio": "1:1", "num_inference_steps": 1, "output_format": "jpeg", "prompt": "A simple blue circle centered on a white background. QA test.", "seed": 20261006}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
