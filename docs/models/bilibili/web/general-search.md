# Bilibili Web General Search API: pricing, parameters and code examples

`bilibili/web/general-search` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns search results from Bilibili based on a search keyword, with sorting options and filters for duration and publication date range.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/general-search", "duration": 0, "keyword": "OpenAI", "order": "totalrank", "page": 1, "page_size": 20, "pubtime_begin_s": 0, "pubtime_end_s": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/general-search', {'duration': 0, 'keyword': 'OpenAI', 'order': 'totalrank', 'page': 1, 'page_size': 20, 'pubtime_begin_s': 0, 'pubtime_end_s': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/general-search", {
  "duration": 0,
  "keyword": "OpenAI",
  "order": "totalrank",
  "page": 1,
  "page_size": 20,
  "pubtime_begin_s": 0,
  "pubtime_end_s": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/general-search", sandbase.Params{
	"duration": 0,
	"keyword": "OpenAI",
	"order": "totalrank",
	"page": 1,
	"page_size": 20,
	"pubtime_begin_s": 0,
	"pubtime_end_s": 0,
})
```

Same call via the path form: `POST /v1/api/bilibili/web/general-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer | yes | Page number  |
| `order` | string | yes | Order method  |
| `keyword` | string | yes | Search keyword  |
| `duration` | integer |  | Duration filter default `0` |
| `page_size` | integer | yes | Number per page  |
| `pubtime_end_s` | integer |  | End date, 10-digit timestamp, must be greater than start date default `0` |
| `pubtime_begin_s` | integer |  | Start date, 10-digit timestamp, must be less than end date default `0` |

## Details

Returns a page of Bilibili video search results for a search `keyword`. Each result carries the video title fields, author, play and like counts, and publish time. You can sort the results and filter them by duration and publication date range.

### Use cases

- Track which videos rank for a brand or topic such as `OpenAI` on Bilibili.
- Collect the top creators (`author`, `mid`) posting about a keyword.
- Compare `play`, `like` and `favorites` across videos to find the most watched content on a topic.
- Build a list of `bvid` values to feed into video detail or comment lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/general-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI", "order": "totalrank", "page": 1, "page_size": 20}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `order` | string | Yes | Order method |
| `page` | integer | Yes | Page number |
| `page_size` | integer | Yes | Number per page |
| `duration` | integer | No | Duration filter |
| `pubtime_begin_s` | integer | No | Start date, 10-digit timestamp, must be less than end date |
| `pubtime_end_s` | integer | No | End date, 10-digit timestamp, must be greater than start date |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "egg_hit": 0,
    "exp_list": {
      "100010": true,
      "5500": true,
      "6699": true
    },
    "in_black_key": 0,
    "in_white_key": 0,
    "is_hit_web_inf": false,
    "next": 2,
    "numPages": 50,
    "numResults": 1000,
    "page": 1,
    "pagesize": 20,
    "result": [
      {
        "aid": 117541628284069,
        "arcurl": "http://www.bilibili.com/video/av117541628284069",
        "area": 0,
        "author": "产品君",
        "badgepay": false,
        "biz_data": null,
        "bvid": "BV1Saxb6PEhv",
        "card_status": 0,
        "cate_name": "",
        "cny_flag": 0,
        "corner": "",
        "cover": ""
      }
    ],
    "rqt_type": "search"
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.result[]` | List of matching videos on the requested page, in ranked order. |
| `data.result[].bvid / data.result[].aid` | The video's BV ID and numeric AID. `arcurl` holds the video page link built from the AID. |
| `data.result[].author / data.result[].mid` | Name and numeric ID of the user who posted the video. |
| `data.result[].description` | Video description text. Long text is cut and ends with an ellipsis. |
| `data.result[].play / data.result[].like / data.result[].favorites / data.result[].danmaku` | View, like, favorite and danmaku (on-screen comment) counts for the video. |
| `data.result[].duration` | Video length as a string such as `3:24`. |
| `data.result[].pubdate` | Publish time as a 10-digit Unix timestamp. |
| `data.result[].rank_index` | Position of the video in the result list, starting at 1. |
| `data.result[].hit_columns` | Parts of the video that matched the keyword, such as `title`, `description` or `tag`. |
| `data.numResults / data.numPages` | Total number of matching results and total number of pages for the current `page_size`. |
| `data.page / data.pagesize / data.next` | Current page number, page size, and the next page number. |

### Notes

- Set `page` and `page_size` to move through results. Use the `data.next` value as the next `page`.
- `pubtime_begin_s` and `pubtime_end_s` take 10-digit timestamps, the same format as `pubdate`. The end value must be greater than the start value.
- Use `bvid` from the results with [Bilibili Video Details](/apis/bilibili/web/one-video) to get more about a single video.
- Use `mid` with [Bilibili User Profile](/apis/bilibili/web/user-profile) to look up a creator.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/general-search.json`](../../../../catalog/models/bilibili/web/general-search.json) · Store page: https://www.sandbase.ai/model/bilibili/web/general-search
