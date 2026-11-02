# WeChat Channels API: 22 endpoints with pricing and code examples

Call 22 WeChat Channels endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`wechat-channels/account-videos`](../models/wechat-channels/account-videos.md) | Get a paginated WeChat Channels account feed by v2Name with continuation-buffer support. Use it to browse videos and other feed entries… | $0.071429 per call |
| [`wechat-channels/convert-export-id`](../models/wechat-channels/convert-export-id.md) | Convert an encrypted WeChat Channels export ID from search results into a usable video object identity. Use it to prepare the identifier… | $0.021429 per call |
| [`wechat-channels/search-account`](../models/wechat-channels/search-account.md) | Looks up a specific WeChat Channels account identity by keyword. Use it to resolve a creator name or account term to the identifier… | $0.071429 per call |
| [`wechat-channels/search-video`](../models/wechat-channels/search-video.md) | Search WeChat Channels videos by keyword with publish-time, sort, page, offset, and continuation-state controls. Use it to find recent or… | $0.114286 per call |
| [`wechat-channels/v2/channel-id-to-username`](../models/wechat-channels/v2/channel-id-to-username.md) | Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels… | $0.01 per call (free daily quota) |
| [`wechat-channels/v2/channel-info`](../models/wechat-channels/v2/channel-info.md) | Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as… | $0.01 per call (free daily quota) |
| [`wechat-channels/v2/collection-videos`](../models/wechat-channels/v2/collection-videos.md) | Returns videos contained within a WeChat Channels collection using a collection ID. Provides video media URLs, decryption keys, and… | $0.01 per call (free daily quota) |
| [`wechat-channels/v2/live-detail`](../models/wechat-channels/v2/live-detail.md) | Returns live-room details including anchor info, status, online count, and replay data using a live ID. Allows switching between raw and… | $0.01 per call (free daily quota) |
| [`wechat-channels/v2/live-history`](../models/wechat-channels/v2/live-history.md) | Returns a creator's broadcast replay list, including media download URLs and decryption keys. Supports cursor pagination via a finder… | $0.01 per call (free daily quota) |
| [`wechat-channels/v2/search-channel-videos`](../models/wechat-channels/v2/search-channel-videos.md) | Search one WeChat Channels creator's videos by keyword, within that channel only. Returns matching video IDs and titles. | $0.01 per call (free daily quota) |
| [`wechat-channels/v2/user-collections`](../models/wechat-channels/v2/user-collections.md) | Returns the video collections displayed on a creator homepage by username. Includes collection metadata and identifiers used to look up… | $0.01 per call (free daily quota) |
| [`wechat-channels/v2/user-profile`](../models/wechat-channels/v2/user-profile.md) | Get a WeChat Channels creator's profile and stats: nickname, bio, region, follower, video, like and favorite counts, and linked accounts. | $0.01 per call (free daily quota) |
| [`wechat-channels/v2/user-videos`](../models/wechat-channels/v2/user-videos.md) | Get the videos on a WeChat Channels account's homepage with descriptions, publish time, like, comment, share and favorite counts, and… | $0.01 per call (free daily quota) |
| [`wechat-channels/v2/video-comments`](../models/wechat-channels/v2/video-comments.md) | Returns first-level comments or nested replies for a WeChat Channels video, including like counts and IP regions, using the video object ID. | $0.01 per call (free daily quota) |
| [`wechat-channels/v2/video-detail`](../models/wechat-channels/v2/video-detail.md) | Get the full detail of a WeChat Channels video: description, author, engagement counts and the media URL with decode key for download.… | $0.01 per call (free daily quota) |
| [`wechat-channels/v2/video-share-url`](../models/wechat-channels/v2/video-share-url.md) | Returns the share URL for a specific WeChat Channels video using its numeric object ID. Supports both raw and simplified parsed response… | $0.01 per call (free daily quota) |
| [`wechat-channels/video-comment`](../models/wechat-channels/video-comment.md) | Get first-level comments for a WeChat Channels video by object ID with continuation-buffer pagination. Use it to review audience… | $0.021429 per call |
| [`wechat-channels/video-download-url`](../models/wechat-channels/video-download-url.md) | Get a downloadable media URL for a WeChat Channels video by object ID and optional nonce ID. Use it to download or play media from a known… | $0.042857 per call |
| [`wechat-channels/video-metrics`](../models/wechat-channels/video-metrics.md) | Get interaction metrics for a WeChat Channels video by object ID with optional continuation-buffer input. Use it to review engagement for… | $0.021429 per call |
| [`wechat-channels/video-share-url`](../models/wechat-channels/video-share-url.md) | Generates a share link for a WeChat Channels video identified by objectId. Use it to share a known Channels video or obtain its link for a… | $0.028571 per call |
| [`wechat-channels/video-sub-comment`](../models/wechat-channels/video-sub-comment.md) | Get replies under a first-level WeChat Channels video comment using the video and root-comment IDs. Use it to continue a threaded comment… | $0.021429 per call |
| [`wechat-channels/video-title`](../models/wechat-channels/video-title.md) | Get lightweight title information for a WeChat Channels video by object ID and optional nonce ID. Use it to identify known video content… | $0.021429 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/account-videos", "v2Name": "v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@finder"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
