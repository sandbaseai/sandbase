# LMArena API: 1 endpoints with pricing and code examples

Call 1 LMArena endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`lmarena/list-available-models`](../models/lmarena/list-available-models.md) | List all models available for direct interaction on LMArena, including their capabilities (input/output modalities), organization,… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lmarena/list-available-models"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
