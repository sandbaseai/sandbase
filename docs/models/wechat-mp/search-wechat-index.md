# WeChat MP WeChat Index Search API: pricing, parameters and code examples

`wechat-mp/search-wechat-index` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.114286 per call · **Modes:** sync

Query WeChat Index for a keyword. Use it to examine trend interest within WeChat before planning content, campaigns, or further article research.

## Pricing

- **$0.114286 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/search-wechat-index", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/search-wechat-index', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/search-wechat-index", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/search-wechat-index", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/search-wechat-index` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Keyword used to query WeChat Index trend signals.  |

## Details

This API returns WeChat Index data for a keyword. The main result is a daily series of index values for that keyword, plus the search page metadata around it. It needs one input, `keyword`.

### Use cases

- Compare daily WeChat Index values for a topic such as `人工智能` before you schedule content.
- Chart the day-by-day index series to spot rises and drops in interest around a campaign.
- Pull the index series for several candidate keywords and rank them by their recent values.
- Read the mini program link in `jumpInfo` to open the full WeChat Index detail page for the same keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/search-wechat-index" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword used to query WeChat Index trend signals. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "category": [
    {
      "type": 0,
      "word": "全部"
    }
  ],
  "continueFlag": 0,
  "cookies": "{\"box_of…",
  "data": [
    {
      "boxID": "0x40000-15048-",
      "boxPos": 1,
      "boxPosMerge": 1,
      "count": 1,
      "items": [
        {
          "docID": "1-7123206500956315942",
          "itemInfo": {
            "data": [
              {
                "index": "57957241",
                "timestamp": 1791043200
              }
            ],
            "title": "人工智能 - 微信指数",
            "type": 1058
          },
          "jumpInfo": {
            "jumpType": 2,
            "reportId": "chart:chart:410447",
            "userName": "gh_935b85261f35@app",
            "weappUrl": "/page/detail/detail?calculate_word=人工智能"
          },
          "source": {
            "iconUrl": "http://mmbiz.qpic.cn/mmbiz_png/uic3vZ5pI29sdd0tUo5t4pxmJMsMO9iaxM8EOxTX1VUAWjQib…",
            "title": "微信指数"
          },
          "title": ""
        }
      ],
      "real_type": 262144,
      "subType": 15048,
      "type": 52,
      "useNativeRender": false
    }
  ],
  "direction": 2,
  "enableQuestionClosely": false,
  "experiment": [
    {
      "key": "mmsearch_topqa_mergebox_combine",
      "value": "1"
    }
  ],
  "isAutoPlayVideo": 1,
  "isDivide": 0,
  "isHomePage": 0,
  "lang": "zh_CN",
  "nomoreText": "没有更多的搜索结果"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].items[].itemInfo.title` | Title of the index card. It has the form `<keyword> - 微信指数`. |
| `data[].items[].itemInfo.data[].index` | WeChat Index value for one day. It comes as a string, so convert it to a number before you chart or compare it. |
| `data[].items[].itemInfo.data[].timestamp` | Unix timestamp in seconds for the day of the matching `index` value. Entries are one day apart. |
| `data[].items[].jumpInfo.weappUrl` | Mini program page path for the full index detail of the keyword. The keyword appears in the `calculate_word` query value. |
| `data[].items[].source.title` | Name of the source shown on the card, `微信指数`. |
| `data[].items[].docID` | ID of the index result item. |
| `category[].type / category[].word` | Result tabs shown with the search, such as `全部`, `视频号` and `文章`. `type` is the numeric code and `word` is the label. |
| `query` | The keyword that was searched. |
| `searchID` | ID of this search request. |
| `offset / pageNumber / continueFlag` | Paging state of the search result. In the sample, `continueFlag` is `0`, `pageNumber` is `1` and `offset` is `20`. |

### Notes

- Send the exact text you want to look up in `keyword`. Chinese keywords work, as in the example `人工智能`.
- Each `timestamp` is in Unix seconds, and each `index` is a string.
- To find related keywords to test, call [WeChat MP Search Suggestions](/apis/wechat-mp/search-suggestions).
- To research articles on the same topic, call [WeChat MP Related Articles](/apis/wechat-mp/v2/related-articles).

### Pricing

$0.114286 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/search-wechat-index.json`](../../../catalog/models/wechat-mp/search-wechat-index.json) · Store page: https://www.sandbase.ai/model/wechat-mp/search-wechat-index
