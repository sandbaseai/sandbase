# Bilibili User Published Videos API: pricing, parameters and code examples

`bilibili/user-video-list` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get videos published by a Bilibili user identified by UID, with an optional continuation parameter from a prior response. Use it to browse a creator's uploads or continue through their video list.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/user-video-list", "uid": "546195"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/user-video-list', {'uid': '546195'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/user-video-list", {
  "uid": "546195"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/user-video-list", sandbase.Params{
	"uid": "546195",
})
```

Same call via the path form: `POST /v1/api/bilibili/user-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Bilibili User ID (UID).  |
| `param` | string |  | Pagination parameter from previous response.  |

## Details

Returns a page of videos published by one Bilibili user, with title, BV ID, cover, play and danmaku counts, and publish time for each video. It needs the creator's numeric `uid`. An optional `param` value continues from a previous response.

### Use cases

- List a creator's newest uploads to track what they published.
- Rank a creator's videos by `play` and `danmaku` counts to find their top content.
- Collect `bvid` values for a creator, then fetch details or comments for each video.
- Page through a long upload history, such as the 682 videos in the sample, to build a full catalog.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/user-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "546195"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Bilibili User ID (UID). |
| `param` | string | No | Pagination parameter from previous response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "count": 682,
    "episodic_button": {
      "text": "播放全部",
      "uri": "bilibili://music/playlist/spacepage/546195?desc=1&offset=0&oid=0&order=time&page…"
    },
    "has_next": true,
    "has_prev": false,
    "item": [
      {
        "author": "老番茄",
        "badges": [
          {
            "bg_color": "#FB7299",
            "bg_color_night": "#BB5B76",
            "bg_style": 1,
            "border_color": "#FB7299",
            "border_color_night": "#BB5B76",
            "text": "热门",
            "text_color": "#FEFEFE",
            "text_color_night": "#E5E5E5"
          }
        ],
        "bvid": "BV1pkxi66ErX",
        "cover": "http://i1.hdslb.com/bfs/archive/53540400bc50b20d9354aa57444966395e99b2d5.jpg",
        "cover_icon": "",
        "cover_left_icon": "",
        "cover_left_text": "",
        "ctime": 1793417100,
        "cursor_attr": {
          "is_last_watched_arc": false,
          "rank": 0
        },
        "danmaku": 2829,
        "duration": 675,
        "first_cid": 43184029788
      }
    ],
    "last_watched_locator": {
      "display_threshold": 10,
      "insert_ranking": 6,
      "text": "定位至上次观看"
    },
    "next_cursor": "116819889232434",
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
| `data.count` | Total number of videos for this user. |
| `data.has_next / data.has_prev` | Whether a next or previous page exists. |
| `data.next_cursor` | Cursor value for the next page. It looks like a video ID. |
| `data.item[].bvid` | The BV ID of the video. |
| `data.item[].title` | Video title. |
| `data.item[].author` | Display name of the uploader. Joint uploads show text such as "等联合创作" after the name, and `is_cooperation` is `true`. |
| `data.item[].play / data.item[].danmaku` | Play count and danmaku (on-screen comment) count for the video. |
| `data.item[].view_content` | Play count as shown in the app, as a short text such as "224.8万". |
| `data.item[].duration` | Video length. The value is a number, for example `675`. |
| `data.item[].ctime` | Publish time as a Unix timestamp. |
| `data.item[].tname` | Name of the video's category. |
| `data.order[].title / data.order[].value` | Sort options shown by the platform: `pubdate` (latest) and `click` (most played). |

### Notes

- Use the `uid` of the creator. The example `546195` is the account of the uploader named 老番茄 in the sample. If you only have a profile link, call [Bilibili User ID Extraction](/apis/bilibili/web/get-user-id) first.
- For the next page, send `data.next_cursor` from the previous response as `param`. Keep going while `data.has_next` is `true`.
- Each item has a `bvid`. Pass it to [Bilibili Video Details](/apis/bilibili/web/one-video) to get the full video record.
- The `param` field inside each item is a video ID. Do not confuse it with the request parameter `param`.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/bilibili/user-video-list.json`](../../../catalog/models/bilibili/user-video-list.json) · Store page: https://www.sandbase.ai/model/bilibili/user-video-list
