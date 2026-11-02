# stability-ai models API: 2 endpoints with pricing and code examples

Call 2 stability-ai models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`stability-ai/stable-audio/3/medium/text-to-audio`](../models/stability-ai/stable-audio/3/medium/text-to-audio.md) | Stable Audio 3 Medium by Stability AI generates music, ambience and sound design up to about 6 minutes from a text prompt. | $0.0376 per call |
| [`stability-ai/stable-audio/3/small/music/text-to-audio`](../models/stability-ai/stable-audio/3/small/music/text-to-audio.md) | Stable Audio 3 Small Music by Stability AI is a fast, low-cost music generator producing tracks up to 2 minutes from a text prompt. | $0.0217 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "stability-ai/stable-audio/3/medium/text-to-audio", "duration": 10, "prompt": "calm lo-fi piano loop"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
