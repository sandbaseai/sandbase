# Kuaishou Livestream Search API: pricing, parameters and code examples

`kuaishou/app/search-live` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Searches Kuaishou livestreams using a specified search term. Returns matching active broadcast rooms with cursor pagination support.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-live", "keyword": "带货"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-live', {'keyword': '带货'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-live", {
  "keyword": "带货"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-live", sandbase.Params{
	"keyword": "带货",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | Cursor, empty for first page default `""` |

## Details

Searches active Kuaishou livestreams by keyword and returns a list of matching broadcast rooms. It needs one input, `keyword`, and accepts an optional `pcursor` to page through results.

### Use cases

- Find live rooms that are broadcasting about a topic or brand name right now.
- Collect live room captions and cover images for a keyword to review what streamers are showing.
- Check whether any livestream matches a keyword before you look up the streamer in more detail.
- Page through all live results for a term by passing back the returned cursor.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes |  |
| `pcursor` | string | No | Cursor, empty for first page |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "debug_id": "4b740b50",
  "debug_info": "gAAAAABq6Y7hNBn1QQMxm_Vpk4cDglqzHDqZWMsVPVntFo1DitGAyY3eNF8CowwWQep6K5W2UD4ahTKw…",
  "extParams": {
    "disablePhotoInsert": false,
    "dynamicShard": false,
    "enableUserInfoNewLine": true,
    "isCreativeMode": false,
    "isShowPymkUserPhotos": true,
    "isShowScrollTopButton": false,
    "livePendantResource": "https://static.yximgs.com/udata/pkg/ks-nearby/nearby_living_tag/origin_196uxh2cv…",
    "outerStreamFetch": 6,
    "pageSingleDoubleStyle": 0,
    "recoResultTitle": "你附近的优惠地点",
    "rsRecoAfterPlayInterval": 2,
    "searchTaskParam": {}
  },
  "host-name": "public-bjmt-c26-kce-node882.idchb1az4.hb1.kwaidc.com",
  "jumpToSlideMode": true,
  "llsid": "2006455567336777042",
  "mixFeeds": [],
  "pcursor": "no_more",
  "portalFlag": true,
  "recoAreaTitle": "",
  "recoInterestFlag": false,
  "recoMixFeeds": [
    {
      "atmosphereType": 0,
      "extInfo": {
        "ext_params": {
          "show_tag": "0_直播中_"
        },
        "liveCornerTagInfo": {
          "contentText": "直播中",
          "iconType": 0,
          "imgUrl": "https://p66-live.wsbkwai.com/udata/widget/5xtsbd34jwy8kgc",
          "recommendReasonText": "",
          "recommendReasonType": 0,
          "type": 2
        },
        "recallSource": "LIVE_OFFICIAL_MEDIA",
        "screenItemKey": "LIVE_STREAM$$1$$0"
      },
      "feedLogCtx": {
        "stExParams": "",
        "stidContainer": "CkExfDIwMDY0NTU1NjczMzY3NzcwNDJ8bGl2ZVN0cmVhbTp6TGthdWY2R0RIa3x7InBnIjoic2x2In18…"
      },
      "isSingleColumnMode": false,
      "itemTransferInfo": "{\"refer_single_double_type\":0}",
      "itemType": 6,
      "live": {
        "acu": 0,
        "audienceCount": "0",
        "autoEnterDelay": 0,
        "caption": "2026浙BA省级争霸赛 杭州vs桐乡",
        "clientComponentLoadScene": 4,
        "coverWidgets": [
          {
            "backgroundColorGradientAngle": 0,
            "extraInfo": "",
            "iconType": 0,
            "imageHeightPx": 14,
            "imageUrls": [
              {
                "cdn": "p66-live.wsbkwai.com",
                "url": "https://p66-live.wsbkwai.com/udata/widget/5xtsbd34jwy8kgc"
              }
            ],
            "imageWidthPx": 14,
            "newIconStyle": 1,
            "pageType": 2
          }
        ],
        "cover_thumbnail_urls": [
          {
            "cdn": "p22.a.yximgs.com",
            "url": "http://p22.a.yximgs.com/uhead/AB/2026/11/02/19/BMjAyNjExMDIxOTA0NTFfMTQ1OTk5MTg5…"
          }
        ],
        "customized": true
      },
      "rank": 0
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `recoMixFeeds[]` | List of matching livestream entries. Each item is one broadcast room, ordered by `rank`. |
| `recoMixFeeds[].rank` | Position of the room in the result list, starting at 0. |
| `recoMixFeeds[].live.caption` | Title text of the livestream as shown on Kuaishou. |
| `recoMixFeeds[].live.audienceCount / recoMixFeeds[].live.acu` | Viewer count fields for the room. `audienceCount` is a string. Both were `0` in this response. |
| `recoMixFeeds[].live.cover_thumbnail_urls[].url` | Cover image URLs for the room, each with the `cdn` host that serves it. |
| `recoMixFeeds[].extInfo.liveCornerTagInfo.contentText` | Label shown on the room card. The value `直播中` means the room is live. |
| `recoMixFeeds[].extInfo.recallSource` | Label for the source that matched this room, such as `LIVE_OFFICIAL_MEDIA`. |
| `recoMixFeeds[].feedLogCtx.stidContainer` | Encoded tracking string attached to each entry. |
| `recoPcursor / pcursor` | Cursor values for paging. Both were `no_more` in this response, which means no further pages. |
| `llsid / requestId` | Identifiers for this search request. |

### Notes

- Leave `pcursor` empty for the first page. For the next page, send the cursor value from the previous response.
- A cursor of `no_more` in `pcursor` or `recoPcursor` means there are no more results.
- Results are in `recoMixFeeds`. The `mixFeeds` list was empty in this response.
- To get details about a streamer, try [Kuaishou User Broadcast Details](/apis/kuaishou/app/user-live-info).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-live.json`](../../../../catalog/models/kuaishou/app/search-live.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-live
