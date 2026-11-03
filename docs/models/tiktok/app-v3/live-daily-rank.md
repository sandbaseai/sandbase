# TikTok LIVE Ranking API: pricing, parameters and code examples

`tiktok/app-v3/live-daily-rank` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get TikTok LIVE rankings: hourly, weekly, rookie and other leaderboards with rank, score and creator.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/live-daily-rank"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/live-daily-rank', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/live-daily-rank", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/live-daily-rank", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/live-daily-rank` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string |  | Live room id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different room ids of different live rooms.  |
| `anchor_id` | string |  | Anchor id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different anchor ids of different live rooms.  |
| `rank_type` | integer |  | Rank type: 0: hourly_rank (Hourly Rank); 1: weekly_rank (Weekly Rank); 5: rookie_star_rank (Rookie Star Rank); 6: sale_rank (Sale Rank); 8: daily_rank (Daily Rank); 10: weekly_game_rank (Weekly Game Rank); 11:…  |
| `region_type` | integer |  | Region type, use the default value, the specific meaning is unknown.  |
| `gap_interval` | integer |  | Time interval, use the default value to represent the current day, use -1 to represent the ranking record.  |

## Details

Returns a TikTok LIVE leaderboard with each creator's rank, score and profile summary. Pick the board with `rank_type` (hourly, weekly, rookie star, daily and others). All inputs are optional, and the request sent here used none, so it returned the daily ranking (`rank_type` 8).

### Use cases

