# hyper3d models API: 4 endpoints with pricing and code examples

Call 4 hyper3d models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`hyper3d/rodin/2.5/fast/image-to-3d`](../models/hyper3d/rodin/2.5/fast/image-to-3d.md) | Rodin Gen-2.5 by Hyper3D (Deemos) generates game- and production-ready 3D assets from one to five reference images, tuned for speed with… | $0.1 per call |
| [`hyper3d/rodin/2.5/fast/text-to-3d`](../models/hyper3d/rodin/2.5/fast/text-to-3d.md) | Rodin Gen-2.5 by Hyper3D (Deemos) generates game- and production-ready 3D assets from a text prompt, tuned for speed with the low tiers. | $0.1 per call |
| [`hyper3d/rodin/2.5/image-to-3d`](../models/hyper3d/rodin/2.5/image-to-3d.md) | Rodin Gen-2.5 by Hyper3D (Deemos) generates game- and production-ready 3D assets from one to five reference images. | from $1.44 to $1.92 per run, depending on parameters |
| [`hyper3d/rodin/2.5/text-to-3d`](../models/hyper3d/rodin/2.5/text-to-3d.md) | Rodin Gen-2.5 by Hyper3D (Deemos) generates game- and production-ready 3D assets from a text prompt. | from $1.44 to $1.92 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hyper3d/rodin/2.5/fast/image-to-3d", "images": "<images>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
