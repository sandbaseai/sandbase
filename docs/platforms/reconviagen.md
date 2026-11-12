# reconviagen models API: 1 endpoints with pricing and code examples

Call 1 reconviagen models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`reconviagen/reconviagen-0.5`](../models/reconviagen/reconviagen-0.5.md) | ReconViaGen 0.5 reconstructs a textured 3D model (GLB with PBR materials) from one or more views of the same object; more views give a… | from $0.25 to $0.35 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reconviagen/reconviagen-0.5", "images": ["https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/61e979cb-8ae9-4cee-a73e-c1402d05faed.png", "https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/3025d72b-49eb-4751-ad7d-502b2e8e7c90.png", "https://static.sandbase.ai/examples/e7aaf9f3-ff36-4f29-9817-19caa1bf2e2c/input/f67785e3-394b-4c82-b251-28f0993af3a0.png"]}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
