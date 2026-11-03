# TikTok Room Gift List API: pricing, parameters and code examples

`tiktok/web/live-gift-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.025 per call · **Modes:** sync

Returns the catalog of gifts available in a TikTok broadcast, including gift identifiers, names, and diamond values. Accepts an optional room identifier to retrieve room-specific options.

## Pricing

- **$0.025 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/live-gift-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/live-gift-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/live-gift-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/live-gift-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/live-gift-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string |  | Live room ID (optional) default `""` |

## Details

Returns the catalog of gifts that viewers can send in a TikTok live broadcast. Each gift has an ID, a name, and a diamond cost. The `room_id` input is optional.

### Use cases

- Build a lookup table that maps gift `id` values to gift names and diamond costs.
- Compare the diamond cost of every gift on the panel to rank cheap and expensive gifts.
- Find gifts that support batch sending or combo sending for a gift tool.
- Download gift icon image URLs for a stream overlay or report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/live-gift-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | No | Live room ID (optional) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "beacon_bubble_priorities": {
      "0": 9999,
      "1": 5000,
      "2": 200,
      "3": 100,
      "4": 300,
      "5": 50,
      "6": 250,
      "7": 500
    },
    "cold_gift_hash": "",
    "doodle_templates": [],
    "downgrade_type": 0,
    "exclusive_recommend_infos": {},
    "gift_configs": {
      "config_infos": []
    },
    "gift_label_priorities": {
      "0": 9999,
      "1": 400,
      "10": 600,
      "11": 600,
      "12": 200,
      "13": 100,
      "14": 300,
      "15": 200,
      "16": 500,
      "17": 300,
      "2": 600,
      "3": 400
    },
    "gift_name_group_map": {},
    "gift_resource_group_map": {},
    "gifts": [
      {
        "batch_gift_info": {
          "available_counts": [
            5
          ],
          "can_batch_send": true
        },
        "biz_extra": {},
        "can_put_in_gift_box": false,
        "color_infos": [],
        "combo": true,
        "describe": "sent Mirwas Beat",
        "diamond_count": 1,
        "disable_gallery_banner": false,
        "duration": 1000,
        "expiration_timestamp": 0,
        "for_linkmic": true,
        "gallery_gift_type": ""
      }
    ],
    "gifts_info": {
      "batch_gift_info": {
        "consume_limit": 10000,
        "dismiss_expire_seconds": 604800
      },
      "beacon_bubble_info": {
        "anchor_gallery_icon": {
          "avg_color": "#FADCF0",
          "height": 28,
          "image_type": 0,
          "is_animated": false,
          "open_web_url": "",
          "uri": "webcast-sg/gift_beacon_bubble_league_D.png",
          "url_list": [
            "https://p16-webcast.tiktokcdn.com/img/alisg/webcast-sg/gift_beacon_bubble_league…"
          ],
          "width": 28
        },
        "live_goal_icon": {
          "avg_color": "#7C9BA3",
          "height": 28,
          "image_type": 0,
          "is_animated": false,
          "open_web_url": "",
          "uri": "webcast-sg/beacon_live_goal_test.png",
          "url_list": [
            "https://p16-webcast.tiktokcdn.com/img/alisg/webcast-sg/beacon_live_goal_test.png…"
          ],
          "width": 28
        },
        "live_goal_schema_url": "sslocal://webcast_lynxview_popup?use_spark=1&url=https%3A%2F%2Flf16-gecko-source…"
      },
      "color_gift_icon_animation": {
        "avg_color": "#E0C8BC",
        "height": 0,
        "image_type": 0,
        "is_animated": false,
        "open_web_url": "",
        "uri": "webcast-sg/MotorcycleV2.webp",
        "url_list": [
          "https://p16-webcast.tiktokcdn.com/img/alisg/webcast-sg/MotorcycleV2.webp~tplv-ob…"
        ],
        "width": 0
      },
      "combo_bar": {},
      "default_loc_color_gift_id": 5765,
      "deprecated1": [],
      "deprecated2": [],
      "deprecated3": [],
      "deprecated4": [],
      "deprecated5": [],
      "deprecated6": [],
      "enable_first_recharge_dynamic_effect": false
    },
    "hash": ""
  },
  "extra": {
    "log_id": "2026110315442524BBC38FF35A6B4D9EBB",
    "now": 1793691865938
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.gifts[].id` | Numeric ID of the gift. |
| `data.gifts[].name` | Display name of the gift. |
| `data.gifts[].describe` | Text shown in the chat when a viewer sends the gift, for example `sent Mantap`. |
| `data.gifts[].diamond_count` | Diamond cost of one gift. |
| `data.gifts[].combo` | Whether the gift can be sent as a combo. |
| `data.gifts[].batch_gift_info.available_counts / data.gifts[].batch_gift_info.can_batch_send` | Batch sizes offered for the gift and whether batch sending is allowed. Some gifts do not include this object. |
| `data.gifts[].is_displayed_on_panel` | Whether the gift appears on the gift panel. |
| `data.gifts[].icon.url_list` | Image URLs for the gift icon. |
| `data.gifts[].lock_info.lock` | Whether the gift is locked. The same object has `gift_level` and `unlock_button_text`. |
| `data.gifts_info.gift_group_infos[].group_count` | Group sizes offered for sending gifts, such as `10`, `99` and `365`. |

### Notes

- Send an empty body `{}` to get the default catalog, or pass `room_id` for a specific room.
- Get a room ID from [TikTok Room ID Resolver](/apis/tiktok/web/live-room-id).
- Use [TikTok Gift Name by ID](/apis/tiktok/web/gift-name-by-id) to look up a single gift name from an `id`.
- The `data.gifts` list has fields that vary by gift. For example, `preview_image` and `gift_label_icon` appear on some gifts only.

### Pricing

$0.025 per successful call. Failed calls are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/live-gift-list.json`](../../../../catalog/models/tiktok/web/live-gift-list.json) · Store page: https://www.sandbase.ai/model/tiktok/web/live-gift-list
