# Kuaishou User Published Videos API: pricing, parameters and code examples

`kuaishou/user-video-list` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get public videos published by a Kuaishou user, with optional cursor-based pagination. Use it to review a creator's content history or select videos for detail and comment requests.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/user-video-list", "userId": "40300058"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/user-video-list', {'userId': '40300058'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/user-video-list", {
  "userId": "40300058"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/user-video-list", sandbase.Params{
	"userId": "40300058",
})
```

Same call via the path form: `POST /v1/api/kuaishou/user-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | The unique user ID on Kuaishou.  |
| `pcursor` | string |  | Pagination cursor for subsequent pages.  |

## Details

This API returns the public posts published by a Kuaishou user, newest first as the platform lists them. It needs the numeric `userId` and accepts an optional `pcursor` to fetch later pages.

### Use cases

- Review a creator's posting history, including captions and engagement counts.
- Collect `photo_id` values to pass to a video detail or comment API.
- Track how much attention a creator's recent posts get through likes, collects and comments.
- Download cover images and background music details for posts a creator published.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/user-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "40300058"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | The unique user ID on Kuaishou. |
| `pcursor` | string | No | Pagination cursor for subsequent pages. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "feeds": [
    {
      "adminTags": [],
      "caption": "🍳 不会做饭？跟着达人学，还能赢大奖！\n#快手美食跟学大赛  火热开启！🔥\n11月9日-次年1月3日。这个冬天，别再只刷美食视频流口水！\n🙋 怎么参加？0门槛，…",
      "collect_count": 0,
      "commentInfo": {
        "commentCountSpecialEffect": false,
        "commentEducationGuide": {
          "guideType": 0,
          "triggerCharCount": 0
        },
        "commentIconType": 0,
        "enableAIPresetGuide": false,
        "permissions": 191
      },
      "comment_count": 0,
      "coverCommonTags": {
        "authorHeadMask": {
          "bgImage": [
            {
              "cdn": "tx2.a.kwimgs.com",
              "url": "https://tx2.a.kwimgs.com/udata/pkg/KS-COVERTAG/feed_tag_certification_blue.a843c…"
            }
          ],
          "darkModeStyle": {
            "bgImage": [
              {
                "cdn": "tx2.a.kwimgs.com",
                "url": "https://tx2.a.kwimgs.com/udata/pkg/KS-COVERTAG/dark_feed_tag_certification_blue.…"
              }
            ]
          },
          "tagType": 86
        },
        "authorHeadMaskEnhanceTag": {
          "bgImage": [
            {
              "cdn": "tx2.a.kwimgs.com",
              "url": "https://tx2.a.kwimgs.com/udata/pkg/KS-COVERTAG/feed_tag_certification_blue.a843c…"
            }
          ],
          "darkModeStyle": {
            "bgImage": [
              {
                "cdn": "tx2.a.kwimgs.com",
                "url": "https://tx2.a.kwimgs.com/udata/pkg/KS-COVERTAG/dark_feed_tag_certification_blue.…"
              }
            ]
          },
          "tagType": 86
        },
        "authorRelationBigHeadTag": {
          "bgImage": [
            {
              "cdn": "js2.a.yximgs.com",
              "url": "http://js2.a.yximgs.com/bs2/fes/app_feed_verified_blue_icon.png"
            }
          ],
          "darkModeStyle": {
            "bgImage": [
              {
                "cdn": "static.yximgs.com",
                "url": "https://static.yximgs.com/udata/pkg/KS-COVERTAG/dark_feed_icon_certification_blu…"
              }
            ]
          },
          "tagType": 86
        },
        "authorRelationEnhanceTag": {
          "bgImage": [
            {
              "cdn": "ali2.a.kwimgs.com",
              "url": "https://ali2.a.kwimgs.com/udata/pkg/KS-SIDEBAR/verified_blue_light_enhanced_3x_v…"
            }
          ],
          "darkModeStyle": {
            "bgImage": [
              {
                "cdn": "ali2.a.kwimgs.com",
                "url": "https://ali2.a.kwimgs.com/udata/pkg/KS-SIDEBAR/verified_blue_enhanced_dark_3x_v4…"
              }
            ]
          },
          "tagType": 86
        },
        "authorRelationTag": {
          "bgImage": [
            {
              "cdn": "tx2.a.kwimgs.com",
              "url": "http://tx2.a.kwimgs.com/bs2/fes/app_feed_verified_blue_icon.png"
            }
          ],
          "darkModeStyle": {
            "bgImage": [
              {
                "cdn": "tx2.a.kwimgs.com",
                "url": "https://tx2.a.kwimgs.com/udata/pkg/KS-COVERTAG/dark_feed_icon_certification_blue…"
              }
            ]
          },
          "tagType": 86
        },
        "rightTopTag": {
          "bgImage": [
            {
              "cdn": "js2.a.yximgs.com",
              "url": "http://js2.a.yximgs.com/bs2/fes/app_feed_tag_singlepicture.png"
            }
          ],
          "darkModeStyle": {
            "bgImage": [
              {
                "cdn": "js2.a.yximgs.com",
                "url": "http://js2.a.yximgs.com/bs2/fes/app_feed_tag_singlepicture.png"
              }
            ]
          },
          "tagType": 8,
          "textColor": "#FFFFFF"
        }
      },
      "cover_thumbnail_urls": [
        {
          "cdn": "zj66.a.kwimgs.com",
          "url": "http://zj66.a.kwimgs.com/upic/2026/11/03/14/BMjAyNjExMDMxNDA3NDhfNDAzMDAwNThfMjE…"
        }
      ],
      "cover_urls": [
        {
          "cdn": "zj66.a.kwimgs.com",
          "url": "http://zj66.a.kwimgs.com/upic/2026/11/03/14/BMjAyNjExMDMxNDA3NDhfNDAzMDAwNThfMjE…"
        }
      ],
      "editInfo": {},
      "enableFullScreenPlay": false,
      "exp_tag": "1_i/2006457346806318098_bsp0",
      "ext_params": {
        "color": "F7F0CE",
        "f": 0,
        "h": 2168,
        "mtype": 6,
        "single": {
          "cdn": [
            "zj66.a.kwimgs.com"
          ],
          "cdnList": [
            {
              "cdn": "zj66.a.kwimgs.com"
            }
          ],
          "list": [
            "/ufile/atlas/NTIzMTQ5NDEzMDYzMDA5OTM4NF8xNzkzNjg2MDY4NTcy_0.webp"
          ],
          "music": "/ufile/atlas/NTIzMTQ5NDEzMDYzMDA5OTM4NF8xNzkzNjg2MDY4NTcy.m4a",
          "musicCdnList": [
            {
              "cdn": "tymov2.a.kwimgs.com"
            }
          ],
          "size": [
            {
              "h": 1920,
              "w": 734
            }
          ],
          "type": 3,
          "volume": 0.0
        },
        "w": 828
      }
    }
  ],
  "host-name": "public-bjy-c26-kce-node720.idchb1az2.hb1.kwaidc.com",
  "llsid": 2006457346806318098,
  "pcursor": "1.789560000704E12",
  "result": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `feeds[]` | One entry per published post. Each entry holds the caption, counts, cover images, author avatar and music. |
