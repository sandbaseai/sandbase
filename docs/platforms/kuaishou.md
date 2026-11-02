# Kuaishou API: 40 endpoints with pricing and code examples

Call 40 Kuaishou endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`kuaishou/app/brand-top-list`](../models/kuaishou/app/brand-top-list.md) | Returns top brand rankings and related live stream links from Kuaishou. Allows filtering ranking data by sub-tab category ID or sub-tab… | $0.001 per call (free daily quota) |
| [`kuaishou/app/generate-share-link`](../models/kuaishou/app/generate-share-link.md) | Generates a shareable URL for Kuaishou application content using a specified object identifier. Returns share link details for the target… | $0.001 per call (free daily quota) |
| [`kuaishou/app/hot-board-categories`](../models/kuaishou/app/hot-board-categories.md) | Returns the active list of hot board categories available in the Kuaishou app. Use this endpoint to inspect category identifiers and names… | $0.001 per call (free daily quota) |
| [`kuaishou/app/hot-board-detail`](../models/kuaishou/app/hot-board-detail.md) | Returns trending topics and search keywords from Kuaishou hot boards based on the specified board identifier and board type. | $0.001 per call (free daily quota) |
| [`kuaishou/app/hot-search-person`](../models/kuaishou/app/hot-search-person.md) | Returns the current Kuaishou hot search person board rankings. Delivers real-time trending individuals and popular figures featured across… | $0.001 per call (free daily quota) |
| [`kuaishou/app/live-top-list`](../models/kuaishou/app/live-top-list.md) | Returns ranking information for trending streams on Kuaishou. Accepts optional tab parameters to filter leaderboards by category. | $0.001 per call (free daily quota) |
| [`kuaishou/app/music-ranking`](../models/kuaishou/app/music-ranking.md) | Returns ranked music tracks on Kuaishou, including track IDs, titles, hot counts, and audio URLs. Supports filtering by chart type and… | $0.001 per call (free daily quota) |
| [`kuaishou/app/one-user-v2`](../models/kuaishou/app/one-user-v2.md) | Returns profile details and personal entrance configurations for a specific Kuaishou account using the target user identifier. | $0.01 per call (free daily quota) |
| [`kuaishou/app/one-video`](../models/kuaishou/app/one-video.md) | Returns detailed video metadata for a single Kuaishou video post using its photo identifier. Query by video ID to inspect post attributes. | $0.001 per call (free daily quota) |
| [`kuaishou/app/one-video-by-url`](../models/kuaishou/app/one-video-by-url.md) | Returns video and photo information for a single Kuaishou post using its shared link. Input the full share URL to retrieve media metadata. | $0.001 per call (free daily quota) |
| [`kuaishou/app/search-comprehensive`](../models/kuaishou/app/search-comprehensive.md) | Returns aggregated search feeds across videos and users on Kuaishou, with filtering options for duration, sort order, and release timeframe. | $0.01 per call (free daily quota) |
| [`kuaishou/app/search-image`](../models/kuaishou/app/search-image.md) | Searches Kuaishou image posts matching a specified search term. Returns feed details including captions, engagement metrics, and… | $0.01 per call (free daily quota) |
| [`kuaishou/app/search-live`](../models/kuaishou/app/search-live.md) | Searches Kuaishou livestreams using a specified search term. Returns matching active broadcast rooms with cursor pagination support. | $0.01 per call (free daily quota) |
| [`kuaishou/app/search-music`](../models/kuaishou/app/search-music.md) | Searches for Kuaishou music tracks by song name or artist keyword. Returns matched audio results with support for cursor-based pagination. | $0.01 per call (free daily quota) |
| [`kuaishou/app/search-user-v2`](../models/kuaishou/app/search-user-v2.md) | Searches for Kuaishou accounts matching a query term. Results can be filtered by gender and account relationship status, as well as sorted… | $0.01 per call (free daily quota) |
| [`kuaishou/app/search-video-v2`](../models/kuaishou/app/search-video-v2.md) | Searches for Kuaishou videos matching a designated keyword query. Returns matching video results with support for cursor-based pagination… | $0.01 per call (free daily quota) |
| [`kuaishou/app/selection-feed`](../models/kuaishou/app/selection-feed.md) | Returns the recommended selection feed from the Kuaishou app home page. The endpoint requires no parameters and provides fresh recommended… | $0.001 per call (free daily quota) |
| [`kuaishou/app/shopping-top-list`](../models/kuaishou/app/shopping-top-list.md) | Returns ranked shopping live streams and top product leaderboards from Kuaishou. Filter results by specific sub-tab identifiers or names. | $0.001 per call (free daily quota) |
| [`kuaishou/app/user-hot-post`](../models/kuaishou/app/user-hot-post.md) | Returns popular posts from a specified Kuaishou user profile, including captions and interaction metrics such as comments and collects. | $0.001 per call (free daily quota) |
| [`kuaishou/app/user-live-info`](../models/kuaishou/app/user-live-info.md) | Returns broadcast information and stream status for a specified Kuaishou account. Requests target a creator profile using the unique user… | $0.001 per call (free daily quota) |
| [`kuaishou/app/user-post-v2`](../models/kuaishou/app/user-post-v2.md) | Retrieves a list of video feeds posted by a specific Kuaishou user. Supports sorting by latest or hot posts and cursor-based pagination. | $0.01 per call (free daily quota) |
| [`kuaishou/app/video-comment`](../models/kuaishou/app/video-comment.md) | Returns comment records for a specified Kuaishou video, including author metadata and like counts. Supports pagination using a cursor. | $0.001 per call (free daily quota) |
| [`kuaishou/app/video-sub-comments`](../models/kuaishou/app/video-sub-comments.md) | Returns sub comments and replies under a root comment for a Kuaishou video. Supports pagination using a cursor and page size configuration. | $0.001 per call (free daily quota) |
| [`kuaishou/app/videos-batch`](../models/kuaishou/app/videos-batch.md) | Retrieves video details for multiple Kuaishou posts in a single request. Specify comma-separated photo IDs to look up information for up… | $0.04 per call |
| [`kuaishou/search-user`](../models/kuaishou/search-user.md) | Search public Kuaishou user accounts by keyword with page-number pagination. Use it to discover relevant creators or accounts before… | $0.014286 per call (free daily quota) |
| [`kuaishou/search-video`](../models/kuaishou/search-video.md) | Search public Kuaishou videos by keyword with cursor-based pagination. Use it to discover relevant videos and continue through additional… | $0.014286 per call (free daily quota) |
| [`kuaishou/user-detail`](../models/kuaishou/user-detail.md) | Get the public profile for a Kuaishou user identified by user ID. Use it to inspect an account found through user or video results. | $0.014286 per call (free daily quota) |
| [`kuaishou/user-video-list`](../models/kuaishou/user-video-list.md) | Get public videos published by a Kuaishou user, with optional cursor-based pagination. Use it to review a creator's content history or… | $0.014286 per call (free daily quota) |
| [`kuaishou/web/generate-share-short-url`](../models/kuaishou/web/generate-share-short-url.md) | Returns a shareable short URL for a specified Kuaishou video or photo post. Supply the target post identifier using the photo_id query… | $0.001 per call (free daily quota) |
| [`kuaishou/web/get-user-id`](../models/kuaishou/web/get-user-id.md) | Resolves a Kuaishou user ID from a provided user share link. Useful for extracting internal profile identifiers from public sharing URLs. | $0.001 per call (free daily quota) |
| [`kuaishou/web/hot-list-v1`](../models/kuaishou/web/hot-list-v1.md) | Returns the current trending hot list from Kuaishou Web. It delivers trending topics and popular content rankings directly from the… | $0.001 per call (free daily quota) |
| [`kuaishou/web/hot-list-v2`](../models/kuaishou/web/hot-list-v2.md) | Returns current trending search rankings and hot topics on Kuaishou web. Supports selecting different ranking boards using the board type… | $0.001 per call (free daily quota) |
| [`kuaishou/web/one-video`](../models/kuaishou/web/one-video.md) | Returns detailed metadata for a single Kuaishou video post using shared link content. Note that photo-only posts are not supported. | $0.002 per call (free daily quota) |
| [`kuaishou/web/one-video-by-url`](../models/kuaishou/web/one-video-by-url.md) | Retrieves video manifest data and streaming representation details for a specific Kuaishou post using its web link. Returns media… | $0.002 per call (free daily quota) |
| [`kuaishou/web/one-video-comment`](../models/kuaishou/web/one-video-comment.md) | Returns root comments for a specified Kuaishou video, including author details, content, and like counts. Queries require a video ID and… | $0.002 per call (free daily quota) |
| [`kuaishou/web/one-video-sub-comment`](../models/kuaishou/web/one-video-sub-comment.md) | Returns sub-comments and replies for a specific comment on a Kuaishou video. Requires the video ID and root comment ID with optional… | $0.01 per call (free daily quota) |
| [`kuaishou/web/one-video-v2`](../models/kuaishou/web/one-video-v2.md) | Retrieves video streaming manifests and media details for a specific Kuaishou video using its unique identifier. | $0.002 per call (free daily quota) |
| [`kuaishou/web/user-collect`](../models/kuaishou/web/user-collect.md) | Retrieves the list of collected or favorited items for a specified Kuaishou account. Supports pagination through cursor tokens to browse… | $0.01 per call (free daily quota) |
| [`kuaishou/web/user-info`](../models/kuaishou/web/user-info.md) | Returns public profile information for a specified Kuaishou web user. Supply the target user identifier to retrieve account metadata. | $0.002 per call (free daily quota) |
| [`kuaishou/web/user-live-replay`](../models/kuaishou/web/user-live-replay.md) | Returns recorded stream replay data for a specified Kuaishou user. The endpoint accepts a user identifier and an optional cursor parameter… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/brand-top-list"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
