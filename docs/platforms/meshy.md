# Meshy models API: 20 endpoints with pricing and code examples

Call 20 Meshy models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`meshy/6.0-lite/retexture`](../models/meshy/6.0-lite/retexture.md) | Meshy 6 Lite Retexture is the lower-cost Meshy retexturing model: repaint an existing 3D model from a text or image style. | $0.36 per call |
| [`meshy/6.0/retexture`](../models/meshy/6.0/retexture.md) | Meshy 6 Retexture repaints an existing 3D model from a text or image style, with optional PBR maps and up to 8K textures. | from $0.33 to $0.5 per run, depending on parameters |
| [`meshy/7.0/image-to-3d`](../models/meshy/7.0/image-to-3d.md) | Meshy 7 turns a single image into a 3D model, with optional textures, PBR maps, 2K geometry, humanoid auto-rigging and animation. | from $0.8 to $1.72 per run, depending on parameters |
| [`meshy/7.0/multi-image-to-3d`](../models/meshy/7.0/multi-image-to-3d.md) | Meshy 7 reconstructs a 3D model from 1–4 views of the same object, with optional textures, PBR maps, 2K geometry, auto-rigging and… | from $0.8 to $1.72 per run, depending on parameters |
| [`meshy/7.0/retexture`](../models/meshy/7.0/retexture.md) | Meshy 7 Retexture repaints an existing 3D model from a text or image style, with optional PBR maps and up to 8K textures. | from $0.33 to $0.5 per run, depending on parameters |
| [`meshy/7.0/text-to-3d`](../models/meshy/7.0/text-to-3d.md) | Meshy 7 generates a 3D model from a text prompt, either as an untextured preview mesh or fully textured, with optional 2K geometry,… | from $0.8 to $1.72 per run, depending on parameters |
| [`meshy/7.1/image-to-3d`](../models/meshy/7.1/image-to-3d.md) | Meshy 7.1 turns a single image into a textured, optionally rigged and animated 3D model. | from $0.96 to $2.304 per run, depending on parameters |
| [`meshy/7.1/multi-image-to-3d`](../models/meshy/7.1/multi-image-to-3d.md) | Meshy 7.1 reconstructs a textured, optionally rigged 3D model from 1–4 views of the same object. | from $0.96 to $2.064 per run, depending on parameters |
| [`meshy/7.1/text-to-3d`](../models/meshy/7.1/text-to-3d.md) | Meshy 7.1 generates a textured, optionally rigged and animated 3D model from a text prompt. | from $1.44 to $2.304 per run, depending on parameters |
| [`meshy/meshy-v6`](../models/meshy/meshy-v6.md) | Meshy 6 turns a single image into a 3D model, with optional textures, PBR maps, humanoid auto-rigging and animation. | from $0.8 to $1.52 per run, depending on parameters |
| [`meshy/meshy-v6/multi-image-to-3d`](../models/meshy/meshy-v6/multi-image-to-3d.md) | Meshy 6 reconstructs a 3D model from 1–4 views of the same object, with optional textures, PBR maps, auto-rigging and animation. | from $0.8 to $1.52 per run, depending on parameters |
| [`meshy/meshy-v6/text-to-3d`](../models/meshy/meshy-v6/text-to-3d.md) | Meshy 6 generates a 3D model from a text prompt, either as an untextured preview mesh or fully textured, with optional rigging and… | from $0.8 to $1.52 per run, depending on parameters |
| [`meshy/n1/retexture`](../models/meshy/n1/retexture.md) | Meshy N1 Retexture repaints an existing 3D model from one reference image or up to four reference views, producing a 2K base color texture. | $0.4 per call |
| [`meshy/relief`](../models/meshy/relief.md) | Meshy Relief turns a photo into a printable 3D relief (GLB and STL) with emboss or engrave carving and an optional curved bend. | $0.8 per call |
| [`meshy/rigging`](../models/meshy/rigging.md) | Meshy Rigging adds a humanoid skeleton to an existing character model and can also apply one animation preset. | from $0.2 to $0.32 per run, depending on parameters |
| [`meshy/rigging/multi-animation`](../models/meshy/rigging/multi-animation.md) | Meshy Rigging Multi-Animation rigs an existing humanoid character model and generates up to 10 animation clips on the same rig. | from $0.44 per run, depending on parameters |
| [`meshy/t2.5/image-to-3d`](../models/meshy/t2.5/image-to-3d.md) | Meshy T2.5 turns a single image into a clean Smart Topology triangle mesh (up to 30,000 triangles), with optional textures, rigging and… | from $0.2 to $0.92 per run, depending on parameters |
| [`meshy/t2.5/text-to-3d`](../models/meshy/t2.5/text-to-3d.md) | Meshy T2.5 generates a clean Smart Topology triangle mesh (up to 30,000 triangles) from a text prompt, untextured in preview mode or… | from $0.2 to $0.92 per run, depending on parameters |
| [`meshy/t2/image-to-3d`](../models/meshy/t2/image-to-3d.md) | Meshy T2 turns a single image into a clean Smart Topology triangle mesh (up to 15,000 triangles), with optional textures, rigging and… | from $0.2 to $0.92 per run, depending on parameters |
| [`meshy/t2/text-to-3d`](../models/meshy/t2/text-to-3d.md) | Meshy T2 generates a clean Smart Topology triangle mesh (up to 15,000 triangles) from a text prompt, untextured in preview mode or… | from $0.2 to $0.92 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/6.0-lite/retexture", "model_url": "https://static.sandbase.ai/examples/083613da-f698-400f-9081-e79012416827/input/53f87138-036f-4a9a-9c0c-18327624516b.glb", "text_style_prompt": "hand-painted cartoon toy box, bright blue with yellow stars"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
