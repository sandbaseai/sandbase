# Bytedance models API: 28 endpoints with pricing and code examples

Call 28 Bytedance models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`bytedance/dreamactor/2.0`](../models/bytedance/dreamactor/2.0.md) | DreamActor 2.0 by ByteDance transfers motion, facial expressions and lip movement from a driving video to the character in a reference… | about $0.25 per call |
| [`bytedance/omnihuman/1.5`](../models/bytedance/omnihuman/1.5.md) | Omnihuman 1.5 is Bytedance's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and… | about $0.8 per call |
| [`bytedance/omnihuman/2.0`](../models/bytedance/omnihuman/2.0.md) | OmniHuman 2.0 by ByteDance turns a single image and an audio track into a talking or performing video that follows the audio. | about $0.525 per call |
| [`bytedance/seed-2.1-pro`](../models/bytedance/seed-2.1-pro.md) | Seed 2.1 Pro is the larger of the two models in ByteDance Seed's Seed2.1 family, offered as Doubao-Seed-2.1-Pro through Doubao and Volcano… | $0.890208 input / $4.451039 output per 1M tokens |
| [`bytedance/seed-speech/tts/2.0`](../models/bytedance/seed-speech/tts/2.0.md) | Seed Speech Tts 2.0 is Bytedance's text-to-speech AI model. Generate human-like voiceovers with expressive intonation, multilingual… | from $0.06 per run, depending on parameters |
| [`bytedance/seedance/2.0/fast/image-to-video`](../models/bytedance/seedance/2.0/fast/image-to-video.md) | ByteDance's most advanced image-to-video model in its fast tier delivering lower latency and cost without compromising on cinematic… | from $0.4 to $1.6 per run, depending on parameters |
| [`bytedance/seedance/2.0/fast/reference-to-video`](../models/bytedance/seedance/2.0/fast/reference-to-video.md) | ByteDance's most advanced reference-to-video model in its fast tier delivering lower latency and cost without compromising on cinematic… | about $1 per call |
| [`bytedance/seedance/2.0/fast/text-to-video`](../models/bytedance/seedance/2.0/fast/text-to-video.md) | ByteDance's most advanced text-to-video model in its fast tier delivering lower latency and cost without compromising on cinematic output,… | from $0.4 to $1.6 per run, depending on parameters |
| [`bytedance/seedance/2.0/image-to-video`](../models/bytedance/seedance/2.0/image-to-video.md) | ByteDance's most advanced image-to-video model transforming still images into cinematic video with native audio, multi-shot editing, and… | from $0.48 to $9.6 per run, depending on parameters |
| [`bytedance/seedance/2.0/mini/image-to-video`](../models/bytedance/seedance/2.0/mini/image-to-video.md) | Seedance 2.0 Mini by Bytedance - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural… | from $0.24 to $0.96 per run, depending on parameters |
| [`bytedance/seedance/2.0/mini/reference-to-video`](../models/bytedance/seedance/2.0/mini/reference-to-video.md) | Seedance 2.0 Mini by Bytedance - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural… | about $0.6 per call |
| [`bytedance/seedance/2.0/mini/text-to-video`](../models/bytedance/seedance/2.0/mini/text-to-video.md) | Seedance 2.0 Mini is Bytedance's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with… | from $0.24 to $0.96 per run, depending on parameters |
| [`bytedance/seedance/2.0/reference-to-video`](../models/bytedance/seedance/2.0/reference-to-video.md) | ByteDance's most advanced reference-to-video model generating cinematic video guided by reference content, with native audio, multi-shot… | about $1.2 per call |
| [`bytedance/seedance/2.0/text-to-video`](../models/bytedance/seedance/2.0/text-to-video.md) | ByteDance's most advanced text-to-video model delivering cinematic output, native audio, multi-shot editing, and director-level camera… | from $0.48 to $9.6 per run, depending on parameters |
| [`bytedance/seedance/2.5/image-to-video`](../models/bytedance/seedance/2.5/image-to-video.md) | ByteDance's next-generation image-to-video model, animating a single still into a native clip up to 30 seconds at 720p with continuous,… | from $0.72 to $7.2 per run, depending on parameters |
| [`bytedance/seedance/2.5/reference-to-video`](../models/bytedance/seedance/2.5/reference-to-video.md) | ByteDance's next-generation reference-to-video model, generating video from multimodal references (images, videos, audio) and locking a… | about $1.8 per call |
| [`bytedance/seedance/2.5/text-to-video`](../models/bytedance/seedance/2.5/text-to-video.md) | ByteDance's next-generation text-to-video model, generating native single-shot clips up to 30 seconds at 720p with coherent motion, native… | from $0.72 to $7.2 per run, depending on parameters |
| [`bytedance/seedream/4.5`](../models/bytedance/seedream/4.5.md) | A new-generation image creation model from ByteDance, Seedream 4.5 integrates text-to-image generation and image editing into a single… | $0.04 per call |
| [`bytedance/seedream/4.5/edit`](../models/bytedance/seedream/4.5/edit.md) | A new-generation image creation model from ByteDance, Seedream 4.5 integrates text-to-image generation and image editing into a single… | $0.04 per call |
| [`bytedance/seedream/5.0/flash`](../models/bytedance/seedream/5.0/flash.md) | Seedream 5.0 Flash is ByteDance's fast, low-cost Seedream 5.0 tier for high-volume text-to-image generation, with roughly 15–20 second… | $0.018 per call |
| [`bytedance/seedream/5.0/flash/edit`](../models/bytedance/seedream/5.0/flash/edit.md) | Seedream 5.0 Flash Editing edits and fuses up to 10 reference images from a text instruction at one flat price per image, with fast 15–20… | $0.018 per call |
| [`bytedance/seedream/5.0/lite`](../models/bytedance/seedream/5.0/lite.md) | Seedream 5.0 Lite — Fast Text-to-Image API The lightweight version of Seedream 5.0, delivering high-quality, low-latency AI image… | $0.035 per call |
| [`bytedance/seedream/5.0/lite/edit`](../models/bytedance/seedream/5.0/lite/edit.md) | Seedream 5.0 Lite — Fast Text-to-Image API The lightweight version of Seedream 5.0, delivering high-quality, low-latency AI image… | $0.035 per call |
| [`bytedance/seedream/5.0/pro`](../models/bytedance/seedream/5.0/pro.md) | Seedream 5.0 Pro by Bytedance - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios,… | from $0.09 per run, depending on parameters |
| [`bytedance/seedream/5.0/pro/edit`](../models/bytedance/seedream/5.0/pro/edit.md) | Seedream 5.0 Pro is Bytedance's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts -… | from $0.096 per run, depending on parameters |
| [`bytedance/seedvr/upscale/image`](../models/bytedance/seedvr/upscale/image.md) | Seedvr Upscale Image by Bytedance - AI-powered image editing, style transfer, and transformation. Edit photos with natural language… | $0.01 per call |
| [`bytedance/seedvr/upscale/video`](../models/bytedance/seedvr/upscale/video.md) | Seedvr Upscale Video by Bytedance - AI-powered video editing and transformation. Apply style transfer, motion control, lip-sync, and… | about $0.31104 per call |
| [`bytedance/upscaler/video`](../models/bytedance/upscaler/video.md) | Bytedance Video Upscaler upscales videos to 4K resolution with AI-powered enhancement. Supports multiple quality tiers (fast, standard,… | about $0.036 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/dreamactor/2.0", "image": "https://static.sandbase.ai/examples/1668055b-f263-449e-a2b0-64ce4b82aba2/input/e2db078d-d0b4-4317-bf55-9372a99f8359.png", "video": "https://static.sandbase.ai/examples/1668055b-f263-449e-a2b0-64ce4b82aba2/input/df52f6c5-d3e1-4bd2-8348-a8f1ab03ac18.mp4"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
