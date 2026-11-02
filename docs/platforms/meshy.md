# Meshy models API: 6 endpoints with pricing and code examples

Call 6 Meshy models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`meshy/6.0-lite/retexture`](../models/meshy/6.0-lite/retexture.md) | Meshy 6 Lite Retexture is the lower-cost Meshy retexturing model: repaint an existing 3D model from a text or image style. | $0.36 per call |
| [`meshy/6.0/retexture`](../models/meshy/6.0/retexture.md) | Meshy 6 Retexture repaints an existing 3D model from a text or image style, with optional PBR maps and up to 8K textures. | from $0.33 to $0.5 per run, depending on parameters |
| [`meshy/7.0/retexture`](../models/meshy/7.0/retexture.md) | Meshy 7 Retexture repaints an existing 3D model from a text or image style, with optional PBR maps and up to 8K textures. | from $0.33 to $0.5 per run, depending on parameters |
| [`meshy/7.1/image-to-3d`](../models/meshy/7.1/image-to-3d.md) | Meshy 7.1 turns a single image into a textured, optionally rigged and animated 3D model. | from $0.96 to $2.304 per run, depending on parameters |
| [`meshy/7.1/multi-image-to-3d`](../models/meshy/7.1/multi-image-to-3d.md) | Meshy 7.1 reconstructs a textured, optionally rigged 3D model from 1–4 views of the same object. | from $0.96 to $2.064 per run, depending on parameters |
| [`meshy/7.1/text-to-3d`](../models/meshy/7.1/text-to-3d.md) | Meshy 7.1 generates a textured, optionally rigged and animated 3D model from a text prompt. | from $1.44 to $2.304 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/6.0-lite/retexture", "model_url": "<model_url>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
