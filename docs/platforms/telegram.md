# Telegram API: 7 endpoints with pricing and code examples

Call 7 Telegram endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`telegram/web/batch-channel-info`](../models/telegram/web/batch-channel-info.md) | Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once. | $0.012 per call (free daily quota) |
| [`telegram/web/channel-info`](../models/telegram/web/channel-info.md) | Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview. | $0.0015 per call (free daily quota) |
| [`telegram/web/channel-posts`](../models/telegram/web/channel-posts.md) | Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor… | $0.0015 per call (free daily quota) |
| [`telegram/web/channel-search`](../models/telegram/web/channel-search.md) | Returns messages matching a search keyword from a specific Telegram channel. Filter results using channel username, query term, and result… | $0.0015 per call (free daily quota) |
| [`telegram/web/post-comments`](../models/telegram/web/post-comments.md) | Returns comments from the linked discussion group of a specified Telegram channel post. Filters include the channel username, post ID, and… | $0.0015 per call (free daily quota) |
| [`telegram/web/post-detail`](../models/telegram/web/post-detail.md) | Retrieves details for a single public Telegram channel post parsed from the web embed view. Provide the channel username and post ID to… | $0.0015 per call (free daily quota) |
| [`telegram/web/similar-channels`](../models/telegram/web/similar-channels.md) | Returns Telegram's official similar channel recommendations based on a specified channel username for channel discovery and audience… | $0.0015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "telegram/web/batch-channel-info", "channels": "telegram"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
