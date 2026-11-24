# openimaginglab models API: 1 endpoints with pricing and code examples

Call 1 openimaginglab models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`openimaginglab/flashvsr-plus`](../models/openimaginglab/flashvsr-plus.md) | Flashvsr Plus is openimaginglab's video-to-video AI model. Transform, enhance, and edit video content using text prompts - from style… | about $0.156 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openimaginglab/flashvsr-plus"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
