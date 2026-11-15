# Twitch API: 3 endpoints with pricing and code examples

Call 3 Twitch endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`twitch/live-streams`](../models/twitch/live-streams.md) | Get currently live streams, optionally filtered by game/category. Returns streams sorted by relevance or viewer count with broadcaster… | $0.03 per call |
| [`twitch/search-streamers`](../models/twitch/search-streamers.md) | Search for Twitch channels/streamers by query. Returns matching channels with live status, follower counts, and current stream info.… | $0.03 per call |
| [`twitch/streamer-profile`](../models/twitch/streamer-profile.md) | Get detailed profile information for a Twitch streamer including followers, description, partner status, social links, and current live… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitch/live-streams"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
