# Midjourney models API: 1 endpoints with pricing and code examples

Call 1 Midjourney models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`midjourney/midjourney-v8.1`](../models/midjourney/midjourney-v8.1.md) | Midjourney V8.1 text-to-image generation. | from $0.08 to $0.12 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "midjourney/midjourney-v8.1", "prompt": "Square flash sale poster for a pair of white running shoes on a bright yellow background. A headline that reads exactly: \"FLASH SALE\". Show the old price \"Was $129.00\" with a strikethrough line, and the new price \"Now $89.00\" larger next to it. At the bottom, a line that reads exactly: \"Ends 2026.10.03\". Render the text exactly as written, with no other text anywhere in the image."}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
