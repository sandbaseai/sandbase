# SoundCloud API: 1 endpoints with pricing and code examples

Call 1 SoundCloud endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`soundcloud/track`](../models/soundcloud/track.md) | Get a SoundCloud track by artist and track slug with title, duration, plays, likes, reposts, comments, genre, artwork and upload date. | $0.00015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "soundcloud/track", "artist": "forss", "track": "flickermood"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
