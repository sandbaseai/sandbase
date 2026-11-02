# Twitter API: 17 endpoints with pricing and code examples

Call 17 Twitter endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`twitter/post-comments`](../models/twitter/post-comments.md) | Get the latest comments for an X (Twitter) post identified by tweet ID, with cursor pagination. Use it to review recent discussion on a… | $0.014286 per call (free daily quota) |
| [`twitter/post-detail`](../models/twitter/post-detail.md) | Get the full detail of an X (Twitter) post identified by its tweet ID. Use it to inspect a known post after finding it through search, a… | $0.014286 per call (free daily quota) |
| [`twitter/search`](../models/twitter/search.md) | Search X (Twitter) by keyword across top, latest, media, people, or list result modes with cursor pagination. Use it to find public… | $0.014286 per call (free daily quota) |
| [`twitter/user-detail`](../models/twitter/user-detail.md) | Get an X (Twitter) user profile identified by its numeric Rest ID. Use it to review a known account before monitoring its posts or… | $0.014286 per call (free daily quota) |
| [`twitter/user-posts`](../models/twitter/user-posts.md) | Get posts published by an X (Twitter) user identified by Rest ID, with cursor pagination. Use it to browse a known account's timeline or… | $0.014286 per call (free daily quota) |
| [`twitter/web/latest-post-comments`](../models/twitter/web/latest-post-comments.md) | Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results. | $0.001 per call (free daily quota) |
| [`twitter/web/post-comments`](../models/twitter/web/post-comments.md) | Returns comment threads and replies under a specified tweet. Provide a tweet ID and paginate through conversations using cursor values. | $0.001 per call (free daily quota) |
| [`twitter/web/retweet-user-list`](../models/twitter/web/retweet-user-list.md) | Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers. | $0.001 per call (free daily quota) |
| [`twitter/web/search-timeline`](../models/twitter/web/search-timeline.md) | Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).… | $0.001 per call (free daily quota) |
| [`twitter/web/trending`](../models/twitter/web/trending.md) | Get trending topics on Twitter / X by country: trend names with their category context, for the United States, Japan, India, the UK and… | $0.001 per call (free daily quota) |
| [`twitter/web/tweet-detail`](../models/twitter/web/tweet-detail.md) | Get a single tweet (X post) by ID: full text, author, media, and like, retweet, reply, quote, bookmark and view counts. | $0.001 per call (free daily quota) |
| [`twitter/web/user-followers`](../models/twitter/web/user-followers.md) | Retrieves follower profiles for a specified Twitter (X) account, including follower counts and verification statuses. Supports pagination. | $0.001 per call (free daily quota) |
| [`twitter/web/user-followings`](../models/twitter/web/user-followings.md) | Returns a list of accounts followed by a specified Twitter (X) user. Results provide follower counts, friend counts, media statistics, and… | $0.001 per call (free daily quota) |
| [`twitter/web/user-media`](../models/twitter/web/user-media.md) | Returns media posts and timeline items for a specified user profile, queried by screen name or user ID. Supports cursor-based pagination… | $0.001 per call (free daily quota) |
| [`twitter/web/user-post-tweet`](../models/twitter/web/user-post-tweet.md) | Returns posts and tweets from a specified Twitter (X) user timeline. Users can be identified by either their screen name or numeric user… | $0.001 per call (free daily quota) |
| [`twitter/web/user-profile`](../models/twitter/web/user-profile.md) | Get a Twitter / X user profile by screen name or user ID: name, bio, follower and following counts, post and media counts, verification… | $0.001 per call (free daily quota) |
| [`twitter/web/user-tweet-replies`](../models/twitter/web/user-tweet-replies.md) | Returns a timeline of replies posted by a specific Twitter user. Filter by username and paginate through responses using cursor tokens. | $0.001 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/post-comments", "tweetId": "1585341984679469056"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
