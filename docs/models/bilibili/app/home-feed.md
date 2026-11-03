# Bilibili App Home Feed API: pricing, parameters and code examples

`bilibili/app/home-feed` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended video items from the Bilibili app home feed. Supports pagination via timestamp index and pull-to-refresh controls.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/home-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/home-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/home-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/home-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/app/home-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `idx` | integer |  | Page index, defaults to current timestamp  |
| `pull` | boolean |  | Pull to refresh default `true` |
| `flush` | integer |  | Flush flag (0=normal load, 1=refresh) default `0` |

## Details

Returns a page of recommended video cards from the Bilibili app home feed. Each card has the title, cover, creator, view and danmaku text, and duration. All inputs are optional, so an empty request returns a first page.

### Use cases

- Collect the videos Bilibili recommends on the app home feed at a given moment.
- Build a list of creators and channels (`up_name`, `tname`) that appear in the feed.
- Feed `args.aid` values into a video detail call to get full metadata for each recommended video.
- Show a mobile-style recommendation list in a custom viewer.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/home-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `flush` | integer | No | Flush flag (0=normal load, 1=refresh) |
| `idx` | integer | No | Page index, defaults to current timestamp |
| `pull` | boolean | No | Pull to refresh |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "config": {
      "auto_refresh_time": 1200,
      "auto_refresh_time_by_active": 1800,
      "auto_refresh_time_by_appear": 1800,
      "autoplay_card": 2,
      "card_density_exp": 1,
      "close_small_window": 1,
      "column": 2,
      "enable_rcmd_guide": true,
      "exposure_duration_end_ratio": 0.800000011920929,
      "exposure_duration_min_ms": 1,
      "exposure_duration_start_ratio": 0.800000011920929,
      "feed_clean_abtest": 0
    },
    "interest_choose": null,
    "items": [
      {
        "ad_info": {
          "card_index": 1,
          "client_ip": "146.190.39.116",
          "index": 1,
          "is_ad_loc": true,
          "request_id": "1793690837234q10a90a18a61q4499",
          "resource": 1897,
          "source": 1898
        },
        "args": {
          "aid": 117522066114493,
          "tid": 19822077,
          "tname": "#悬疑推理",
          "up_id": 281188808,
          "up_name": "听风的蚕基地"
        },
        "can_play": 1,
        "card_goto": "av",
        "card_type": "small_cover_v2",
        "cover": "http://i1.hdslb.com/bfs/archive/87c3fe6006d435225f498f2960d0f72ec970d5fa.jpg",
        "cover_info_priority": 123,
        "cover_left_1_content_description": "2491观看",
        "cover_left_2_content_description": "-弹幕",
        "cover_left_icon_1": 1,
        "cover_left_icon_2": 3,
        "cover_left_text_1": "2491"
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
| `data.items[].title` | Title of the recommended video. |
| `data.items[].args.aid` | Numeric ID of the video. It matches `param` and `player_args.aid`. |
| `data.items[].args.up_id / data.items[].args.up_name` | ID and display name of the creator who uploaded the video. |
| `data.items[].args.tid / data.items[].args.tname` | ID and name of the channel or tag attached to the video, for example `#悬疑推理`. |
| `data.items[].cover` | URL of the cover image. |
| `data.items[].cover_left_text_1 / data.items[].cover_left_text_2` | View count and danmaku count as display text, for example `1.7万`. A `-` means no count is shown. |
| `data.items[].cover_right_text / data.items[].player_args.duration` | Video length as display text such as `13:01`, and as a number `781`, which equals 13 minutes 1 second. |
| `data.items[].player_args.cid` | ID of the video part (`cid`) used by the player. |
| `data.items[].uri` | App deep link that opens the video in the Bilibili app. |
| `data.items[].idx` | Index value of the card. It looks like a Unix timestamp in seconds and counts down by one from card to card. |

### Notes

- Send `{}` to get the first page. `idx` defaults to the current timestamp.
- For the next page, try passing the last item's `idx` as the `idx` parameter. Use `flush` set to `1` for a refresh load.
- Some items carry an `ad_info` object. Items without it are normal video cards.
- To get full details for a video, pass its `args.aid` to [Bilibili App Single Video Details](/apis/bilibili/app/one-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili App Bangumi Tab](/apis/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/apis/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Single Video Details](/apis/bilibili/app/one-video): Returns detailed video metadata for a specific Bilibili video.

---
Machine-readable: [`catalog/models/bilibili/app/home-feed.json`](../../../../catalog/models/bilibili/app/home-feed.json) · Store page: https://www.sandbase.ai/model/bilibili/app/home-feed
