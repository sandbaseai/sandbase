# Bilibili API: 46 endpoints with pricing and code examples

Call 46 Bilibili endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`bilibili/app/bangumi-tab`](../models/bilibili/app/bangumi-tab.md) | Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients. | $0.001 per call (free daily quota) |
| [`bilibili/app/cinema-tab`](../models/bilibili/app/cinema-tab.md) | Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring… | $0.001 per call (free daily quota) |
| [`bilibili/app/home-feed`](../models/bilibili/app/home-feed.md) | Returns recommended video items from the Bilibili app home feed. Supports pagination via timestamp index and pull-to-refresh controls. | $0.001 per call (free daily quota) |
| [`bilibili/app/one-video`](../models/bilibili/app/one-video.md) | Returns detailed video metadata for a specific Bilibili video. Looks up video information using either an AV ID or a BV ID. | $0.001 per call (free daily quota) |
| [`bilibili/app/popular-feed`](../models/bilibili/app/popular-feed.md) | Retrieves popular video feed items from the Bilibili app. Supports pagination through page index and previous video identifiers. | $0.001 per call (free daily quota) |
| [`bilibili/app/search-all`](../models/bilibili/app/search-all.md) | Returns comprehensive search results across Bilibili content via the mobile app interface. Filters results by search keyword, sorting… | $0.001 per call (free daily quota) |
| [`bilibili/app/search-by-type`](../models/bilibili/app/search-by-type.md) | Returns categorized search results from Bilibili based on a target query string. Supports filtering by search type, adjusting sort order,… | $0.001 per call (free daily quota) |
| [`bilibili/app/user-info`](../models/bilibili/app/user-info.md) | Returns account profile details and uploaded video archives for a specified Bilibili creator using their unique user identifier. | $0.001 per call (free daily quota) |
| [`bilibili/app/user-videos`](../models/bilibili/app/user-videos.md) | Returns uploaded video listings for a specified Bilibili creator account. Supports pagination controls and filtering by post types such as… | $0.001 per call (free daily quota) |
| [`bilibili/app/video-comments`](../models/bilibili/app/video-comments.md) | Returns user comments for a specified Bilibili video by AV or BV identifier. Supports sorting comments by popularity or post time, with… | $0.001 per call (free daily quota) |
| [`bilibili/search-video`](../models/bilibili/search-video.md) | Search Bilibili videos by keyword with page-based pagination and sorting by general ranking, play count, publish time, danmaku count, or… | $0.014286 per call (free daily quota) |
| [`bilibili/user-detail`](../models/bilibili/user-detail.md) | Get a Bilibili user profile identified by UID. Use it to look up a known account for creator research, profile review, or subsequent… | $0.014286 per call (free daily quota) |
| [`bilibili/user-video-list`](../models/bilibili/user-video-list.md) | Get videos published by a Bilibili user identified by UID, with an optional continuation parameter from a prior response. Use it to browse… | $0.014286 per call (free daily quota) |
| [`bilibili/video-caption`](../models/bilibili/video-caption.md) | Get caption data for a Bilibili video segment identified by BVID, AID, and CID. Use it to obtain subtitles for transcript extraction,… | $0.014286 per call (free daily quota) |
| [`bilibili/video-comment`](../models/bilibili/video-comment.md) | Get comments for a Bilibili video identified by AID, with optional cursor pagination. Use it to review audience discussion, continue… | $0.014286 per call (free daily quota) |
| [`bilibili/video-danmu`](../models/bilibili/video-danmu.md) | Get one page of danmaku comments for a Bilibili video segment identified by AID and CID. Use it to review time-synchronized audience… | $0.014286 per call (free daily quota) |
| [`bilibili/video-detail`](../models/bilibili/video-detail.md) | Get details for a Bilibili video identified by its BVID. Use it to look up a known video for content review, cataloging, or subsequent… | $0.014286 per call (free daily quota) |
| [`bilibili/web/all-live-areas`](../models/bilibili/web/all-live-areas.md) | Returns the complete list of streaming broadcast areas and categories on Bilibili. This endpoint provides category identifiers and… | $0.001 per call (free daily quota) |
| [`bilibili/web/bv-to-aid`](../models/bilibili/web/bv-to-aid.md) | Converts a Bilibili BV identifier to its corresponding numeric AID value. Input the target video BV string to return the legacy video… | $0.001 per call (free daily quota) |
| [`bilibili/web/collect-folders`](../models/bilibili/web/collect-folders.md) | Returns the collection folders owned by a specific Bilibili user. Supply the user identifier via `uid` to inspect their public collection… | $0.001 per call (free daily quota) |
| [`bilibili/web/com-popular`](../models/bilibili/web/com-popular.md) | Returns a comprehensive list of trending videos on Bilibili, including video metadata, author details, and engagement statistics across… | $0.001 per call (free daily quota) |
| [`bilibili/web/comment-reply`](../models/bilibili/web/comment-reply.md) | Returns replies to a specific comment on a Bilibili video by video ID and comment ID. Supports pagination to browse threaded discussion… | $0.001 per call (free daily quota) |
| [`bilibili/web/dynamic-detail`](../models/bilibili/web/dynamic-detail.md) | Returns detailed information for a specified Bilibili dynamic post, such as image, text, or article dynamics, using its unique dynamic ID. | $0.001 per call (free daily quota) |
| [`bilibili/web/dynamic-detail-v2`](../models/bilibili/web/dynamic-detail-v2.md) | Returns detailed data for a specific Bilibili dynamic post using its dynamic ID. Designed for video dynamics, providing author modules and… | $0.001 per call (free daily quota) |
| [`bilibili/web/general-search`](../models/bilibili/web/general-search.md) | Returns search results from Bilibili based on a search keyword, with sorting options and filters for duration and publication date range. | $0.001 per call (free daily quota) |
| [`bilibili/web/get-user-id`](../models/bilibili/web/get-user-id.md) | Extracts and returns a Bilibili user ID from a provided space share link. Takes a user profile URL and resolves the numeric account… | $0.001 per call (free daily quota) |
| [`bilibili/web/hot-search`](../models/bilibili/web/hot-search.md) | Returns current trending search keywords along with their heat scores from Bilibili. Results are restricted according to the specified… | $0.001 per call (free daily quota) |
| [`bilibili/web/live-room-detail`](../models/bilibili/web/live-room-detail.md) | Returns detailed metadata and status information for a specified Bilibili live broadcast room based on the provided room identifier. | $0.001 per call (free daily quota) |
| [`bilibili/web/live-videos`](../models/bilibili/web/live-videos.md) | Returns stream URLs and playback connection details for a specific Bilibili broadcast room. Filter using the unique room identifier. | $0.001 per call (free daily quota) |
| [`bilibili/web/one-video`](../models/bilibili/web/one-video.md) | Returns detailed metadata and honor tags for a single Bilibili video based on its unique BV identifier, including recommendation status. | $0.001 per call (free daily quota) |
| [`bilibili/web/one-video-v2`](../models/bilibili/web/one-video-v2.md) | Returns detailed metadata and playback information for a specific Bilibili video using its unique video and CID identifiers. | $0.002 per call (free daily quota) |
| [`bilibili/web/one-video-v3`](../models/bilibili/web/one-video-v3.md) | Returns detailed metadata for a single Bilibili video, including season information, episode titles, duration, and post timestamps via its… | $0.001 per call (free daily quota) |
| [`bilibili/web/user-collection-videos`](../models/bilibili/web/user-collection-videos.md) | Returns video data stored within a specified collection folder on Bilibili. Supports pagination to browse through items in the folder. | $0.001 per call (free daily quota) |
| [`bilibili/web/user-dynamic`](../models/bilibili/web/user-dynamic.md) | Retrieves dynamic feed posts and timeline updates for a specified Bilibili user by UID, with optional offset-based pagination. | $0.001 per call (free daily quota) |
| [`bilibili/web/user-post-videos`](../models/bilibili/web/user-post-videos.md) | Returns videos posted on a Bilibili user's homepage. Query by user identifier with options to control sorting order and page number. | $0.001 per call (free daily quota) |
| [`bilibili/web/user-post-videos-v2`](../models/bilibili/web/user-post-videos-v2.md) | Get user homepage video data V2 on Bilibili. Returns the platform data as structured JSON. | $0.001 per call (free daily quota) |
| [`bilibili/web/user-profile`](../models/bilibili/web/user-profile.md) | Returns profile details and charging sponsor information for a specified Bilibili account based on the provided user UID. | $0.001 per call (free daily quota) |
| [`bilibili/web/user-relation-stat`](../models/bilibili/web/user-relation-stat.md) | Returns relationship statistics, including following and follower counts, for a specified Bilibili account using their user ID. | $0.001 per call (free daily quota) |
| [`bilibili/web/user-up-stat`](../models/bilibili/web/user-up-stat.md) | Returns total video view and like counts for a specified Bilibili creator account. Lookup requires the user unique identifier. | $0.001 per call (free daily quota) |
| [`bilibili/web/video-comments`](../models/bilibili/web/video-comments.md) | Returns comment threads and reply metadata for a specific Bilibili video. Query by video ID with optional page numbering. | $0.001 per call (free daily quota) |
| [`bilibili/web/video-danmaku`](../models/bilibili/web/video-danmaku.md) | Returns timed on-screen danmaku comments for a specified Bilibili video in XML format using the video content identifier (cid). | $0.001 per call (free daily quota) |
| [`bilibili/web/video-detail`](../models/bilibili/web/video-detail.md) | Returns detailed metadata, season sections, and episode listings for a specific Bilibili video using its unique video identifier. | $0.001 per call (free daily quota) |
| [`bilibili/web/video-parts`](../models/bilibili/web/video-parts.md) | Returns video part details for a specified Bilibili video using its video ID. The response includes the duration and creation timestamp… | $0.001 per call (free daily quota) |
| [`bilibili/web/video-play-info`](../models/bilibili/web/video-play-info.md) | Returns playback stream information, including video stream URLs, MIME types, and frame rates, for a single Bilibili video URL. | $0.001 per call (free daily quota) |
| [`bilibili/web/video-playurl`](../models/bilibili/web/video-playurl.md) | Returns video playback stream URLs and DASH metadata for a specified Bilibili video. Requires both the video identifier and the content… | $0.001 per call (free daily quota) |
| [`bilibili/web/video-subtitle`](../models/bilibili/web/video-subtitle.md) | Returns subtitle data for a specified Bilibili video based on its video ID and CID. Helps retrieve available caption tracks and related… | $0.001 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/bangumi-tab"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
