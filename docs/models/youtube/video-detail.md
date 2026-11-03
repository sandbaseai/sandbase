# YouTube Video Details API: pricing, parameters and code examples

`youtube/video-detail` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get public details for a YouTube video identified by video ID. Use it to inspect a known video before further content or comment analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-detail", "videoId": "dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-detail', {'videoId': 'dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-detail", {
  "videoId": "dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-detail", sandbase.Params{
	"videoId": "dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `lang` | string |  | Optional IETF language tag for localized video details, such as en-US. Leave empty to use the default language.  |
| `videoId` | string | yes | The unique identifier for a YouTube video.  |

## Details

Returns public details for one YouTube video: title, description, view and like counts, channel info, thumbnails, music credits, related videos, and lists of audio, video and subtitle file links. It needs a `videoId`, such as `dQw4w9WgXcQ`.

### Use cases

- Check the view count, like count and publish time of a known video.
- Read the channel name, handle and subscriber text for the channel that owns a video.
- Pull the music credits (song, artist, album) listed on a music video.
- Collect related video IDs and titles to find more videos to analyze.
- List the available subtitle language codes for a video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"videoId": "dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `videoId` | string | Yes | The unique identifier for a YouTube video. |
| `lang` | string | No | Optional IETF language tag for localized video details, such as en-US. Leave empty to use the default language. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "audios": {
    "errorId": "Success",
    "expiration": 1793713698,
    "items": [
      {
        "extension": "m4a",
        "isDrc": false,
        "lastModified": 1766955925572207,
        "lengthMs": 213089,
        "mimeType": "audio/mp4; codecs=\"mp4a.40.2\"",
        "size": 3449447,
        "sizeText": "3.3MB",
        "url": "https://redirector.googlevideo.com/videoplayback?expire=1793713698&ei=wpHpao6zJ4…"
      }
    ]
  },
  "channel": {
    "avatar": [
      {
        "height": 48,
        "url": "https://yt3.ggpht.com/_ShEGOdg-t5YGJse14Ooq6FYBZqX_QSlhaTNjG06miYusm5lWm1UroLyVx…",
        "width": 48
      }
    ],
    "handle": "@RickAstleyYT",
    "id": "UCuAXFkgsw1L7xaCfnd5JJOw",
    "isVerified": true,
    "isVerifiedArtist": true,
    "name": "Rick Astley",
    "subscriberCountText": "4.56M subscribers",
    "type": "channel"
  },
  "commentCountText": "2.4M",
  "description": "The official video for “Never Gonna Give You Up” by Rick Astley. \n\nNever: The Au…",
  "errorId": "Success",
  "id": "dQw4w9WgXcQ",
  "isCommentDisabled": false,
  "isLiveNow": false,
  "isLiveStream": false,
  "isRegionRestricted": false,
  "isUnlisted": false,
  "lengthSeconds": 213
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id / title / description` | The video ID, the video title, and the start of the video description. |
| `viewCount / likeCount` | Total views and likes as plain numbers. |
| `commentCountText` | Comment count as display text, such as `2.4M`. |
| `lengthSeconds` | Video length in seconds. |
| `publishedTime / publishedTimeText` | Publish time as an ISO 8601 timestamp with a UTC offset, and the same date as display text. |
| `isLiveNow / isLiveStream / isUnlisted / isRegionRestricted / isCommentDisabled` | Boolean flags that show whether the video is live, a live stream, unlisted, region restricted, or has comments turned off. |
| `channel.id / channel.handle / channel.name` | ID, handle and name of the channel that published the video. |
| `channel.subscriberCountText / channel.isVerified` | Subscriber count as display text, and whether the channel is verified. |
| `musicCredits[].title / musicCredits[].artist / musicCredits[].album` | Song title, artist and album listed for the video. |
| `related.items[].id / related.items[].title / related.items[].viewCountText` | ID, title and view count text of each related video. |
| `videos.items[].quality / videos.items[].url / audios.items[].url` | Quality label and file link for each video or audio stream. The `hasAudio` field shows whether a video file includes sound. |
| `subtitles.items[].code / subtitles.items[].url` | Language code and file link for each subtitle track. |

### Notes

- Take the `videoId` from a YouTube watch URL, where it follows `v=`. Video IDs in this response, such as `E9de-cmycx8`, are 11 characters.
- Pass `lang` as a language tag such as `en-US` to get localized details. Leave it out for the default language.
- The stream and subtitle links come with an `expiration` value, a Unix timestamp in seconds. Use the links before that time.
- Use `related.nextToken` to continue the related video list. For comments, call [YouTube Video Comments](/apis/youtube/video-comments).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/youtube/video-detail.json`](../../../catalog/models/youtube/video-detail.json) · Store page: https://www.sandbase.ai/model/youtube/video-detail
