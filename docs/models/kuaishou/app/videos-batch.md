# Kuaishou Batch Video Details API: pricing, parameters and code examples

`kuaishou/app/videos-batch` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.04 per call · **Modes:** sync

Retrieves video details for multiple Kuaishou posts in a single request. Specify comma-separated photo IDs to look up information for up to 40 videos at once.

## Pricing

- **$0.04 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/videos-batch", "photo_ids": "5228960823332207296,5196309727975443273,5222486898325987583"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/videos-batch', {'photo_ids': '5228960823332207296,5196309727975443273,5222486898325987583'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/videos-batch", {
  "photo_ids": "5228960823332207296,5196309727975443273,5222486898325987583"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/videos-batch", sandbase.Params{
	"photo_ids": "5228960823332207296,5196309727975443273,5222486898325987583",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/videos-batch` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `photo_ids` | string | yes | Photo ID list, multiple IDs separated by commas, max 40 per request  |

## Details

Returns details for several Kuaishou videos in one call. The only input is `photo_ids`, a comma-separated string of up to 40 photo IDs. The response has a `photos` list with one entry per video.

### Use cases

- Pull like, comment and collect counts for a set of videos from one account to compare their engagement.
- Download cover image and video stream URLs for a batch of posts you already track.
- Read captions and hashtags of event videos to group them by topic.
- Check video length and frame size for many posts before processing them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/videos-batch" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_ids": "5228960823332207296,5196309727975443273,5222486898325987583"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_ids` | string | Yes | Photo ID list, multiple IDs separated by commas, max 40 per request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "host-name": "public-bjzey-c34-kce-node1456.idchb1az3.hb1.kwaidc.com",
  "photos": [
    {
      "adminTags": [],
      "canShowQuickCommentGuide": true,
      "caption": "零跑A10正式发布 2026年冲击年销100万辆  #2025广州国际车展  #2025广州车展  #上汽车之家看有用的车展指南",
      "captionToComment": "零跑A10正式发布 2026年冲击年销100万辆 #2025广州国际车展 #2025广州车展 #上汽车之家看有用的车展指南",
      "collect_count": 4,
      "commentGuessSearch": {
        "displayPrefix": "相关搜索：",
        "extParams": "{\"all_source\":\"p2q_semantic_recall_v1\",\"entrySource\":\"search_entrance_comment_tr…",
        "iconUrl": "https://ali2.a.kwimgs.com/udata/pkg/se-cdn/search_blue3x.png",
        "searchWord": "零跑全域自研",
        "searchWordMD5": "ba63484b615923962aaced09bbad743a",
        "searchWordUrl": "kwai://search?keyword=零跑全域自研&sessionId=MzIwXzBfMTc5MzY5MTM4MDI5OV9fNDQyNA&source…",
        "sessionId": "MzIwXzBf…"
      },
      "commentInfo": {
        "commentCountSpecialEffect": true,
        "commentEducationGuide": {
          "guideType": 0,
          "triggerCharCount": 0
        },
        "commentIconType": 0,
        "enableAIPresetGuide": false,
        "permissions": 191
      },
      "commentTopBarPriority": [
        {
          "bizType": "PLC",
          "subBizType": "51"
        }
      ],
      "comment_count": 11,
      "coronaVipInfo": {
        "enableFilmAd": false,
        "filmAdInfo": {
          "pageId": 100014436,
          "posId": 9777,
          "subPageId": 100017199
        },
        "inspireAdInfo": {
          "pageId": 100011251,
          "posId": 20578,
          "subPageId": 100024209
        },
        "vipPhoto": false
      },
      "cover_thumbnail_urls": [
        {
          "cdn": "ws2.a.kwimgs.com",
          "url": "http://ws2.a.kwimgs.com/upic/2025/11/22/14/BMjAyNTExMjIxNDE2NTdfOTAzNTExNzcyXzE4…"
        }
      ],
      "danmakuInfo": {
        "danmakuShowDirection": 2,
        "defaultDanmaku": "发个友善的弹幕吧",
        "hasDanmaku": true,
        "paster": false,
        "photoDanmakuGuide": false
      }
    }
  ],
  "result": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `photos[]` | One entry per requested video. Each entry holds the fields below. |
| `photos[].caption` | Post text, including hashtags written as `#tag`. |
| `photos[].like_count / photos[].comment_count / photos[].collect_count / photos[].forward_count` | Counts of likes, comments, collects and forwards for the video. |
| `photos[].duration` | Video length. The value 56233 for a clip matches `ext_params.video`, which suggests milliseconds. |
| `photos[].ext_params.w / photos[].ext_params.h` | Video width and height in pixels. A portrait clip shows `w` 720 and `h` 1280. |
| `photos[].main_mv_urls[].url` | Video stream URL. Each item pairs a `cdn` host with a `url`, so the same video is offered on more than one host. |
| `photos[].cover_thumbnail_urls[].url` | Cover image URL for the video, one per `cdn` host. |
| `photos[].headurls[].url` | Avatar image URL of the author, one per `cdn` host. |
| `photos[].kwaiId` | Public Kuaishou ID of the author, for example `Autohome`. |
| `photos[].commentGuessSearch.searchWord` | Suggested related search phrase shown with the comments. |

### Notes

- Get photo IDs from a list API such as [Kuaishou User Video List (V2)](/apis/kuaishou/app/user-post-v2) or [Kuaishou Video Search (V2)](/apis/kuaishou/app/search-video-v2).
- Send `photo_ids` as one string with IDs separated by commas, up to 40 per request. Each ID is a long number such as `5228960823332207296`.
- For one video only, use [Kuaishou Video Details (V1)](/apis/kuaishou/app/one-video).
- URLs in the response may end with a cut tag value, so use them soon after the call.

### Pricing

$0.04 per successful call. Failed calls are not charged.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/videos-batch.json`](../../../../catalog/models/kuaishou/app/videos-batch.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/videos-batch
