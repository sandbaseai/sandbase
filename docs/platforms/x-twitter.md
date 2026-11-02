# X (Twitter) API: 11 endpoints with pricing and code examples

Call 11 X (Twitter) endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`twitter/article`](../models/twitter/article.md) | Get a public X long-form article from its wrapper post URL, including its author, engagement, cover image, and structured content blocks. | about $0.00054 per call |
| [`twitter/community`](../models/twitter/community.md) | Fetch a Twitter/X community's public details (name, description, member count, join policy) by URL. | about $0.0001 per call |
| [`twitter/community-tweets`](../models/twitter/community-tweets.md) | List recent tweets posted in a Twitter/X community by URL. | about $0.00045 per call |
| [`twitter/followers`](../models/twitter/followers.md) | Fetch the follower list of any public X (Twitter) account by username with cursor pagination. Limit is a per-page maximum and a native… | about $0.00045 per call |
| [`twitter/following`](../models/twitter/following.md) | List the accounts a public X (Twitter) account follows by username with cursor pagination. Limit is a per-page maximum; follow the… | about $0.00045 per call |
| [`twitter/search-communities`](../models/twitter/search-communities.md) | Search X (Twitter) communities by keyword and get their id, name, topic, and member count with cursor pagination. This is how you find a… | about $0.0011 per call |
| [`twitter/search-users`](../models/twitter/search-users.md) | Search X (Twitter) accounts by keyword - the People tab of X search. Matches handles, display names, and profile bios, and returns… | about $0.00054 per call |
| [`twitter/thread`](../models/twitter/thread.md) | Resolve the linear self-thread containing an X (Twitter) post, from its root through the author's linked continuations. This excludes… | about $0.00269 per call |
| [`twitter/trends`](../models/twitter/trends.md) | Get current X (Twitter) trends for worldwide, a country, or a city in X ranking order, including the resolved location. | about $0.0001 per call |
| [`twitter/tweet`](../models/twitter/tweet.md) | Fetch a single Twitter/X tweet by URL with its full text and engagement counts (likes, retweets, replies, quotes, bookmarks, views). | about $0.00022 per call |
| [`twitter/tweet-transcript`](../models/twitter/tweet-transcript.md) | Extract the spoken transcript from a Twitter/X video tweet by URL. | about $0.0012 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/article", "url": "https://x.com/Decentralisedco/status/1905545699552375179"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
