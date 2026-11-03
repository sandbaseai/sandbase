# Kuaishou Single Video Details API: pricing, parameters and code examples

`kuaishou/web/one-video` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a single Kuaishou video post using shared link content. Note that photo-only posts are not supported.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/one-video", "share_text": "https://www.kuaishou.com/f/X-f2k5KJpiXN1SY"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/one-video', {'share_text': 'https://www.kuaishou.com/f/X-f2k5KJpiXN1SY'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/one-video", {
  "share_text": "https://www.kuaishou.com/f/X-f2k5KJpiXN1SY"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/one-video", sandbase.Params{
	"share_text": "https://www.kuaishou.com/f/X-f2k5KJpiXN1SY",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_text` | string | yes | 作品分享链接/Photo share link  |

## Details

Returns metadata for one Kuaishou video post. It needs a shared link to the post in `share_text`. The response is a list with one object that holds counts, author info, cover and video URLs, and stream variants.

### Use cases

- Pull the view, like, comment and share counts of a video that someone shared as a link.
- Collect the author name, Kuaishou ID and user ID behind a shared video.
- Get the cover image and MP4 URLs of a video to archive or preview it.
- Read the resolution and duration of a video to check its format before processing it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/one-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_text": "https://www.kuaishou.com/f/X-f2k5KJpiXN1SY"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_text` | string | Yes |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "adminTags": [],
    "caption": "外 星 鸭 脖",
    "commentCount": 3248,
    "commentShowType": 2,
    "coverUrls": [
      {
        "cdn": "p2.a.yximgs.com",
        "url": "https://p2.a.yximgs.com/upic/2024/11/08/17/BMjAyNDExMDgxNzQwMzlfMjI4OTA1ODAyXzE0…"
      }
    ],
    "duration": 58750,
    "exp_tag": "1_a/2006452015065702178_s0",
    "ext_params": {
      "color": "7D7A7D",
      "h": 1280,
      "interval": 60,
      "mtype": 3,
      "sound": 58751,
      "video": 58750,
      "w": 720
    },
    "forcePublic": "H4sIAAAAAAAA%2F%2BNQEmCQ2Lbi8PnlLEaSXOzFGYlFqZ4pQnyGFoYmBhaGFuaWRoaGJgBl99ASJgAA…",
    "forwardCount": 0,
    "headUrl": "https://p4-pro.a.yximgs.com/uhead/AB/2025/08/11/21/BMjAyNTA4MTEyMTEyNDlfMjI4OTA1…",
    "headUrls": [
      {
        "cdn": "p4-pro.a.yximgs.com",
        "url": "https://p4-pro.a.yximgs.com/uhead/AB/2025/08/11/21/BMjAyNTA4MTEyMTEyNDlfMjI4OTA1…"
      }
    ]
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[].photoId` | ID of the post. Pass it to the comment APIs to read the post's comments. |
| `[].caption` | Text caption of the video. |
| `viewCount / likeCount / commentCount / shareCount / forwardCount` | Engagement counts for the video. Read them as the totals at the time of the call. |
| `[].timestamp` | Publish time of the post as a 13-digit number. It looks like Unix time in milliseconds. |
| `[].duration` | Length of the video. The value `58750` matches `ext_params.video`, so it is most likely milliseconds. |
| `[].width / [].height` | Frame size of the video in pixels (`720` by `1280` in the sample). |
| `[].mainMvUrls[].url` | Direct MP4 links to the video, listed once per CDN host in `cdn`. |
| `[].coverUrls[].url` | Cover image links for the video, one per CDN host. |
| `[].userId / [].userEid / [].userName / [].kwaiId` | Identity of the author: numeric user ID, encoded user ID, display name and Kuaishou ID. `kwaiId` appears on the root object and inside `soundTrack.user`. |
| `[].manifest.adaptationSet[].representation[]` | Stream variants of the video. Each has `avgBitrate`, `backupUrl` links, and a `comment` string that names the codec and quality. |
| `[].soundTrack.name / [].soundTrack.audioUrls[].url` | Name of the audio track and links to its `.m4a` file. |

### Notes

- Set `share_text` to a Kuaishou share link such as `https://www.kuaishou.com/f/X-f2k5KJpiXN1SY`.
- Photo-only posts are not supported. Check `photoType`, which is `VIDEO` for a video post.
- To read comments on the video, call [Kuaishou Video Comments (Web)](/apis/kuaishou/web/one-video-comment) with the post ID.
- For another version of this lookup, see [Kuaishou Single Video Details (V2)](/apis/kuaishou/web/one-video-v2).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Web Share Short URL](/apis/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/one-video.json`](../../../../catalog/models/kuaishou/web/one-video.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/one-video
