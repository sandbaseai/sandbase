# Recraft models API: 2 endpoints with pricing and code examples

Call 2 Recraft models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`recraft/recraft/v4.1`](../models/recraft/recraft/v4.1.md) | Recraft V4.1 by Recraft - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles,… | $0.035 per call |
| [`recraft/recraft/v4.1/utility`](../models/recraft/recraft/v4.1/utility.md) | Recraft V4.1 Utility by Recraft - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios,… | from $0.04 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "recraft/recraft/v4.1", "prompt": "Tilt-shift miniature effect on a real Portuguese fishing village at golden hour, colorful boats in the harbor appearing toy-like, selective focus band across the middle, saturated primary colors of blue red and yellow boats against white buildings, 90mm tilt-shift lens, the familiar made fantastical, Wes Anderson color sensibility"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
