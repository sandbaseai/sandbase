# Waveinflu API: 3 endpoints with pricing and code examples

Call 3 Waveinflu endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`waveinflu/creator-search`](../models/waveinflu/creator-search.md) | Finds creators from a natural-language brief instead of a seed account. `platform` and `query` are required; add `limit` (1–100, default… | from $0.004977 to $0.4977 per run, depending on parameters |
| [`waveinflu/email-lookup`](../models/waveinflu/email-lookup.md) | Looks up the contact email for one Instagram, TikTok, or YouTube creator from a profile URL. | $0.001991 per call (free daily quota) |
| [`waveinflu/similar-creators`](../models/waveinflu/similar-creators.md) | Finds creators similar to a seed account on Instagram, TikTok, or YouTube. | from $0.004977 to $0.4977 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "waveinflu/creator-search", "query": "beauty creators in the US"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
