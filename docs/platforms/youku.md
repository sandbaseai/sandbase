# Youku API: 3 endpoints with pricing and code examples

Call 3 Youku endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`youku/search-video`](../models/youku/search-video.md) | Search Youku videos by keyword with page-based pagination. Use it to discover videos related to a topic, title, creator, or other search… | $0.013889 per call (free daily quota) |
| [`youku/user-detail`](../models/youku/user-detail.md) | Get a Youku user profile identified by UID. Use it to look up a known account for creator research, profile review, or related video… | $0.013889 per call (free daily quota) |
| [`youku/video-detail`](../models/youku/video-detail.md) | Get details for a Youku video identified by video ID. Use it to look up a known video for content review, cataloging, or subsequent video… | $0.013889 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youku/search-video", "keyword": "电影"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
