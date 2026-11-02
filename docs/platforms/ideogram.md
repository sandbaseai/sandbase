# Ideogram models API: 4 endpoints with pricing and code examples

Call 4 Ideogram models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`ideogram-ai/ideogram-v3`](../models/ideogram-ai/ideogram-v3.md) | 3.0 is Ideogram's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural language… | from $0.03 to $0.09 per run, depending on parameters |
| [`ideogram-ai/ideogram-v3/edit`](../models/ideogram-ai/ideogram-v3/edit.md) | Ideogram V3 Edit by ideogram-ai - AI-powered image editing, style transfer, and transformation. Edit photos with natural language… | from $0.03 to $0.09 per run, depending on parameters |
| [`ideogram/4.5`](../models/ideogram/4.5.md) | Ideogram 4.5 generates images from a text prompt, with reliable text rendering and polished graphic design output. | from $0.03 to $0.22 per run, depending on parameters |
| [`ideogram/4.5/edit`](../models/ideogram/4.5/edit.md) | Ideogram 4.5 edits an image from a text instruction, with an optional mask and style references, with reliable text rendering and polished… | from $0.008 to $0.22 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ideogram-ai/ideogram-v3", "prompt": "The Bone Forest stretched across the horizon, its trees fashioned from the ossified remains of ancient leviathans that once swam through the sky. Shamans with antlers growing from their shoulders and eyes that revealed the true nature of any being they beheld conducted rituals to commune with the spirits that still inhabited the calcified grove. In sky writes \"Ideogram V3 in router.ai\""}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
