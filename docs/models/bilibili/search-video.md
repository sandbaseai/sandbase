# Bilibili Video Search API: pricing, parameters and code examples

`bilibili/search-video` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search Bilibili videos by keyword with page-based pagination and sorting by general ranking, play count, publish time, danmaku count, or favorites.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/search-video", "keyword": "原神"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/search-video', {'keyword': '原神'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/search-video", {
  "keyword": "原神"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/search-video", sandbase.Params{
	"keyword": "原神",
})
```

Same call via the path form: `POST /v1/api/bilibili/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for pagination.  |
| `order` | string |  | Sorting criteria for search results. one of: `general`, `click`, `pubdate`, `dm`, `stow`; default `"general"` |
| `keyword` | string | yes | Search keyword.  |

## Details

Returns one page of Bilibili video search results for a keyword. Each result has the video IDs, title-matched author, play, like, favorite and danmaku counts, duration and publish time. The only required input is `keyword`.

### Use cases

- Track which videos rank first for a game or brand keyword such as `原神`.
- Find the most played or most favorited videos on a topic by setting `order` to `click` or `stow`.
- Monitor new uploads about a keyword by sorting with `pubdate`.
- Collect `bvid` and `mid` values to feed into video detail or creator lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "原神"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `order` | string | No | Sorting criteria for search results. |
| `page` | string | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "egg_hit": 0,
    "exp_list": {
      "100010": true,
      "105208": true,
      "106000": true,
      "5502": true,
      "55020101": true,
      "64778101": true,
      "65785101": true,
      "6600": true,
      "70529100": true,
      "73163100": true,
      "78757104": true,
      "78772100": true
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
        "aid": 117547651307164,
        "arcurl": "http://www.bilibili.com/video/av117547651307164",
        "area": 0,
        "author": "原神",
        "badgepay": false,
        "biz_data": null,
        "bvid": "BV19b4A6PECX",
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
| `data.result[].bvid / data.result[].aid` | The BV ID and numeric AV ID of the video. `arcurl` holds the video page link when it is set. |
| `data.result[].author / data.result[].mid` | Name and numeric ID of the uploader. |
| `data.result[].play / data.result[].danmaku / data.result[].favorites / data.result[].like` | Counts of plays, danmaku comments, favorites and likes for the video. |
| `data.result[].duration` | Video length as a text value such as `11:21`. |
| `data.result[].pubdate` | Publish time as a Unix timestamp in seconds. |
| `data.result[].description` | Video description text. The `desc` field is empty in this response. |
| `data.result[].pic` | Cover image URL. It starts with `//`, so add a scheme such as `https:` before use. |
| `data.result[].hit_columns` | Lists which parts of the video matched the keyword, such as `title`, `description`, `author` or `tag`. It is `null` for some results. |
| `data.result[].rank_index` | Position of the result in the ranking, starting at 1. |
| `data.result[].biz_data` | Extra block that holds ad data. It is `null` for normal results and filled for ad slots, where `is_ad_loc` is `true`. |
| `data.page / data.pagesize / data.numPages / data.numResults / data.next` | Current page number, results per page, total pages, total result count and the next page number. |

### Notes

- Pass `page` to move through results. The response `data.next` gives the next page number, and `data.page` shows the current one.
- Valid `order` values are `general` (default), `click`, `pubdate`, `dm` and `stow`.
- Ad results can appear in `data.result[]`. They have a filled `biz_data` object, and some have an empty `arcurl`, `pic`, or zero `like` and `favorites`.
- Use the `bvid` with [Bilibili Video Details](/apis/bilibili/web/one-video) or [Bilibili Video Comments](/apis/bilibili/video-comment). Use `mid` with [Bilibili User Profile](/apis/bilibili/user-detail).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/bilibili/search-video.json`](../../../catalog/models/bilibili/search-video.json) · Store page: https://www.sandbase.ai/model/bilibili/search-video
