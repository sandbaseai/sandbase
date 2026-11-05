# DeepSeek models API: 9 endpoints with pricing and code examples

Call 9 DeepSeek models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`deepseek/deepseek-chat`](../models/deepseek/deepseek-chat.md) | DeepSeek-V3 is the latest model from the DeepSeek team, building upon the instruction following and coding abilities of the previous… | $0.32 input / $0.89 output per 1M tokens |
| [`deepseek/deepseek-v3.2`](../models/deepseek/deepseek-v3.2.md) | DeepSeek-V3.2 is DeepSeek's open-weight, reasoning-first model released in December 2025 as the official successor to V3.2-Exp. It… | $0.252 input / $0.378 output per 1M tokens |
| [`deepseek/deepseek-v4-flash`](../models/deepseek/deepseek-v4-flash.md) | DeepSeek V4 Flash is an efficiency-optimized Mixture-of-Experts model from DeepSeek with 284B total parameters and 13B activated… | $0.3 input / $1.2 output per 1M tokens |
| [`deepseek/deepseek-v4-flash-0731`](../models/deepseek/deepseek-v4-flash-0731.md) | DeepSeek V4 Flash 0731 is a sparse mixture-of-experts model from DeepSeek, with 13B active parameters out of 284B total. This… | $0.3 input / $1.2 output per 1M tokens |
| [`deepseek/deepseek-v4-flash-vision-exp`](../models/deepseek/deepseek-v4-flash-vision-exp.md) | DeepSeek V4 Flash Vision Exp is an experimental multimodal understanding model that accepts mixed text and image input and produces text… | $0.3 input / $1.2 output per 1M tokens |
| [`deepseek/deepseek-v4-pro`](../models/deepseek/deepseek-v4-pro.md) | DeepSeek V4 Pro is the large tier of DeepSeek's V4 family, a 1.6T-parameter mixture-of-experts model with 49B active parameters,… | $1.32 input / $3.96 output per 1M tokens |
| [`deepseek/deepseek-v4-pro-0813`](../models/deepseek/deepseek-v4-pro-0813.md) | DeepSeek V4 Pro 0813 is the pinned GA release of DeepSeek V4 Pro from August 2026, for workloads that need a fixed version. It keeps V4… | $1.32 input / $3.96 output per 1M tokens |
| [`deepseek/deepseek-v4.1-flash`](../models/deepseek/deepseek-v4.1-flash.md) | DeepSeek V4.1 Flash is the smallest model in DeepSeek's V4.1 architecture family, released in September 2026 with native visual… | $0.3 input / $1.2 output per 1M tokens |
| [`deepseek/deepseek-v4.1-flash-economy`](../models/deepseek/deepseek-v4.1-flash-economy.md) | DeepSeek V4.1 Flash Economy is a lower-cost service tier of the October 17, 2026 snapshot of DeepSeek V4.1 Flash, served through… | $0.3 input / $1.2 output per 1M tokens |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "deepseek/deepseek-chat"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
