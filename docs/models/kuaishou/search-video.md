# Kuaishou Video Search API: pricing, parameters and code examples

`kuaishou/search-video` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search public Kuaishou videos by keyword with cursor-based pagination. Use it to discover relevant videos and continue through additional result pages.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/search-video", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/search-video', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/search-video", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/search-video", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/kuaishou/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor returned by the previous response. Omit or leave blank for the first page; maximum 256 characters.  |
| `keyword` | string | yes | The search keyword to find videos.  |

## Details

Returns a page of public Kuaishou video results for a search keyword. Each result is a feed item with caption, rank and some engagement data. The only required input is `keyword`.

### Use cases

- Find Kuaishou videos about a topic such as food and keep them in the order the platform returns.
- Collect captions and hashtags to see how creators describe a topic.
- Compare `collect_count` across results to spot videos that viewers save often.
- Page through results with `cursor` to build a larger set of videos for one keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The search keyword to find videos. |
| `cursor` | string | No | Pagination cursor returned by the previous response. Omit or leave blank for the first page; maximum 256 characters. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": "dks_7d02ffa7e12141128d4dcf3d058f9447",
  "mixFeeds": [
    {
      "atmosphereType": 0,
      "extInfo": {
        "clickTriggerInnerStream": false,
        "ext_params": {
          "relevance_score": "0.9887988"
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
        "screenItemKey": "PHOTO$$1$$0",
        "showPlcFeatureEntry": false,
        "showPoiInfo": false
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
              "actionUrl": "kwai://search?keyword=吃套餐&sessionId=MzIwXzBfMTc5MzY5MTM3NzE2OF9fMzI3Ng&source=se…",
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
            "all_source": "p2q_semantic_recall_v8,p2q_semantic_recall_v1,p2q_query_extend",
            "entry_source": "search_entrance_featured_bottom_bar_search",
            "is_hotbar": "\u0000",
            "query_id": "24e3f6c493a47d34d831d5623556fbd3",
            "query_list_id": "MzIwXzBfMTc5MzY5MTM3NzE2OF9fMzI3Ng",
            "query_name": "吃套餐",
            "rel_score": "0.736762",
            "stg_recall_source": "p2q_query_extend"
          }
        },
        "canShowQuickCommentGuide": true,
        "caption": "天天下雨都不知道更新什么了😔，希望不要挑剔…记录生活📝",
        "captionToComment": "天天下雨都不知道更新什么了😔，希望不要挑剔…记录生活📝",
        "clearScreenSameAuthorCount": 3218,
        "collect_count": 3558,
        "commentGuessSearch": {
          "displayPrefix": "相关搜索：",
          "extParams": "{\"all_source\":\"p2q_semantic_recall_v4,p2q_query_extend\",\"entrySource\":\"search_en…",
          "iconUrl": "https://ali2.a.kwimgs.com/udata/pkg/se-cdn/search_blue_ios_3x.png",
          "searchWord": "农村小石犯了什么罪",
          "searchWordMD5": "3b004fb7d70f1cbe187c5eb1f0108c83",
          "searchWordUrl": "kwai://search?keyword=农村小石犯了什么罪&sessionId=MzIwXzBfMTc5MzY5MTM3NzE2OF9fMzI3Ng&sou…",
          "sessionId": "MzIwXzBf…"
        }
      },
      "feedLogCtx": {
        "stidContainer": "IpgBMXwyMDEwMjY4MDU2MjYxMDU5MjgxfHBob3RvOjUyMjI3NjgyMTk1NjA4MDE4NzB8eyJwZyI6InNj…"
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
        "fontWeight": 500,
        "keywordList": [
          {
            "colorDark": "#F73B68",
            "colorLight": "#FE3666",
            "fontSize": 14,
            "fontWeight": 500,
            "keyword": "热评",
            "keywordMode": 1
          }
        ],
        "maxLines": 2
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cursor` | Pagination token for the next page. Send it back as the `cursor` parameter. |
| `mixFeeds[]` | List of search result items for the current page. |
| `mixFeeds[].feed.caption` | Video caption text, including hashtags and emoji. |
| `mixFeeds[].feed.collect_count` | Number of collects (saves) the video has. It appears only on some items. |
| `mixFeeds[].feed.clearScreenSameAuthorCount` | A count tied to the same author as the video. The response does not explain it further. |
| `mixFeeds[].rank` | Position of the item in the result list, starting at `0`. |
| `mixFeeds[].extInfo.ext_params.relevance_score` | Relevance score of the item for the keyword, as a string such as `0.9887988`. |
| `mixFeeds[].feed.captionSearchInfo.searchWordList[]` | Search phrases the platform extracted from the caption. |
| `mixFeeds[].feed.bottomEntryInfo.eventTrackData.query_name` | Suggested related search phrase shown with the video, such as `吃套餐`. |
| `mixFeeds[].itemType` | Numeric item type code. All items in this sample use `5`. |

### Notes

- Omit `cursor` for the first page. For the next page, pass the top-level `cursor` value from the previous response, for example `dks_7d02ffa7e12141128d4dcf3d058f9447`. The maximum length is 256 characters.
- The response is the platform's original data structure. Many fields are interface and tracking settings, so read the `feed` object first.
- For a newer result format, try [Kuaishou Video Search (V2)](/apis/kuaishou/app/search-video-v2).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/kuaishou/search-video.json`](../../../catalog/models/kuaishou/search-video.json) · Store page: https://www.sandbase.ai/model/kuaishou/search-video
