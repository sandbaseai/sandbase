# WeChat Channels Video Search API: pricing, parameters and code examples

`wechat-channels/search-video` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.114286 per call · **Modes:** sync

Search WeChat Channels videos by keyword with publish-time, sort, page, offset, and continuation-state controls. Use it to find recent or ordered video results and continue web-search pages.

## Pricing

- **$0.114286 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/search-video", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/search-video', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/search-video", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/search-video", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Search result offset returned by the previous WeChat Channels search response. Use 0 for the first page. default `0` |
| `keyword` | string | yes | Search keyword for WeChat Channels video results.  |
| `sortType` | string |  | Sort order for WeChat Channels video search results. one of: `COMPREHENSIVE`, `LATEST`, `HOT`; default `"COMPREHENSIVE"` |
| `currentPage` | integer |  | Current page number starting from 1 for WeChat Channels web search pagination. default `1` |
| `publishTimeType` | string |  | Publish time filter for WeChat Channels video web search. one of: `ALL`, `ONE_DAY`, `SEVEN_DAYS`, `HALF_YEAR`; default `"ALL"` |

## Details

Returns WeChat Channels video search results for a keyword. Each result has a thumbnail, duration, relative post time, and IDs. The only required input is `keyword`. You can also filter by publish time, change the sort order, and page through results.

### Use cases

- Find the newest WeChat Channels videos about a topic by setting `sortType` to `LATEST`.
- Collect `exportId` values for videos on a keyword to pass to other WeChat Channels APIs.
- Track which videos for a keyword are flagged as hot in the results.
- Page through results for a keyword and build a list of video thumbnails and durations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword for WeChat Channels video results. |
| `currentPage` | integer | No | Current page number starting from 1 for WeChat Channels web search pagination. |
| `offset` | integer | No | Search result offset returned by the previous WeChat Channels search response. Use 0 for the first page. |
| `publishTimeType` | string | No | Publish time filter for WeChat Channels video web search. |
| `sortType` | string | No | Sort order for WeChat Channels video search results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "category": [
    {
      "selected": 1,
      "type": 0,
      "word": "全部"
    }
  ],
  "continueFlag": 1,
  "cookies": "{\"box_of…",
  "data": [
    {
      "subBoxes": [
        {
          "boxID": "0x80000000000-1-7530317014626261982",
          "boxMergeTag": 0,
          "boxMergeType": 107,
          "boxMergeValue": 1,
          "boxPos": 1,
          "boxPosMerge": 1,
          "count": 1,
          "items": [
            {
              "dateTime": "24分钟前",
              "docID": "finderobjv0UP6MxTQvwWPRuGhk22QE9GBai7N8Taj+Z0zTJE2Z3o0=",
              "duration": "00:16",
              "exportId": "export/UzFfBgAAxNuCbEAoaFONk8zT4DCKQA_XKca_aXvLDm97NtOzoQ",
              "hashDocID": "7530317014626261982",
              "image": "https://findermp.video.qq.com/251/20304/stodownload?encfilekey=KGDRibp2wkicLzqUk…",
              "isHot": true,
              "jumpInfo": {
                "extInfo": "{\"behavior\":[\"report_feed_read\"],\"encryptedObjectId\":\"export/UzFfBgAAxNuCbEAoaFO…",
                "jumpType": 9
              }
            }
          ]
        }
      ],
      "type": 107
    }
  ],
  "direction": 2,
  "enableQuestionClosely": false,
  "experiment": [
    {
      "key": "mmsearch_live_double_auto_play_exp",
      "value": "1"
    }
  ],
  "isAutoPlayVideo": 1,
  "isDivide": 1,
  "isHomePage": 1,
  "lang": "zh_CN",
  "offset": 12
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].subBoxes[].items[].docID / hashDocID` | Identifiers for the result video. `hashDocID` is a numeric string that also appears in the matching `boxID`. |
| `data[].subBoxes[].items[].exportId` | Export ID for the video, in the form `export/...`. Use it to look up the video in other WeChat Channels APIs. |
| `data[].subBoxes[].items[].duration` | Video length as text, for example `00:16`. |
| `data[].subBoxes[].items[].dateTime` | Relative post time as shown in the app, for example `24分钟前` (24 minutes ago). |
| `data[].subBoxes[].items[].pubTime` | Publish time as a Unix timestamp in seconds. Not every item has it. |
| `data[].subBoxes[].items[].image` | URL of the video thumbnail. |
| `data[].subBoxes[].items[].isHot` | `true` when the platform marks the video as hot. Most items omit it. |
| `data[].subBoxes[].items[].jumpInfo.extInfo` | JSON string with the data the app uses to open the video, including `encryptedObjectId`. |
| `continueFlag` | `1` in this response, which shows that more results can be fetched. |
| `offset / pageNumber / cookies` | Paging state for the next request. `offset` was `12` and `pageNumber` was `2` in this response. |

### Notes

- For the first page, send `offset` as `0` and `currentPage` as `1`. For the next page, send the `offset` value from the previous response and increase `currentPage`.
- The `cookies` string in the response carries continuation state, including `box_offset`.
- Use the `searchID` and `query` fields to match a response to the search that produced it.
- To get details for a result, pass its `exportId` to [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail) or [WeChat Channels Video Metrics](/apis/wechat-channels/video-metrics).

### Pricing

$0.114286 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/search-video.json`](../../../catalog/models/wechat-channels/search-video.json) · Store page: https://www.sandbase.ai/model/wechat-channels/search-video
