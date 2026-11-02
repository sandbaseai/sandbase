# Pipixia API: 17 endpoints with pricing and code examples

Call 17 Pipixia endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`pipixia/app/hashtag-detail`](../models/pipixia/app/hashtag-detail.md) | Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier. | $0.0015 per call (free daily quota) |
| [`pipixia/app/hashtag-post-list`](../models/pipixia/app/hashtag-post-list.md) | Returns a list of posts associated with a specific hashtag on Pipixia. Filter by hashtag identifier, sort options, and paginate through… | $0.0015 per call (free daily quota) |
| [`pipixia/app/home-feed`](../models/pipixia/app/home-feed.md) | Returns recommended posts from the Pipixia home feed. Supports cursor-based pagination to browse subsequent pages of feed items. | $0.0015 per call (free daily quota) |
| [`pipixia/app/home-short-drama-feed`](../models/pipixia/app/home-short-drama-feed.md) | Returns short drama and novel recommendations from the Pipixia home feed. Supports pagination to browse through items sequentially. | $0.0015 per call (free daily quota) |
| [`pipixia/app/hot-search-board-detail`](../models/pipixia/app/hot-search-board-detail.md) | Returns detailed items from a Pipixia hot search board, including item identifiers, like metrics, and highlighted comments for a specified… | $0.0015 per call (free daily quota) |
| [`pipixia/app/hot-search-board-list`](../models/pipixia/app/hot-search-board-list.md) | Get the Pipixia hot search boards: trending posts with daily likes and top comments. | $0.0015 per call (free daily quota) |
| [`pipixia/app/hot-search-words`](../models/pipixia/app/hot-search-words.md) | Returns the current list of trending search keywords from Pipixia. Helps track popular search topics and user query trends across the… | $0.0015 per call (free daily quota) |
| [`pipixia/app/increase-post-view-count`](../models/pipixia/app/increase-post-view-count.md) | Registers an increment for a Pipixia post view count using the specified cell ID. Returns a status code along with a response timestamp. | $0.0015 per call (free daily quota) |
| [`pipixia/app/post-comment-list`](../models/pipixia/app/post-comment-list.md) | Returns comments for a Pipixia post using its video identifier. Supports cursor-based pagination and cell type filtering to browse feedback. | $0.0015 per call (free daily quota) |
| [`pipixia/app/post-detail`](../models/pipixia/app/post-detail.md) | Returns detailed data for a Pipixia post, including video and photo content, using a specific post identifier and optional post type. | $0.0015 per call (free daily quota) |
| [`pipixia/app/post-statistics`](../models/pipixia/app/post-statistics.md) | Returns engagement metrics and statistics for a single Pipixia post using its identifier. Includes figures such as likes, comments, and… | $0.0015 per call (free daily quota) |
| [`pipixia/app/search`](../models/pipixia/app/search.md) | Search Pipixia (ByteDance humor community) by keyword across posts, videos, images, users and hashtags. | $0.0015 per call (free daily quota) |
| [`pipixia/app/short-url`](../models/pipixia/app/short-url.md) | Returns a shortened link for a specified web address. Takes an original web link as input and converts it into a Pipixia-compatible short… | $0.0015 per call (free daily quota) |
| [`pipixia/app/user-follower-list`](../models/pipixia/app/user-follower-list.md) | Returns a list of followers for a specified Pipixia user account. Supports pagination through cursor tokens to navigate subsequent pages. | $0.0015 per call (free daily quota) |
| [`pipixia/app/user-following-list`](../models/pipixia/app/user-following-list.md) | Retrieves the list of accounts followed by a specified Pipixia user. Returns profile summaries and engagement statistics with cursor… | $0.0015 per call (free daily quota) |
| [`pipixia/app/user-info`](../models/pipixia/app/user-info.md) | Retrieves public profile details for a Pipixia user, including avatar image URLs. Takes a user identifier obtained from a share link. | $0.0015 per call (free daily quota) |
| [`pipixia/app/user-post-list`](../models/pipixia/app/user-post-list.md) | Returns a list of posts, including videos and photos, for a specified user profile. Supports pagination via cursor and feed count… | $0.0015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/hashtag-detail", "hashtag_id": "129559"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
