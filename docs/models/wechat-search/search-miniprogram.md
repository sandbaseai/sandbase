# WeChat Mini Program Search API: pricing, parameters and code examples

`wechat-search/search-miniprogram` · data API · WeChat Search · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.114286 per call · **Modes:** sync

Search WeChat Mini Programs by keyword with page, offset, and continuation-state pagination. Use it to discover mini programs related to a brand, service, topic, or product.

## Pricing

- **$0.114286 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-search/search-miniprogram", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-search/search-miniprogram', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-search/search-miniprogram", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-search/search-miniprogram", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-search/search-miniprogram` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Search result offset returned by the previous response. Use 0 for the first page. default `0` |
| `keyword` | string | yes | Search keyword for WeChat mini program web search.  |
| `currentPage` | integer |  | Current page number starting from 1 for WeChat web search pagination. default `1` |

## Details

This API returns WeChat Mini Programs that match a search keyword. Each result has a short description, an icon URL, and the app ID and original ID needed to open the mini program. Send a `keyword`, and optionally `currentPage` and `offset` for paging.

### Use cases

- Find mini programs that match a brand name or service keyword.
- Collect mini program app IDs for a topic such as AI assistants to build a competitor list.
- Read result descriptions to see how mini programs describe their features for a given keyword.
- Check which mini programs appear for a term and in what order.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-search/search-miniprogram" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword for WeChat mini program web search. |
| `currentPage` | integer | No | Current page number starting from 1 for WeChat web search pagination. |
| `offset` | integer | No | Search result offset returned by the previous response. Use 0 for the first page. |

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
  "continueFlag": 1,
  "cookies": "{\"box_of…",
  "data": [
    {
      "boxExtraInfo": {
        "real_type": 262208,
        "resultType": 0,
        "subType": 0,
        "title": "小程序"
      },
      "subBoxes": [
        {
          "boxExtraInfo": null,
          "boxID": "split-0x40-0-3978567686",
          "boxMergeTag": 0,
          "boxMergeType": 109,
          "boxMergeValue": 3,
          "boxPos": 1,
          "boxPosMerge": 1,
          "count": 1
        }
      ],
      "type": 109
    }
  ],
  "direction": 2,
  "enableQuestionClosely": false,
  "experiment": [
    {
      "key": "mmsearch_shopping_cart_entry",
      "value": "1"
    }
  ],
  "isAutoPlayVideo": 1,
  "isDivide": 0,
  "isHomePage": 0,
  "lang": "zh_CN",
  "offset": 20
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].subBoxes[].items[].jumpInfo.appID` | The mini program app ID, for example `wxdb0efd7c7855e881`. |
| `data[].subBoxes[].items[].jumpInfo.userName` | The mini program original ID, ending in `@app`. |
| `data[].subBoxes[].items[].desc` | The mini program description. Matched keywords are wrapped in `<em class="highlight">` tags. |
| `data[].subBoxes[].items[].iconUrl` | URL of the mini program icon image. |
| `data[].subBoxes[].items[].docID` | The result document ID. It matches the number at the end of the parent `boxID`. |
| `data[].subBoxes[].boxPos` | The position of the result box in the list, starting at 1. |
| `offset` | The offset to send in the next request to get the following page. |
| `continueFlag` | A value of `1` appears in this response. Its key name suggests more results can be fetched. |
| `cookies` | A JSON string with the continuation state for the search, including `box_offset` and `cookies_buffer`. |
| `query / pageNumber / searchID` | The keyword that was searched, the page number of this response, and the ID of this search. |

### Notes

- Use any word or phrase as `keyword`. The example uses `人工智能`.
- For the first page, send `currentPage` as `1` and `offset` as `0`. For the next page, raise `currentPage` and send the `offset` value from the previous response.
- The first entry in `data[].subBoxes[]` can be a box with no `items`. Skip boxes that have no `items` when you read results.
- To search other WeChat content, use [WeChat Account Search](/apis/wechat-search/search-account) or [WeChat Article Search](/apis/wechat-search/search-article).

### Pricing

$0.114286 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-search/search-miniprogram.json`](../../../catalog/models/wechat-search/search-miniprogram.json) · Store page: https://www.sandbase.ai/model/wechat-search/search-miniprogram
