# Hitem3D models API: 7 endpoints with pricing and code examples

Call 7 Hitem3D models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`hitem3d/hi3d/image-to-3d`](../models/hitem3d/hi3d/image-to-3d.md) | Hi3D by Hitem3D generates a 3D model from a single image, with a selectable model version (v1.5, v2.0, v2.1, or portrait-tuned variants)… | from $0.4 to $0.9 per run, depending on parameters |
| [`hitem3d/hi3d/multi-view-to-3d`](../models/hitem3d/hi3d/multi-view-to-3d.md) | Hi3D by Hitem3D generates a 3D model from a front view plus optional back, left and right views, with a selectable model version and… | from $0.4 to $0.9 per run, depending on parameters |
| [`hitem3d/hi3d/multicolor`](../models/hitem3d/hi3d/multicolor.md) | Hi3D Multicolor by Hitem3D converts a textured GLB model into a model with a limited set of flat colors, for multi-color 3D printing. | $0.4 per call |
| [`hitem3d/hi3d/split`](../models/hitem3d/hi3d/split.md) | Hi3D Split by Hitem3D splits a 3D model into parts, either by a humanoid character template with optional joints or by granularity for… | $0.4 per call |
| [`hitem3d/hi3d/texture`](../models/hitem3d/hi3d/texture.md) | Hi3D Texture by Hitem3D adds textures to an untextured GLB model using a reference image. It uses the v1.5 texture models. | $0.2 per call |
| [`hitem3d/hi3d/v3.0/image-to-3d`](../models/hitem3d/hi3d/v3.0/image-to-3d.md) | Hi3D 3.0 by Hitem3D reconstructs a detailed, watertight 3D model at 2048³ resolution from a single image, with optional texture and PBR… | from $2.16 to $10.92 per run, depending on parameters |
| [`hitem3d/hi3d/v3.0/multi-view-to-3d`](../models/hitem3d/hi3d/v3.0/multi-view-to-3d.md) | Hi3D 3.0 by Hitem3D reconstructs a detailed 3D model at 2048³ resolution from a front view plus optional back, left and right views. | from $2.16 to $10.92 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hitem3d/hi3d/image-to-3d", "image": "https://storage.googleapis.com/falserverless/example_inputs/dog.png"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
