# Tripo3D models API: 5 endpoints with pricing and code examples

Call 5 Tripo3D models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`tripo3d/tripo-h3.1/image-to-3d`](../models/tripo3d/tripo-h3.1/image-to-3d.md) | Tripo H3.1 by Tripo3D - convert 2D images into 3D models with AI. Generate textured 3D assets from single photos for games, AR/VR,… | from $0.24 to $0.78 per run, depending on parameters |
| [`tripo3d/tripo-h3.1/multiview-to-3d`](../models/tripo3d/tripo-h3.1/multiview-to-3d.md) | Tripo H3.1 Multiview To 3d by Tripo3D - convert 2D images into 3D models with AI. Generate textured 3D assets from single photos for… | from $0.24 to $0.78 per run, depending on parameters |
| [`tripo3d/tripo-h3.1/text-to-3d`](../models/tripo3d/tripo-h3.1/text-to-3d.md) | Tripo H3.1 is Tripo3D's text-to-3D AI model. Turn written descriptions into textured 3D objects with realistic geometry and materials. | from $0.12 to $0.66 per run, depending on parameters |
| [`tripo3d/tripo-p2/image-to-3d`](../models/tripo3d/tripo-p2/image-to-3d.md) | Tripo P2 is Tripo3D's latest flagship 3D generation model. It reconstructs a production-ready mesh with optional PBR textures from a… | from $1.2 to $1.56 per run, depending on parameters |
| [`tripo3d/tripo-p2/text-to-3d`](../models/tripo3d/tripo-p2/text-to-3d.md) | Tripo P2 is Tripo3D's latest flagship 3D generation model. It turns a text description into a production-ready mesh with optional PBR… | from $1.2 to $1.56 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-h3.1/image-to-3d", "image": "<image>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