- Track which creators lead the daily or weekly LIVE leaderboard.
- Spot rookie creators climbing the rookie star board for partnership outreach.
- Compare the score gap between the top ranks and a given creator's position.
- Store board snapshots over time to chart how a creator's rank changes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/live-daily-rank" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `anchor_id` | string | No | Anchor id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different anchor ids of different live rooms. |
| `gap_interval` | integer | No | Time interval, use the default value to represent the current day, use -1 to represent the ranking record. |
| `rank_type` | integer | No | Rank type: 0: hourly_rank (Hourly Rank); 1: weekly_rank (Weekly Rank); 5: rookie_star_rank (Rookie Star Rank); 6: sale_rank (Sale Rank); 8: daily_rank (Daily Rank); 10: weekly_game_rank (Weekly Game Rank); 11: daily_game |
| `region_type` | integer | No | Region type, use the default value, the specific meaning is unknown. |
| `room_id` | string | No | Live room id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different room ids of different live rooms. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "rank_view": {
      "bulletin": {
        "enable": false,
        "notice_type": "",
        "schema": ""
      },
      "bulletin_loop": {
        "bulletins": []
      },
      "countdown": 72967,
      "cut_off_line": [
        {
          "content": {
            "default_format": {
              "bold": false,
              "color": "#ffffffff",
              "font_size": 0,
              "italic": false,
              "italic_angle": 0,
              "use_heigh_light_color": false,
              "use_remote_clor": false,
              "weight": 400
            },
            "default_pattern": "Top 20 LIVE creators will get ranking rewards",
            "key": "pm_mt_Live_WRbonus",
            "pieces": []
          },
          "cut_off_index": 20
        }
      ],
      "empty_rank_schema": "",
      "has_last_rank": true,
      "is_position_safe": true,
      "midday_peak_time_stamp": 1793732400,
      "next_period_time_stamp": 1793764800,
      "owner_rank": {
        "gap": {
          "ban_Info": 0,
          "button": {
            "action": 2,
            "button_content": {
              "default_format": {
                "bold": false,
                "color": "#ffffffff",
                "font_size": 0,
                "italic": false,
                "italic_angle": 0,
                "use_heigh_light_color": false,
                "use_remote_clor": false,
                "weight": 400
              },
              "default_pattern": "Send Gift",
              "key": "pm_mt_live_page_gift",
              "pieces": []
            },
            "button_display_type": 0,
            "button_type": "",
            "schema_url": ""
          },
          "display_type": 0,
          "gap_description": {
            "default_format": {
              "bold": false,
              "color": "#ffffffff",
              "font_size": 0,
              "italic": false,
              "italic_angle": 0,
              "use_heigh_light_color": false,
              "use_remote_clor": false,
              "weight": 400
            },
            "default_pattern": "{0:string} Diamonds to reach No. {1:string}",
            "key": "pm_mt_Live_WRdiamonds",
            "pieces": [
              {
                "string_value": "182.6K",
                "type": 1
              }
            ]
          },
          "gap_extra": {
            "class_rank_extra": {
              "bottom_schema": ""
            },
            "skip_info": {
              "is_skip": false,
              "skip_schema": ""
            },
            "tile_bottom_bar": {}
          },
          "gap_score": 0
        },
        "labels": [],
        "rank": 0,
        "rank_str": "99+",
        "rank_user": {
          "avatar_thumb": {
            "avg_color": "",
            "height": 0,
            "image_type": 0,
            "is_animated": false,
            "open_web_url": "",
            "uri": "100x100/tos-useast5-avt-0068-tx/34d4c2168595f3ae99ab5abed81d806f",
            "url_list": [
              "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/34d4c2168595f3a…"
            ],
            "width": 0
          },
          "badge_list": [],
          "display_id": "user778826688166389",
          "enigma_info": {
            "is_enigma_mask_on": false
          },
          "follow_info": {
            "follow_status": 0,
            "follower_count": 7321,
            "following_count": 9,
            "push_status": 0
          },
          "follow_status": 0,
          "id": 6952422426752205830,
          "id_str": "6952422426752205830"
        },
        "room_id": 0,
        "room_id_str": "",
        "score": 0
      },
      "primary_tabs": [],
      "rank_extra_info": {
        "class_extra": {
          "class_type": 400,
          "creator_class_image": {
            "avg_color": "",
            "height": 14,
            "image_type": 0,
            "is_animated": false,
            "open_web_url": "",
            "uri": "tos-alisg-i-cuqfs489yo-sg/class_rank/D2.png",
            "url_list": [
              "http://p16-common-sign.tiktokcdn-us.com/tos-alisg-i-cuqfs489yo-sg/class_rank/D2.…"
            ],
            "width": 32
          }
        },
        "hall_of_fame_rank_extra": {
          "is_first_day": false
        }
      }
    }
  },
  "extra": {
    "now": 1793691833381
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.rank_view.title` | Name of the board returned, for example `Daily Ranking`. |
| `data.rank_view.rank_type` | Numeric id of the board. It matches the `rank_type` request parameter. |
| `data.rank_view.ranks[].rank / data.rank_view.ranks[].rank_str` | Position of the creator on the board, as a number and as a string. |
| `data.rank_view.ranks[].score / data.rank_view.ranks[].score_description` | The creator's score on this board. `score_description` is a short display form such as `1.0M`. |
| `data.rank_view.ranks[].rank_user.display_id` | The creator's TikTok username. |
| `data.rank_view.ranks[].rank_user.id_str` | The creator's user ID as a string. |
| `data.rank_view.ranks[].rank_user.follow_info.follower_count` | Follower count of the ranked creator. |
| `data.rank_view.cut_off_line[].content.default_pattern` | Text describing the reward cutoff, such as the top 20 creators getting ranking rewards. `cut_off_index` gives the cutoff rank. |
| `data.rank_view.owner_rank.rank_str` | Rank of the account tied to the request, shown as `99+` in this response. |
| `data.rank_view.owner_rank.gap.gap_description.pieces[].string_value` | Values that fill the gap text, for example the diamonds needed to reach the next rank. |

### Notes

- Get `room_id` and `anchor_id` from [TikTok Broadcast Room Information](/apis/tiktok/app-v3/live-room-info). They change the `owner_rank` data.
- Use `gap_interval` -1 to get the ranking record instead of the current day.
- `data.rank_view.countdown`, `midday_peak_time_stamp` and `next_period_time_stamp` are timing values for the board period. The timestamps look like Unix seconds.
- To check whether a ranked creator is live now, call [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Creator Search Insights](/apis/tiktok/app-v3/creator-search-insights): Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category a…
- [TikTok Creator Search Insights Detail](/apis/tiktok/app-v3/creator-search-insights-detail): Get detailed statistics for a TikTok Creator Search Insights query: popularity over time and audience breakdown by age, gender and country.

---
Machine-readable: [`catalog/models/tiktok/app-v3/live-daily-rank.json`](../../../../catalog/models/tiktok/app-v3/live-daily-rank.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/live-daily-rank
