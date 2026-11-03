# WeChat Search API: pricing, parameters and code examples

`wechat-search/v2/search` · data API · WeChat Search · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Search WeChat with one endpoint: official account articles, accounts, Channels videos, live streams, news and more. Filter by vertical, sort and publish time, with cursor pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-search/v2/search", "business_type": "article", "keyword": "南开大学 法学院 2026 博士 拟录取名单", "offset": 0, "publish_time": "all", "raw": false, "sort": "default"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-search/v2/search', {'business_type': 'article', 'keyword': '南开大学 法学院 2026 博士 拟录取名单', 'offset': 0, 'publish_time': 'all', 'raw': False, 'sort': 'default'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-search/v2/search", {
  "business_type": "article",
  "keyword": "南开大学 法学院 2026 博士 拟录取名单",
  "offset": 0,
  "publish_time": "all",
  "raw": false,
  "sort": "default"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-search/v2/search", sandbase.Params{
	"business_type": "article",
	"keyword": "南开大学 法学院 2026 博士 拟录取名单",
	"offset": 0,
	"publish_time": "all",
	"raw": false,
	"sort": "default",
})
```

Same call via the path form: `POST /v1/api/wechat-search/v2/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw search response; False=simplified parsing. default `true` |
| `sort` |  |  | Optional, default `default`. Sort (result page "sort" dropdown, common to all verticals) — `default`/0 (relevance) / `latest`/1 (newest) / `hot`/2 (most liked); string key or integer, invalid values rejected (400). default `"default"` |
| `cursor` |  |  | Optional. Pagination cursor. Leave empty for the first page; for the next page pass back the `cursor` returned in the previous response (repeat the same `sort` / `publish_time`), and use `continue_flag` to check…  |
| `offset` | integer |  | Optional, default 0 (>=0). Pass `0` for the first page; **use `cursor` to paginate — offset alone does not work** (it returns the first page every time). default `0`; range 0– |
| `keyword` | string | yes | Search keyword (1-100 chars)  |
| `publish_time` |  |  | Optional, default `all`. Publish time (result page "time" dropdown, common) — `all`/0 / `day`/1 / `week`/2 / `half_year`/3; string key or integer, invalid values rejected (400). default `"all"` |
| `business_type` | string |  | Optional, default `all`. Vertical string key, only the following are supported — `all` / `account` / `article` / `video` / `live_stream` / `moments` / `news` / `book` / `listen` / `image` / `encyclopedia` /… one of: `all`, `account`, `article`, `video`, `live_stream`, `moments`, `news`, `book`, `listen`, `image`, `encyclopedia`, `weixin_index`; default `"all"` |

## Details

Searches WeChat for a keyword and returns matching results from the vertical you choose with `business_type`, such as official account articles, accounts, Channels videos, live streams or news. It needs one input, `keyword`. Filters for sort order and publish time narrow the results.

### Use cases

