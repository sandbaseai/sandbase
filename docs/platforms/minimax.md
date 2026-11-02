# Minimax models API: 4 endpoints with pricing and code examples

Call 4 Minimax models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`minimax/minimax-m2.5`](../models/minimax/minimax-m2.5.md) | MiniMax-M2.5 is a MiniMax M2-series language model released in February 2026 for real-world productivity, trained with reinforcement… | $0.3 input / $1.2 output per 1M tokens |
| [`minimax/minimax-m2.7`](../models/minimax/minimax-m2.7.md) | MiniMax-M2.7 is a MiniMax M2-series language model that MiniMax describes as its first model to take part in its own development, building… | $0.3 input / $1.2 output per 1M tokens |
| [`minimax/minimax-m3`](../models/minimax/minimax-m3.md) | MiniMax-M3 is MiniMax's flagship multimodal foundation model, which MiniMax describes as open-weight. It is built on MiniMax Sparse… | $0.3 input / $1.2 output per 1M tokens |
| [`minimax/minimax-m3.1-flash`](../models/minimax/minimax-m3.1-flash.md) | MiniMax-M3.1-Flash is the fast, cost-efficient tier of MiniMax's M3.1 generation, which MiniMax describes as an ultra-efficient… | $0.15 input / $0.6 output per 1M tokens |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/minimax-m2.5"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
