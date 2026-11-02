# HiDream models API: 1 endpoints with pricing and code examples

Call 1 HiDream models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`hidream-ai/hidream-o1/dev`](../models/hidream-ai/hidream-o1/dev.md) | Hidream O1 Dev by hidream-ai - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios,… | $0.02 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hidream-ai/hidream-o1/dev", "prompt": "<prompt>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
