# Lightricks models API: 7 endpoints with pricing and code examples

Call 7 Lightricks models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`lightricks/ltx-2.3-fast/image-to-video`](../models/lightricks/ltx-2.3-fast/image-to-video.md) | Ltx 2.3 Fast is Lightricks's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and… | from $0.36 to $3.84 per run, depending on parameters |
| [`lightricks/ltx-2.3-fast/text-to-video`](../models/lightricks/ltx-2.3-fast/text-to-video.md) | Ltx 2.3 Fast by Lightricks - generate cinematic videos from text descriptions with AI. Create high-quality video content with natural… | from $0.36 to $3.84 per run, depending on parameters |
| [`lightricks/ltx-2.3-pro/audio-to-video`](../models/lightricks/ltx-2.3-pro/audio-to-video.md) | Ltx 2.3 Pro Audio To Video by Lightricks - advanced AI model for audio-to-video. Delivers high-quality results with fast inference,… | about $0.5 per call |
| [`lightricks/ltx-2.3-pro/image-to-video`](../models/lightricks/ltx-2.3-pro/image-to-video.md) | Ltx 2.3 Pro by Lightricks - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion,… | from $0.48 to $3.2 per run, depending on parameters |
| [`lightricks/ltx-2.3-pro/retake`](../models/lightricks/ltx-2.3-pro/retake.md) | Ltx 2.3 Pro Retake by Lightricks - AI-powered video editing and transformation. Apply style transfer, motion control, lip-sync, and visual… | from $0.2 to $2 per run, depending on parameters |
| [`lightricks/ltx-2.3-pro/text-to-video`](../models/lightricks/ltx-2.3-pro/text-to-video.md) | Ltx 2.3 Pro is Lightricks's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic… | from $0.48 to $3.2 per run, depending on parameters |
| [`lightricks/ltx-2.3-pro/video-extend`](../models/lightricks/ltx-2.3-pro/video-extend.md) | Ltx 2.3 Pro Extend by Lightricks - AI-powered video editing and transformation. Apply style transfer, motion control, lip-sync, and visual… | from $0.2 to $2 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lightricks/ltx-2.3-fast/image-to-video", "image": "https://static.sandbase.ai/examples/78072a01-7219-4993-a8f3-089836e6ad15/input/cc432447-c109-463d-a28b-0e4b21c66923.png", "prompt": "Snorkel lens ground-scraping tracking shot following a barefoot Ethiopian long-distance runner training on a dirt road at dawn, camera inches from the ground racing alongside, her feet kicking up red dust in slow motion at 240fps, Rift Valley landscape blurred in the background, the texture of earth and callused skin in hyper-detail, 40mm snorkel lens at ground height, Nike Running documentary meets Lu'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
