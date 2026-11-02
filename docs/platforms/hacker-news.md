# Hacker News API: 4 endpoints with pricing and code examples

Call 4 Hacker News endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`hacker-news/profile`](../models/hacker-news/profile.md) | Get a Hacker News user's public profile by username - karma, bio, and account details as clean JSON. | about $0.0015 per call |
| [`hacker-news/search`](../models/hacker-news/search.md) | Search Hacker News by keyword - matching stories with title, link, author, points, and comment count as clean JSON. | about $0.0015 per call |
| [`hacker-news/story`](../models/hacker-news/story.md) | Get a Hacker News story by id - title, link, author, points, and comment count as clean JSON. | about $0.0015 per call |
| [`hacker-news/story-comments`](../models/hacker-news/story-comments.md) | List the comments on a Hacker News story by id - text, author, and timestamp as clean JSON. | about $0.0015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hacker-news/profile", "handle": "pg"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
