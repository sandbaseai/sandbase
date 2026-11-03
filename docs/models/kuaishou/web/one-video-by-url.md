# Kuaishou Single Video by URL API: pricing, parameters and code examples

`kuaishou/web/one-video-by-url` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Retrieves video manifest data and streaming representation details for a specific Kuaishou post using its web link. Returns media properties such as resolution, frame rate, and direct video URLs.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/one-video-by-url", "url": "https://v.kuaishou.com/GKTpYm"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/one-video-by-url', {'url': 'https://v.kuaishou.com/GKTpYm'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/one-video-by-url", {
  "url": "https://v.kuaishou.com/GKTpYm"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/one-video-by-url", sandbase.Params{
	"url": "https://v.kuaishou.com/GKTpYm",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/one-video-by-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | 作品链接/Photo URL  |

## Details

Returns details for one Kuaishou post, including the author, engagement counts, cover images, direct video URLs and a stream manifest with the available quality representations. It needs a Kuaishou post link in `url`, such as a `v.kuaishou.com` short link.

### Use cases

- Download or play a Kuaishou video by taking direct file links from `photo.mainMvUrls`.
- Compare the bitrate variants of one video using `photo.manifest.adaptationSet[].representation[]`.
- Track the views, likes, comments and shares of a post from a shared link.
- Check who published a post and whether the account is verified.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/one-video-by-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://v.kuaishou.com/GKTpYm"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "counts": {
    "collectionCount": 1836,
    "fanCount": 69651241,
    "followCount": 5,
    "photoCount": 10863
  },
  "photo": {
    "adminTags": [],
    "caption": "现场视频！中央军委政治工作会议在延安召开，习近平出席会议并发表重要讲话。（来源：央视时政）",
    "cccCoverMap": {
      "height": 1155,
      "width": 870
    },
    "commentCount": 2820,
    "commentShowType": 2,
    "coverUrls": [
      {
        "cdn": "p23.a.yximgs.com",
        "url": "https://p23.a.yximgs.com/upic/2024/06/19/21/BMjAyNDA2MTkyMTA5NDJfMTA5NjYzNzQwMV8…"
      }
    ],
    "duration": 15682,
    "exp_tag": "1_u/2006456229091442258_s0",
    "ext_params": {
      "color": "191818",
      "h": 960,
      "interval": 29,
      "mtype": 3,
      "sound": 15701,
      "video": 15682,
      "w": 720
    },
    "forcePublic": "H4sIAAAAAAAA%2F%2BNQEmCQ2Hn35s4fzABK4wL6CwAAAA%3D%3D",
    "forwardCount": 0,
    "headUrl": "https://p4-pro.a.yximgs.com/uhead/AB/2022/12/07/19/BMjAyMjEyMDcxOTEyMzFfMTA5NjYz…"
  },
  "result": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `photo.photoId / photo.photoType` | The ID of the post and its type. In this response the type is `VIDEO`. |
| `photo.caption` | The text that the author wrote for the post. |
| `photo.viewCount / likeCount / commentCount / shareCount / forwardCount` | Engagement counts for the post. Each key is a separate count, for example `photo.viewCount` for views and `photo.likeCount` for likes. |
| `photo.timestamp` | The time of the post as a 13-digit number. It looks like a Unix time in milliseconds. |
| `photo.duration / photo.width / photo.height` | The length and the pixel size of the video. `photo.duration` is 15682 in this response, which fits milliseconds. |
| `photo.mainMvUrls[].url / photo.mainMvUrls[].cdn` | Direct MP4 links to the video, each on a different CDN host. The links carry signed query strings. |
| `photo.coverUrls[].url / photo.webpCoverUrls[].url` | Cover image links in JPG and WebP form, one for each CDN host. |
| `photo.manifest.adaptationSet[].representation[]` | One entry per available encoding of the video. Each entry has `avgBitrate`, `backupUrl` and a `comment` that names the codec and the resolution tier. |
| `photo.userName / photo.userId / photo.userEid / photo.kwaiId` | The author's display name, numeric ID, encoded ID and Kuaishou ID. |
| `photo.verified / photo.verifiedDetail.description` | Shows whether the author is verified and the verification label. In this response the label is the name of a news organisation. |
| `counts.fanCount / counts.photoCount / counts.followCount / counts.collectionCount` | Counts for the author's account, such as followers and number of posts. |

### Notes

- Pass a Kuaishou share link in `url`. The example uses the short form `https://v.kuaishou.com/GKTpYm`.
- `photo.photoId` is a numeric string. You can use it with [Kuaishou Single Video Details](/apis/kuaishou/web/one-video) for more post data.
- Use [Kuaishou Video Comments (Web)](/apis/kuaishou/web/one-video-comment) to read the comments on the post.
- The `result` field is `1` in this successful response.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Web Share Short URL](/apis/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/one-video-by-url.json`](../../../../catalog/models/kuaishou/web/one-video-by-url.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/one-video-by-url
