# Xigua API: 6 endpoints with pricing and code examples

Call 6 Xigua endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`xigua/app-v2/one-video`](../models/xigua/app-v2/one-video.md) | Returns lightweight single video data and associated related video information from Xigua for a specific post by its unique item ID. | $0.0015 per call (free daily quota) |
| [`xigua/app-v2/one-video-play-url`](../models/xigua/app-v2/one-video-play-url.md) | Returns the direct playback URL for a specific Xigua video using its unique item identifier. Developers supply the target video ID to… | $0.0015 per call (free daily quota) |
| [`xigua/app-v2/search-video`](../models/xigua/app-v2/search-video.md) | Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and… | $0.0015 per call (free daily quota) |
| [`xigua/app-v2/user-info`](../models/xigua/app-v2/user-info.md) | Returns profile and personal information for a specified Xigua account. Queries details using the target user identifier. | $0.0015 per call (free daily quota) |
| [`xigua/app-v2/user-post-list`](../models/xigua/app-v2/user-post-list.md) | Returns a list of posts from a specific Xigua user account. Supports paginated results using timestamp cursor tokens. | $0.0015 per call (free daily quota) |
| [`xigua/app-v2/video-comment-list`](../models/xigua/app-v2/video-comment-list.md) | Returns comments for a specified Xigua video. Supports paginating through discussion threads using offset and result count parameters. | $0.0015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/one-video", "item_id": "<item_id>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
