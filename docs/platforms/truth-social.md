# Truth Social API: 3 endpoints with pricing and code examples

Call 3 Truth Social endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`truth-social/post`](../models/truth-social/post.md) | Get a single Truth Social post by its URL - text, author, engagement (likes, comments, shares), and timestamp as clean JSON. | about $0.0011 per call |
| [`truth-social/profile`](../models/truth-social/profile.md) | Get a Truth Social account's public profile by handle - display name, bio, follower/following counts, and post count as clean JSON. | about $0.0011 per call |
| [`truth-social/user-posts`](../models/truth-social/user-posts.md) | List a Truth Social account's recent posts by handle - text, engagement (likes, comments, shares), and timestamps as clean JSON. | about $0.0012 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "truth-social/post", "url": "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
