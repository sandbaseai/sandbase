# Threads API: 9 endpoints with pricing and code examples

Call 9 Threads endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`threads/web/post-detail`](../models/threads/web/post-detail.md) | Returns detailed information for a specific Threads post using its numeric ID. Call this endpoint to inspect post content and metadata… | $0.003 per call (free daily quota) |
| [`threads/web/post-detail-v2`](../models/threads/web/post-detail-v2.md) | Returns detailed information for a specific Threads post. Queries can be performed using either a full post link or a post short code as… | $0.003 per call (free daily quota) |
| [`threads/web/search-profiles`](../models/threads/web/search-profiles.md) | Searches Threads user profiles based on a specified text query string. Returns matching user accounts and profile information from the… | $0.003 per call (free daily quota) |
| [`threads/web/search-recent`](../models/threads/web/search-recent.md) | Searches recent Threads content matching a specified keyword query. Returns matching web posts with cursor-based pagination support. | $0.003 per call (free daily quota) |
| [`threads/web/user-info`](../models/threads/web/user-info.md) | Get a Threads (Meta) user profile by username: name, bio, follower count and verification status. | $0.003 per call (free daily quota) |
| [`threads/web/user-info-by-id`](../models/threads/web/user-info-by-id.md) | Returns detailed Threads user profile information based on a specified user ID. Ideal for retrieving public account metadata directly… | $0.003 per call (free daily quota) |
| [`threads/web/user-posts`](../models/threads/web/user-posts.md) | Returns a list of posts from a specified Threads account. Accepts a user identifier and an optional pagination cursor to retrieve… | $0.003 per call (free daily quota) |
| [`threads/web/user-replies`](../models/threads/web/user-replies.md) | Returns a list of replies posted by a specific Threads user. Query replies using a target user identifier and an optional pagination cursor. | $0.003 per call (free daily quota) |
| [`threads/web/user-reposts`](../models/threads/web/user-reposts.md) | Returns a list of reposted threads for a specified Threads user account. Requires the user ID and supports pagination via an optional… | $0.003 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/post-detail", "post_id": "3349029093483693129"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
