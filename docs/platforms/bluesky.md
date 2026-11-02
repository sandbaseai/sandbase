# Bluesky API: 3 endpoints with pricing and code examples

Call 3 Bluesky endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`bluesky/post`](../models/bluesky/post.md) | Get a single Bluesky post by URL - text, author handle, like, reply, and repost counts as clean JSON. | about $0.0011 per call |
| [`bluesky/profile`](../models/bluesky/profile.md) | Get a Bluesky user's public profile by handle - display name, bio, follower and post counts as clean JSON. | about $0.0011 per call |
| [`bluesky/user-posts`](../models/bluesky/user-posts.md) | List a Bluesky account's recent posts (text, author handle, like, reply, and repost counts) by handle as clean JSON. | about $0.0011 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bluesky/post", "url": "https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
