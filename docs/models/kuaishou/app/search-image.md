# Kuaishou Image Post Search API: pricing, parameters and code examples

`kuaishou/app/search-image` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Searches Kuaishou image posts matching a specified search term. Returns feed details including captions, engagement metrics, and pagination tokens.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-image", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-image', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-image", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-image", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-image` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | Cursor, empty for first page default `""` |

## Details

Returns Kuaishou image posts that match a search term. Each result includes the caption, the poster's IP location, a collect count, and a relevance score. You pass a `keyword` and can pass a `pcursor` to page through results.

### Use cases

- Collect image posts that mention a brand or topic, such as `OpenAI`, and read their captions and hashtags.
- Rank posts for a keyword by `relevance_score` to pick the closest matches first.
- Compare `collect_count` across posts to see which image posts people save most.
- Group results by `captionIpLocation` to see which regions post about a topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-image" \
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
  "debug_id": "4151e0f9",
  "debug_info": "gAAAAABq6Y7lTZtazFcoSV1itJOzNbNva6Oxe8PEDJ9cUUJ2VSCUI9Hj-ZrRU1nB4xQNNI-opDIkkL7x…",
  "extParams": {
    "disablePhotoInsert": false,
    "dynamicShard": false,
    "isCreativeMode": false,
    "isShowPymkUserPhotos": true,
    "isShowScrollTopButton": false,
    "livePendantResource": "https://static.yximgs.com/udata/pkg/ks-nearby/nearby_living_tag/origin_196uxh2cv…",
    "outerStreamFetch": 6,
    "pageSingleDoubleStyle": 0,
    "rsRecoAfterPlayInterval": 2,
    "searchTaskParam": {},
    "sessionParams": "",
    "streamExtParams": "{\"single\":false,\"predict\":false,\"searchDetailCost\":{\"filterItem\":14,\"getView\":22…"
  },
  "feeds": [
    {
      "atmosphereType": 0,
      "extInfo": {
        "clickTriggerInnerStream": false,
        "ext_params": {
          "relevance_score": "0.89858866"
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
              "actionUrl": "kwai://search?keyword=黄仁勋ai舞蹈&sessionId=MzIwXzBfMTc5MzY5MTM2NDk1Ml9fMzUwNw&sourc…",
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
            "all_source": "p2q_semantic_recall_v8",
            "entry_source": "search_entrance_featured_bottom_bar_search",
            "is_hotbar": "\u0000",
            "query_id": "fc079611e9eff69b5d6924befd4e9eff",
            "query_list_id": "MzIwXzBfMTc5MzY5MTM2NDk1Ml9fMzUwNw",
            "query_name": "黄仁勋ai舞蹈",
            "rel_score": "0.415438",
            "stg_recall_source": "p2q_semantic_recall_v8"
          }
        },
        "canShowQuickCommentGuide": true,
        "caption": "那一刻，ai的齿轮正在悄然转动。 #黄仁勋 #openai #chatgpt",
        "captionIpLocation": "Jiangxi",
        "captionToComment": "那一刻，ai的齿轮正在悄然转动。 #黄仁勋 #openai #chatgpt",
        "clearScreenSameAuthorCount": 13,
        "collect_count": 207
      },
      "feedLogCtx": {
        "logParams": "{\"SEARCH\":{\"dr_type\":\"IMAGE_ATLAS\",\"dr_id\":\"5201939237396139534\",\"dr_rank\":0,\"dr…",
        "stidContainer": "In8xfDIwMTAxOTYwMzM3Nzc1ODU2MDF8cGhvdG86NTIwMTkzOTIzNzM5NjEzOTUzNHx7InBnIjoic2ki…"
      },
      "isSingleColumnMode": false,
      "itemTransferInfo": "{\"refer_single_double_type\":0}",
      "itemType": 5,
      "rank": 0
    }
  ],
  "host-name": "public-bjx-c97-kce-node107.idchb1az1.hb1.kwaidc.com",
  "llsid": "2010196033777585601",
  "pcursor": "1",
  "portalFlag": true,
  "recoInterestFlag": false,
  "recoPcursor": "no_more",
  "requestId": "MTRfMF8xNzkzNjkxMzY0NTEwX184NjAw",
  "responseCode": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `feeds[]` | One search result per item. Each item holds the post data under `feed` and search metadata around it. |
| `feeds[].rank` | Position of the result in the search list, starting at `0`. Values can skip numbers, so do not assume they are continuous. |
| `feeds[].feed.caption` | Text of the post, including hashtags. Long captions end with an ellipsis. |
| `feeds[].feed.captionIpLocation` | IP location label of the poster, such as `Jiangxi` or `Guangdong`. |
| `feeds[].feed.collect_count` | Number of times the post has been collected. |
| `feeds[].extInfo.ext_params.relevance_score` | Relevance score for the post against the search term, returned as a string such as `0.89858866`. |
| `feeds[].feedLogCtx.logParams` | JSON string. Inside it, `dr_id` holds the post ID, `dr_author_id` holds the author ID, and `dr_type` is `IMAGE_ATLAS` for these image posts. |
| `feeds[].feed.commentInfo` | Comment settings for the post. It appears on some results only. |
| `pcursor` | Cursor for the next page. The sample response returns `1`. |
| `recoPcursor` | Cursor for recommended results. The value `no_more` means there are none left. |

### Notes

- Leave `pcursor` empty for the first page. Send the `pcursor` value from the response to get the next page.
- The `keyword` value is free text, for example `OpenAI`.
- `dr_id` and `dr_author_id` are inside the `feeds[].feedLogCtx.logParams` string. Parse that string as JSON to read them.
- To search videos instead of image posts, use [Kuaishou Video Search (V2)](/apis/kuaishou/app/search-video-v2).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-image.json`](../../../../catalog/models/kuaishou/app/search-image.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-image
