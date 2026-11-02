# Xiaomi models API: 2 endpoints with pricing and code examples

Call 2 Xiaomi models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`xiaomi/mimo-v2.6-flash`](../models/xiaomi/mimo-v2.6-flash.md) | MiMo-V2.6-Flash is the efficiency tier of Xiaomi's open-source MiMo-V2.6 series, released in September 2026 as a natively omni-modal… | $0.14 input / $0.28 output per 1M tokens |
| [`xiaomi/mimo-v2.6-pro`](../models/xiaomi/mimo-v2.6-pro.md) | MiMo-V2.6-Pro is the flagship of Xiaomi's open-source MiMo-V2.6 series, a trillion-parameter, natively omni-modal reasoning model released… | $0.435 input / $0.87 output per 1M tokens |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaomi/mimo-v2.6-flash"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
