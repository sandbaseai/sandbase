# Kuaishou Single Video Details (V2) API: pricing, parameters and code examples

`kuaishou/web/one-video-v2` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Retrieves video streaming manifests and media details for a specific Kuaishou video using its unique identifier.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/one-video-v2", "photo_id": "5193494945927590140"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/one-video-v2', {'photo_id': '5193494945927590140'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/one-video-v2", {
  "photo_id": "5193494945927590140"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/one-video-v2", sandbase.Params{
	"photo_id": "5193494945927590140",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/one-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `photo_id` | string | yes | 作品ID/Photo ID  |

## Details

Returns details for one Kuaishou video: caption, engagement counts, author info, cover and video file URLs, a stream manifest with several encodings, and the soundtrack. It needs the video's `photo_id`.

### Use cases

- Download or preview a Kuaishou video by picking a file URL from `photo.mainMvUrls` or the manifest.
- Compare the encodings listed in the manifest, such as AVC and HEVC at different bitrates, before choosing one to play.
- Track a post's `viewCount`, `likeCount`, `commentCount` and `shareCount` over repeated lookups.
- Collect the soundtrack name, artist and audio file URLs used in a video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/one-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_id": "5193494945927590140"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_id` | string | Yes |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "counts": {
    "collectionCount": 9947,
    "fanCount": 359746,
    "followCount": 2,
    "photoCount": 683
  },
  "photo": {
    "adminTags": [],
    "caption": "哥哥我会魔法一人就能变成两@李秀妍u #李秀妍u #为自己代言",
    "commentCount": 3053,
    "commentShowType": 2,
    "coverUrls": [
      {
        "cdn": "p23.a.yximgs.com",
        "url": "https://p23.a.yximgs.com/upic/2024/12/29/22/BMjAyNDEyMjkyMjE1NDJfMzc5NTIxNDQxMV8…"
      }
    ],
    "duration": 30266,
    "exp_tag": "1_i/2010302189902940289_s0",
    "ext_params": {
      "color": "1B140F",
      "h": 960,
      "interval": 60,
      "mtype": 3,
      "sound": 30210,
      "video": 30266,
      "w": 720
    },
    "forcePublic": "H4sIAAAAAAAA%2F%2BNQEmCQeLHw0%2BwdLADBVRUjCwAAAA%3D%3D",
    "forwardCount": 0,
    "headUrl": "https://p66.a.kwimgs.com/uhead/AB/2024/11/24/18/BMjAyNDExMjQxODI2MzJfMzc5NTIxNDQ…",
    "headUrls": [
      {
        "cdn": "p66.a.kwimgs.com",
        "url": "https://p66.a.kwimgs.com/uhead/AB/2024/11/24/18/BMjAyNDExMjQxODI2MzJfMzc5NTIxNDQ…"
      }
    ]
  },
  "result": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `photo.caption` | Text posted with the video, including the @mentions and hashtags. |
| `photo.viewCount / photo.likeCount / photo.commentCount / photo.shareCount / photo.forwardCount` | Engagement counts for the video. |
| `photo.duration` | Video length as a number. The value 30266 matches `photo.ext_params.video`, so it looks like milliseconds. |
| `photo.width / photo.height` | Frame size of the video in pixels. |
| `photo.timestamp` | Time value for the post, as a 13-digit number (looks like Unix milliseconds). |
| `photo.mainMvUrls[].url` | Direct MP4 links to the video, one for each CDN host in `cdn`. |
| `photo.manifest.adaptationSet[].representation[]` | Available encodings of the video. Each entry has `avgBitrate`, a `backupUrl` list and a `comment` that names the codec and resolution tier. |
| `photo.coverUrls[].url / photo.webpCoverUrls[].url` | Cover image links in JPEG and WebP form, one for each CDN host. |
| `photo.userId / photo.userEid / photo.userName` | Numeric ID, string ID and display name of the author. |
| `photo.soundTrack.name / photo.soundTrack.artist / photo.soundTrack.audioUrls[].url` | Name, artist and audio file links (m4a) of the sound used in the video. |
| `counts.fanCount / counts.followCount / counts.photoCount / counts.collectionCount` | Counts shown for the author's account: fans, accounts followed, posts and collections. |

### Notes

- `photo_id` is a string of digits, for example `5193494945927590140`. The same value comes back in `photo.photoId`.
- `photo.share_info` holds the author and post IDs in the short form used in share links.
- To start from a share link instead of an ID, use [Kuaishou Single Video by URL](/apis/kuaishou/web/one-video-by-url).
- To read the comments on this video, call [Kuaishou Video Comments (Web)](/apis/kuaishou/web/one-video-comment).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Web Share Short URL](/apis/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/one-video-v2.json`](../../../../catalog/models/kuaishou/web/one-video-v2.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/one-video-v2
