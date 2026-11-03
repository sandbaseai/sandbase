# TikTok Music Chart List API: pricing, parameters and code examples

`tiktok/app-v3/music-chart-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns TikTok music chart rankings and track details. Supports filtering by chart type scene alongside cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/music-chart-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/music-chart-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/music-chart-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/music-chart-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/music-chart-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page, default 50, max 50 default `50` |
| `scene` | integer |  | Chart type default `0` |
| `cursor` | integer |  | Pagination cursor, default 0 default `0` |

## Details

Returns a ranked list of tracks from a TikTok music chart, with album, artist and audio details for each track. All inputs are optional. Use `scene` to pick the chart type, and `count` and `cursor` to page through results.

### Use cases

- Pull the current ranked tracks on a TikTok music chart to see which songs are trending.
- Collect artist names and handles from chart entries to build a list of artists to follow.
- Compare the `trend` value of tracks across calls to see which songs are moving on the chart.
- Feed chart track IDs into a music lookup to get full details for each song.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/music-chart-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number per page, default 50, max 50 |
| `cursor` | integer | No | Pagination cursor, default 0 |
| `scene` | integer | No | Chart type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "chart_info": {
    "id": 7245341979050396417,
    "update_time": 1793232000
  },
  "cover_image_url": "https://p16-common.tiktokcdn-us.com/musically-maliva-obj/U7w9pGIoKqZ6S8EGYy1IoXc…",
  "cursor": 50,
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110307435533B07F050ABE7A018069",
    "now": 1793691835000
  },
  "has_more": 0,
  "log_pb": {
    "impr_id": "2026110307435533B07F050ABE7A018069"
  },
  "msg": "success",
  "music_list": [
    {
      "id": 7245341979050396417,
      "music_info": {
        "album": "Kiss All The Time. Disco, Occasionally.",
        "allow_offline_music_to_detail_page": false,
        "artists": [
          {
            "avatar": {
              "uri": "tos-useast5-avt-0068-tx/d062dfc2badc475f0cf94e49c38d75a3",
              "url_list": [
                "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d062dfc2badc475…"
              ],
              "url_prefix": null
            },
            "enter_type": 2,
            "follow_status": 0,
            "follower_status": 0,
            "handle": "hshq",
            "is_block": false,
            "is_blocked": false,
            "is_private_account": false
          }
        ],
        "audition_duration": 60,
        "author": "Harry Styles",
        "author_deleted": false,
        "author_position": null,
        "avatar_medium": {
          "height": 720,
          "uri": "tos-useast5-avt-0068-tx/d062dfc2badc475f0cf94e49c38d75a3",
          "url_list": [
            "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d062dfc2badc475…"
          ],
          "url_prefix": null,
          "width": 720
        }
      },
      "trend": 4
    }
  ],
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `music_list[]` | The chart entries. Each item is one ranked track. |
| `music_list[].id` | ID of the chart entry. |
| `music_list[].trend` | Number that describes the trend of the track on the chart. The response does not state what each value means. |
| `music_list[].music_info.album` | Album name of the track. |
| `music_list[].music_info.author` | Display name of the artist. |
| `music_list[].music_info.artists[].handle` | TikTok handle of the artist. |
| `music_list[].music_info.audition_duration` | Preview length of the track. The response does not state the unit. |
| `music_list[].music_info.avatar_medium.url_list[]` | Image URLs for the artist avatar at 720 by 720 pixels. |
| `chart_info.id / chart_info.update_time` | ID of the chart and its update time as a Unix timestamp in seconds. |
| `cursor / has_more` | Pagination state. `cursor` is the value for the next page, and `has_more` is `0` when no more pages remain. |

### Notes

- The request works with an empty body. `count` defaults to 50, which is also the maximum.
- To get the next page, send the returned `cursor` value as `cursor` in the next request while `has_more` is not `0`.
- `scene` selects the chart type as an integer, and the default is `0`. The documentation does not list other values.
- For full details on a single track, call [TikTok Music Details](/apis/tiktok/app-v3/music-detail). To see videos that use a track, call [TikTok Music Video List](/apis/tiktok/app-v3/music-video-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/music-chart-list.json`](../../../../catalog/models/tiktok/app-v3/music-chart-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/music-chart-list
