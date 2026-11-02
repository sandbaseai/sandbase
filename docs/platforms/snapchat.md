# Snapchat API: 1 endpoints with pricing and code examples

Call 1 Snapchat endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`snapchat/profile`](../models/snapchat/profile.md) | Fetch a Snapchat user's public profile by username: display name, bio, subscriber count, and recent public content. | about $0.0011 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "snapchat/profile", "username": "nasa"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
