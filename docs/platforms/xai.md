# xAI models API: 20 endpoints with pricing and code examples

Call 20 xAI models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`x-ai/grok-4.3`](../models/x-ai/grok-4.3.md) | Grok 4.3 is an xAI reasoning model that xAI describes as fast and reliable, with strong tool calling and instruction following. It accepts… | $1.25 input / $2.5 output per 1M tokens |
| [`x-ai/grok-4.5`](../models/x-ai/grok-4.5.md) | Grok 4.5 is an xAI reasoning model for coding, agentic tasks and knowledge work, released on the xAI API in July 2026 and trained… | $2 input / $6 output per 1M tokens |
| [`x-ai/grok-4.6`](../models/x-ai/grok-4.6.md) | Grok 4.6 is xAI's frontier reasoning model for coding, agentic tasks and knowledge work, released in August 2026 as the successor to Grok… | $2 input / $6 output per 1M tokens |
| [`x-ai/grok-4.7`](../models/x-ai/grok-4.7.md) | Grok 4.7 is xAI's flagship reasoning model for coding, agentic tasks and knowledge work, released on the xAI API in September 2026 as the… | $2 input / $6 output per 1M tokens |
| [`xai/grok-imagine-image/2.0/edit`](../models/xai/grok-imagine-image/2.0/edit.md) | Grok Imagine Image 2.0 Edit is xAI's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts… | from $0.04 to $0.08 per run, depending on parameters |
| [`xai/grok-imagine-image/2.0/text-to-image`](../models/xai/grok-imagine-image/2.0/text-to-image.md) | Grok Imagine Image 2.0 by xAI - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios,… | from $0.04 to $0.08 per run, depending on parameters |
| [`xai/grok-imagine-image/edit`](../models/xai/grok-imagine-image/edit.md) | Grok Imagine Image Edit is xAI's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts -… | from $0.02 per run, depending on parameters |
| [`xai/grok-imagine-image/quality`](../models/xai/grok-imagine-image/quality.md) | Grok Imagine Image Quality by xAI - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios,… | from $0.05 to $0.07 per run, depending on parameters |
| [`xai/grok-imagine-image/quality/edit`](../models/xai/grok-imagine-image/quality/edit.md) | Grok Imagine Image Quality Edit is xAI's intelligent image editing model. Transform, retouch, and reimagine existing images using text… | from $0.05 to $0.07 per run, depending on parameters |
| [`xai/grok-imagine-video/1.5/image-to-video`](../models/xai/grok-imagine-video/1.5/image-to-video.md) | Grok Imagine Video 1.5 is xAI's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion,… | from $0.09 to $2.11 per run, depending on parameters |
| [`xai/grok-imagine-video/1.5/lite/image-to-video`](../models/xai/grok-imagine-video/1.5/lite/image-to-video.md) | Grok Imagine Video 1.5 Lite, the low-cost tier of xAI's video model, animates an image into a 1-15 second video with native audio. | from $0.03 to $2.11 per run, depending on parameters |
| [`xai/grok-imagine-video/1.5/lite/text-to-video`](../models/xai/grok-imagine-video/1.5/lite/text-to-video.md) | Grok Imagine Video 1.5 Lite, the low-cost tier of xAI's video model, turns a text prompt into a 1-15 second video with native audio. | from $0.02 to $2.1 per run, depending on parameters |
| [`xai/grok-imagine-video/1.5/reference-to-video`](../models/xai/grok-imagine-video/1.5/reference-to-video.md) | Grok Imagine Video 1.5 is xAI's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion,… | from $0.09 to $2.11 per run, depending on parameters |
| [`xai/grok-imagine-video/1.5/text-to-video`](../models/xai/grok-imagine-video/1.5/text-to-video.md) | Grok Imagine Video 1.5 by xAI - generate cinematic videos from text descriptions with AI. Create high-quality video content with natural… | from $0.08 to $3.75 per run, depending on parameters |
| [`xai/grok-imagine-video/image-to-video`](../models/xai/grok-imagine-video/image-to-video.md) | Grok Imagine Video is xAI's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and… | from $0.052 to $1.052 per run, depending on parameters |
| [`xai/grok-imagine-video/reference-to-video`](../models/xai/grok-imagine-video/reference-to-video.md) | Grok Imagine Video is xAI's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and… | from $0.052 to $0.702 per run, depending on parameters |
| [`xai/grok-imagine-video/text-to-video`](../models/xai/grok-imagine-video/text-to-video.md) | Grok Imagine Video by xAI - generate cinematic videos from text descriptions with AI. Create high-quality video content with natural… | from $0.05 to $0.75 per run, depending on parameters |
| [`xai/grok-imagine-video/video-edit`](../models/xai/grok-imagine-video/video-edit.md) | Grok Imagine Video Edit is xAI's video-to-video AI model. Transform, enhance, and edit video content using text prompts - from style… | about $0.3 per call |
| [`xai/grok-imagine-video/video-extend`](../models/xai/grok-imagine-video/video-extend.md) | Grok Imagine Video Extend is xAI's video-to-video AI model. Transform, enhance, and edit video content using text prompts - from style… | from $0.12 to $0.6 per run, depending on parameters |
| [`xai/grok-tts`](../models/xai/grok-tts.md) | Grok Tts by xAI - convert text to natural-sounding speech with AI. Supports multiple voices, languages, emotions, and speaking styles for… | from $0.015 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "x-ai/grok-4.3"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
