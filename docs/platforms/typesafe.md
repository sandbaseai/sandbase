# TypeSafe models API: 2 endpoints with pricing and code examples

Call 2 TypeSafe models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`typesafe/jev-1.13`](../models/typesafe/jev-1.13.md) | Jev 1.13 is a version of Jev, TypeSafe AI's flagship and first public System One model, which makes structured decisions for software… | $0.042 input / $0 output per 1M tokens |
| [`typesafe/jev-1.14`](../models/typesafe/jev-1.14.md) | Jev 1.14 is the latest version of Jev, TypeSafe AI's flagship and first public System One model, which makes structured decisions for… | $0.042 input / $0 output per 1M tokens |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "typesafe/jev-1.13"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