- Track new official account articles about a brand or topic with `sort` set to `latest`.
- Collect article titles, snippets and links for a keyword to build a media monitoring feed.
- Find which official accounts publish most on a subject by reading the source name of each result.
- Limit a search to the last day or week with `publish_time` to check recent coverage.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-search/v2/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI", "business_type": "article", "raw": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (1-100 chars) |
| `business_type` | string | No | Optional, default `all`. Vertical string key, only the following are supported — `all` / `account` / `article` / `video` / `live_stream` / `moments` / `news` / `book` / `listen` / `image` / `encyclopedia` / `weixin_index |
| `cursor` | string | No | Optional. Pagination cursor. Leave empty for the first page; for the next page pass back the `cursor` returned in the previous response (repeat the same `sort` / `publish_time`), and use `continue_flag` to check whether  |
| `offset` | integer | No | Optional, default 0 (>=0). Pass `0` for the first page; **use `cursor` to paginate — offset alone does not work** (it returns the first page every time). |
| `publish_time` | string | No | Optional, default `all`. Publish time (result page "time" dropdown, common) — `all`/0 / `day`/1 / `week`/2 / `half_year`/3; string key or integer, invalid values rejected (400). |
| `raw` | boolean | No | Optional, default True. True=raw search response; False=simplified parsing. |
| `sort` | string | No | Optional, default `default`. Sort (result page "sort" dropdown, common to all verticals) — `default`/0 (relevance) / `latest`/1 (newest) / `hot`/2 (most liked); string key or integer, invalid values rejected (400). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_type": 2,
  "categories": null,
  "continue_flag": 1,
  "count": 38,
  "cursor": "hO0SuC6V7gEWmcGXQvsJ5wYWU4HyplzRxHlbePoYMtHLQY0vwElfi8d9LA-X87FzUQ7qOvpJTpv4SPHP…",
  "debug_id": "e5835ac5",
  "debug_info": "gAAAAABq6ZE7ot2LojpCJR304JESp7F_lWS4y7oOLUfqwVqQ9TIO8WNyZlsFYGWjOnT9jqzEk27z2sgB…",
  "items": [
    {
      "date": 1793688900,
      "desc": "<em class=\"highlight\">OpenAI</em>不是一家普通的公司。GPT-6 Astra、5亿年化营收、全球最大的AI用户入口，这些东西是真…",
      "docID": "5774067735576686510",
      "docType": 0,
      "doc_url": "http://mp.weixin.qq.com/s?__biz=MzU4ODQwNTIxMw==&mid=2247595037&idx=1&sn=8c2c2d5…",
      "itemShowType": 0,
      "mpScene": 7,
      "source": {
        "dateTime": "51分钟前",
        "title": "人工智能产业链union"
      },
      "src_type": 49,
      "thumbUrl": "https://mmbiz.qpic.cn/sz_mmbiz_jpg/9NdMVNE3GyZlQFyh70as5OnDBo1sPia1hpUW8PMhpoHnf…",
      "timestamp": 1793688900,
      "title": "【投融资】没人抢了：<em class=\"highlight\">OpenAI</em>的估值，一周之内自己砍掉了1500亿美元"
    }
  ],
  "keyword": "OpenAI",
  "no_more": null,
  "offset": 38,
  "total": 280
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].title` | Article title. Search matches are wrapped in `<em class="highlight">` tags. |
| `items[].desc` | Short text snippet of the article, with matched keywords wrapped in `<em class="highlight">` tags. |
| `items[].doc_url` | Link to the article on mp.weixin.qq.com. |
| `items[].source.title` | Name of the official account that published the article. |
| `items[].source.dateTime` | Relative publish time as shown on the WeChat result page, for example `51分钟前` or `1天前`. |
| `items[].timestamp / items[].date` | Publish time of the article as a Unix timestamp in seconds. |
| `items[].thumbUrl` | Cover image URL for the article. |
| `items[].docID` | Identifier of the result document. |
| `count / total` | `count` is the number of items in this page's result. `total` is the overall result count reported by the search. |
| `continue_flag / cursor` | `continue_flag` is `1` when more pages exist. `cursor` is the value to pass back to get the next page. |

### Notes

- To get the next page, pass the returned `cursor` back with the same `keyword`, `sort` and `publish_time`. Check `continue_flag` first.
- `offset` alone does not paginate. It returns the first page every time, so use `cursor`.
- `sort` accepts `default`, `latest` or `hot`. `publish_time` accepts `all`, `day`, `week` or `half_year`.
- To search only accounts, articles or Channels videos, see [WeChat Account Search](/apis/wechat-search/search-account), [WeChat Article Search](/apis/wechat-search/search-article) or [WeChat Search for Channels Videos](/apis/wechat-search/v2/search-videos).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Search for Channels Videos](/apis/wechat-search/v2/search-videos): Search WeChat Channels videos specifically (`video` vertical), with the result page's "duration" filter, "relevance/newest/most-liked" sort, and "time" dropdow…

---
Machine-readable: [`catalog/models/wechat-search/v2/search.json`](../../../../catalog/models/wechat-search/v2/search.json) · Store page: https://www.sandbase.ai/model/wechat-search/v2/search
