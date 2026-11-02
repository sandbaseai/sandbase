# Toutiao API: 8 endpoints with pricing and code examples

Call 8 Toutiao endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`toutiao/app/article-info`](../models/toutiao/app/article-info.md) | Returns details and interface settings for a specified Toutiao post. Provide the post ID to inspect article properties and action settings. | $0.0015 per call (free daily quota) |
| [`toutiao/app/comments`](../models/toutiao/app/comments.md) | Returns user comments and interaction metrics for a specific Toutiao post. Results can be paginated through comment batches using an… | $0.0015 per call (free daily quota) |
| [`toutiao/app/user-id`](../models/toutiao/app/user-id.md) | Resolves a Toutiao user profile URL into numeric and secure user identifiers. Returns the user ID and sec_user_id associated with the… | $0.0015 per call (free daily quota) |
| [`toutiao/app/user-info`](../models/toutiao/app/user-info.md) | Get a Toutiao (Jinri Toutiao) user profile by user ID: name, bio, avatar, follower, following and like counts, and content tabs. | $0.0015 per call (free daily quota) |
| [`toutiao/app/video-info`](../models/toutiao/app/video-info.md) | Returns detailed information for a specified Toutiao video using its post identifier. Useful for retrieving metadata and content status… | $0.0015 per call (free daily quota) |
| [`toutiao/search`](../models/toutiao/search.md) | Search Toutiao web articles by keyword. Use it to discover relevant articles for topic research, media monitoring, or source collection. | $0.069444 per call |
| [`toutiao/web/article-info`](../models/toutiao/web/article-info.md) | Returns detailed post information and interface action settings for a specified Toutiao article based on its unique post identifier. | $0.0015 per call (free daily quota) |
| [`toutiao/web/video-info`](../models/toutiao/web/video-info.md) | Returns detailed information for a specified Toutiao video post. Retrieve post metadata and related video attributes using a valid post… | $0.0015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/app/article-info", "group_id": "7450114952884503059"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
