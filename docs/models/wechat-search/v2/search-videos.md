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

Returns a page of WeChat Channels videos that match a keyword. Each item has the title, creator name, duration, publish time, cover image and video size. The only required input is `keyword`.

### Use cases

- Find Channels videos that mention a brand or topic, such as OpenAI.
- Collect the creators who post most often about a niche from `items[].source.title`.
- Watch for new coverage of a topic by sorting with `sort=latest` and `publish_time=day`.
- Filter for short clips or long explainers with the `duration` parameter.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-search/v2/search-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI", "raw": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (1-100 chars) |
| `cursor` | string | No | Optional. Pagination cursor, same usage as universal search `/fetch_search`. Leave empty for the first page; for the next page pass back the `cursor` from the previous response (repeat the same `duration` / `sort` / `pub |
| `duration` | string | No | Optional, default `all`. Duration tier (Channels video only) — `all`/0 / `short`/1 (<5min) / `medium`/2 (5-10min) / `long`/3 (20min+); string key or integer, invalid values rejected (400). |
| `offset` | integer | No | Optional, default 0 (>=0). Pass `0` for the first page; use `cursor` to paginate (offset alone does not work). |
| `publish_time` | string | No | Optional, default `all`. Publish time — `all`/0 / `day`/1 / `week`/2 / `half_year`/3; string key or integer, invalid values rejected (400). |
| `raw` | boolean | No | Optional, default True. True=raw search response; False=simplified parsing. |
| `sort` | string | No | Optional, default `default`. Sort — `default`/0 (relevance) / `latest`/1 (newest) / `hot`/2 (most liked); string key or integer, invalid values rejected (400). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_type": 7,
  "categories": null,
  "continue_flag": 1,
  "count": 10,
  "cursor": "kA37R_TZEBYnxEEkMYBugXwCxhM--hPjff4t00CtdR1gQuf-uvAVpBwmBWqHh2HRm_a_lfcbaSHh31sb…",
  "debug_id": "ac94ff14",
  "debug_info": "gAAAAABq6ZE6UtG9zVM5FmtCPzMrn22Bqkdpp2QNquseu5JK9z2G53SCFIhd7OyyrMJQ57C-VEzbhRC2…",
  "items": [
    {
      "dateTime": "39分钟前",
      "docID": "finderobjv0UlnDG0ddjVCqh5VN6UG+LlTA+QeV/CnqyCKIy8kceXU=",
      "duration": "00:15",
      "exportId": "export/UzFfBgAAxJaPSFACX12Nk8zT4DCKoaC6lwk5wrEvKxvwSb3XOg",
      "hashDocID": "13808060375097204523",
      "height": 1920,
      "image": "https://findermp.video.qq.com/251/20304/stodownload?encfilekey=KGDRibp2wkicJ2V9G…",
      "isHot": true,
      "jumpInfo": {
        "extInfo": "{\"behavior\":[\"report_feed_read\"],\"encryptedObjectId\":\"export/UzFfBgAAxJaPSFACX12…",
        "jumpType": 9
      },
      "noPlayIcon": true,
      "pubTime": 1793689596,
      "showType": 1
    }
  ],
  "keyword": "OpenAI",
  "no_more": null,
  "offset": 10,
  "total": 167
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].title` | Video title and hashtags. Matched keywords are wrapped in `<em class="highlight">` tags, so strip them before display. |
| `items[].source.title` | Display name of the Channels creator who posted the video. |
| `items[].source.iconUrl` | URL of the creator's avatar image. |
| `items[].duration` | Video length as a `mm:ss` string, for example `03:31`. |
| `items[].pubTime / items[].dateTime` | `pubTime` is the publish time as a Unix timestamp in seconds. `dateTime` is a relative label in Chinese, such as `39分钟前`. |
| `items[].exportId / items[].docID / items[].hashDocID` | Identifiers for the video. `exportId` starts with `export/`. |
| `items[].image` | URL of the video cover image. |
| `items[].width / items[].height` | Video frame size. A height larger than the width means a vertical video. |
| `items[].isHot` | Set to `true` on some items. The response does not explain the exact rule, so treat it as a flag from the search result. |
| `total / count / cursor` | `total` is the number of matches reported for the keyword. `count` is the number of items on this page. `cursor` is the token for the next page. |

### Notes

- For the first page, leave `cursor` empty and keep `offset` at `0`. For the next page, pass back the `cursor` from the previous response. `offset` alone does not paginate.
- Repeat the same `duration`, `sort` and `publish_time` values when you request the next page.
- `sort` accepts `default`, `latest` or `hot`, or the numbers 0, 1 and 2. `publish_time` accepts `all`, `day`, `week` or `half_year`.
- To search articles, accounts or other WeChat content, use [WeChat Search](/apis/wechat-search/v2/search) or [WeChat Account Search](/apis/wechat-search/search-account).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Search](/apis/wechat-search/v2/search): Search WeChat with one endpoint: official account articles, accounts, Channels videos, live streams, news and more.

---
Machine-readable: [`catalog/models/wechat-search/v2/search-videos.json`](../../../../catalog/models/wechat-search/v2/search-videos.json) · Store page: https://www.sandbase.ai/model/wechat-search/v2/search-videos
