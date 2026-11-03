# Kuaishou Comprehensive Search API: pricing, parameters and code examples

`kuaishou/app/search-comprehensive` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns aggregated search feeds across videos and users on Kuaishou, with filtering options for duration, sort order, and release timeframe.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-comprehensive", "keyword": "汽车之家"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-comprehensive', {'keyword': '汽车之家'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-comprehensive", {
  "keyword": "汽车之家"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-comprehensive", sandbase.Params{
	"keyword": "汽车之家",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-comprehensive` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | 分页游标/Pagination cursor  |
| `duration` | string |  | Duration filter one of: `all`, `under_1_min`, `1_to_5_min`, `over_5_min`; default `"all"` |
| `sort_type` | string |  | Sort type one of: `all`, `newest`, `most_likes`; default `"all"` |
| `publish_time` | string |  | Publish time filter one of: `all`, `one_day`, `one_week`, `one_month`; default `"all"` |

## Details

Returns a mixed Kuaishou search feed for a keyword. The feed holds video posts and other result cards such as encyclopedia boxes. The only required input is `keyword`.

### Use cases

- Collect Kuaishou videos that mention a brand such as OpenAI, with captions and save counts.
- Rank search results by `relevance_score` to find the posts that match a keyword best.
- Read the search filter labels and related search words to see how Kuaishou groups a topic.
- Pull the encyclopedia card for a company or person to get a short description and basic facts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-comprehensive" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes |  |
| `duration` | string | No | Duration filter |
| `pcursor` | string | No |  |
| `publish_time` | string | No | Publish time filter |
| `sort_type` | string | No | Sort type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "costInfo": {
    "S_A": 746,
    "S_A_RE": 466,
    "S_A_RPC": 150
  },
  "extParams": {
    "chatFlag": false,
    "dayConfig": 3,
    "descPageUrl": "disableTriggerRecoPageList=false]]]https://ppg.viviv.com/doodle/VqedGfkY.html?hy…",
    "disablePhotoInsert": false,
    "doubleColumnBeginIndex": 0,
    "dynamicShard": false,
    "hasGradientBg": false,
    "hashTagSingle": false,
    "isCreativeMode": false,
    "isOpenTab": 0,
    "isShowPymkUserPhotos": true,
    "isShowScrollTopButton": false
  },
  "host-name": "public-bjx-c87-kce-node114.idchb1az1.hb1.kwaidc.com",
  "isRecommendResult": false,
  "jumpToSlideMode": true,
  "llsid": "2006449988689940162",
  "mixFeeds": [
    {
      "atmosphereType": 0,
      "extInfo": {
        "clickTriggerInnerStream": false,
        "ext_params": {
          "relevance_score": "0.95159405"
        },
        "feedback": {
          "contentList": [
            {
              "id": "search_quality2",
              "text": "内容违规、血腥、低俗"
            }
          ],
          "otherContent": {
            "id": "search_other",
            "text": "其他"
          },
          "unInterestList": [
            {
              "id": "search_seenlonger",
              "text": "不再看到该作者"
            }
          ]
        },
        "recallSource": "0",
        "recoBgColor": "#CCFFFFFF",
        "recoIconUrl": [
          {
            "cdn": "p66-plat.ndcjl.com",
            "url": "https://p66-plat.ndcjl.com/udata/pkg/se-cdn/collect_01.png"
          }
        ],
        "recoTextColor": "#222222",
        "recoType": 100
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
              "actionUrl": "kwai://search?keyword=正版chatgpt下载入口&sessionId=MzIwXzBfMTc5MzY5MTM1OTE3MV9fNjA2Mw…",
              "backgroundColor": "#333333",
              "bottomWeakStyleType": 0,
              "enableForceClose": false,
              "fontColor": "#FFFFFF",
              "fontSize": 13,
              "iconHeight": 48,
              "iconRightMargin": 4.0
            },
            "delayShowWeakStyle": false,
            "playVideoEndToStrongMillis": 0,
            "showStrongVideoCountdownMillis": 0,
            "showStrongVideoMillis": 0,
            "strongStyleCloseHideWeakStyle": false,
            "styleTriggers": []
          },
          "eventTrackData": {
            "all_source": "p2q_query_extend",
            "entry_source": "search_entrance_featured_bottom_bar_search",
            "is_hotbar": "\u0000",
            "query_id": "bbd83c67a5b7000bfc8bdd163885933a",
            "query_list_id": "MzIwXzBfMTc5MzY5MTM1OTE3MV9fNjA2Mw",
            "query_name": "正版chatgpt下载入口",
            "rel_score": "0.082518",
            "stg_recall_source": "p2q_query_extend"
          }
        },
        "canShowQuickCommentGuide": true,
        "caption": "世界上最强大的AI排名，2026年\r\n#世界之最  #AI  #大模型  #deepseek",
        "captionSpliceAnnotation": "(来源：其他平台)",
        "captionToComment": "世界上最强大的AI排名，2026年 \n#世界之最 #AI #大模型 #deepseek",
        "clearScreenSameAuthorCount": 958,
        "collect_count": 5294
      },
      "feedLogCtx": {
        "stidContainer": "IpgBMXwyMDA2NDQ5OTg4Njg5OTQwMTYyfHBob3RvOjUyNDgxMDExMjc4OTEyMjEzNzl8eyJwZyI6InNj…"
      },
      "isSingleColumnMode": false,
      "itemTransferInfo": "{\"refer_single_double_type\":0}",
      "itemType": 5,
      "rank": 0,
      "searchTitleInfo": {
        "actionType": 1,
        "colorDark": "#E6E6E6",
        "colorLight": "#222222",
        "enableBgColor": true,
        "fontSize": 14,
        "fontWeight": 400,
        "keywordList": [
          {
            "colorDark": "#F73B68",
            "colorLight": "#FE3666",
            "fontSize": 14,
            "fontWeight": 400,
            "keyword": "热评",
            "keywordMode": 1
          }
        ],
        "maxLines": 2
      }
    }
  ],
  "pcursor": "1",
  "portalFlag": true,
  "recoInterestFlag": false,
  "recoPcursor": "no_more",
  "recoPymkFlag": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `mixFeeds[]` | Result items in display order. Each item is a video post or a special card, such as an encyclopedia box. |
| `mixFeeds[].rank` | Position of the item in the result list, starting at 0. |
| `mixFeeds[].itemType` | Type code of the item. The sample shows `5` for video posts and `25` for an encyclopedia card. |
| `mixFeeds[].feed.caption` | Caption text of the video, including hashtags. |
| `mixFeeds[].feed.collect_count` | Number of times the video was saved (collected). |
| `mixFeeds[].extInfo.ext_params.relevance_score` | Relevance of the video to the keyword, given as a decimal string. |
| `mixFeeds[].feed.commentGuessSearch.searchWord` | Related search phrase shown with the video. |
| `mixFeeds[].mixKbox[].kboxObject.TKDatas[].jsonContent.desc` | Short description in an encyclopedia card, for example a company summary. |
| `extParams.multiFilterModels[].filterModels[]` | Filter options Kuaishou offers for sort order, publish time and duration. Each option has a `name` and a `filterType` code. |
| `llsid` | ID of this search session. |

### Notes

- Send `pcursor` to page through results. Use the cursor value from a previous response.
- Use `sort_type`, `publish_time` and `duration` to filter. Allowed values are in the parameter list, such as `most_likes`, `one_week` and `under_1_min`.
- Not every item in `mixFeeds` is a video. Check `itemType` before you read `feed` fields.
- To get full details for a video found here, call [Kuaishou Video Details (V1)](/apis/kuaishou/app/one-video).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-comprehensive.json`](../../../../catalog/models/kuaishou/app/search-comprehensive.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-comprehensive
