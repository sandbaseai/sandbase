# WeChat Search API: pricing, parameters and code examples

`wechat-search/v2/search` · data API · WeChat Search · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Search WeChat with one endpoint: official account articles, accounts, Channels videos, live streams, news and more. Filter by vertical, sort and publish time, with cursor pagination.

## Pricing

- **$0.015 per call** (USD)
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

Run a WeChat universal search for a keyword. Choose the vertical with `business_type` (articles, accounts, videos, live streams, news, and more) and get titles, sources, timestamps and links.

### Use cases

- Find WeChat official account articles about a topic or brand.
- Discover official accounts and Channels creators in a niche.
- Monitor new WeChat coverage with `sort=latest` and `publish_time`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-search/v2/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI", "business_type": "article", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (1-100 chars) |
| `raw` | boolean | No | Optional, default True. |
| `sort` | string | No | Optional, default `default`. |
| `cursor` | string | No | Optional. |
| `offset` | integer | No | Optional, default 0 (>=0). |
| `publish_time` | string | No | Optional, default `all`. |
| `business_type` | string | No | Optional, default `all`. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "keyword": "OpenAI",
  "business_type": 2,
  "count": 38,
  "total": 315,
  "continue_flag": 1,
  "cursor": "<next page cursor>",
  "items": [
    {
      "title": "OpenAI「疯狂28天」首日，这都发了些啥啊…",
      "source": {
        "dateTime": "4小时前",
        "title": "量子位"
      },
      "timestamp": 1791260267,
      "doc_url": "http://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247931194&idx=1…"
    }
  ]
}
```

### Notes

- Paginate with `cursor`: pass back the `cursor` from the previous response with the same keyword and filters.
- Set `raw` to `false` for a simplified response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Search for Channels Videos](/model/wechat-search/v2/search-videos): Search WeChat Channels videos specifically (`video` vertical), with the result page's "duration" filter, "relevance/newest/most-liked" sort, and "time" dropdow…

---
Machine-readable: [`catalog/models/wechat-search/v2/search.json`](../../../../catalog/models/wechat-search/v2/search.json) · Store page: https://www.sandbase.ai/model/wechat-search/v2/search
