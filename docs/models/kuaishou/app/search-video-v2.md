# Kuaishou Video Search (V2) API: pricing, parameters and code examples

`kuaishou/app/search-video-v2` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Searches for Kuaishou videos matching a designated keyword query. Returns matching video results with support for cursor-based pagination across multiple pages.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-video-v2", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-video-v2', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-video-v2", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-video-v2", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | Pagination cursor, empty for first page, pass pcursor from previous response default `""` |

## Details

Returns a list of Kuaishou video results for a search keyword. Each result carries the video caption, the poster's IP location, a relevance score and a rank. The only required input is `keyword`.

### Use cases

- Collect the top Kuaishou videos that mention a brand or product name such as `OpenAI`.
- Sort results by `extInfo.ext_params.relevance_score` to find the videos that match a query best.
- Read captions and hashtags to see how a topic is described in Chinese-language short video.
- Page through results with `pcursor` to build a larger sample of videos for one keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes |  |
| `pcursor` | string | No | Pagination cursor, empty for first page, pass pcursor from previous response |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "debug_id": "2abea813",
  "debug_info": "gAAAAABq6Y7n8R1XKFkSSvMijb4ucgA8kO2L5gjP2pWwiLU2B7CC9oiq48Y_XvvhEsOQawxGgfz_5xDp…",
  "extParams": {
    "disablePhotoInsert": false,
    "dynamicShard": false,
    "isCreativeMode": false,
    "isShowPymkUserPhotos": true,
    "isShowScrollTopButton": false,
    "livePendantResource": "https://static.yximgs.com/udata/pkg/ks-nearby/nearby_living_tag/origin_196uxh2cv…",
    "outerStreamFetch": 10,
    "pageSingleDoubleStyle": 0,
    "rsRecoAfterPlayInterval": 2,
    "searchTaskParam": {},
    "sessionParams": "",
    "streamExtParams": "{\"single\":false,\"predict\":false,\"searchDetailCost\":{\"filterItem\":5,\"getView\":202…"
  },
  "host-name": "public-bjy-c26-kce-node-canary34.idchb1az2.hb1.kwaidc.com",
  "jumpToSlideMode": true,
  "llsid": "2006455553511323202",
  "mixFeeds": [
    {
      "atmosphereType": 0,
      "extInfo": {
        "clickTriggerInnerStream": false,
        "ext_params": {
          "relevance_score": "0.8565725"
        },
        "feedback": {
          "contentList": [
            {
              "id": "search_quality2",
              "text": " Poor quality"
            }
          ],
          "otherContent": {
            "id": "search_other",
            "text": "Other"
          },
          "unInterestList": [
            {
              "id": "search_seenlonger",
              "text": "Author Unlike"
            }
          ]
        },
        "recallSource": "0",
        "screenItemKey": "PHOTO$$1$$0",
        "showPlcFeatureEntry": false
      },
      "feed": {
        "adminTags": [],
        "bottomEntryInfo": {
          "bizExtraData": {},
          "bottomBizType": 14,
          "bottomStyleInfo": {
            "bottomStrongStyle": {
              "actionUrl": "",
              "backgroundColor": "",
              "bottomStrongStyleType": 0,
              "enableForceClose": false,
              "fontColor": "",
              "fontSize": 0,
              "iconHeight": 0,
              "iconUrl": ""
            },
            "bottomWeakStyle": {
              "actionUrl": "kwai://search?keyword=chatgpt的声音&sessionId=MzIwXzBfMTc5MzY5MTM2NjI2OV9fNDM2&sour…",
              "backgroundColor": "#333333",
              "bottomWeakStyleType": 0,
              "enableForceClose": false,
              "fontColor": "#FFFFFF",
              "fontSize": 13,
              "iconHeight": 48,
              "iconRightMargin": 4
            },
            "delayShowWeakStyle": false,
            "playVideoEndToStrongMillis": 0,
            "showStrongVideoCountdownMillis": 0,
            "showStrongVideoMillis": 0,
            "strongStyleCloseHideWeakStyle": false,
            "styleTriggers": []
          },
          "eventTrackData": {
            "all_source": "p2q_semantic_recall_v8,p2q_semantic_recall_v1",
            "entry_source": "search_entrance_featured_bottom_bar_search",
            "is_hotbar": "\u0000",
            "query_id": "e219f429b3379bf9ac5257cde3212009",
            "query_list_id": "MzIwXzBfMTc5MzY5MTM2NjI2OV9fNDM2",
            "query_name": "chatgpt的声音",
            "rel_score": "0.787150",
            "stg_recall_source": "p2q_semantic_recall_v1"
          }
        },
        "canShowQuickCommentGuide": true,
        "caption": "炸裂更新！亲测gpt5.6语音交互！无延迟真同传，翻译专业这下彻底玩完 #ChatGPT #OpenAI #人工智能 #翻译 ",
        "captionFontInfo": {
          "enableShow": true,
          "fontSize": 3,
          "rowHeight": 1.3
        },
        "captionIpLocation": "Sichuan",
        "captionSearchInfo": {
          "actionUrlList": [
            "kwai://search?keyword=gpt5%2E6&sessionId=MzIwXzBfMTc5MzY5MTM2NjI2OV9fNDM2&source…"
          ],
          "captionSearchType": 2,
          "dataSource": 0,
          "extParams": "{\"entrySourceList\":[\"search_entrance_cap_keyword\"]}\n",
          "offsetList": [
            7
          ],
          "queryIdList": [
            "914987353e931242e5fdc6246b9b0baa"
          ],
          "searchWordList": [
            "gpt5.6"
          ],
          "sessionId": "MzIwXzBf…"
        },
        "captionToComment": "炸裂更新！亲测gpt5.6语音交互！无延迟真同传，翻译专业这下彻底玩完 #ChatGPT #OpenAI #人工智能 #翻译 "
      },
      "feedLogCtx": {
        "stidContainer": "IoABMXwyMDA2NDU1NTUzNTExMzIzMjAyfHBob3RvOjUxODkyNzI4NzI5MzM1MDgzMTd8eyJwZyI6InNm…"
      },
      "isSingleColumnMode": false,
      "itemTransferInfo": "{\"refer_single_double_type\":0}",
      "itemType": 5,
      "rank": 0
    }
  ],
  "pcursor": "1",
  "portalFlag": true,
  "recoInterestFlag": false,
  "recoPcursor": "no_more",
  "responseCode": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `mixFeeds[]` | List of search results. Each item is one video entry in ranked order. |
