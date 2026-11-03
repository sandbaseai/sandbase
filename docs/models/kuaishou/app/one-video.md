# Kuaishou Video Details (V1) API: pricing, parameters and code examples

`kuaishou/app/one-video` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed video metadata for a single Kuaishou video post using its photo identifier. Query by video ID to inspect post attributes.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/one-video", "photo_id": "5193494945927590140"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/one-video', {'photo_id': '5193494945927590140'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/one-video", {
  "photo_id": "5193494945927590140"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/one-video", sandbase.Params{
	"photo_id": "5193494945927590140",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `photo_id` | string | yes | 作品ID/Photo ID  |

## Details

Returns metadata for one Kuaishou video post, including its caption, engagement counts, duration, cover images and video file URLs. It needs the post's `photo_id` as input.

### Use cases

- Read the like, comment and collect counts of a single Kuaishou video to track how a post performs.
- Pull the caption and hashtags of a video to see how a creator describes the post.
- Get the video file URLs and cover image URLs to preview or archive a specific post.
- Check the video length and frame size before processing the file.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/one-video" \
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
  "host-name": "public-bjzey-c34-kce-node373.idchb1az3.hb1.kwaidc.com",
  "photos": [
    {
      "adminTags": [],
      "canShowQuickCommentGuide": true,
      "caption": "哥哥我会魔法一人就能变成两@李秀妍u(O4489551526) #李秀妍u #为自己代言",
      "captionSearchInfo": {
        "actionUrlList": [
          "kwai://search?keyword=%E5%93%A5%E5%93%A5%E6%88%91%E4%BC%9A%E9%AD%94%E6%B3%95&ses…"
        ],
        "captionSearchType": 2,
        "dataSource": 0,
        "extParams": "{\"entrySourceList\":[\"search_entrance_cap_keyword\"]}\n",
        "offsetList": [
          0
        ],
        "queryIdList": [
          "12884d6cc3162e18e00d3f66e82dc247"
        ],
        "searchWordList": [
          "哥哥我会魔法"
        ],
        "sessionId": "MzIwXzBf…"
      },
      "captionToComment": "哥哥我会魔法一人就能变成两@李秀妍u(O4489551526) #李秀妍u #为自己代言",
      "collect_count": 9947,
      "commentGuessSearch": {
        "displayPrefix": "相关搜索：",
        "extParams": "{\"all_source\":\"p2q_semantic_recall_v8\",\"entrySource\":\"search_entrance_comment_tr…",
        "iconUrl": "https://ali2.a.kwimgs.com/udata/pkg/se-cdn/search_blue3x.png",
        "searchWord": "李秀妍跳舞后背录屏",
        "searchWordMD5": "1f4a5960222268ee00ee0f66d2039d43",
        "searchWordUrl": "kwai://search?keyword=李秀妍跳舞后背录屏&sessionId=MzIwXzBfMTc5MzY5MTM1ODEyNV9fOTUxMg&sou…",
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
      "comment_count": 3053,
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
          "url": "http://ws2.a.kwimgs.com/upic/2024/12/29/22/BMjAyNDEyMjkyMjE1NDJfMzc5NTIxNDQxMV8x…"
        }
      ]
    }
  ],
  "result": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `photos[].caption` | Caption text of the post, including hashtags and @mentions. |
| `photos[].like_count` | Number of likes on the post. |
| `photos[].comment_count / collect_count / forward_count` | Counts of comments, collects (saves) and forwards for the post. |
| `photos[].duration` | Length of the video. The value 30266 matches `ext_params.video`, so it is most likely in milliseconds (about 30 seconds). |
| `photos[].ext_params.w / h` | Width and height of the video in pixels (720 by 960 in the sample). |
| `photos[].main_mv_urls[].url` | Video file URLs, with the CDN host name in `cdn`. Each entry is an alternative address for the same video. |
| `photos[].cover_thumbnail_urls[].url` | Cover image URLs for the video, one per CDN host. |
| `photos[].headurls[].url` | Avatar image URLs of the post author. |
| `photos[].captionSearchInfo.searchWordList` | Search phrases that Kuaishou extracted from the caption. |
| `photos[].commentGuessSearch.searchWord` | Related search phrase shown with the comments. |

### Notes

- `photo_id` is a numeric string, such as `5193494945927590140`. The response is a `photos` array with one item for this lookup.
- Only the video ID is needed here. To start from a share link instead, use [Kuaishou Video Details by URL](/apis/kuaishou/app/one-video-by-url).
- To look up several posts in one call, use [Kuaishou Batch Video Details](/apis/kuaishou/app/videos-batch).
- To read the comments on a post, call [Kuaishou Video Comments (App)](/apis/kuaishou/app/video-comment).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/one-video.json`](../../../../catalog/models/kuaishou/app/one-video.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/one-video
