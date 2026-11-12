# pixal3d models API: 1 endpoints with pricing and code examples

Call 1 pixal3d models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`pixal3d/pixal3d`](../models/pixal3d/pixal3d.md) | Pixal3D generates a high-fidelity textured 3D model (GLB) from a single image. | from $0.3 to $0.42 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pixal3d/pixal3d", "image": "https://static.sandbase.ai/examples/0aae330f-ad5f-4988-8393-79047a49cd88/input/d0c53122-f929-4cd4-9073-2a48d77f2859.png"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
