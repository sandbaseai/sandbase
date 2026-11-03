# WeChat Search for Channels Videos API: pricing, parameters and code examples

`wechat-search/v2/search-videos` · data API · WeChat Search · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Search WeChat Channels videos by keyword with duration, sort (relevance, newest, most liked) and publish-time filters. Returns titles, creators, duration, likes and publish time.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-search/v2/search-videos", "keyword": "商业", "offset": 0, "publish_time": "half_year", "raw": false, "sort": "latest"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-search/v2/search-videos', {'keyword': '商业', 'offset': 0, 'publish_time': 'half_year', 'raw': False, 'sort': 'latest'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-search/v2/search-videos", {
  "keyword": "商业",
  "offset": 0,
  "publish_time": "half_year",
  "raw": false,
  "sort": "latest"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-search/v2/search-videos", sandbase.Params{
	"keyword": "商业",
	"offset": 0,
	"publish_time": "half_year",
	"raw": false,
	"sort": "latest",
})
```

Same call via the path form: `POST /v1/api/wechat-search/v2/search-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw search response; False=simplified parsing. default `true` |
| `sort` |  |  | Optional, default `default`. Sort — `default`/0 (relevance) / `latest`/1 (newest) / `hot`/2 (most liked); string key or integer, invalid values rejected (400). default `"default"` |
| `cursor` |  |  | Optional. Pagination cursor, same usage as universal search `/fetch_search`. Leave empty for the first page; for the next page pass back the `cursor` from the previous response (repeat the same `duration` / `sort` /…  |
| `offset` | integer |  | Optional, default 0 (>=0). Pass `0` for the first page; use `cursor` to paginate (offset alone does not work). default `0`; range 0– |
| `keyword` | string | yes | Search keyword (1-100 chars)  |
| `duration` |  |  | Optional, default `all`. Duration tier (Channels video only) — `all`/0 / `short`/1 (<5min) / `medium`/2 (5-10min) / `long`/3 (20min+); string key or integer, invalid values rejected (400). default `"all"` |
| `publish_time` |  |  | Optional, default `all`. Publish time — `all`/0 / `day`/1 / `week`/2 / `half_year`/3; string key or integer, invalid values rejected (400). default `"all"` |

## Details

Search the WeChat Channels video vertical for a keyword. Filter by video length and publish time, sort by relevance, newest or most liked, and paginate with a cursor.

### Use cases

- Find Channels videos about a brand or topic.
- Discover active Channels creators in a niche.
- Track new short-video coverage with `sort=latest`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-search/v2/search-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (1-100 chars) |
| `raw` | boolean | No | Optional, default True. |
| `sort` | string | No | Optional, default `default`. |
| `cursor` | string | No | Optional. |
| `offset` | integer | No | Optional, default 0 (>=0). |
| `duration` | string | No | Optional, default `all`. |
| `publish_time` | string | No | Optional, default `all`. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "count": 10,
  "cursor": "<next page cursor>",
  "items": [
    {
      "title": "... #人工智能  #AI安全  #OpenAI  #企业AI",
      "duration": "01:23",
      "likeNum": "2",
      "pubTime": 1791270001,
      "source": {
        "title": "<user>"
      }
    }
  ]
}
```

### Notes

- `duration`: all, short (<5 min), medium (5–10 min) or long.
- Paginate with the `cursor` from the previous response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Search](/apis/wechat-search/v2/search): Search WeChat with one endpoint: official account articles, accounts, Channels videos, live streams, news and more.

---
Machine-readable: [`catalog/models/wechat-search/v2/search-videos.json`](../../../../catalog/models/wechat-search/v2/search-videos.json) · Store page: https://www.sandbase.ai/model/wechat-search/v2/search-videos
