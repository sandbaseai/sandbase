# trellis models API: 4 endpoints with pricing and code examples

Call 4 trellis models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`trellis/trellis`](../models/trellis/trellis.md) | TRELLIS by Microsoft generates a textured 3D mesh (GLB) from a single image using structured 3D latents. | $0.02 per call |
| [`trellis/trellis-2`](../models/trellis/trellis-2.md) | TRELLIS.2 by Microsoft generates a textured 3D model (GLB with PBR materials) from a single image. | from $0.25 to $0.45 per run, depending on parameters |
| [`trellis/trellis-2/retexture`](../models/trellis/trellis-2/retexture.md) | TRELLIS.2 Retexture by Microsoft paints new textures onto an existing 3D mesh (GLB, OBJ, PLY or STL) from a reference image. | from $0.2 to $0.24 per run, depending on parameters |
| [`trellis/trellis/multi`](../models/trellis/trellis/multi.md) | TRELLIS by Microsoft generates a textured 3D mesh (GLB) from several views of the same object. | $0.02 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trellis/trellis", "image": "https://static.sandbase.ai/examples/fe2420f6-f986-41b0-8ba0-a396d9df8b9b/input/9976ef54-909a-45aa-b4ce-c4fa20a068ad.png"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
