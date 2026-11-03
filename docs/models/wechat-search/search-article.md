# WeChat Article Search API: pricing, parameters and code examples

`wechat-search/search-article` · data API · WeChat Search · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.114286 per call · **Modes:** sync

Search WeChat Official Account articles by keyword with publish-time and sort filters plus page, offset, and continuation-state pagination.

## Pricing

- **$0.114286 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-search/search-article", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-search/search-article', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-search/search-article", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-search/search-article", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-search/search-article` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Search result offset returned by the previous response. Use 0 for the first page. default `0` |
| `keyword` | string | yes | Search keyword for WeChat Official Account articles.  |
| `sortType` | string |  | Sort order for WeChat Official Account article web search results. one of: `COMPREHENSIVE`, `LATEST`, `HOT`; default `"COMPREHENSIVE"` |
| `currentPage` | integer |  | Current page number starting from 1 for WeChat web search pagination. default `1` |
| `publishTimeType` | string |  | Publish time filter for WeChat Official Account article web search. one of: `ALL`, `ONE_DAY`, `SEVEN_DAYS`, `HALF_YEAR`; default `"ALL"` |

## Details

This API returns WeChat Official Account articles that match a keyword. Each result has a snippet with the keyword highlighted, a publish timestamp, and a link to the article. The only required input is `keyword`.

### Use cases

- Track how Official Accounts cover a topic such as AI by searching a keyword with the `LATEST` sort.
- Collect article links for a keyword to build a reading list or a content archive.
- Find the most talked-about articles on a subject in the past week with `SEVEN_DAYS` and the `HOT` sort.
- Check which phrases appear around a keyword by reading the highlighted snippets in `desc`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-search/search-article" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword for WeChat Official Account articles. |
| `currentPage` | integer | No | Current page number starting from 1 for WeChat web search pagination. |
| `offset` | integer | No | Search result offset returned by the previous response. Use 0 for the first page. |
| `publishTimeType` | string | No | Publish time filter for WeChat Official Account article web search. |
| `sortType` | string | No | Sort order for WeChat Official Account article web search results. |

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
      "boxID": "0x2-0-15529639845716571706",
      "boxPos": 1,
      "boxPosMerge": 1,
      "count": 1,
      "items": [
        {
          "date": 1793685626,
          "desc": "他说，<em class=\"highlight\">人工智能</em>已经开始改变人们的工作方式。ChatGPT等工具帮助人们提高效率，也有越来越多的人开始将<e…",
          "docID": "15529639845716571706",
          "docType": 0,
          "doc_url": "http://mp.weixin.qq.com/s?__biz=MzA5MjA5MTEwNg==&mid=2656751197&idx=7&sn=ed85b9f…",
          "itemShowType": 0,
          "mpScene": 7,
          "reportId": "15529639845716571706:mp:887366"
        }
      ],
      "real_type": 2,
      "resultType": 0,
      "subType": 0,
      "totalCount": 242,
      "type": 2,
      "useNativeRender": false
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
  "offset": 18
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].items[].doc_url` | Link to the article on mp.weixin.qq.com. |
| `data[].items[].desc` | Text snippet from the article. Matches of the keyword are wrapped in `<em class="highlight">` tags. |
| `data[].items[].date` | Article publish time as a Unix timestamp in seconds. |
| `data[].items[].docID / data[].items[].reportId` | Identifiers for the article. `reportId` combines the `docID` with a suffix. |
| `data[].totalCount` | Total number of matching results reported for the search. It is the same value in every box. |
| `data[].boxPos` | Position of the result box in the result list, starting at 1. |
| `offset` | Offset to send as `offset` in the next request to get the following page. |
| `pageNumber` | Page number the response refers to. |
| `continueFlag` | Flag set to `1` in this response. |
| `cookies` | JSON string holding continuation state for the search, including `box_offset`. |
| `searchID` | Identifier for this search request. |

### Notes

- Set `publishTimeType` to `ALL`, `ONE_DAY`, `SEVEN_DAYS` or `HALF_YEAR`. Set `sortType` to `LATEST` or `HOT` to change the result order. If you omit it, the default sort applies.
- For the next page, send the `offset` value from the previous response together with a higher `currentPage`. Use `offset` 0 for the first page.
- Each element of `data` is a result box and holds its articles in `items`. In this response each box holds one article.
- To search accounts instead of articles, use [WeChat Account Search](/apis/wechat-search/search-account).

### Pricing

$0.114286 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-search/search-article.json`](../../../catalog/models/wechat-search/search-article.json) · Store page: https://www.sandbase.ai/model/wechat-search/search-article
