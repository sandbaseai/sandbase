# Tripo3D models API: 12 endpoints with pricing and code examples

Call 12 Tripo3D models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`tripo3d/tripo-h3.1/image-to-3d`](../models/tripo3d/tripo-h3.1/image-to-3d.md) | Tripo H3.1 by Tripo3D - convert 2D images into 3D models with AI. Generate textured 3D assets from single photos for games, AR/VR,… | from $0.24 to $0.78 per run, depending on parameters |
| [`tripo3d/tripo-h3.1/multiview-to-3d`](../models/tripo3d/tripo-h3.1/multiview-to-3d.md) | Tripo H3.1 Multiview To 3d by Tripo3D - convert 2D images into 3D models with AI. Generate textured 3D assets from single photos for… | from $0.24 to $0.78 per run, depending on parameters |
| [`tripo3d/tripo-h3.1/text-to-3d`](../models/tripo3d/tripo-h3.1/text-to-3d.md) | Tripo H3.1 is Tripo3D's text-to-3D AI model. Turn written descriptions into textured 3D objects with realistic geometry and materials. | from $0.12 to $0.66 per run, depending on parameters |
| [`tripo3d/tripo-p1/image-to-3d`](../models/tripo3d/tripo-p1/image-to-3d.md) | Tripo P1 is Tripo3D's image-to-3D model. It reconstructs a 3D mesh with optional textures from a single image. | from $0.48 to $0.6 per run, depending on parameters |
| [`tripo3d/tripo-p1/text-to-3d`](../models/tripo3d/tripo-p1/text-to-3d.md) | Tripo P1 is Tripo3D's text-to-3D model. It generates a 3D mesh with optional textures from a text description. | from $0.36 to $0.48 per run, depending on parameters |
| [`tripo3d/tripo-p2/image-to-3d`](../models/tripo3d/tripo-p2/image-to-3d.md) | Tripo P2 is Tripo3D's latest flagship 3D generation model. It reconstructs a production-ready mesh with optional PBR textures from a… | from $1.2 to $1.56 per run, depending on parameters |
| [`tripo3d/tripo-p2/text-to-3d`](../models/tripo3d/tripo-p2/text-to-3d.md) | Tripo P2 is Tripo3D's latest flagship 3D generation model. It turns a text description into a production-ready mesh with optional PBR… | from $1.2 to $1.56 per run, depending on parameters |
| [`tripo3d/tripo-v2.5/image-to-3d`](../models/tripo3d/tripo-v2.5/image-to-3d.md) | Tripo v2.5 by Tripo3D generates a textured 3D mesh from a single image, with optional HD textures, PBR materials and quad topology. | from $0.2 to $0.45 per run, depending on parameters |
| [`tripo3d/tripo-v2.5/multiview-to-3d`](../models/tripo3d/tripo-v2.5/multiview-to-3d.md) | Tripo v2.5 by Tripo3D reconstructs a textured 3D mesh from a front view plus optional left, back and right views of the same object. | from $0.2 to $0.45 per run, depending on parameters |
| [`tripo3d/tripo/remesh`](../models/tripo3d/tripo/remesh.md) | Tripo Remesh rebuilds an existing 3D model with clean triangle or quad topology at a target face count. Accepts GLB, OBJ, FBX or STL input. | from $0.42 to $0.48 per run, depending on parameters |
| [`tripo3d/tripo/segment`](../models/tripo3d/tripo/segment.md) | Tripo Segment splits an existing 3D model into named parts. Accepts GLB, OBJ, FBX or STL input. | $0.48 per call |
| [`tripo3d/triposplat`](../models/tripo3d/triposplat.md) | TripoSplat by Tripo3D turns a single image into a 3D Gaussian splat for real-time rendering. Output is a .ply or .splat file. | $0.05 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-h3.1/image-to-3d", "image": "https://static.sandbase.ai/examples/33fdcc66-c331-4b8f-a4b0-95e695982eee/input/bb9227a2-ef6e-4c7d-afa4-073779ff3a60.png"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
