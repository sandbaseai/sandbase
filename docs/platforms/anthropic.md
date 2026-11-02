# Anthropic models API: 15 endpoints with pricing and code examples

Call 15 Anthropic models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`anthropic/claude-fable-5`](../models/anthropic/claude-fable-5.md) | Claude Fable 5 is a Mythos-class model from Anthropic, built for autonomous knowledge work and coding. It supports text, image, and file… | $10 input / $50 output per 1M tokens |
| [`anthropic/claude-fable-5.1`](../models/anthropic/claude-fable-5.1.md) | Claude Fable 5.1 improves on Claude Fable 5 across the board, with the biggest gains in agentic coding, long-running agentic workflows,… | $10 input / $50 output per 1M tokens |
| [`anthropic/claude-fable-5.5`](../models/anthropic/claude-fable-5.5.md) | Claude Fable 5.5 is the expected successor to Claude Fable 5.1, Anthropic's tier above Opus for repository-scale coding, long-running… |  |
| [`anthropic/claude-haiku-4.5`](../models/anthropic/claude-haiku-4.5.md) | Claude Haiku 4.5 is Anthropic’s fastest and most efficient model, delivering near-frontier intelligence at a fraction of the cost and… | $1 input / $5 output per 1M tokens |
| [`anthropic/claude-haiku-5.5`](../models/anthropic/claude-haiku-5.5.md) | Claude Haiku 5.5 is Anthropic's small, fast model for high-volume, cost-sensitive work such as summarization, classification, compaction,… | $0.1 input / $0.5 output per 1M tokens |
| [`anthropic/claude-opus-4.5`](../models/anthropic/claude-opus-4.5.md) | Claude Opus 4.5 is Anthropic’s frontier reasoning model optimized for complex software engineering, agentic workflows, and long-horizon… | $5 input / $25 output per 1M tokens |
| [`anthropic/claude-opus-4.6`](../models/anthropic/claude-opus-4.6.md) | Opus 4.6 is Anthropic’s strongest model for coding and long-running professional tasks. It is built for agents that operate across entire… | $5 input / $25 output per 1M tokens |
| [`anthropic/claude-opus-4.7`](../models/anthropic/claude-opus-4.7.md) | Opus 4.7 is the next generation of Anthropic's Opus family, built for long-running, asynchronous agents. Building on the coding and… | $5 input / $25 output per 1M tokens |
| [`anthropic/claude-opus-4.8`](../models/anthropic/claude-opus-4.8.md) | Claude Opus 4.8 is Anthropic's most capable generally available model in the Opus family. It supports text, image, and file inputs with… | $5 input / $25 output per 1M tokens |
| [`anthropic/claude-opus-5`](../models/anthropic/claude-opus-5.md) | Claude Opus 5 is the most powerful model in the Claude 5 family from Anthropic. It excels at complex reasoning, analysis, and creative… | $5 input / $25 output per 1M tokens |
| [`anthropic/claude-opus-5.5`](../models/anthropic/claude-opus-5.5.md) | Claude Opus 5.5 is the most powerful model in the Claude 5 family from Anthropic. It excels at complex reasoning, analysis, and creative… | $4 input / $20 output per 1M tokens |
| [`anthropic/claude-sonnet-4.5`](../models/anthropic/claude-sonnet-4.5.md) | Claude Sonnet 4.5 is Anthropic’s most advanced Sonnet model to date, optimized for real-world agents and coding workflows. It delivers… | $3 input / $15 output per 1M tokens |
| [`anthropic/claude-sonnet-4.6`](../models/anthropic/claude-sonnet-4.6.md) | Sonnet 4.6 is Anthropic's most capable Sonnet-class model yet, with frontier performance across coding, agents, and professional work. It… | $3 input / $15 output per 1M tokens |
| [`anthropic/claude-sonnet-5`](../models/anthropic/claude-sonnet-5.md) | Claude Sonnet 5 is a Sonnet-class model for high-quality coding, agentic workflows, reasoning, vision, structured outputs, and tool use. | $2 input / $10 output per 1M tokens |
| [`anthropic/claude-sonnet-5.5`](../models/anthropic/claude-sonnet-5.5.md) | Claude Sonnet 5.5 is Anthropic's Sonnet-class model for well-scoped everyday work, succeeding Claude Sonnet 5 as a direct upgrade. It is… | $2 input / $10 output per 1M tokens |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "anthropic/claude-fable-5"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
