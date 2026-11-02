# Z-Ai models API: 6 endpoints with pricing and code examples

Call 6 Z-Ai models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`z-ai/glm-4.5-air`](../models/z-ai/glm-4.5-air.md) | GLM-4.5-Air is the lightweight member of Z.ai's GLM-4.5 family, a mixture-of-experts model with 106B total and 12B active parameters built… | $0.2 input / $1.1 output per 1M tokens |
| [`z-ai/glm-5.2`](../models/z-ai/glm-5.2.md) | GLM-5.2 is Z.ai's open-weight flagship text model released in June 2026 for long-horizon tasks, and the first GLM model to deliver that… | $1.4 input / $4.4 output per 1M tokens |
| [`z-ai/glm-5.3`](../models/z-ai/glm-5.3.md) | GLM-5.3 is Z.ai's flagship text model for complex software engineering and long-horizon agent work, built on the same base model as… | $1.4 input / $4.4 output per 1M tokens |
| [`z-ai/glm-5.3-flash`](../models/z-ai/glm-5.3-flash.md) | GLM-5.3-Flash is the first native multimodal model in Z.ai's GLM-5 series, a 320B-parameter mixture-of-experts model with 18B active… | $0.15 input / $0.5 output per 1M tokens |
| [`z-ai/glm-5.3-flashx`](../models/z-ai/glm-5.3-flashx.md) | GLM-5.3-FlashX is the high-speed tier of Z.ai's GLM-5.3-Flash, documented together with Flash and delivering inference speeds of up to 200… | $0.37 input / $1.25 output per 1M tokens |
| [`z-ai/glm-5.5`](../models/z-ai/glm-5.5.md) | GLM 5.5 is listed on SandBase as an upcoming model in Z.ai's GLM series and is not yet available on SandBase. As of early October 2026,… |  |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "z-ai/glm-4.5-air"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
