# sandbase-ai models API: 1 endpoints with pricing and code examples

Call 1 sandbase-ai models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`sandbase-ai/cat-vton`](../models/sandbase-ai/cat-vton.md) | CatVTON is a virtual try-on model. It dresses the person in a photo with a garment from a second image, with controls for the covered body… | $0.00125 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sandbase-ai/cat-vton"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
