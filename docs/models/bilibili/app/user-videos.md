# Bilibili User Videos API: pricing, parameters and code examples

`bilibili/app/user-videos` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns uploaded video listings for a specified Bilibili creator account. Supports pagination controls and filtering by post types such as archives or seasons.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/user-videos", "page": 1, "post_filter": "archive", "ps": 20, "user_id": "203680252"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/user-videos', {'page': 1, 'post_filter': 'archive', 'ps': 20, 'user_id': '203680252'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/user-videos", {
  "page": 1,
  "post_filter": "archive",
  "ps": 20,
  "user_id": "203680252"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/user-videos", sandbase.Params{
	"page": 1,
	"post_filter": "archive",
	"ps": 20,
	"user_id": "203680252",
})
```

Same call via the path form: `POST /v1/api/bilibili/app/user-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ps` | integer |  | Page size default `20` |
| `page` | integer |  | Page number default `1` |
| `user_id` | string | yes | User ID (required)  |
| `post_filter` | string |  | Filter type (archive/season/contribute) default `"archive"` |

## Details

Returns a page of uploaded videos for one Bilibili creator account. You send the creator's numeric `user_id`, and you can set the page, page size and post filter.

### Use cases

- Track new uploads from a Bilibili creator by reading the newest items in `data.item`.
- Compare play counts and danmaku counts across a creator's videos to see which uploads got the most attention.
- Build a catalog of a channel with titles, covers, durations and category names.
- Count the total uploads of an account with `data.count`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/user-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "203680252"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID (required) |
| `page` | integer | No | Page number |
| `post_filter` | string | No | Filter type (archive/season/contribute) |
| `ps` | integer | No | Page size |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "count": 1967,
    "episodic_button": {
      "text": "播放全部",
      "uri": "bilibili://music/playlist/spacepage/203680252?desc=1&offset=0&oid=0&order=time&p…"
    },
    "item": [
      {
        "author": "AYCS2",
        "bvid": "BV1oY4u6REdF",
        "cover": "http://i0.hdslb.com/bfs/archive/c80f8c142e993379aa9ac7cd7520cfc219d1f0e3.jpg",
        "cover_icon": "",
        "cover_left_icon": "",
        "cover_left_text": "",
        "ctime": 1793671323,
        "danmaku": 60,
        "duration": 168,
        "first_cid": 43279320428,
        "goto": "av",
        "icon_type": 0
      }
    ],
    "order": [
      {
        "title": "最新发布",
        "value": "pubdate"
      }
    ]
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Total number of videos for this creator under the current filter. |
| `data.item[].title` | Title of the video. |
| `data.item[].bvid` | The BV ID of the video. The share link in `three_point` uses the same ID. |
| `data.item[].author` | Name of the uploader. |
| `data.item[].play / danmaku` | Numeric play count and danmaku (on-screen comment) count of the video. |
| `data.item[].view_content` | Play count as display text, for example `3.4万`. |
| `data.item[].duration` | Length of the video. The value `168` is a plain number. |
| `data.item[].ctime` | Publish time as a Unix timestamp in seconds. |
| `data.item[].publish_time_text` | Relative or short date text for the publish time, as shown in the app, for example `5小时前`. |
| `data.item[].tname / cover` | Category name of the video and the URL of its cover image. |
| `data.order[].title / value` | Sort options offered by the app, such as `pubdate` and `click`. |

### Notes

- `user_id` is the numeric ID of the creator, for example `203680252`. If you only have a profile link, use [Bilibili User ID Extraction](/apis/bilibili/web/get-user-id) to get it.
- Page through the list with `page` and `ps`. Compare `data.count` with the number of items you have collected to know when to stop.
- `post_filter` accepts `archive`, `season` or `contribute`. The default is `archive`.
- For details on a single video, call [Bilibili App Single Video Details](/apis/bilibili/app/one-video) with the `bvid`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili App Bangumi Tab](/apis/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/apis/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/apis/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/user-videos.json`](../../../../catalog/models/bilibili/app/user-videos.json) · Store page: https://www.sandbase.ai/model/bilibili/app/user-videos