| `mixFeeds[].rank` | Position of the result in the list, starting at `0`. |
| `mixFeeds[].feed.caption / mixFeeds[].feed.captionToComment` | Caption text of the video, including its hashtags. |
| `mixFeeds[].feed.captionIpLocation` | IP location shown for the poster, such as `Sichuan` or `Shanghai`. |
| `mixFeeds[].feed.captionSearchInfo.searchWordList[]` | Keywords found inside the caption that link to other searches. Present only on some items. |
| `mixFeeds[].extInfo.ext_params.relevance_score` | Relevance score of the video to the search keyword. It is returned as a string. |
| `mixFeeds[].feed.bottomEntryInfo.eventTrackData.query_name` | Suggested related search query shown under the video. |
| `mixFeeds[].feed.clearScreenSameAuthorCount` | Count attached to the video's author. Its exact meaning is not described in the response. |
| `pcursor` | Cursor value for the next page of results. |
| `recoPcursor` | Cursor for recommended results. The value `no_more` means there are none. |

### Notes

- Leave `pcursor` empty for the first page. Pass the `pcursor` value from the previous response to get the next page.
- The response also contains interface data such as colors, feedback options and `kwai://` links. You can ignore these for most uses.
- The response has no video ID field in the trimmed sample. To get full details for a video, use [Kuaishou Video Details by URL](/apis/kuaishou/app/one-video-by-url) with a video link.
- To search other content types, use [Kuaishou User Search (V2)](/apis/kuaishou/app/search-user-v2) or [Kuaishou Livestream Search](/apis/kuaishou/app/search-live).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-video-v2.json`](../../../../catalog/models/kuaishou/app/search-video-v2.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-video-v2
