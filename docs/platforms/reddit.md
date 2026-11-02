# Reddit API: 35 endpoints with pricing and code examples

Call 35 Reddit endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`reddit/app/check-subreddit-muted`](../models/reddit/app/check-subreddit-muted.md) | Checks whether a specified Reddit subreddit is muted by the current account using its ID. Supports an optional flag to format the returned… | $0.0015 per call (free daily quota) |
| [`reddit/app/comment-replies`](../models/reddit/app/comment-replies.md) | Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor. Supports custom sorting methods and data… | $0.0015 per call (free daily quota) |
| [`reddit/app/community-highlights`](../models/reddit/app/community-highlights.md) | Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID. Supports… | $0.0015 per call (free daily quota) |
| [`reddit/app/dynamic-search`](../models/reddit/app/dynamic-search.md) | Search Reddit posts, communities, comments, media and users with the Reddit app search. Sort by relevance, hot, top, new or comments and… | $0.0015 per call (free daily quota) |
| [`reddit/app/games-feed`](../models/reddit/app/games-feed.md) | Returns recommended gaming posts from Reddit app feeds. Supports filtering by sorting method and time range, with optional response… | $0.0015 per call (free daily quota) |
| [`reddit/app/home-feed`](../models/reddit/app/home-feed.md) | Returns Reddit mobile app home feed content including post metadata, author details, scores, and media links. Supports sorting methods,… | $0.0015 per call (free daily quota) |
| [`reddit/app/news-feed`](../models/reddit/app/news-feed.md) | Returns news-related recommended content from the Reddit app, including current affairs discussions, with optional subtopic filtering and… | $0.0015 per call (free daily quota) |
| [`reddit/app/popular-feed`](../models/reddit/app/popular-feed.md) | Returns trending and popular posts across Reddit with engagement metrics, subreddit details, and media metadata. Supports sorting and time… | $0.0015 per call (free daily quota) |
| [`reddit/app/post-comments`](../models/reddit/app/post-comments.md) | Returns comment trees for a specific Reddit post by its ID. Supports comment sorting by hot, new, top, best, or controversial, with… | $0.0015 per call (free daily quota) |
| [`reddit/app/post-details`](../models/reddit/app/post-details.md) | Returns detailed metadata for a Reddit post by ID, including engagement metrics, author info, and subreddit data. Supports optional… | $0.0015 per call (free daily quota) |
| [`reddit/app/post-details-batch`](../models/reddit/app/post-details-batch.md) | Returns detailed post data for up to five Reddit posts specified by ID. Supports optional comment context and structured data formatting. | $0.0075 per call (free daily quota) |
| [`reddit/app/post-details-batch-large`](../models/reddit/app/post-details-batch-large.md) | Returns details for up to 30 Reddit posts in a single request using comma-separated post IDs. Supports optional comment context and… | $0.0375 per call |
| [`reddit/app/search-typeahead`](../models/reddit/app/search-typeahead.md) | Returns autocomplete suggestions for the Reddit search box based on typed input. Includes options to toggle adult content, apply safe… | $0.0015 per call (free daily quota) |
| [`reddit/app/subreddit-feed`](../models/reddit/app/subreddit-feed.md) | Returns the post stream for a specified subreddit. Supports sorting methods, cursor pagination, and filters to exclude specific post IDs. | $0.0015 per call (free daily quota) |
| [`reddit/app/subreddit-info`](../models/reddit/app/subreddit-info.md) | Returns detailed metadata for a Reddit subreddit, such as rules, descriptions, and app installations. Look up data by subreddit name with… | $0.0015 per call (free daily quota) |
| [`reddit/app/subreddit-post-channels`](../models/reddit/app/subreddit-post-channels.md) | Returns post channel and flair details for a target subreddit. Supports custom sort methods and time range filters. | $0.0015 per call (free daily quota) |
| [`reddit/app/subreddit-settings`](../models/reddit/app/subreddit-settings.md) | Returns settings and configuration details for a specified Reddit subreddit, including posting rules, flair settings, and moderation… | $0.0015 per call (free daily quota) |
| [`reddit/app/subreddit-style`](../models/reddit/app/subreddit-style.md) | Returns rules, styling details, and moderator information for a designated Reddit subreddit. Accepts the subreddit name and an optional… | $0.0015 per call (free daily quota) |
| [`reddit/app/trending-searches`](../models/reddit/app/trending-searches.md) | Returns currently trending search queries and topics from the Reddit mobile application, with an option to clean and format the output data. | $0.0015 per call (free daily quota) |
| [`reddit/app/user-active-subreddits`](../models/reddit/app/user-active-subreddits.md) | Returns a list of Reddit communities where a specified user participates most actively. Supports optional response formatting. | $0.0015 per call (free daily quota) |
| [`reddit/app/user-comments`](../models/reddit/app/user-comments.md) | Returns a list of comments submitted by a specified Reddit user. Supports multiple sorting options, customizable page sizes, and… | $0.0015 per call (free daily quota) |
| [`reddit/app/user-posts`](../models/reddit/app/user-posts.md) | Returns a list of posts submitted by a specified Reddit user. Results can be sorted by new, top, hot, or controversial order with optional… | $0.0015 per call (free daily quota) |
| [`reddit/app/user-profile`](../models/reddit/app/user-profile.md) | Returns detailed profile information for a specified Reddit app user by username. Supports an optional flag to clean and format the output… | $0.0015 per call (free daily quota) |
| [`reddit/app/user-trophies`](../models/reddit/app/user-trophies.md) | Returns a list of public trophies and achievements for a specified Reddit account. Users can supply a username and optionally request… | $0.0015 per call (free daily quota) |
| [`reddit/post`](../models/reddit/post.md) | Fetch a single Reddit post by URL, including its full body text, score, comment count, upvote ratio, and subreddit, as normalized JSON. | about $0.0005 per call |
| [`reddit/post-comments`](../models/reddit/post-comments.md) | List the comments on a Reddit post by URL (author, body, score, timestamp, parent comment). Replies carry the parentId of the comment they… | about $0.0006 per call |
| [`reddit/post-transcript`](../models/reddit/post-transcript.md) | Extract the spoken transcript from a Reddit video post by URL. | about $0.0012 per call |
| [`reddit/profile`](../models/reddit/profile.md) | Fetch a Reddit user's public profile (karma split, post and comment counts, bio, avatar, account age) by username. | about $0.0008 per call |
| [`reddit/search`](../models/reddit/search.md) | Search Reddit posts by keyword with an optional continuation token. Use it to discover topic-related discussions or continue through… | $0.013889 per call (free daily quota) |
| [`reddit/subreddit-details`](../models/reddit/subreddit-details.md) | Fetch a subreddit's metadata (weekly active users, description, and category). | about $0.00038 per call |
| [`reddit/subreddit-posts`](../models/reddit/subreddit-posts.md) | Fetch posts from a subreddit listing (hot, new, or top). | about $0.00038 per call |
| [`reddit/subreddit-search`](../models/reddit/subreddit-search.md) | Search posts within a single subreddit by query, sort, and timeframe. | about $0.00035 per call |
| [`reddit/trending-posts`](../models/reddit/trending-posts.md) | Get currently trending Reddit posts across all subreddits with stable cursor pagination. | about $0.0003 per call |
| [`reddit/user-comments`](../models/reddit/user-comments.md) | List a Reddit user's comments by username, sorted by new, top, hot, or controversial, with the parent post title and subreddit on every… | about $0.0006 per call |
| [`reddit/user-posts`](../models/reddit/user-posts.md) | List a Reddit user's posts by username, sorted by new, top, hot, or controversial, with cursor pagination. | about $0.00038 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/check-subreddit-muted", "subreddit_id": "<subreddit_id>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
