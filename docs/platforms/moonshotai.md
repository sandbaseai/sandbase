# Moonshotai models API: 4 endpoints with pricing and code examples

Call 4 Moonshotai models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`moonshotai/kimi-k2.5`](../models/moonshotai/kimi-k2.5.md) | Kimi K2.5 is Moonshot AI's open-source native multimodal agentic model, built by continuing pretraining of Kimi K2 on about 15 trillion… | $0.6 input / $3 output per 1M tokens |
| [`moonshotai/kimi-k2.6`](../models/moonshotai/kimi-k2.6.md) | Kimi K2.6 is Moonshot AI's general-purpose multimodal model, taking text, image and video input with both thinking and non-thinking modes… | $0.95 input / $4 output per 1M tokens |
| [`moonshotai/kimi-k3`](../models/moonshotai/kimi-k3.md) | Kimi K3 is Moonshot AI's flagship model, a 2.8-trillion-parameter open-weight mixture-of-experts model with native visual understanding… | $3 input / $15 output per 1M tokens |
| [`moonshotai/kimi-k3.1-pro`](../models/moonshotai/kimi-k3.1-pro.md) | Kimi K3.1 Pro is Moonshot AI's flagship open-weight multimodal reasoning model, a post-trained successor to Kimi K3 with a 1M-token… | $2 input / $10 output per 1M tokens |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "moonshotai/kimi-k2.5"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
