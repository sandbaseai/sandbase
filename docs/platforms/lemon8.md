# Lemon8 API: 16 endpoints with pricing and code examples

Call 16 Lemon8 endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`lemon8/app/discover-banners`](../models/lemon8/app/discover-banners.md) | Returns the current promotional and featured banners displayed on the Lemon8 discover page. Applications can use this data to inspect… | $0.0015 per call (free daily quota) |
| [`lemon8/app/discover-tab`](../models/lemon8/app/discover-tab.md) | Returns the main content featured on the Lemon8 discover tab. Retrieve trending recommendations and highlighted posts directly from the… | $0.0015 per call (free daily quota) |
| [`lemon8/app/discover-tab-information-tabs`](../models/lemon8/app/discover-tab-information-tabs.md) | Returns the Editor's Picks and discover tab information from the Lemon8 mobile app. Use this endpoint to inspect curated featured… | $0.0015 per call (free daily quota) |
| [`lemon8/app/hot-search-keywords`](../models/lemon8/app/hot-search-keywords.md) | Returns trending search keywords and topics currently popular on Lemon8. Call this endpoint to track real-time user discovery trends… | $0.0015 per call (free daily quota) |
| [`lemon8/app/item-id`](../models/lemon8/app/item-id.md) | Resolves a Lemon8 share URL into its canonical post ID. Accepts both long and short sharing links copied from the web platform or mobile… | $0.0015 per call (free daily quota) |
| [`lemon8/app/item-ids`](../models/lemon8/app/item-ids.md) | Batch resolves Lemon8 post IDs from shared URLs. Accepts an array of share links and returns corresponding post IDs for up to 10 links at… | $0.0015 per call (free daily quota) |
| [`lemon8/app/post-comment-list`](../models/lemon8/app/post-comment-list.md) | Retrieves the list of comments for a specific Lemon8 post. Requires the post item ID, group ID, and media ID with support for paginated… | $0.0015 per call (free daily quota) |
| [`lemon8/app/post-detail`](../models/lemon8/app/post-detail.md) | Returns detailed information for a specified Lemon8 post using its unique post ID. Retrieve post metadata and content metrics by providing… | $0.0015 per call (free daily quota) |
| [`lemon8/app/search`](../models/lemon8/app/search.md) | Search Lemon8 posts and users by keyword: post titles, content, authors, images and engagement, with Top and other tabs, sorting and… | $0.0015 per call (free daily quota) |
| [`lemon8/app/topic-info`](../models/lemon8/app/topic-info.md) | Returns detailed information and background visual assets for a specific Lemon8 topic using its unique forum identifier. | $0.0015 per call (free daily quota) |
| [`lemon8/app/topic-post-list`](../models/lemon8/app/topic-post-list.md) | Returns posts under a specific topic or hashtag on Lemon8. Requires the topic category ID, category parameter, and hashtag name. | $0.0015 per call (free daily quota) |
| [`lemon8/app/user-follower-list`](../models/lemon8/app/user-follower-list.md) | Returns the followers list for a specified Lemon8 user. Accepts a user identifier and an optional pagination cursor to browse through… | $0.0015 per call (free daily quota) |
| [`lemon8/app/user-following-list`](../models/lemon8/app/user-following-list.md) | Returns the list of accounts followed by a specified Lemon8 user. Accepts a user identifier and supports cursor-based pagination for… | $0.0015 per call (free daily quota) |
| [`lemon8/app/user-id`](../models/lemon8/app/user-id.md) | Returns a Lemon8 user ID extracted from a user profile share link. Input supports long or short sharing URLs copied from the web or app. | $0.0015 per call (free daily quota) |
| [`lemon8/app/user-ids`](../models/lemon8/app/user-ids.md) | Resolves Lemon8 user identifiers in batch from shared profile links. Accepts an array of up to 10 share links per request and returns the… | $0.0015 per call (free daily quota) |
| [`lemon8/app/user-profile`](../models/lemon8/app/user-profile.md) | Returns profile information for a specified Lemon8 user. The query requires a unique user identifier. | $0.0015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/discover-banners"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
