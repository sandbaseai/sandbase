# Kuaishou App Selection Feed API: pricing, parameters and code examples

`kuaishou/app/selection-feed` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the recommended selection feed from the Kuaishou app home page. The endpoint requires no parameters and provides fresh recommended video items on each call.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/selection-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/selection-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/selection-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/selection-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/selection-feed` with the body above minus `model`.

## Details

Returns the recommended selection feed from the Kuaishou app home page. The request takes no parameters, and each call returns a list of recommended video items in `feeds`.

### Use cases

- Sample the videos Kuaishou recommends on its home page, with captions, durations and engagement counts.
- Collect cover image URLs and video dimensions for the recommended items.
- Find the search terms Kuaishou suggests next to each video, such as `commentGuessSearch.searchWord`.
- Track which hashtags and topics appear in recommended captions across repeated calls.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/selection-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "costInfo": {
    "S_A": 1242,
    "S_A_D": 171,
    "S_A_RE": 1071
  },
  "debug_id": "2f39d5f8",
  "debug_info": "gAAAAABq6Y7zElbKGYkN4ThlcjewMepiYvPmFkkG2sfz6RDonTFKVHJ3mFCwBamq2l7ttanm1YvWwQde…",
  "edgeRealtimeConfig": {
    "edgeConfigArgs": "{\"edge_index_score_ensemble_weight\":-3.0,\"static_exp_tags\":\"1256:1257:1258:1259:…",
    "edgeConfigVersion": "B3A6B44FF91D89D653AB3AB1ABB9CED0",
    "edgeModelArgs": "{}"
  },
  "feeds": [
    {
      "adminTags": [],
      "canShowQuickCommentGuide": true,
      "caption": "#热门短剧",
      "captionFontInfo": {
        "enableShow": true,
        "fontSize": 3,
        "rowHeight": 1.3
      },
      "captionIpLocation": "Shandong",
      "captionToComment": "#热门短剧",
      "clearScreenSameAuthorCount": 14,
      "collect_count": 1618,
      "commentGuessSearch": {
        "displayPrefix": "相关搜索：",
        "extParams": "{\"all_source\":\"p2q_recall_exp_v24\",\"entrySource\":\"search_entrance_comment_trendi…",
        "iconUrl": "https://ali2.a.kwimgs.com/udata/pkg/se-cdn/search_blue_ios_3x.png",
        "searchWord": "山洞藏军火短剧",
        "searchWordMD5": "88959b0fb639d8b32bf7ce34b85115ce",
        "searchWordUrl": "kwai://search?keyword=山洞藏军火短剧&sessionId=MzIwXzBfMTc5MzY5MTM3OTQ3Nl9fOTg4Mg&sourc…",
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
        "extFunctionAreasList": [
          {
            "ext": "",
            "key": "MOUNT_PHOTO_COMMENT",
            "text": "添加视频评论"
          }
        ],
        "permissions": 6591
      },
      "commentTopBarPriority": [
        {
          "bizType": "PLC",
          "subBizType": "51"
        }
      ],
      "comment_count": 195
    }
  ],
  "host-name": "public-bjy-c58-kce-node276.idchb1az2.hb1.kwaidc.com",
  "isNewRefluxUser": true,
  "isPreload": false,
  "isUnfollowFeeds": false,
  "itemFeatureSwitch": false,
  "llsid": "2010196644821208257",
  "new_notify": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `feeds[]` | One recommended video item. The response returns a list of these. |
| `feeds[].caption` | Caption text of the video. It can contain hashtags such as `#热门短剧`. |
| `feeds[].captionIpLocation` | Location label shown with the caption, for example `Shandong` or `Hebei`. |
| `feeds[].duration` | Length of the video. Values such as `15000` and `184999` match the `ext_params.video` value for the same item. |
| `feeds[].collect_count / feeds[].comment_count / feeds[].downloadCount / feeds[].forwardCount` | Counts of collects, comments, downloads and forwards for the video. |
| `feeds[].ext_params.w / feeds[].ext_params.h` | Width and height of the video. |
| `feeds[].cover_thumbnail_urls[].url` | Cover image URL for the video. Each entry has a `cdn` host name and a `url`. |
| `feeds[].commentGuessSearch.searchWord` | Related search phrase shown with the video. |
| `feeds[].danmakuInfo.danmakuCount` | Number of danmaku (on-screen comments) on the video. Some items do not include this field. |
| `feeds[].exp_tag` | Experiment tag string attached to the feed item. |

### Notes

- The request body is an empty object `{}`. The feed has no pagination parameters, so call the endpoint again to get new items.
- Some fields, such as `bottomEntryInfo`, `danmakuInfo.danmakuCount` and `disclaimerMsgV2`, appear only on some items.
- To get full details for a video from the feed, use [Kuaishou Video Details (V1)](/apis/kuaishou/app/one-video) or [Kuaishou Video Comments (App)](/apis/kuaishou/app/video-comment).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/selection-feed.json`](../../../../catalog/models/kuaishou/app/selection-feed.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/selection-feed
