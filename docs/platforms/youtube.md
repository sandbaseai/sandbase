# YouTube API: 54 endpoints with pricing and code examples

Call 54 YouTube endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`youtube/channel`](../models/youtube/channel.md) | Fetch a YouTube channel's stats (subscribers, video count, total views, description) and the links on its About page, by handle or channel… | about $0.00045 per call |
| [`youtube/channel-community-posts`](../models/youtube/channel-community-posts.md) | List a YouTube channel's community posts by handle or channel ID with cursor pagination (text, likes, image, publish time). | about $0.0012 per call |
| [`youtube/channel-lives`](../models/youtube/channel-lives.md) | List a YouTube channel's live and past-live streams by handle or channel ID with cursor pagination (title, views, length, publish time). | about $0.0012 per call |
| [`youtube/channel-playlists`](../models/youtube/channel-playlists.md) | List a YouTube channel's playlists by handle or channel ID with cursor pagination (title, video count, thumbnail). | about $0.0012 per call |
| [`youtube/channel-shorts`](../models/youtube/channel-shorts.md) | Get public Shorts from a YouTube channel ID with optional continuation-token pagination. Use it to browse a channel's short-form videos… | $0.013889 per call (free daily quota) |
| [`youtube/channel-videos`](../models/youtube/channel-videos.md) | Get public videos from a YouTube channel, with optional cursor-based pagination. Use it to browse a channel's uploads and continue through… | $0.013889 per call (free daily quota) |
| [`youtube/comment-replies`](../models/youtube/comment-replies.md) | List replies to a YouTube comment using a continuation token with cursor pagination (text, author, likes, publish time). | about $0.0012 per call |
| [`youtube/community-post`](../models/youtube/community-post.md) | Fetch a single YouTube community post by URL (text, images, channel, publish time). | about $0.0012 per call |
| [`youtube/playlist`](../models/youtube/playlist.md) | List every video in a YouTube playlist (title, length, and channel per video plus playlist owner and totals). | about $0.0012 per call |
| [`youtube/search`](../models/youtube/search.md) | Search YouTube and get matching videos (title, channel, views, length, publish time) as normalized JSON. | about $0.0005 per call |
| [`youtube/search-hashtag`](../models/youtube/search-hashtag.md) | Search YouTube videos by hashtag with cursor pagination (title, channel, views, length, publish time). | about $0.0012 per call |
| [`youtube/search-shorts`](../models/youtube/search-shorts.md) | Search YouTube Shorts by keyword and get matching Shorts (title, views, URL) with cursor pagination as normalized JSON. | about $0.0012 per call |
| [`youtube/trending-shorts`](../models/youtube/trending-shorts.md) | List currently trending YouTube Shorts (title, channel, views, likes, duration). | about $0.0012 per call |
| [`youtube/video`](../models/youtube/video.md) | Fetch a YouTube video or Short's metadata (title, channel, views, likes, duration, publish date) by URL or ID. | about $0.0008 per call |
| [`youtube/video-captions`](../models/youtube/video-captions.md) | Get available caption tracks for a YouTube video or request captions in SRT, XML, JSON3, or plain-text format. Use it to support… | $0.013889 per call (free daily quota) |
| [`youtube/video-comment`](../models/youtube/video-comment.md) | Get first-level comments for a YouTube video with sorting, locale options, and cursor pagination. Use it to review audience discussion or… | $0.013889 per call (free daily quota) |
| [`youtube/video-comments`](../models/youtube/video-comments.md) | List the comments on a YouTube video or Short by URL with cursor pagination (text, author, likes, reply count). | about $0.0008 per call |
| [`youtube/video-detail`](../models/youtube/video-detail.md) | Get public details for a YouTube video identified by video ID. Use it to inspect a known video before further content or comment analysis. | $0.013889 per call (free daily quota) |
| [`youtube/video-sponsors`](../models/youtube/video-sponsors.md) | Detect suspected sponsors and paid promotions in a YouTube video by URL (sponsor names, websites, confidence). | about $0.0012 per call |
| [`youtube/video-transcript`](../models/youtube/video-transcript.md) | Fetch the transcript/captions of a YouTube video or Short by URL or ID. | about $0.0009 per call |
| [`youtube/video-transcript-full`](../models/youtube/video-transcript-full.md) | Fetch a YouTube video or Short transcript with timed segments and its provenance: whether the words are creator-written captions or… | about $0.002 per call |
| [`youtube/web-v2/channel-community-posts`](../models/youtube/web-v2/channel-community-posts.md) | Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts. Supports pagination via… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/channel-description`](../models/youtube/web-v2/channel-description.md) | Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links. Filter by country… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/channel-id`](../models/youtube/web-v2/channel-id.md) | Resolves a YouTube channel URL to its canonical channel ID. Accepts various channel URL structures including handle, channel, custom, and… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/channel-shorts`](../models/youtube/web-v2/channel-shorts.md) | Returns a list of YouTube Shorts from a specified channel. Supports lookups by channel identifier or URL, optional response formatting,… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/channel-url`](../models/youtube/web-v2/channel-url.md) | Returns standard and vanity channel URLs for a specified YouTube channel. Takes a unique channel ID to look up the corresponding handle… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/channel-videos`](../models/youtube/web-v2/channel-videos.md) | Returns a list of videos for a specified YouTube channel, including title, duration, URLs, and view counts. Supports pagination and region… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/general-search`](../models/youtube/web-v2/general-search.md) | YouTube comprehensive search with multiple filter options for precise result filtering. | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/general-search-v2`](../models/youtube/web-v2/general-search-v2.md) | Returns YouTube search results matching a query keyword. Supports filtering by content type, upload date, duration, features, and sorting… | $0.003 per call (free daily quota) |
| [`youtube/web-v2/post-comment-replies`](../models/youtube/web-v2/post-comment-replies.md) | Returns second-level comment replies for a YouTube post. Supports pagination using continuation tokens, along with optional country and… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/post-comments`](../models/youtube/web-v2/post-comments.md) | Returns comments from a YouTube community post with support for pagination, formatted output, and regional localization settings. | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/post-detail`](../models/youtube/web-v2/post-detail.md) | Returns detailed information for a YouTube community post, including post text, media attachments, and engagement metrics. Filter results… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/related-videos`](../models/youtube/web-v2/related-videos.md) | Returns a list of related videos for a given YouTube video by ID or URL. Includes an option to format the returned output structure. | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/search-channels`](../models/youtube/web-v2/search-channels.md) | Searches YouTube channels by query terms and returns channel listings. Supports paginated results using continuation tokens and optional… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/search-suggestions`](../models/youtube/web-v2/search-suggestions.md) | Returns YouTube autocomplete search suggestions for a given keyword query. Supports optional geographic region and language filtering. | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/shorts-search`](../models/youtube/web-v2/shorts-search.md) | YouTube Shorts specialized search using native YouTube API. | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/shorts-search-v2`](../models/youtube/web-v2/shorts-search-v2.md) | Searches for YouTube Shorts matching a query keyword. Results can be filtered by upload date and sorted by relevance, upload date, view… | $0.003 per call (free daily quota) |
| [`youtube/web-v2/signed-stream-url`](../models/youtube/web-v2/signed-stream-url.md) | Returns a signed playback stream URL for a specific YouTube video format. Requires a format itag identifier alongside either a video ID or… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/video-captions`](../models/youtube/web-v2/video-captions.md) | Returns available video caption tracks or transcripts in multiple formats, filtered by video identifier and language code. | $0.012 per call (free daily quota) |
| [`youtube/web-v2/video-captions-result`](../models/youtube/web-v2/video-captions-result.md) | Returns the status and finished captions for an asynchronous video caption request by job ID. Supports output formats including SRT, XML,… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/video-comment-replies`](../models/youtube/web-v2/video-comment-replies.md) | Returns second-level replies for a YouTube video comment using a continuation token, with optional filters for region, language, and… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/video-comments`](../models/youtube/web-v2/video-comments.md) | Retrieves top-level comments for a YouTube video specified by video ID. Supports sorting by top or newest, regional localization, and… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/video-info`](../models/youtube/web-v2/video-info.md) | Returns detailed video information and caption tracks for a specified YouTube video ID. Supports optional parameters to format output data… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/video-info-v2`](../models/youtube/web-v2/video-info-v2.md) | Returns comprehensive details for a YouTube video identified by its ID or direct URL, with an option to retrieve a cleaned payload format. | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/video-streams`](../models/youtube/web-v2/video-streams.md) | Returns stream details and media information for a specified YouTube video. Queries accept either a direct video identifier or a full… | $0.0015 per call (free daily quota) |
| [`youtube/web-v2/video-streams-v2`](../models/youtube/web-v2/video-streams-v2.md) | Retrieves stream information and playback details for a YouTube video. Queries data using either a video ID or a full video URL. | $0.0045 per call (free daily quota) |
| [`youtube/web/channel-id`](../models/youtube/web/channel-id.md) | Retrieves the unique YouTube channel ID associated with a specific channel name. Provide the target channel name to receive the matching… | $0.0015 per call (free daily quota) |
| [`youtube/web/channel-id-v2`](../models/youtube/web/channel-id-v2.md) | Resolves a YouTube channel URL into its unique channel ID and standardized channel URL. Accepts various URL formats including handles,… | $0.0015 per call (free daily quota) |
| [`youtube/web/channel-info`](../models/youtube/web/channel-info.md) | Returns profile details and external links for a specified YouTube channel. Look up channel data using a channel identifier. | $0.0015 per call (free daily quota) |
| [`youtube/web/channel-short-videos`](../models/youtube/web/channel-short-videos.md) | Returns a list of YouTube Shorts from a specified channel. Supports pagination through an optional continuation token to browse additional… | $0.0015 per call (free daily quota) |
| [`youtube/web/channel-url`](../models/youtube/web/channel-url.md) | Returns the standard channel URL and vanity handle URL for a specified YouTube channel. Takes a unique channel ID as input to resolve… | $0.0015 per call (free daily quota) |
| [`youtube/web/relate-video`](../models/youtube/web/relate-video.md) | Returns a list of related videos for a given YouTube video ID. Supports pagination using a continuation token to retrieve additional… | $0.0015 per call (free daily quota) |
| [`youtube/web/search-channel`](../models/youtube/web/search-channel.md) | Searches videos within a specific YouTube channel using a keyword query. Returns matching video details including title, view count, post… | $0.0015 per call (free daily quota) |
| [`youtube/web/search-video`](../models/youtube/web/search-video.md) | Search YouTube videos by keyword and get video ID, title, channel, views, length and publish time, with country, language and upload-date… | $0.0015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