| `feeds[].photo_id` | Numeric ID of the post. Use it to request details or comments for that post. |
| `feeds[].caption` | Text the creator wrote for the post, including hashtags and line breaks. |
| `feeds[].like_count / comment_count / collect_count / forward_count` | Engagement counts for the post: likes, comments, collects and forwards. |
| `feeds[].cover_urls[].url` | Full-size cover image URL. Each item lists one CDN host in `cdn`, so the same image appears under several hosts. |
| `feeds[].cover_thumbnail_urls[].url` | Thumbnail version of the cover image, in `webp` format. |
| `feeds[].headurls[].url` | Avatar image URL of the author. |
| `feeds[].kwaiId` | The author's Kuaishou handle. |
| `feeds[].music.artist / music.duration` | Artist name and length of the music attached to the post. `music.audioUrls[].url` holds the audio file links. |
| `feeds[].ext_params.single.size[]` | Width `w` and height `h` of each image in an image post. `ext_params.single.list` holds the image paths. |

### Notes

- Get `userId` from a profile lookup such as [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id).
- For the next page, send the cursor value from the response as `pcursor` with the same `userId`.
- Pass `photo_id` to [Kuaishou Video Details (V1)](/apis/kuaishou/app/one-video) for full details of one post.
- Image posts in the list carry `ext_params.single` data with image paths instead of a video file.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/kuaishou/user-video-list.json`](../../../catalog/models/kuaishou/user-video-list.json) · Store page: https://www.sandbase.ai/model/kuaishou/user-video-list
