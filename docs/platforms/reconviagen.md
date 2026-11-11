# reconviagen models API: 1 endpoints with pricing and code examples

Call 1 reconviagen models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`reconviagen/reconviagen-0.5`](../models/reconviagen/reconviagen-0.5.md) | ReconViaGen 0.5 reconstructs a textured 3D model (GLB with PBR materials) from one or more views of the same object; more views give a… | from $0.25 to $0.35 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reconviagen/reconviagen-0.5", "images": "https://storage.googleapis.com/falserverless/model_tests/video_models/front.png"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
