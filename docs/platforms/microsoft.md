# Microsoft models API: 2 endpoints with pricing and code examples

Call 2 Microsoft models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`microsoft/mai-image-2.5-pro/edit`](../models/microsoft/mai-image-2.5-pro/edit.md) | Mai Image 2.5 Pro Edit by Microsoft - AI-powered image editing, style transfer, and transformation. Edit photos with natural language… | from $0.29 per run, depending on parameters |
| [`microsoft/mai-image-2.5/edit`](../models/microsoft/mai-image-2.5/edit.md) | Mai Image 2.5 Edit by Microsoft - AI-powered image editing, style transfer, and transformation. Edit photos with natural language… | $0.05 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "microsoft/mai-image-2.5-pro/edit", "prompt": "Turn this into a clean, futuristic product shot with soft studio lighting.", "image": "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input.png"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
